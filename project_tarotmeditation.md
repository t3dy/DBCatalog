---
name: project_tarotmeditation
description: Browser canvas annotator for marking up tarot card images with Sefiroth / Tree-of-Life overlays.
type: project
status: STABLE
tags: [tarot, canvas, annotation, static-site]
---

# Project: TarotMeditation

**Location** · `C:\Dev\TarotMeditation` — **Type** · single-page static web app — **Stack** · vanilla HTML/CSS/JS (HTML5 canvas), no build, no deps — **Verified** · functional standalone file (serve + open)

## What it is
A lightweight browser tool for annotating tarot card images with Sefiroth / Tree-of-Life overlays.

## Architecture
One 925-line `index.html` ("Tarot Sefiroth Annotator"). Three stacked canvases (background card / annotation / draw) + a 300px control sidebar; state serialized to localStorage as JSON. `.claude/launch.json` runs `npx serve -p 5500 .`. Pure client-side.

## Fragile parts
Persistence is localStorage-only (no export/cloud; data lost on cache clear). Monolithic single-file. No dependency pinning. (`CDevTarotMeditation` does not exist — not a duplicate.)

## Status & next
Functional standalone tool.

## Related
- [[project_tarotdev]] — the larger sibling: a tarot knowledge DB / scholarship pipeline (different domain — data vs. annotation UI)
