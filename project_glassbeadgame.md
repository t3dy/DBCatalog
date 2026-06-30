---
title: Glass Bead Game
type: project
description: A browser Glasperlenspiel — place esoteric-history "beads," qualify them with alchemical glyph attributes, and let the engine derive grounded relations between adjacent beads, scored for reconciling opposites and spanning disciplines.
tags: [project, react, typescript, vite, game, esoteric, hesse, leary, raw, alchemy, deckard-boundary, grounding-rule, knowledge-portals, supabase]
updated: 2026-06-27
---

# Glass Bead Game

A web-based *Glasperlenspiel* that fuses three source streams — Hermann Hesse's *Das Glasperlenspiel* (bead/tile synthesis, the "reconciliation of opposites," the "crystal of insights"), Joshua Fost's *Toward the Glass Bead Game* (a concrete RDF/JSON-LD grid of subject–predicate–object triads), and Timothy Leary & Robert Anton Wilson's *Game of Life* / eight-circuit model (progression, reality-tunnel lenses, Maybe Logic). The act of play is interdisciplinary synthesis. It lives at `C:\Dev\glassbeadgame`, is built React + Vite + TypeScript, and is deployed live at https://t3dy.github.io/GlassBeadWebGame/ (repo: https://github.com/t3dy/GlassBeadWebGame).

## What it is

You **draw cards** sourced from real esoteric and intellectual history and **infuse glass beads** on a grid with their significance; you **apply alchemical glyphs** from an always-available bank to qualify what each bead means; and adjacent beads form a triad — a *subject → operation → object* statement. The reward structure prizes triads that **reconcile opposites** (Sol/Luna, Fire/Water) or **span disciplines** (a Bach fugue with an I Ching hexagram). Play is solo (meditative high-score) or **two-player hot-seat** (hands hidden behind a curtain on handoff). A standing **always-a-move invariant** guarantees a legal move from every state: *meditate* (Pass) refills the hand and never deadlocks, and applying a glyph from the bank is a second always-legal floor.

The repository is deliberately scoped to a **playable core**. A large speculative design — a signature-keyed "Adventure Starter" story engine, eight-circuit progression and skill tree, draft phases, private goals, divinatory board modes, worker-placement roles, and online collaborative play — is fully specified under `docs/` and **bracketed** behind the core.

The non-negotiable **Grounding Rule** (the "Golden Rule"): all player-facing content — placeholders, system copy, glyph glosses, card text — must derive from a cited source (Hesse / Leary / RAW, or a knowledge-portal entry). No invented filler; flag-don't-fill when a source is missing.

## Architecture / Data model

A **pure-TypeScript engine** (`src/engine/`, no React, no I/O) is the testable core — a concrete instance of the workspace's [[architecture_deckard_boundary]] discipline (pure logic out of the view). The board is conceptually an **RDF graph of bead–tile–bead triads** serialized as JSON-LD with a `gbg:` namespace (the Fost grounding; full triple/ontology/`DataStore` spec in `docs/DATA_MODEL.md`).

A **model pivot (2026-06-18)** reshaped the realized mechanic away from the original manual process-tile model: glyphs are now **bead attributes** in four banks (Planets/Metals, Zodiac/Processes, Principles, Elements), and **relations are derived programmatically** — the engine compares adjacent beads' attributes against a grounded `RELATION_CORPUS` (`src/engine/relations.ts`; e.g. Ficino's *De Vita* on the benefics against melancholy, the coniunctio, contraries) and scores the result. Persistence is **localStorage behind a `DataStore` interface** (`src/store/dataStore.ts`, key `gbg_save_v1`) so local-first play needs no network.

A **Unified Esoteric Ontology** ("the Crystal") feeds game assets: `tools/ingest/build_corpus.py` (pure stdlib, re-runnable) fuses four study DBs into a static build-time artifact `src/data/corpus/unified.corpus.json` — **2,470 entities · 3,685 relations** (per `unified.manifest.json`: AlchemyTimeline 847e/2044r, MedievalMagicDB 368e/260r, Renaissance Magic/RMDB 829e/479r, TheosophicalAlchemyDB 426e/800r; typeCounts: 300 figures, 551 texts, 471 concepts, 956 events, 62 locations, 178 emblems; `lowConfidence: 0`). The corpus is **lazy-loaded** (its own ~3MB chunk) so the main bundle is untouched if it never loads; `entityToCard()` turns entities into playable cards and `observe.ts` turns the relation graph into cited adjacency situations. This is the [[concept_database_theories]] *Procedural Engine fed by Knowledge Portals* model made concrete.

## Status (2026-06-27) — honest and specific

**Contra the CLAUDE.md line "Scaffolding has not been generated yet" (stale): scaffolding exists, the core is built, and the game is deployed.** The vertical-slice spine is real; the large optional design remains specified-only.

