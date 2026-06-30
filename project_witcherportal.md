---
title: WitcherPortal
type: project
description: A DH portal on the Eastern European folklore, history, and magic behind Sapkowski's Witcher saga.
tags: [project, stub, folklore, slavic, witcher, database, dh]
updated: 2026-06-27
---

# WitcherPortal

A digital humanities portal on the Eastern European folklore, history, and magical traditions behind Sapkowski's *Witcher* saga. Its architecture mirrors AtalantaClaudiens: SQLite as source of truth, a Python static-site generator, vanilla HTML/CSS/JS, GitHub Pages–deployable, with no frameworks. The domain model covers folklore creatures (striga, leshy, rusalka), historical events (600–1900 CE), magical traditions (*czary*, dvoeverie, znachorka herbalism, Sendivogian alchemy), regions, and a scholarly bibliography (Brückner, Kolberg, Ivanits). A core constraint keeps Witcher fiction separate from folkloric fact — folklore entries describe the historical/ethnographic creature, with an optional `witcher_connection` field for in-fiction links — and every datum carries provenance. (Distinct from the WitchcraftStudiesDB project.)

## Status (2026-06-27)
Pipeline-driven portal (init → seed → build); per user memory, an active knowledge portal with an interactive trial map.

## Pointers
- `C:\Dev\witcherportal\CLAUDE.md`
- `C:\Dev\witcherportal\README.md`
- `C:\Dev\witcherportal\witcher_seed.json`

Related: [[project_claudiens]] · [[project_witchcraftstudiesdb]] · [[index]]
