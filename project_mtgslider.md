---
name: project_mtgslider
description: MTG thematic-research pipeline — theme → Scryfall search → curation → image fetch → packet → PowerPoint slideshow.
type: project
status: STABLE
tags: [mtg, scryfall, python, pipeline, pptx]
---

# Project: MTGSLIDER

**Location** · `C:\Dev\MTGSLIDER` — **Type** · Python CLI pipeline — **Stack** · Python ≥3.11, requests + python-pptx, SQLite, pytest — **Verified** · pytest lastfailed empty; `.pptx` artifacts present (not re-run this session)

## What it is
A deterministic pipeline that turns a theme into a curated Magic: The Gathering card slideshow: theme → Scryfall search → manual curation → image fetch → packet → PowerPoint.

## Architecture
CLI under `src/mtgslider/` — entry `python -m mtgslider` (`__main__.py` → `cli.py`) or the `mtgslider` console script. Flow: `scryfall.py` (cached, rate-limited client) → `themes.py` (+ `db.py` SQLite) → `images.py` (download with provenance) → `packet.py` (JSON+MD) → `slideshow/` with two backends sharing one packet: `v1_template/` (deterministic, ships now) and `compiler/` (semantic slide types, maturing).

## Fragile parts
None observed structurally. `paths.py` uses `__file__`-relative root (portable). No LLM calls, no scraping — deterministic by design. The `compiler/` backend is more mature than its README admits.

## Status & next
Slice 1 complete and shipping (alchemists / cats / dogs / books themes generated).

## Related
- [[project_alchemyscryfall]] — also Scryfall-sourced (MTG↔alchemy); no code dependency
- [[project_draftacademy]] — MTG-family educational site
