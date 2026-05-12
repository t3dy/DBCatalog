# Project: Bach Studies

**Location**: `C:\Dev\BachStudies`
**Type**: Digital Humanities Database

## Overview
A project presenting scholarly research and analysis related to Bach Studies. It strictly utilizes the standard "DH Framework" developed across the other Digital Humanities repositories.

## Architecture & Invariants
- **Pipeline**: SQLite (source of truth) → Python Scripts → Static HTML/CSS/JS → GitHub Pages.
- **System Invariants**:
  1. Data flows ONE direction: Source → DB → HTML.
  2. Generated HTML is never edited directly.
  3. The database is never edited directly (only via pipeline scripts).
  4. All content carries explicit provenance markers (`source_method`, `review_status`, `confidence`).
  5. AI-generated content defaults to DRAFT/MEDIUM and cannot auto-promote.

## Related Entities & Concepts
- [[Johann Sebastian Bach]]
- [[Digital Humanities]]
- [[DH Framework]]
