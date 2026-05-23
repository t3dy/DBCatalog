# Project: DH Admin Panel

**Location**: `C:\Dev\wiki\admin` (lives inside the DBCatalog repository)
**Type**: Internal Tooling / Admin Interface

## Overview
A local Flask admin panel that provides a unified editing interface across all DH project SQLite databases. Runs on `localhost:5001` — local-only by design, requiring no authentication. A single `config.json` registers every project, maps it to its SQLite file and rebuild script, and declares which tables and fields are editable. The panel is the primary tool for advancing entries through the DRAFT → Reviewed → Verified review pipeline.

## Architecture
- **Stack**: Python (Flask 3.x), Jinja2 templates, Vanilla HTML/CSS/JS. Zero external front-end dependencies.
- **Data flow**: Admin panel reads from and writes to each project's own SQLite database directly. It does not maintain a separate copy of the data. After editing, the "Rebuild Site" button runs the project's existing `build_site.py` script to regenerate the static HTML.
- **Config**: `admin/config.json` — one entry per project, declaring `db_path`, `rebuild_script`, and per-table schema: `editable_fields`, `tag_fields`, `review_field`, `confidence_field`, and `relationships` (supports both junction-table and FK patterns).
- **Logging**: Every save writes a timestamped entry to `admin/admin_log.json` recording which project, table, entity, and fields were changed — without storing field values.

## Key Features
- **Prose editing**: Multi-line textarea for description, central claim, scholarly lineage, disputes, quotable evidence — every field declared in the config.
- **Tag editing**: Clickable chips for toggling enum tags (tradition, period, language) plus a raw text input for custom tags. Both stay in sync.
- **Review status + confidence**: Button-group selectors (DRAFT / Reviewed / Verified) and (LOW / MEDIUM / HIGH) on every entity. Saving does NOT auto-promote status — the human controls it explicitly.
- **Relationship editing**: Checkbox grid for junction-table relationships (figure ↔ concept) and single-select for FK relationships (figure → primary text).
- **Rebuild trigger**: One-click button that runs the project's `build_site.py` and reports success or failure inline.

## Registering a New Project
Add an entry to `config.json` under `"projects"`. Minimum required keys:

```json
"my_project": {
  "name": "Display Name",
  "db_path": "C:/Dev/my_project/my.db",
  "rebuild_script": "C:/Dev/my_project/build_site.py",
  "tables": {
    "entities": {
      "display_name": "Entities",
      "display_field": "name",
      "editable_fields": [
        {"name": "description", "label": "Description", "type": "textarea"}
      ],
      "tag_fields": [],
      "review_field": "review_status",
      "confidence_field": "confidence",
      "relationships": []
    }
  }
}
```

## Running
```bash
cd admin
pip install -r requirements.txt
python app.py
# → http://localhost:5001
```

## System Invariants
- **Deckard Boundary**: The admin panel is the human-verification layer, not the LLM layer. It never generates content — it only displays and saves what a human types.
- **No auto-promotion**: Saving an entity never automatically advances `review_status`. The human selects the status explicitly on every save.
- **Config-driven SQL**: Table and column names come exclusively from `config.json`, never from user input. Values are always parameterized. This makes the dynamic SQL safe by construction.
- **Log without values**: `admin_log.json` records which fields were changed, not what they were changed to. The SQLite database is the single source of truth for all values.

## Related Entities & Concepts
- [[Deckard Boundary]]
- [[DRAFT Review Cycle]]
- [[Wiki Field Guide]]
- [[RenMagDB]]
- [[HermeticDB]]
- [[WitchcraftStudiesDB]]
- [[CrowleyDB]]
- [[WitcherFolkloreDB]]
