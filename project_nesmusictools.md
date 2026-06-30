---
name: project_nesmusictools
description: A family of NES/chiptune → REAPER music tools (extraction, MIDI, 2A03 synth, render pipelines) descending from NSFRIPPER.
type: project
status: ACTIVE
tags: [music, nes, chiptune, reaper, python, cluster]
---

# Project: NES Music Tools (cluster)

**Location** · `C:\Dev\` (multiple dirs) — **Type** · audio tooling family — **Stack** · Python, REAPER RPP/ReaScript, JSFX 2A03 synth, NSF/ROM traces, MIDI — **Verified** · none this session

## What it is
One evolving project family (Mar–Jun 2025) for turning NES game music into NES-accurate audio and REAPER projects, descending from [[project_nsfripper]] (the Konami 6502/Bach root ancestor).

## Members
| Dir | Role | Status |
|---|---|---|
| `NESMusicStudio` | NSF/ROM → MIDI → REAPER/WAV/MP4 → YouTube pipeline (largest) | active, committed |
| `REAPERBEYONDNES` | Multi-system (NES→GBA) extract/arrange/synth; declared NSFRIPPER successor (broadest) | active, **not git** |
| `NESjamtools` | Game music + MIDI → NES-accurate audio/REAPER (newest) | active, **not git** |
| `ReapNES-Studio` | REAPER 2A03 JSFX synth + live keyboard env | active, committed |
| `nes-music-lab` | Research-grade extraction/reconstruction, provenance-focused | stalled, uncommitted |
| `arpeggiator-composer` | Deterministic MIDI arpeggiator for REAPER | stalled, uncommitted |
| `NESARPEGDESIGNS` | empty stub | never started |

## Fragile parts
`REAPERBEYONDNES` and `NESjamtools` are **not git repos** (loss risk). `nes-music-lab` and `arpeggiator-composer` have git but zero commits (work uncommitted on disk). `NESARPEGDESIGNS` is empty.

## Status & next
Live frontier: `NESMusicStudio` (YouTube endpoint) + `REAPERBEYONDNES` (multi-chip). Recommend `git init` + initial commit on the two non-git actives to stop loss risk.

## Related
- [[project_nsfripper]] — root ancestor (Konami 6502/Bach)
- [[project_fuguejukebox]] — adjacent chiptune generator (Atalanta fugues)
- [[project_bachstudies]] — Bach-mashup thread
