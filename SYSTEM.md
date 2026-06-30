---
name: system
description: How LLMs operate inside the wiki — principles, the four operations, the verify-before-done gate. Read this first when working in C:\Dev\wiki.
type: system
tags: [governance, operations, meta]
---

# Wiki Operating System

The single always-read doc for working in `C:\Dev\wiki`. Keep it short — every line
here is paid on each read. Detail lives in on-demand pages, not here.

## Principles

1. **Reality over design.** Measurements, builds, and query results beat documentation
   and speculation. When they conflict, the wiki is wrong — fix the wiki.
2. **Outward not deeper.** Surface what exists before adding more. A thin accurate page
   beats a thick speculative one.
3. **Honesty before completion.** Document what you could *not* verify. Never report a
   task done on assumption. See the gate below.

## The Four Operations

- **Ingest** — read a source project, write/refresh `project_<slug>.md` from the template
  in [[style]], add it to `index.md`, append an entry to `log.md`.
- **Synthesize** — answer a cross-project question by reading the relevant pages; if the
  answer is reusable, file it as a new concept/strategy page and index it.
- **Lint** — hunt stale claims, dead `[[links]]`, orphans, contradictions. Fix them and
  log it. Anything that turned out false also gets an entry in [[audit-failures]].
- **Handoff** — at session end, record what changed, what was verified, and what remains
  in the source project's own `PHASESTATUS.md` (not here).

## The Verify-Before-Done Gate

Before writing "done", "complete", "deployed", or "working" anywhere, confirm against
real output — not against the edit you just made:

- **Build** ran clean (keep the tail of the output).
- **Live URL** responds and renders (one concrete data point you changed is visible).
- **Data** writes confirmed by query (row counts before/after), not inferred.
- **Hidden coupling** traced: hardcoded lists, unrun fetch scripts, build-time generation.
  Grep before you trust. See [[environment-health]] for the known traps.

If you cannot verify a thing, say so plainly and stop short of the completion claim.
If you discover a new failure mode, add it to [[environment-health]] and [[audit-failures]].

## Pointers

- Writing style + the project-page template → [[style]]
- Known fragile codepaths and silent-failure traps → [[environment-health]]
- Chronological record of what broke and why → [[audit-failures]]
- Navigation hub → `index.md` · change log → `log.md`
- Resolve "my X projects" (e.g. "my alchemy databases") → [[registry]] (+ generated `registry.tsv`)
