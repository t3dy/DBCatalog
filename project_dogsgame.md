---
name: project_dogsgame
description: Noir text-adventure life-sim prototype based on four real dogs in Sultan, WA; encounter-driven.
type: project
status: ACTIVE
tags: [game, text-adventure, narrative, vanilla-js, python]
---

# Project: DOGSGAME (4DOGS)

**Location** · `C:\Dev\DOGSGAME` — **Type** · browser + terminal game — **Stack** · vanilla HTML/CSS/JS (localStorage) + companion Python 3 — **Verified** · live at t3dy.github.io/4DOGS-GAME; `python code/dogsim.py --test` for headless check

## What it is
A noir text-adventure / life-sim prototype built around four real dogs in Sultan, WA — encounter-driven exploration.

## Architecture
Three-tier context-engineering layout (`CEAUDIT.md`): `canon/` = immutable facts (dogs, yard, 16 B### behavior files), `design/` = speculation, `code/` = builds. Single-file layered engine (World kernel → Encounters → Catalog/Cases → TextRenderer → Sequencer → play loop). Entry points: `code/noir.html` (main game, 17 scenes / 6 cases), `code/showcase.html` (4-era mockup: TEXT/ULTIMA V/SIMS/NES), `code/dogsim.py` (terminal). **Read `CEAUDIT.md` first.**

## Fragile parts
`noir.html` and `dogsim.py` are separate kernels (no shared engine); showcase eras don't share state; no save/load (in-memory only); single-dog (Okie) scope freeze. The SQLite/vector substrate in CEAUDIT is proposed, not built. No hardcoded-path / broken-build issues.

## Status & next
Active "exploration phase"; v1 not yet committed. Parked sibling designs in-repo: `K9_PATROL_ROGUELIKE.md`, `SHAMANIC_VOYAGES.md`.

## Related
- [[project_emblemroguelike]], [[project_emblemnovel]] — workspace game family (aesthetic/structure, no code dependency)
