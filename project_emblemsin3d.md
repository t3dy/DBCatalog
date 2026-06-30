---
name: project_emblemsin3d
description: Walkable three.js 3D worlds rendering Maier's Atalanta Fugiens emblems as carved woodcut reliefs with 8-bit fugues.
type: project
status: ACTIVE
tags: [3d, emblems, threejs, atalanta, webaudio]
---

# Project: EMBLEMSIN3D

**Location** · `C:\Dev\EMBLEMSIN3D` — **Type** · static ES-module web app (no build) — **Stack** · three.js 0.160 via jsDelivr importmap, Canvas2D, WebAudio NES-APU synth, Python catalog generators — **Verified** · none this session

## What it is
A mature multi-page 3D site rendering Maier's *Atalanta Fugiens* emblems as carved woodcut reliefs you can walk through, scored with 8-bit fugues; ~1,500-plate catalog.

## Architecture
Multi-page static site; each `.html` pairs with a `.js`. Entry `index.html` → `main.js` (Emblem VIII courtyard + lab + Sobel ink shader). Hubs: `gallery.html`, `grandtour.html`, `jukebox.html`, `experiments.html`, `scene.html?id=`. Generated data in `catalog.js`/`emblemdata.js`/`emblem_explanations.js`. Serve with `python -m http.server`.

## Fragile parts
Hardcoded `C:/Dev`-root serving + cross-project reads (`EmblemRoguelike/assets/fugues.json`, Claudiens DB) — breaks if siblings move. CDN dependency (offline-fragile). Placeholder for missing `diogenes-1688.jpg`. Luminance-Sobel outlines flagged for replacement. **`ANTIGRAVEMBLEMSIN3D` is a scratch Vite fork that verbatim-mirrors this repo, adds `antigrav.html`/`gameforge.html`, and sets `vite fs.allow:['..']` — exposing all of `C:\Dev`.**

## Status & next
Runs and is feature-rich (gallery, grand tour, jukebox, Emblem VIII flagship). TODO: promote woodcuts to full scenes; replace Sobel outlines.

## Related
- [[project_claudiens]] — Atalanta Fugiens DB
- [[project_hpin3d]] — sibling HP-in-3D
- [[project_occultimgdb]], [[project_emblemroguelike]], [[project_alchemytimelinemap]]
