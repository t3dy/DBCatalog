---
name: environment-health
description: Living registry of fragile codepaths and silent-failure traps across C:\Dev projects. Check the relevant row before editing a project; add a row when you find a new trap.
type: reference
status: ACTIVE
tags: [health, fragility, traps, meta]
---

# Environment Health Registry

On-demand reference (not loaded every session). Before editing a project, read its rows.
When you discover a new trap, add a row here **and** log the incident in [[audit-failures]].

## Silent-failure traps

These do not error — they quietly do the wrong thing. The most dangerous class.

| Project | Trap | Symptom | Mitigation |
|---|---|---|---|
| HPMarginalia | `build_site.py` reads a **hardcoded scholar list**; depends on a separate `fetch_catalog`-style step | Editing `sources`/DB alone leaves the live site unchanged | Trace the build inputs; run the fetch step; rebuild; verify the rendered page |
| HPMarginalia | Image analysis on `images.web_path` (compressed) instead of `images.master_path` | Degraded/invalid vision readings | Always use `master_path`; call `assert_not_web_derivative()` first |
| ESOFEED / EsotericBeatNews | Two-stage: `fetch_catalog.py` (local) then `build.py` (CI). Editing `sources.json` alone does nothing | Feed/site doesn't reflect source edits | Run fetch locally, commit `catalog.json`, then build; verify rendered `site/` |
| Esoteric* portals | Static-site builders generate HTML at build time from JSON/DB | Source edits "don't show up" until the builder reruns | Identify the generator; rerun; diff the output |
| Corpus jobs | Rate-limit truncation corrupts agent JSON writes mid-batch | Malformed/short JSON, field-name mismatches | Write each batch to its own file; validate schema before merge |
| Emblem-3D family, FUGUEJUKEBOX, MemoryPalace, AlchemyBeatEmUp | **Hardcoded absolute `C:\Dev\...` paths** + cross-project reads (e.g. `EmblemRoguelike/assets/fugues.json`, `Claudiens/site/images/emblems` at `AlchemyBeatEmUp/scripts/03_pixelate_emblems.py:27`, `WIKI=C:\Dev\wiki`) | Silent break / wrong data if a sibling project moves or is renamed | Treat sibling paths as a dependency; grep for `C:\Dev` literals before moving anything |
| HPin3D (and others) | **Stale planning docs** (`STATUS.md` says "NOT STARTED" while app is shipped; `TECH_STACK.md` lists uninstalled deps) | Docs contradict reality; misleads the next session | Trust the code over the doc; reconcile or mark docs aspirational |

## Runtime / build fragility

| Project | Fragile codepath | Note |
|---|---|---|
| EmblemRoguelike / *in3D | `Object3D.position` assigned as if writable | It's read-only; mutate `.position.set(...)` or `.copy(...)` |
| Three.js scenes | Over-aggressive woodcut/shader passes | Can black out most of the frame; verify with a screenshot, not just a clean console |
| JS modules | Duplicate `const` declarations (e.g. redeclared `left`) | Breaks module load entirely; lint on edit |
| SocMagWeb | Session cookie unsigned/forgeable | Privilege-escalation risk (SM-024 class); gate auth paths in review |
| ANTIGRAVEMBLEMSIN3D | `vite.config` sets `fs.allow: ['..']` | Dev server can serve all of `C:\Dev` | Scope `fs.allow` to the project; don't expose the drive root |
| NESjamtools, REAPERBEYONDNES, Bookstore, antigravbeadgame | **Working copy not under git** (no `.git`) | Uncommitted work can be lost; no history/recovery | `git init` + initial commit on actives; treat non-git dirs as volatile |

## Context / credentials traps

| Trap | Reality | Mitigation |
|---|---|---|
| "I lack DB/Supabase access" | Credentials usually already in `.env*` or dropped earlier in-session | Check `.env`, `.env.local`, repo secrets **before** asking |
| "What's the live URL?" | The site was built here; the URL is knowable | Record live URL + repo + deploy target on each project page |
| "Built the wrong artifact type" | Concept catalog vs. citation tracker, etc. | Confirm the exact deliverable type before building, not after |

## How to extend

Add a row in the right table, keep it to one line, and cross-link the incident in
[[audit-failures]]. Do not narrate — this is a lookup table, not prose.
