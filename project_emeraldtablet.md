---
title: "Project: HermeticDB (EmeraldTablet)"
type: project
description: "Authoritative scholarly reference portal for the history of Hermeticism. SQLite → Python → static HTML/CSS/JS → GitHub Pages. Modeled on the Dictionary of Gnosis and Western Esotericism."
tags: [hermeticism, digital-humanities, encyclopedia, sqlite, static-site]
---

# Project: HermeticDB (EmeraldTablet)

**Location**: `C:\Dev\EmeraldTablet`
**Repo**: `t3dy/HermeticDB`
**GitHub Pages**: serves from `docs/`
**Current Phase**: Phase 4 — Dictionary Architecture + Content Depth

## Overview

An authoritative scholarly reference portal for the history of Hermeticism — the textual tradition centered on Hermes Trismegistus from Late Antiquity through modernity. Built to the historiographical standards of Wouter J. Hanegraaff and modeled explicitly on the *Dictionary of Gnosis and Western Esotericism* (Brill, 2006).

Three constituencies: (1) scholars, (2) students, (3) serious independent researchers. Designed for relational browsing — every entity links to at least 3 others.

## Architecture

SQLite → Python pipeline → static HTML/CSS/JS → GitHub Pages. Python stdlib only.

- **Database**: `db/emerald_tablet.db`
- **Deploy script**: `HERMETICDB/scripts/DEPLOY_PORTAL.py`
- **Ingestion scripts**: `scripts/`

## Current DB Size (2026-05-17)

- 84 texts, 90 persons, 74 concepts, 34 timeline events
- concept_links table: populated but NOT rendered (critical gap)
- Most prose fields under target word counts (content depth is Phase 4 priority)

## System Files (overhauled 2026-05-17)

| File | Purpose |
|------|---------|
| `PROMPTS.md` | Canonical vision — read first every session |
| `STYLEGUIDE.md` | Precise word counts + section templates per content type |
| `CLAUDE.md` | Claude Code entry point + routing table |
| `AGENTS.md` | Agent-specific rules + vocabulary lock |
| `PHASESTATUS.md` | DB row counts + phase goals |
| `TAKEAWAYS1.md` | Lessons from prior DH projects |

## Content Standards (from STYLEGUIDE.md)

| Content Type | Min Words | Max Words | Lit. Items | Internal Links |
|---|---|---|---|---|
| Dictionary — index card | 60 | 120 | — | — |
| Dictionary — encyclopedia | 1,500 | 2,500 | 8 | 3 |
| Person biography | 1,200 | 2,200 | 5 | 3 |
| Text analysis | 1,000 | 1,800 | 5 | 2 |
| Timeline event | 100 | 250 | — | — |

## Dictionary Architecture (Phase 4)

Two-level system:
1. `/dictionary/[slug].html` — encyclopedia pages (Level 2, 1,500–2,500 words)
2. `/concepts/[slug].html` — relational browsing pages (concept_links rendered)
3. `/dictionary/index.html` — index card grid with filtering

## Historiographical Framework

- Actor/Analyst distinction (Hanegraaff) — NEVER collapsed
- No reification of "Hermeticism" as a bounded tradition
- Medieval continuity: 12th–13th c. Latin tradition not a break from Renaissance
- Arabic transmission is central (Jabir, al-Kindi, Picatrix, Harran Sabians)
- Yates Paradigm is contested — present with named critics (Hanegraaff, Copenhaver)

## Key Source on Disk

`C:\Users\PC\Downloads\Wouter J. Hanegraaff (editor) - Dictionary of Gnosis & Western Esotericism (2006, Brill Academic Publishers) - libgen.li.pdf`

## Agent Swarm Pattern

Three agent types (all staging-file pattern, no Bash):
- **Type A** — Dictionary Encyclopedia Writer (→ `staging/dictionary/[slug].json`)
- **Type B** — Biography Enricher (→ `staging/persons/[slug].json`)
- **Type C** — Relational Auditor (→ `staging/concept_links.json`)

See `PROMPTS.md` Part VI for full specs.
