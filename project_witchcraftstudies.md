# Project: WitchcraftStudiesDB

**Location**: `C:\Dev\WitchcraftStudiesDB`
**Type**: Digital Humanities Database

## Overview
A scholarly DH corpus tracking the historiography of European witchcraft from the medieval witch-craze through contemporary academic reassessment. Draws on primary trial records, demonological treatises, and the major revisionist scholarly literature from Keith Thomas and Alan Macfarlane to Carlo Ginzburg and Robin Briggs.

## Core Content
- **Trial Records**: 500+ documented prosecutions with fields for region, date, accusation type, verdict, and presiding authority.
- **Demonologies**: 45 cataloged treatises spanning *Malleus Maleficarum* (1487) through 17th-century decline texts, with full bibliographic provenance.
- **Scholars**: 30 key historians with career profiles, methodological stances, and cross-linked bibliography entries.
- **Geography**: 12 regional prosecution clusters (German territories, Scottish Highlands, English counties, Basque country) with spatial data for mapping.
- **Terminology**: 85 defined legal, theological, and folk-magic terms across Latin and vernacular sources.

## Architecture
- **Pipeline**: SQLite → Python Scripts → Static HTML → GitHub Pages.
- **Data Ingestion**: PyMuPDF for treatise parsing, spaCy NER for defendant and accusation entity extraction from trial transcripts.
- **Frontend**: Vanilla HTML/CSS/JS; maps rendered via Leaflet.js using GeoJSON regional shapefiles.

## System Invariants
- **Source Hierarchy**: Primary trial records take precedence over secondary scholarship; all summary claims tagged with `source_method` and `confidence` fields.
- **Periodization**: Trials are bucketed into five distinct waves to distinguish the 15th-century institutional craze from regional outbreaks and the 17th-century decline.

## Related Entities & Concepts
- [[Witchcraft]]
- [[Malleus Maleficarum]]
- [[Carlo Ginzburg]]
- [[Keith Thomas]]
- [[Early Modern History]]
- [[Folk Magic]]
- [[RenMagDB]]
