---
name: project_fuguejukebox
description: NES-style chiptune variations of Maier's 50 Atalanta Fugiens emblem fugues — 10 treatments per emblem, 500 MP3s.
type: project
status: STABLE
tags: [audio, chiptune, atalanta, python, pipeline]
---

# Project: FUGUEJUKEBOX

**Location** · `C:\Dev\FUGUEJUKEBOX` — **Type** · offline audio-generation pipeline — **Stack** · Python 3 + scipy + ffmpeg — **Verified** · spot-check per project MANIFEST (not re-run this session)

## What it is
An offline pipeline generating NES-style chiptune variations of the 50 fugues in Maier's *Atalanta Fugiens* — 10 treatments per emblem (500 MP3s total).

## Architecture
Two stages. `generate_variations.py` parses EmblemRoguelike's `fugues.json` → per-emblem `variations.json` (3 harmonic + 3 scale-run + 4 effects). `render_to_audio.py` synthesizes square-wave audio (ADSR + reverb/vibrato/delay) and exports MP3 via ffmpeg. `build_all.py` runs both. Output: 500 MP3s in `emblems/`.

## Fragile parts
External ffmpeg dependency on the export path. Hardcoded C-major scale + simple triadic harmony. Reads sibling `EmblemRoguelike/assets/fugues.json` — breaks if that path moves.

## Status & next
Reported COMPLETE (500 MP3s + build logs). NSFRIPPER / live-REAPER integration explicitly out of scope.

## Related
- [[project_emblemroguelike]] — fugue data source + square-wave synth lineage
- [[project_nesmusictools]] — broader NES/chiptune tooling family
- [[project_claudiens]], [[project_emblemnovel]] — shared Maier corpus
