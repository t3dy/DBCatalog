---
title: ALCHEMYTIMELINEMAP
type: project
description: An interactive timeline and map of alchemy and chemistry — 500 events from Late Antiquity through the early modern period.
tags: [project, stub, alchemy, timeline, map, database]
updated: 2026-06-27
---

# ALCHEMYTIMELINEMAP

An interactive timeline and map of alchemy and chemistry covering 500 events spanning Late Antiquity through the early modern period across Europe, North Africa, and the Middle East. The pipeline is SQLite → Python (idempotent, SQLite-backed) → static HTML/CSS/JS → GitHub Pages, with no frameworks or runtime dependencies. Agent work is routed through task-specific prompts in `docs/agents/`, with staged agent output validated before ingestion. `PHASESTATUS.md` is the single source of truth for project state.

## Status (2026-06-27)
Live on GitHub Pages; static-site pipeline in place. (README last updated 2026-05-23.)

## Pointers
- `C:\Dev\ALCHEMYTIMELINEMAP\README.md`
- `C:\Dev\ALCHEMYTIMELINEMAP\CLAUDE.md`
- `C:\Dev\ALCHEMYTIMELINEMAP\PHASESTATUS.md`
- Live: https://t3dy.github.io/AlchemyTimelineMap/

Related: [[project_emblemroguelike]] · [[project_theosophicalalchemydb]] · [[concept_database_theories]] · [[index]]
