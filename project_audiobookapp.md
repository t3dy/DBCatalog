---
title: audiobook-app (AudiobookPlayer)
type: project
description: A personal-use Android audiobook player with read-along PDF/text that auto-syncs to playback.
tags: [project, stub, android, kotlin, audio]
updated: 2026-06-27
---

# audiobook-app (AudiobookPlayer)

A personal-use Android audiobook player that browses local audio folders (via SAF), plays with progress persistence, makes bookmarks and clips, exports clips as real audio files, and — the newer direction — reads along with an associated PDF/text document that auto-syncs to playback. Built in Kotlin with Jetpack Compose, Room, Media3/ExoPlayer, and Coroutines+Flow, using manual DI (no Hilt), targeting Android 10+ (API 29+), offline-first with no backend. The architecture enforces strict layering (UI → ViewModel → Repository → DAO/Storage), a single repository data door, and `MediaService` as the sole player owner. `HANDOVER.md` is the single source of truth for current state.

## Status (2026-06-27)
Active personal project; status tracked in HANDOVER.md (not in CLAUDE.md).

## Pointers
- `C:\Dev\audiobook-app\CLAUDE.md`
- `C:\Dev\audiobook-app\HANDOVER.md`
- `C:\Dev\audiobook-app\docs\DECISIONS.md`

Related: [[architecture_frontend_patterns]] · [[index]]
