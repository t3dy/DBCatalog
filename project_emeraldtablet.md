# Project: HermeticDB (EmeraldTablet)

**Location**: `C:\Dev\EmeraldTablet`
**Type**: Zero-Loss Knowledge Portal

## Overview
A deterministically-grounded repository and web portal for tracking Hermetic, Alchemical, and Neoplatonic textual transmission. Unlike the standard DH static HTML architecture, this project uses a more complex frontend stack and an advanced ingestion pipeline.

## Architecture
- **Backend / Ingestion**: A multi-pass autonomous Python pipeline.
  - *Pre-Processing*: Parsed 70+ academic volumes into 10,000+ atomic segments.
  - *Extraction*: Swarm agent extraction identified figures, manuscripts, and concepts.
  - *Synthesis*: 7,003 atomic claims harvested with verbatim citations and woven into Wikipedia-style scholarly articles.
- **Frontend**: Next.js 15 Application (Static Site Generation - SSG).
- **Truth State**: Stored in `db/emerald_tablet.db` (SQLite).

## Key Features
- **Chronological Era Navigation**: Organized by Antiquity, Medieval, and Renaissance periods.
- **Relational Browsing**: Bi-directional links between scholars, concepts, and primary source texts.
- **Provenance Tooltips**: Every claim has instant verification directly back to the source document, achieving a "zero-loss" data pipeline.

## Related Entities & Concepts
- [[Hermeticism]]
- [[Alchemy]]
- [[Neoplatonism]]
- [[Emerald Tablet]]
- [[Knowledge Graphs]]