What is actually **built and verified** (per `HANDOVER_CURRENT.md`, `package.json`, and the `src/` tree):
- **Playable prototype, deployed.** Live on GitHub Pages via Actions (note: README/handover say GitHub Pages + Actions; the *planned* host in CLAUDE.md/DEPLOYMENT.md was Vercel + Supabase — the actual deploy is GitHub Pages). End-to-end verified: setup (solo / 2-player) → infuse bead → apply glyph → derived-relation readout (coherence / interdisciplinary / counterpoint) → end turn → hot-seat handoff → conclude → winner.
- **The four core engine systems**: `engine/types.ts`, `engine/engine.ts` (pure `applyMove` reducer; `meditate`/Pass total; `legalMoveKinds` always includes it), `engine/glyphBank.ts`, `engine/relations.ts` (programmatic derived relations), plus `connections.ts`, `occupations.ts` (12-occupation meeple bank), and `content.ts` (the homebrew/DLC overlay).
- **Print Shop** (`content.ts`, persisted `gbg_homebrew_v1`): full editability — edit any card/glyph, copy explanations, forge a new card to hand.
- **DLC packs**: player-curated topical decks (create/edit/export/import as JSON) plus built-in packs in `src/data/dlc/` (alchemists, hermetica, persecution, raw, scholastica, societasMagica, links). The **Societas Magica** DLC was reworked for privacy — Figures · Concepts · Places of pre-modern learned magic, all historical & cited (no living scholars), per `docs/CARD_STYLE_GUIDE.md`.
- **The Crystal layer is live in-game**: a "✦ Draw from the Crystal" action; glyph-attribution at scale (`engine/glyphAttribution.ts`) enriches the ~931 corpus cards from operation/planet/element/principle/stage.
- **Accounts + cloud sync (Phase 5/6): code-complete but NOT live.** Full auth + auto-sync layer (`src/auth/`, `src/store/sync.ts`, `src/store/supabase.ts`, `src/ui/`) with **local-first / graceful guest mode** (runs with no env vars). Backend is a single migration `supabase/migrations/0001_init.sql` (profiles · user_library · games; owner-only RLS; `username_available` RPC). **To go live still requires manual user action**: provision Supabase, run the SQL, disable email confirmation, set the two `VITE_` env vars. Verified only in guest mode ("Guest · local only").
- **Tests**: Vitest, `npm test`. Source tree currently holds **38 `it()` cases across 8 test files** (engine 8, glyphAttribution 6, corpus 6, connections 5, authClient 4, content 3, place 3, userLibrary 3); handover snapshots cite running totals at each milestone (6/6 → 14/14 → 37/37). Includes the always-a-move property test. Builds clean (`tsc -b && vite build`).

What is **specified only / bracketed** (in `docs/`, not built): the correspondence engine v1 + Tier-A **Adventure Starters**; the eight circuits + full scoring depth + Tai Gi win-state; **progression** (character sheet, topic XP, skill tree, portals-as-inventory); **draft phases & private goals**; **board modes** (Tarot/Geomancy/I Ching/Sigil-on-Kamea); **roles/worker-placement** beyond the first meeple cut; **online collaborative** play; the Tree-of-Life skill topology + A∴A∴ grades (an optional overlay, sourced from CROWLEYDB); Tailwind + Framer Motion polish (UI is still plain CSS).

## Tech

TypeScript (strict) · React 18 · Vite 6 · plain CSS ("Green Stone" palette; Tailwind + Framer Motion planned/bracketed) · pure-TS engine reducer · Vitest · localStorage behind a `DataStore` interface · `@supabase/supabase-js` (cloud sync, code-complete, dormant) · GitHub Pages + GitHub Actions (build → test → deploy on push to `main`). Python stdlib for the corpus ingestion tool. Five specialist Claude agents under `.claude/agents/` (magister-ludi orchestrator, crucible-engineer, bead-smith, mirror-warden, narrative-designer), with a per-turn narrative-review protocol and a tickets board.

## Relation to the ecosystem

Glass Bead Game is the **game-shaped consumer** of the same esoteric DH knowledge portals this wiki documents. Where [[project_claudiens]] and the other DH sites are read-mostly scholarship, GBG is a *Procedural Engine fed by Knowledge Portals* — the synthesizing quadrant of [[concept_database_theories]] — ingesting four study DBs into one playable "Crystal." It shares the workspace's [[architecture_deckard_boundary]] instinct (pure TS engine vs. React view) and its Grounding-Rule / provenance discipline, and its plain-CSS, framework-light view layer sits in the same lineage as [[architecture_frontend_patterns]].

Conceptually it operationalizes the user's **RAW/Leary frame** (eight circuits, reality tunnels, Maybe Logic — cf. the wiki's RAW corpus) as game mechanics. It is also the most literal realization of the user's broader **"Correspondence Bus" / portals-as-inventory** idea: cards are translations of portal entries into game terms, "portals" are acquired into a player inventory that opens skill-tree branches, and the lazy-loaded corpus is a correspondence index the engine queries to surface grounded relations between adjacent beads — a playable cousin of the **Memory Palace** retrieval pattern and the [[architecture_context_engineering]] discipline of feeding a procedural surface from a cited store. The orchestration-by-specialist-agents-over-a-wiki workflow mirrors the workspace's [[architecture_prompt_archaeology_machines]] ethos.

## Pointers

- Agent entry point: `C:\Dev\glassbeadgame\CLAUDE.md` (note: its "scaffolding not generated" line is stale).
- Live state: `C:\Dev\glassbeadgame\HANDOVER_CURRENT.md`.
- Phased roadmap + acceptance gates: `C:\Dev\glassbeadgame\PLAN.md`.
- Player-facing overview: `C:\Dev\glassbeadgame\README.md`.
- Highest-priority spec: `docs/GAME_LOOP.md`; mechanics: `docs/MECHANICS.md`; triple/ontology/`DataStore`: `docs/DATA_MODEL.md`; the Crystal: `docs/UNIFIED_ONTOLOGY.md`; card voice + glyph attribution + privacy: `docs/CARD_STYLE_GUIDE.md`; progression: `docs/PROGRESSION.md`; corpus pipeline: `docs/CARD_CORPUS.md`.
- Engine: `src/engine/` (`engine.ts`, `relations.ts`, `content.ts`, `glyphAttribution.ts`). Corpus: `src/data/corpus/unified.corpus.json` + `unified.manifest.json`; ingestion: `tools/ingest/build_corpus.py`. Backend: `supabase/migrations/0001_init.sql`.
