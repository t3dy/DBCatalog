---
name: project_hpin3d
description: 3D web viewer turning Hypnerotomachia Poliphili and Atalanta Fugiens emblems into explorable alchemical worlds.
type: project
status: ACTIVE
tags: [3d, emblems, threejs, hypnerotomachia, atalanta]
---

# Project: HPin3D (Emblems in 3D)

**Location** · `C:\Dev\HPin3D` — **Type** · 3D web viewer + mini-games — **Stack** · Three.js r168 + PixiJS + GSAP via CDN importmap (no build step) — **Verified** · none this session

## What it is
A browser 3D viewer that turns the woodcuts of the 1499 *Hypnerotomachia Poliphili* and Maier's *Atalanta Fugiens* into walkable alchemical worlds, plus standalone mini-games.

## Architecture
Entry `src/index.html` loads `src/main.js`, a world switcher (HP / Atalanta / Archives) using an ES-module importmap pulling Three/GSAP/Pixi from CDN. Scene modules in `src/scenes/` (EmblemScene ~845 LOC, ArchivesScene, HPScene). Data is committed JSON in `src/data/`, produced by `scripts/export_for_3d.py` + `enrich_emblems.py` from sibling `atalanta.db`/`hp.db`.

## Fragile parts
`STATUS.md` is badly out of sync — claims "Phase 0 / NOT STARTED" while the app is built and committed (stale-docs trap). `TECH_STACK.md` specifies Vite/Theatre.js/Tone/Zustand, none installed (aspirational; the real app is CDN-only). Manual cache-bust (`main.js?v=8`). Cross-project path coupling to sibling HP/Atalanta DBs.

## Status & next
Functional static app (open `src/index.html` or serve the dir). Reconcile the stale planning docs to shipped reality.

## Related
- [[project_hypnerotomachia]] — data source (this repo's marginalia DB)
- [[project_emblemsin3d]] — parallel Atalanta-in-3D effort
- [[project_claudiens]] — Atalanta Fugiens scholarship/DB
- [[project_emblemroguelike]], [[project_emblemnovel]] — shared emblem-game lineage
