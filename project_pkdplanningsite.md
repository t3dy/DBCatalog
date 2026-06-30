---
name: project_pkdplanningsite
description: Single-page site teaching the "PKD Planning System" — 33 Claude Code slash commands named after Philip K. Dick characters.
type: project
status: STABLE
tags: [pkd, claude-code, tooling, vite, showcase]
---

# Project: PKD Planning Site

**Location** · `C:\Dev\pkd-planning-site` — **Type** · Vite SPA (dev-tooling showcase) — **Stack** · React 19, TS, Vite 8, Tailwind v4, GitHub Actions Pages — **Verified** · live at t3dy.github.io/pkd-planning-site (`dist/` present)

## What it is
A single-page site documenting the "PKD Planning System" — 33 Claude Code slash commands named after Philip K. Dick characters; a meta-doc of the user's own planning/slash-command discipline.

## Architecture
Vite SPA; `index.html` mounts `#root` via `src/main.tsx` → `src/App.tsx` (nearly all logic in one component). Skill content loaded from root `skill-texts.json` (~58 KB). Features: skill cards, quiz, mini-game, workflow slider.

## Fragile parts
Requires `npm install --legacy-peer-deps` (peer-dep conflicts). Monolithic single `App.tsx`.

## Status & next
Built and deployed.

## Related
- [[project_querypat]] — shares the PKD motif (this is about dev workflow, not the author)
- [[project_pkdfestsite]] — sibling PKD-themed site
