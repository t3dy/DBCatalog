---
name: project_memorypalace
description: Illustrated browsable front-end over the C:\Dev\wiki, staged as Camillo's seven-tier Theatre of Memory.
type: project
status: ACTIVE
tags: [wiki, frontend, dh, static-site, memory]
---

# Project: MemoryPalace

**Location** · `C:\Dev\MemoryPalace` — **Type** · static-site viewer over the wiki — **Stack** · Python (`build.py`, python-markdown) → JSON + vanilla-JS theatre UI — **Verified** · generated data present; runs at localhost:5188 (not re-run this session)

## What it is
A browsable, illustrated front-end for `C:\Dev\wiki` — this LLM-Wiki memory system — arranged as the seven tiers of Giulio Camillo's Theatre of Memory (100 pages → 106 loci).

## Architecture
`build.py` parses `C:\Dev\wiki\*.md` (frontmatter + body), renders markdown to HTML, resolves `[[wikilinks]]` to in-palace anchors, assigns each page to one of seven tiers, and emits `data/palace.json` + `assets/js/palace-data.js`. `index.html` + `assets/js/palace.js` give a hash-routed theatre UI. Annexes: Living Gates (`data/live_sites.json`) and the Atlas (`diagrams/*.svg`). Rebuild = `python build.py`.

## Fragile parts
Hardcoded absolute path `WIKI = C:\Dev\wiki` in `build.py` (non-portable). Goes stale if not rebuilt after wiki edits. Liveness-checked URLs in `live_sites.json` can drift.

## Status & next
Built and runnable. **Re-run `build.py` after this session's wiki additions** to surface the new project pages as loci.

## Related
- [[system]] — the wiki's operating rules; this renders the wiki it governs
- `index.md` — the page catalog MemoryPalace consumes
