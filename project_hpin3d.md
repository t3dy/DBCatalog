---
name: project_hpin3d
description: 3D web viewer turning Hypnerotomachia Poliphili and Atalanta Fugiens emblems into explorable alchemical worlds, with guided research tours and a plate atlas.
type: project
status: ACTIVE
tags: [3d, emblems, threejs, hypnerotomachia, atalanta, tours]
---

# Project: HPin3D (Emblems in 3D)

**Location** · `C:\Dev\HPin3D` — **Live** · https://t3dy.github.io/EmblemsIn3d/ (repo `t3dy/EmblemsIn3d`, GitHub Pages) — **Type** · 3D web viewer + guided tours + mini-games — **Stack** · Three.js r168 (+ OrbitControls) / GSAP / Tone.js via CDN importmap, no build step — **Verified** · 2026-06-29, live site renders; Tours/Plates/images return 200

## What it is
A browser 3D viewer that turns the woodcuts of the 1499 *Hypnerotomachia Poliphili* and Maier's *Atalanta Fugiens* into explorable alchemical worlds, plus standalone mini-games. All 51 emblems are navigable (5 are fully-built showcase scenes; the rest get a generic sculptural scene + text card).

## Architecture
Entry `src/index.html` → `src/main.js`, a world switcher with **five** tabs: **Hypnerotomachia** (orbitable Fountain of Venus), **Atalanta Animata** (gallery wall of 51 textured woodcut plates → click to enter a scene), **Plates** (2-D image atlas → lightbox with motto/epigram/Enter-3-D), **Tours** (see below), **Archives** (bipartite HP-folio ↔ AF-emblem graph). ES-module importmap pulls Three/GSAP from CDN. Scenes in `src/scenes/` (EmblemScene with OrbitControls, HPScene, ArchivesScene). Committed JSON in `src/data/` (`emblems.json`, `hp_symbols.json`, `tours.json`, …) produced from sibling `atalanta.db`/`hp.db`. Emblem plates self-hosted in `images/emblems/` (relative paths for Pages).

## Tours (models ↔ research)
`tours.json` defines **four** guided journeys whose stops fly the camera through the actual emblem scenes while a right-rail surfaces the research: **The Scholarship** (each emblem's `discourse_summary`), **Chemical Symbolism** (the 10 planetary-metal signs from `hp_symbols.json`, glyph + marginalia-hand notes, paired to emblems), **The Great Work** (Nigredo→Albedo→Citrinitas→Rubedo), and **The Two Books** (generated at runtime from `world_links.json` — the 9 documented HP↔AF cross-references, each pairing a Maier emblem with the Poliphilo folio it answers). The rail composes editorial ledes with the real data at runtime. The **Oracle** and **Fugue Scroll** games also expose each emblem's `discourse_summary` via a collapsible reveal. This is the worked example in [[concept_opportunity_audit]].

## Look & lighting (carved reliefs + diorama)
The 46 non-showcase emblems render as **lit 3-D woodcut reliefs**: the plate image drives a subtle (inverted) displacement map plus a runtime Sobel-derived normal map on a MeshStandardMaterial, so ink lines catch a raking key light as engraved relief (warm parchment tint + contact shadow). 33 of them additionally float their extracted figure cutouts as a **2.5-D parallax diorama** (`scripts/build_diorama.py` → `diorama.json` → `images/cutouts/`; depth inferred from bbox-Y + category). The 5 showcase scenes get the same plate as a dim carved **backdrop**. The gallery wall is now lit emissive-floored plates (bright-safe). Lighting: `RoomEnvironment` IBL (PMREM, no HDRI) + neutral warm-white key / cool fill / stage-tinted rim. Mirrors sibling `C:\Dev\EMBLEMSIN3D\relief.js` (validated against); HPin3D adds runtime normal maps + the cutout diorama. `_applyReliefTextures()` in `src/scenes/EmblemScene.js` is the shared workhorse.

## Fragile parts
`STATUS.md` / `TECH_STACK.md` are stale (claim "NOT STARTED" / list uninstalled Vite/Theatre/Zustand; the real app is CDN-only) — stale-docs trap. Manual cache-bust (`main.js?v=19`, `EmblemScene.js?v=9`). Canvas-sizing + missing-asset traps fixed but recorded in [[environment-health]]. Cross-project DB coupling to sibling HP/Atalanta DBs. Diorama renderer + gallery-wall + relief-tune were shipped under a **wedged preview-screenshot tool** (structurally verified — data/asset 200s, zero console errors, emissive-floor brightness guarantee — aesthetics pending a live eyeball).

## HP rooms (folio-keyed)
The Hypnerotomachia world now cycles **four** orbitable rooms (arrow keys; Archives folio-nodes route by folio): **Fountain of Venus** (f.80), **Planetary Palace** (f.88 — the 7 metals on pedestals, Saturn→Sol→Luna, canvas-glyph plaques), **Three Doors** (f.119 — Virtue / Middle Way / Pleasure portals), **Quinta Essentia** (f.164 — a radiant dodecahedron over the four elements). `HPScene(sceneKey)` branches; `HP_ROOMS` table in `main.js`. Still unmodelled: alchemical_temple (f.28/31), procession (f.162), garden (f.14).

## Status & next
Shipped and live (carved reliefs, 2.5-D diorama, lit gallery wall, 4 tours, 4 HP rooms, games↔research). **Caveat:** the diorama, gallery wall, relief tune, and all 3 new HP rooms shipped under a wedged preview-screenshot tool — structurally verified (build + navigate, zero console errors) but **not yet visually confirmed**; a single live eyeball could redirect a lot of this work. Reconcile stale planning docs to reality once confirmed.
- Tune the diorama depth heuristic / cutout coverage once visually verified; the [[project_emblemprintshop]] cutouts remain the source.

## Related
- [[project_hypnerotomachia]] — marginalia DB (source of `hp_symbols` annotator-hand notes)
- [[project_claudiens]] — Atalanta Fugiens scholarship/DB; source of the web-optimized emblem plates
- [[project_emblemsin3d]] — separately-indexed Atalanta-in-3D effort (confirm whether distinct from this repo; possible lint merge)
- [[project_emblemroguelike]], [[project_emblemnovel]], [[project_alchemybeatemup]] — shared emblem-asset lineage
