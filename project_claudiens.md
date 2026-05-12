# Project: AtalantaClaudiens

**Location**: `C:\Dev\Claudiens`
**Type**: Digital Humanities Website

## Overview
A digital humanities website showcasing H.M.E. De Jong's scholarship on Michael Maier's *Atalanta Fugiens* (1618). This is an alchemical emblem book combining 50 engraved plates, Latin mottos, epigrams, prose discourses, and three-voice musical fugues.

## Key Features
- **Emblem Views**: Presents all 50 emblems with comparative views (original source material alongside scholarly commentary).
- **Scholarship Cross-Referencing**: Integrates scholarship from De Jong, Tilton, Craven, Wescott, Pagel, Miner, and others.
- **Source Mapping**: Maps Maier's textual sources (e.g., *Turba Philosophorum*, *Rosarium*, *Tabula Smaragdina*, Ovid) directly to individual emblems.
- **Reference Tools**: Provides an alchemical dictionary, reception timeline, and bibliography.
- **Data Provenance**: Every piece of data is marked by its source method (Deterministic, Corpus Extraction, LLM Assisted, Seed Data, Human Verified), review status, and confidence level. LLM-assisted content is visually marked with review badges.

## Architecture & Tech Stack
- **Flow**: Source Corpus (.md) → Python Scripts → SQLite → `build_site.py` → Static HTML → GitHub Pages.
- **Stack**: Pure HTML/CSS/JS served from GitHub Pages. No frameworks, build tools, or runtime dependencies.

## Related Entities & Concepts
- [[Michael Maier]]
- [[Atalanta Fugiens]]
- [[H.M.E. De Jong]]
- [[Digital Humanities]]
- [[Alchemy]]
