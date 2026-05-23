"""
DH Admin Panel — local-only editing interface for all DH project SQLite databases.
Run with: python app.py
Access at: http://localhost:5001

Security note: localhost-only by design. Table/column names come exclusively from
config.json (admin-controlled), never from user input, so dynamic SQL is safe.
All value parameters are fully parameterized.
"""

import json
import os
import subprocess
from datetime import datetime

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "dh-admin-local-only"

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")
LOG_PATH = os.path.join(os.path.dirname(__file__), "admin_log.json")

REVIEW_STATUSES = ["DRAFT", "Reviewed", "Verified"]
CONFIDENCE_LEVELS = ["LOW", "MEDIUM", "HIGH"]


# ── helpers ──────────────────────────────────────────────────────────────────

def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def get_db(db_path):
    import sqlite3
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def append_log(entry):
    log = []
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH) as f:
            log = json.load(f)
    log.append({"timestamp": datetime.now().isoformat(), **entry})
    with open(LOG_PATH, "w") as f:
        json.dump(log, f, indent=2)


def get_project_or_404(config, project_key):
    proj = config["projects"].get(project_key)
    if not proj:
        from flask import abort
        abort(404)
    return proj


# ── routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    config = load_config()
    projects = []
    for key, proj in config["projects"].items():
        db_exists = os.path.exists(proj["db_path"])
        projects.append({"key": key, "proj": proj, "db_exists": db_exists})
    return render_template("index.html", projects=projects)


@app.route("/project/<project_key>")
def project(project_key):
    config = load_config()
    proj = get_project_or_404(config, project_key)

    conn = get_db(proj["db_path"])
    tables_data = {}
    for table_key, table_cfg in proj["tables"].items():
        display_field = table_cfg["display_field"]
        # Safe: table_key and display_field come from config, not user input
        rows = conn.execute(
            f"SELECT id, {display_field}, review_status, confidence "
            f"FROM {table_key} ORDER BY id DESC LIMIT 100"
        ).fetchall()
        tables_data[table_key] = {"config": table_cfg, "rows": rows}
    conn.close()

    return render_template(
        "project.html",
        project_key=project_key,
        proj=proj,
        tables_data=tables_data,
    )


@app.route("/edit/<project_key>/<table>/<int:entity_id>", methods=["GET", "POST"])
def edit_entity(project_key, table, entity_id):
    config = load_config()
    proj = get_project_or_404(config, project_key)
    table_cfg = proj["tables"].get(table)
    if not table_cfg:
        from flask import abort
        abort(404)

    conn = get_db(proj["db_path"])

    if request.method == "POST":
        updates = {}

        # Prose fields
        for field in table_cfg.get("editable_fields", []):
            updates[field["name"]] = request.form.get(field["name"], "").strip()

        # Tag fields
        for field in table_cfg.get("tag_fields", []):
            if field["type"] == "tags":
                # Stored as comma-separated string
                raw = request.form.get(field["name"], "")
                updates[field["name"]] = ", ".join(
                    t.strip() for t in raw.split(",") if t.strip()
                )
            else:
                updates[field["name"]] = request.form.get(field["name"], "").strip()

        # Review status and confidence
        review_field = table_cfg.get("review_field")
        confidence_field = table_cfg.get("confidence_field")
        if review_field:
            updates[review_field] = request.form.get(review_field, "Reviewed")
        if confidence_field:
            updates[confidence_field] = request.form.get(confidence_field, "MEDIUM")

        # Mark as human-verified in source_method if the column exists
        try:
            conn.execute(
                f"UPDATE {table} SET source_method = 'Human_Verified' WHERE id = ?",
                (entity_id,),
            )
        except Exception:
            pass  # column may not exist in every schema

        if updates:
            set_clause = ", ".join(f"{k} = ?" for k in updates)
            values = list(updates.values()) + [entity_id]
            conn.execute(f"UPDATE {table} SET {set_clause} WHERE id = ?", values)

        # Junction table relationships
        for rel in table_cfg.get("relationships", []):
            if rel["type"] == "junction":
                jt = rel["junction_table"]
                src = rel["source_id"]
                tgt = rel["target_id"]
                # Replace all existing links with the submitted selection
                conn.execute(f"DELETE FROM {jt} WHERE {src} = ?", (entity_id,))
                selected_ids = request.form.getlist(f"rel_{rel['name']}")
                for tid in selected_ids:
                    conn.execute(
                        f"INSERT INTO {jt} ({src}, {tgt}) VALUES (?, ?)",
                        (entity_id, int(tid)),
                    )

        conn.commit()
        append_log({
            "project": project_key,
            "table": table,
            "entity_id": entity_id,
            "fields_edited": [f["name"] for f in table_cfg.get("editable_fields", [])]
                             + [f["name"] for f in table_cfg.get("tag_fields", [])],
        })
        flash("Saved.", "success")
        conn.close()
        return redirect(url_for("edit_entity", project_key=project_key, table=table, entity_id=entity_id))

    # GET — load entity and relationship options
    row = conn.execute(f"SELECT * FROM {table} WHERE id = ?", (entity_id,)).fetchone()
    if row is None:
        from flask import abort
        conn.close()
        abort(404)

    relationships = {}
    for rel in table_cfg.get("relationships", []):
        all_options = conn.execute(
            f"SELECT id, {rel['display_field']} FROM {rel['table']} ORDER BY {rel['display_field']}"
        ).fetchall()
        if rel["type"] == "junction":
            current_ids = {
                r[0] for r in conn.execute(
                    f"SELECT {rel['target_id']} FROM {rel['junction_table']} WHERE {rel['source_id']} = ?",
                    (entity_id,),
                ).fetchall()
            }
        else:
            current_ids = set()
        relationships[rel["name"]] = {
            "config": rel,
            "all_options": all_options,
            "current_ids": current_ids,
        }

    conn.close()
    return render_template(
        "entity.html",
        project_key=project_key,
        proj=proj,
        table=table,
        table_cfg=table_cfg,
        entity=row,
        relationships=relationships,
        review_statuses=REVIEW_STATUSES,
        confidence_levels=CONFIDENCE_LEVELS,
    )


@app.route("/rebuild/<project_key>", methods=["POST"])
def rebuild(project_key):
    config = load_config()
    proj = get_project_or_404(config, project_key)
    script = proj.get("rebuild_script", "")
    if not script or not os.path.exists(script):
        flash("No rebuild script found at the configured path.", "warning")
        return redirect(url_for("project", project_key=project_key))

    result = subprocess.run(
        ["python", script],
        capture_output=True,
        text=True,
        cwd=os.path.dirname(script),
    )
    if result.returncode == 0:
        flash("Rebuild complete.", "success")
    else:
        flash(f"Rebuild failed: {result.stderr[:300]}", "error")
    return redirect(url_for("project", project_key=project_key))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
