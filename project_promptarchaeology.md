---
name: project_promptarchaeology
description: Read-only distant-reading tool surfacing patterns in the user's own ~1.45M LLM prompts (over megabase.db).
type: project
status: ACTIVE
tags: [prompt-archaeology, megabase, sqlite, distant-reading, python]
---

# Project: promptarchaeology

**Location** · `C:\Dev\promptarchaeology` — **Type** · CLI analysis tool + static site — **Stack** · Python + SQLite (read-only views), GitHub Pages — **Verified** · dated reports through 2026-06-28 present (not re-run this session)

## What it is
A read-only "distant reading" tool that surfaces patterns in the user's own ~1.45M LLM prompts — values, obsessions, pushbacks — over the megabase corpus. Backs the `promptarchaeology-heldscalla` coaching skill.

## Architecture
Two TEMP SQLite views (`pa_prompts`, `pa_cascades`) isolate the `role='user'` subset of `C:\Dev\megabase\megabase.db` (opened read-only, `mode=ro`). Named `queries/NN_*.sql` files run via `tools/run.py <name>` (partial match) → dated `reports/*.md`. `tools/chunk_cascade.py` splits a large conversation into prompt-only chunks; `coach.py` + `build_site.py` drive the skill and static site. Entry points: `tools/run.py`, `tools/chunk_cascade.py`.

## Fragile parts
Hardcoded absolute path to the external `C:\Dev\megabase\megabase.db` — breaks if megabase moves/renames (see [[environment-health]]). All analysis depends on the megabase schema (`messages.role`, `conversations`) it does not own.

## Status & next
Active; reports generated through late June 2026.

## Related
- [[project_megabase]] — the upstream 1.45M-prompt corpus it reads
- [[project_socialsdb]] — sibling personal-data mining hub
