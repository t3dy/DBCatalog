---
name: project_alchemybeatemup
description: DH pipeline turning historical alchemical engravings into pixel-art sprites for a "lab-is-the-boss" beat-em-up.
type: project
status: STABLE
tags: [alchemy, game, sprites, pixel-art, pipeline, python, sqlite]
---

# Project: AlchemyBeatEmUp

**Location** · `C:\Dev\AlchemyBeatEmUp` — **Type** · asset pipeline + static viewer — **Stack** · Python (Pillow, numpy, scipy, requests, PyYAML) + SQLite + vanilla JS, GitHub Pages — **Verified** · 324 sprites + deployed viewer (pages.yml ~35s); not re-run this session

## What it is
A digital-humanities pipeline that turns historical alchemical engravings into pixel-art sprites for a planned beat-em-up where "the lab is the boss." Currently an asset artifact + planning, not yet a playable game.

## Architecture
SQLite `db/alchemical_images.db` (14 tables, 442+ rows) is the spine. Scrapers (Wikimedia, Internet Archive) pull raw images; `02_load_assets.py` ingests YAML-in-markdown catalogs; the pixelator (median filter + median-cut quantize, no dither) emits sprites; `06_export_to_json.py` writes `data.json` for the viewer. Entry points: `README.md`, `index.html`, `scripts/0*.py`, `RETROSPECTIVE.md`.

## Fragile parts
**Hardcoded cross-project path** in `scripts/03_pixelate_emblems.py:27` → `C:\Dev\Claudiens\site\images\emblems` (reads the sibling Claudiens repo) — see [[environment-health]]. Heuristic text-page classifier has false positives (the "unicorn" blooper). Cross-DB ATTACH integration (report 07) is conceptual, not executed.

## Status & next
Stable asset pipeline; game layer deferred. Roadmap (`APISTUFF.md`): per-manuscript bbox crops, 2D-FFT classifier, vision-LLM bounding boxes.

## Related
- [[project_claudiens]] — shares the emblem images / scholarly substrate
- [[project_alchemyblockinvaders]], [[project_alchemytetris]] — sibling alchemy-game experiments
- [[project_emblemprintshop]] — the no-API emblem CV extraction lineage
