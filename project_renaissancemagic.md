# Project: RenMagDB (Renaissance Magic)

**Location**: `C:\Dev\renaissance magic`
**Type**: Digital Humanities Database

## Overview
A digital humanities project cataloging a research corpus of 337 scholarly documents on Renaissance magic. It covers figures ranging from Marsilio Ficino to John Dee, and intellectual traditions including Hermeticism, Kabbalah, and the Enochian *Calls*. 

## Core Content
- **Corpus**: 337 cataloged scholarly documents.
- **Biographies**: 29 figures (22 historical practitioners, 7 modern scholars).
- **Dictionary**: 139 terminology definitions across Latin, Greek, Hebrew, and Arabic roots.
- **Timeline**: 58 chronological events spanning from Plato to modern 2006 scholarship.
- **Primary Sources**: Library of 36 referenced ancient to Renaissance texts.

## Architecture
- **Pipeline**: SQLite → Python Scripts → Static HTML → GitHub Pages.
- **Data Ingestion**: PyMuPDF for document parsing, Regex and spaCy NER for metadata, TF-IDF for topic clusters, and LLM-assisted generation for definitions (all tagged as DRAFT pending review).
- **Frontend**: Vanilla HTML/CSS/JS with a warm parchment color palette.

## Related Entities & Concepts
- [[Renaissance Magic]]
- [[Marsilio Ficino]]
- [[John Dee]]
- [[Hermeticism]]
- [[Kabbalah]]
- [[Digital Humanities]]
