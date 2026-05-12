# Project: QueryPat (Philip K. Dick Knowledge Portal)

**Location**: `C:\querypat`
**Type**: Scholarly Knowledge Portal (React App)

## Overview
A comprehensive scholarly knowledge portal about Philip K. Dick (1928–1982), covering his life, fiction, *Exegesis*, correspondence, and academic reception. It treats PKD studies as a contested archive: interpretations are explicitly attributed, and contradictions across sources are surfaced rather than flattened. 

## Core Content
- **Exegesis Segments**: 1,107 chronological text chunks with tracked recurring concepts.
- **Dictionary**: 310 published terms detailing theological concepts and bespoke PKD vocabulary.
- **Biography**: 646 events extracted from autobiographical passages.
- **Archive**: 237 scholarly documents, biographies, and fanzines classified by evidentiary lane (A: Fiction, B: Exegesis, C: Scholarship, D: Synthesis, E: Primary).
- **Scholars**: 119 scholars profiled with interpretive stances and lineages.

## Architecture
- **Backend/Extraction**: Python pipeline orchestrating extraction from PyMuPDF, heuristic linking, LLM enrichment, and editorial overrides into a SQLite database.
- **Frontend**: React 19 + TypeScript + Vite, using HashRouter and Fuse.js for client-side fuzzy search. JSON bundles are exported by route for fast static hosting on GitHub Pages.
- **Ontology**: Deeply structured by `PKDontology.md`, governing the fact-vs-interpretation line and contradiction registries.

## Related Entities & Concepts
- [[Philip K. Dick]]
- [[The Exegesis]]
- [[Knowledge Graphs]]
- [[Digital Humanities]]
- [[Ontology Engineering]]
