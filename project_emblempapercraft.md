---
name: project_emblempapercraft
description: Layered paper pop-up (papercraft) viewer rendering Atalanta Fugiens emblems as shadow-cast stacked cutouts in their original engraving style.
type: project
status: ACTIVE
tags: [3d, emblems, threejs, papercraft, atalanta, shadows]
---

# Project: EmblemPapercraft

**Location** · `C:\Dev\EmblemPapercraft` — **Live** · https://t3dy.github.io/EmblemPapercraft/ (repo `t3dy/EmblemPapercraft`, GitHub Pages) — **Type** · static Three.js viewer — **Stack** · Three.js r168 (CDN importmap, no build) · OrbitControls · PCF soft shadow maps · ACES — **Verified** · 2026-07-01, **visually** (screenshot tool recovered): dim/blank backings both read as genuine paper shadow-boxes; Emblem V pops as figures + architecture over a recessed page.

## What it is
Renders each of the 51 *Atalanta Fugiens* emblems as a **layered paper pop-up**: the extracted figure cutouts are stacked as flat "paper" cards in front of the full plate and lit so every card casts its cut shape as a shadow onto the layers behind it — 3-D through shadow, not geometry, keeping the original woodcut linework. The papercraft counterpart to [[project_hpin3d]]'s carved *reliefs* of the same plates.

## The core technique
Depth reads from **shadow**, so each cutout mesh gets `customDepthMaterial = MeshDepthMaterial({ map, alphaTest, depthPacking: RGBADepthPacking })` — the shadow is the cut silhouette, not the bounding rectangle. A warm raking `DirectionalLight` (shadow map on) throws those shapes onto the backing page, a backing board, and a table. Full plate = backing page; cutouts lift forward by an inferred depth (a "pop depth" slider scales it).

## Architecture
`index.html` (UI + importmap) → `js/papercraft.js` (renderer, nav, depth). Data self-contained: `data/emblems.json` (labels), `data/layers.json` (per-emblem cutout manifest: `cx,cy,nw,nh,depth,file`), `images/emblems/` (51 plates), `images/cutouts/` (143 cutouts across 51 emblems; 33 have ≥2 layers → a real pop-up, sparser plates show flat). `scripts/build_layers.py` regenerates from [[project_emblemprintshop]]. Viewport fallback + resize-retry guard the 0-dimension-boot NaN-aspect trap ([[environment-health]]).

## Look controls
A **backing mode** toggle (plate / dim / blank, default *dim*) sets how the page reads behind the pops: *dim* darkens the engraving so bright cutouts stand out; *blank* is a pure cream shadow-box; *plate* keeps the full plate. A **pop-depth** slider scales the lift. `gallery.html` is the examples index — a "richest pop-ups" featured row (8 emblems with ≥5 layers) over all 51, each card deep-linking `index.html?emblem=N`.

## Status & next
Shipped + **live** on GitHub Pages (refined: backing modes, stronger shadows, examples gallery, deep-linking). Next: per-card paper thickness/curl; a fold-flat → pop-up animation; print-ready net/tab export for building the models in real paper; optionally denuded backings via inpainting.

## Related
- [[project_hpin3d]] — sibling; carves the same plates into 3-D reliefs + a 2.5-D diorama (shares the cutout pipeline)
- [[project_emblemprintshop]] — source of the 743 labelled figure cutouts
- [[project_claudiens]] — Atalanta Fugiens scholarship/DB; ultimate source of the plates
