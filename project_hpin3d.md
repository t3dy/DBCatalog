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
`tours.json` defines three guided journeys whose stops fly the camera through the actual emblem scenes while a right-rail surfaces the research: **The Scholarship** (each emblem's `discourse_summary`), **Chemical Symbolism** (the 10 planetary-metal signs from `hp_symbols.json`, glyph + marginalia-hand notes, paired to emblems), **The Great Work** (Nigredo→Albedo→Citrinitas→Rubedo). The rail composes editorial ledes with the real data at runtime. This is the worked example in [[concept_opportunity_audit]].

## Look & lighting (carved reliefs)
The 46 non-showcase emblems render as **lit 3-D woodcut reliefs**: the plate image drives a subtle (inverted) displacement map plus a runtime Sobel-derived normal map on a MeshStandardMaterial, so ink lines catch a raking key light as engraved relief. The 5 hand-built showcase scenes get the same plate as a dim carved **backdrop** behind their animated figures. Lighting is `RoomEnvironment` image-based light (PMREM, no HDRI) + a neutral warm-white key / cool fill / stage-tinted rim rig — neutral key so forms read, saturated colour reserved for mood. Technique mirrors sibling `C:\Dev\EMBLEMSIN3D\relief.js` (which this validated against); HPin3D adds the runtime normal maps. `_applyReliefTextures()` in `src/scenes/EmblemScene.js` is the shared workhorse.

## Fragile parts
`STATUS.md` / `TECH_STACK.md` are stale (claim "NOT STARTED" / list uninstalled Vite/Theatre/Zustand; the real app is CDN-only) — stale-docs trap. Manual cache-bust (`main.js?v=16`, `EmblemScene.js?v=7`). Canvas-sizing + missing-asset traps fixed but recorded in [[environment-health]]. Cross-project DB coupling to sibling HP/Atalanta DBs.

## Status & next
Shipped and live. Reconcile stale planning docs to reality. Concrete next fronts:
- **Layered diorama**: [[project_emblemprintshop]] has 743 labelled transparent-PNG cutouts across all 51 emblems (per-emblem `summary.json` with bbox, category, iconographic meaning) — usable as 2.5-D parallax cutout layers, but needs a depth-ordering pass (no Z metadata; infer from bbox-Y + detection order).
- Extend tours to draw on the broader corpus ([[project_claudiens]], [[project_hypnerotomachia]] marginalia); deeper HP rooms; light the gallery wall as carved plates.

## Related
- [[project_hypnerotomachia]] — marginalia DB (source of `hp_symbols` annotator-hand notes)
- [[project_claudiens]] — Atalanta Fugiens scholarship/DB; source of the web-optimized emblem plates
- [[project_emblemsin3d]] — separately-indexed Atalanta-in-3D effort (confirm whether distinct from this repo; possible lint merge)
- [[project_emblemroguelike]], [[project_emblemnovel]], [[project_alchemybeatemup]] — shared emblem-asset lineage
