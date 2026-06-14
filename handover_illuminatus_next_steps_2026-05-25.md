---
title: "Handover: Illuminatus / RAW Portal Next Steps"
type: handover
description: "Session handover for continuing the Illuminatus and Robert Anton Wilson knowledge portal in a new window."
tags: [handover, illuminatus, raw, next-steps, portal]
---

# Handover: Illuminatus / RAW Portal Next Steps

## Current Goal

Build a Digital Humanities knowledge portal for *The Illuminatus! Trilogy*, Robert Anton Wilson, Discordianism, counterculture, psychedelia, occult/esoteric studies, and related literary networks.

The portal should use the existing project pattern:

- short card summaries for overview and browsing
- longer page essays for close reading
- relational browsing across people, places, texts, concepts, routines, themes, and maps
- interactive maps with hover summaries and click-through reading frames
- source-aware editorial caution around occult, psychedelic, and conspiratorial claims

## Workspace

Primary repo:

`C:\dev\wiki`

Important RAW ingest source directory:

`E:\pdf\RAW HPL PKD WSB etc misc SF\raw_ingest_20260524\ai_md_exports`

The worktree is dirty. Treat existing modified/untracked RAW and Illuminatus files as intentional unless the user explicitly asks for cleanup.

## Files Added Or Advanced In This Window

### Machine-Readable Structure

- `illuminatus_manifest.json`: top-level portal sections, seed entities, project files, and build targets.
- `raw_manifest.json`: RAW biography, associates, books, section cards, and media placeholders.
- `ontology_raw_illuminatus.json`: entity classes, relationship vocabulary, evidence statuses, and placeholder protocol.
- `relationships_raw_illuminatus.json`: initial curated relationship graph for replacing keyword-only relation browsing.
- `map_layers_illuminatus.json`: main atlas and book-specific map layer definitions.
- `map_layers_historical_illuminatus.json`: Historical Illuminatus Europe-travel map layers and route template.

### Writing Seeds

- `illuminatus_concept_cards.md`: first concept-card layer for Discordianism, Operation Mindfuck, reality tunnels, model agnosticism, Chapel Perilous, conspiracy as literary form, occult parody, Qabalah, Thelema, secret societies, paranoia, general semantics, psychedelic epistemology, and media ecology.
- `illuminatus_routine_cards.md`: Burroughs-adjacent routine cards for conspiracy callbacks, bureaucratic control, initiatory confusion, media contagion, occult instruction, Discordian reversal, sexual farce, secret-name catalogs, paranoid detective logic, cosmic jokes, and cut-up proximity.
- `illuminatus_focus_pages.md`: page seeds for `Detective Story`, `Discordian Initiation`, `Conspiracy Cartography`, and `Occult Instruction Manual`.
- `project_illuminatus.md`: now includes a `Manifest Files` section linking the JSON entry points.

### Homepage Work From Earlier

- `index.html` includes search, filters, thematic lenses, sort modes, and a relation drawer.
- The `Illuminatus!` card has a direct `RAW Hub` link to `project_illuminatus_raw.md`.
- Browser verification passed through local HTTP for filtering, searching, and opening the relation drawer.

## Editorial Direction

Write like a literature professor, religious studies professor, esoteric studies scholar, and DH editor working together.

Core rules:

- Use academic encyclopedia style.
- Distinguish evidence, interpretation, speculation, and esoteric association.
- Do not flatten RAW's ambiguity into simple beliefs.
- Preserve irony, masks, initiatory play, paranoia, counterculture rhetoric, and model agnosticism.
- Do not reproduce long copyrighted passages from source texts.
- Use placeholders when details are not verified.

Preferred placeholders:

- `[Need to add more bibliographic detail]`
- `[Need to add more interview detail]`
- `[Need to add more transcript detail]`
- `[Need to add more zine metadata]`
- `[Need to add more source confirmation]`
- `[Need to add more chapter and subplot detail]`
- `[Need to add more location evidence]`

## Progressive Context Rule

Do not load the whole corpus.

Use this order:

1. Style and architecture files.
2. Relevant manifest.
3. Relevant card file.
4. Specific long page only if needed.
5. Source excerpt only when enriching or auditing one entry.

Key files:

- `project_illuminatus_styleguide.md`
- `architecture_context_engineering.md`
- `concept_raw_ontology.md`
- `illuminatus_manifest.json`
- `raw_manifest.json`
- `relationships_raw_illuminatus.json`

## Suggested Next Tasks

1. Add concept pages for the highest-value entries:
   - `Discordianism`
   - `Operation Mindfuck`
   - `Reality Tunnels`
   - `Model Agnosticism`
   - `Chapel Perilous`
2. Add person cards/pages for:
   - Robert Shea
   - Timothy Leary
   - William S. Burroughs
   - Philip K. Dick
   - Kerry Thornley
   - Aleister Crowley
3. Create normalized JSON card records from the existing markdown files.
4. Build an actual `illuminatus.html` prototype using:
   - manifest-driven sections
   - concept/routine/focus cards
   - relation graph from `relationships_raw_illuminatus.json`
   - map layer placeholders from the map JSON files
5. Prototype the map UI with Leaflet or MapLibre:
   - main all-locations map
   - layer controls
   - hover summaries
   - click-through reading frame
6. Begin location extraction from `raw_book_illuminatus.md` and `raw_book_the_earth_will_shake.md`, but only summarize and cite; do not copy extended passages.

## Current Risks

- Many entities are seeded from card-level summaries, not full source audit.
- Location data is not yet verified.
- Relationship graph is intentionally conservative and incomplete.
- RAW media, zines, and interviews still need bibliographic verification.
- Some official/public web sources may have changed; browse and cite if current publication or archive status matters.

## Useful Commands

Validate JSON:

```powershell
Get-ChildItem -Name illuminatus_manifest.json,raw_manifest.json,ontology_raw_illuminatus.json,relationships_raw_illuminatus.json,map_layers_illuminatus.json,map_layers_historical_illuminatus.json | ForEach-Object { $null = Get-Content -Raw $_ | ConvertFrom-Json; "$_ ok" }
```

Find RAW/Illuminatus files:

```powershell
rg --files | rg "raw_|illuminatus|ontology|manifest|relationships|map_layers"
```

Check worktree:

```powershell
git status --short
```

## Best Next Move

Build `illuminatus.html` as a manifest-aware portal prototype rather than adding more static prose first. The manifest now knows about the concept, routine, and focus-page seed files, so the next window can make the writing, maps, and relation graph browseable immediately.
