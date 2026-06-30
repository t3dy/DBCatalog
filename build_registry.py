#!/usr/bin/env python3
"""Harvest every project_*.md (+ goetia) into registry.tsv — the machine-readable
project index used to resolve cross-project references.

Deterministic layer only (the Deckard Boundary): this script extracts facts
(slug, name, type, status, repo path, live URL, tags, one-liner). The *semantic*
theme/alias map ("my alchemy databases" -> which projects) is hand-curated in
registry.md and is NOT generated here.

Run:  python build_registry.py
"""
import re, glob, os

WIKI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(WIKI, "registry.tsv")
DEV = r"C:\Dev"

# A Windows path: drive letter, colon, backslash, then non-space/non-markup chars.
PATH_RE = re.compile(r"[A-Za-z]:\\[^\s`*·:]+")
URL_RE = re.compile(r"https?://[^\s`)>\]]+")
STRIP_SUFFIXES = ("\\README.md", "\\CLAUDE.md", "\\PHASESTATUS.md", "\\STATUS.md")

_REAL_DIRS = [d for d in os.listdir(DEV) if os.path.isdir(os.path.join(DEV, d))] if os.path.isdir(DEV) else []


def _leafkey(p):
    return re.sub(r"[^a-z0-9]", "", os.path.basename(p.rstrip("\\")).lower())


def resolve(p):
    """Map a path guessed from prose onto a real directory: drop trailing files,
    and recover dir names with spaces (e.g. 'renaissance' -> 'renaissance magic')
    by prefix-matching the leaf against actual C:\\Dev subdirectories."""
    if not os.path.isdir(p) and "." in os.path.basename(p):
        p = os.path.dirname(p)
    if os.path.isdir(p):
        return p.rstrip("\\")
    if p.lower().startswith(DEV.lower() + "\\"):
        leaf = p[len(DEV) + 1:].split("\\")[0]
        exact = [d for d in _REAL_DIRS if d.lower() == leaf.lower()]
        if exact:
            return os.path.join(DEV, exact[0])
        pref = [d for d in _REAL_DIRS if d.lower().startswith(leaf.lower())]
        if pref:
            return os.path.join(DEV, min(pref, key=len))
    return p.rstrip("\\")


def parse_frontmatter(text):
    fm = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for line in text[3:end].splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    fm[k.strip()] = v.strip().strip("'\"")
    return fm


def first_heading(text):
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if not m:
        return ""
    name = m.group(1).strip()
    return re.sub(r"^Project:\s*", "", name)


def clean_path(p):
    p = p.strip().strip("`")
    for suf in STRIP_SUFFIXES:
        if p.endswith(suf):
            p = p[: -len(suf)]
    return p.rstrip("\\")


def best_path(text, slug):
    """Pick the candidate whose folder name best matches the project slug, so a
    page that merely *mentions* C:\\Dev\\wiki doesn't get it picked as its own root."""
    stem = re.sub(r"[^a-z0-9]", "", slug.replace("project_", "").lower())
    cands = {resolve(clean_path(p)) for p in PATH_RE.findall(text)}
    cands = {c for c in cands if "\\" in c and c.lower() != DEV.lower() and len(c) > 3}
    if not cands:
        return ""

    def score(c):
        lk = _leafkey(c)
        return (lk == stem, bool(stem) and (lk.startswith(stem) or stem.startswith(lk)),
                os.path.isdir(c), -len(c))

    return max(cands, key=score)


def first_url(text):
    for m in URL_RE.finditer(text):
        u = m.group(0).rstrip(".*,")
        if "githubusercontent" not in u and "fonts." not in u:
            return u
    return ""


def tags_of(fm):
    raw = fm.get("tags", "")
    raw = raw.strip().lstrip("[").rstrip("]")
    parts = [t.strip().strip("'\"") for t in raw.split(",") if t.strip()]
    # drop noise tags that carry no discriminating meaning
    return [t for t in parts if t not in ("project", "stub")]


def rows():
    files = sorted(glob.glob(os.path.join(WIKI, "project_*.md")))
    files += [f for f in glob.glob(os.path.join(WIKI, "goetia_*.md"))]
    for path in files:
        slug = os.path.splitext(os.path.basename(path))[0]
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        fm = parse_frontmatter(text)
        name = fm.get("title") or first_heading(text) or slug
        desc = fm.get("description", "").strip()
        if not desc:
            body = text.split("---", 2)[-1] if text.startswith("---") else text
            for line in body.splitlines():
                line = line.strip()
                if line and not line.startswith(("#", "**", "-", "|", "<")):
                    desc = line
                    break
        yield {
            "slug": slug,
            "name": name,
            "type": fm.get("type", ""),
            "status": fm.get("status", ""),
            "path": best_path(text, slug),
            "live": first_url(text),
            "tags": " ".join(tags_of(fm)),
            "desc": desc[:160],
        }


def main():
    cols = ["slug", "name", "type", "status", "path", "live", "tags", "desc"]
    lines = ["\t".join(cols)]
    n = 0
    missing_path = []
    for r in rows():
        lines.append("\t".join(r[c].replace("\t", " ").replace("\n", " ") for c in cols))
        n += 1
        if not r["path"]:
            missing_path.append(r["slug"])
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"registry.tsv: {n} projects")
    if missing_path:
        print(f"  no path extracted for: {', '.join(missing_path)}")


if __name__ == "__main__":
    main()
