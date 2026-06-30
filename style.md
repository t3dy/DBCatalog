---
name: style
description: Wiki writing voice, markdown conventions, and the lean project-page template. Read before authoring or refreshing a page.
type: system
tags: [style, template, conventions, meta]
---

# Wiki Style & Template

## Voice

- **Reportorial density.** Information per line is high; no marketing, no filler. "37
  entries, 89% verified" beats "most of the entries are done".
- **Assumption-transparent.** Name the fragility. "Known trap: build.py hardcods the
  scholar list" is more valuable than a clean-looking silence.
- **Sourced.** Tie claims to a file+line (`scripts/build.py:42`) or a wiki page. If you
  did not verify it this session, mark it `(unverified)`.

## Markdown conventions

- **Cross-refs:** `[[project_slug]]` for wiki pages (slug = the `name:` field, no `.md`).
- **Source code:** `` `C:\Dev\proj\file.py:42` `` — path + line, not prose description.
- **Code blocks** always carry a language tag.
- **Tables** when comparing 3+ items; otherwise a short list.
- **Frontmatter** on every page: `name`, `description`, `type`, `status`, `tags`.

## Length discipline

Target a project page at **~1.5 KB**. The good pages (`project_crowleydb.md`,
`project_emblemroguelike.md`) sit there. Pages over ~6 KB (pico, glassbeadgame) are the
anti-pattern — split deep material into a linked concept page instead of growing the
project page.

## Project-page template

```markdown
---
name: project_<slug>
description: <one-line hook — what it IS, not what it does>
type: project
status: ACTIVE | STABLE | ARCHIVED | SCRATCH
tags: [<area>, <area>]
---

# Project: <Name>

**Location** · `C:\Dev\<path>` — **Type** · <DB|Game|Portal|Tool|Site> —
**Stack** · <lang/framework> — **Verified** · <YYYY-MM-DD | none this session>

## What it is
<1–2 sentences. The thing, plainly.>

## Architecture
<Data model + pipeline in 2–4 sentences or a short list. Name the entry points.>

## Fragile parts
<Hardcoded deps, silent-failure traps, one-touch breakage — or "none observed (unverified)".>

## Status & next
<What's built · what's actually verified · what's next or blocked.>

## Related
- [[<page>]] — <why linked>
```

## Status vocabulary

- **ACTIVE** — under current development.
- **STABLE** — built and verified, not changing much.
- **ARCHIVED** — done, superseded, or abandoned (say which).
- **SCRATCH** — experiment/prototype; document lightly, flag as not load-bearing.
