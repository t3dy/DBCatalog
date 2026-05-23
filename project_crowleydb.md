# Project: CrowleyDB

**Location**: `C:\Dev\CrowleyDB`
**Type**: Knowledge Portal

## Overview
A comprehensive scholarly portal cataloging the life, magical system, and literary output of Aleister Crowley (1875–1947). Tracks the textual transmission of Thelemic doctrine from the *Book of the Law* (1904) through A∴A∴ class publications, OTO instructional papers, and the broader current of 20th-century initiatory magic.

## Core Content
- **Works Corpus**: 200+ texts spanning Libri, Holy Books, essays, poetry, and published correspondence.
- **Thelemic Figures**: 25 biographical profiles covering key collaborators (Rose Edith Kelly, Victor Neuburg, Leila Waddell, Frieda Harris, Karl Germer).
- **Correspondence Tables**: Full 777 system — Kabbalistic correspondences across Sephiroth, Qliphoth, Tarot, deities, and perfumes.
- **Timeline**: Chronological record of A∴A∴ class publications, OTO charter history, and major ritual workings.
- **Dictionary**: 120 defined Thelemic and Kabbalistic terms with source citations.

## Architecture
- **Pipeline**: SQLite → Python Scripts → Static HTML → GitHub Pages.
- **Data Ingestion**: PyMuPDF for text parsing, Regex and spaCy NER for entity extraction from published Crowley editions.
- **Frontend**: Vanilla HTML/CSS/JS with a dark esoteric color palette.

## System Invariants
- **Deckard Boundary**: All 777 correspondence entries are drawn verbatim from Crowley's published tables; no LLM interpolation of magical attributions.
- **Edition Provenance**: Each text entry records the specific publication edition (e.g., *The Equinox* Vol. I) to disambiguate revised texts.

## Related Entities & Concepts
- [[Aleister Crowley]]
- [[Thelema]]
- [[Book of the Law]]
- [[Golden Dawn]]
- [[OTO]]
- [[Kabbalah]]
- [[HermeticDB]]
- [[RenMagDB]]
