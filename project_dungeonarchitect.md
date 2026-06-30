---
title: dungeon-architect
type: project
description: A gamified learning system framing a decision engine with a dungeon-exploration metaphor, built on XState and SQLite.
tags: [project, stub, learning, decision-engine, react, xstate]
updated: 2026-06-27
---

# dungeon-architect

A gamified learning system — a decision engine wrapped in a dungeon-exploration metaphor (per its package description). The implementation is a TypeScript/React 19 app using XState (`xstate`, `@xstate/react`) for the `dungeon-machine` state machine, `better-sqlite3` for storage, and Vite for dev, with an event-log layer (`event-log.ts`, `browser-event-log.ts`) suggesting an event-sourced model. A "slice 1" test harness (`test-slice1.ts`, run via `tsx`) indicates vertical-slice development. The folder has no README/CLAUDE; this stub is grounded in `package.json` and `src/`. Per user memory, the v1 scope is frozen with an event-sourced character model and three projections.

## Status (2026-06-27)
Early build (v0.1.0); slice-1 scaffolding present, no in-repo docs yet.

## Pointers
- `C:\Dev\dungeon-architect\package.json`
- `C:\Dev\dungeon-architect\src\dungeon-machine.ts`
- `C:\Dev\dungeon-architect\src\test-slice1.ts`

Related: [[project_vibecoding]] · [[index]]
