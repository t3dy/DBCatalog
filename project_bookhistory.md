# Project: Book History & Transcription Pipelines

## Overview
**Type**: Archival Pipeline / Textual Ingestion
**Path**: `C:\Dev\book_history`, `C:\Dev` (Epub/PDF Scripts)

A collection of critical python scripts and methodologies focused on converting raw historical texts (Epubs, PDFs, Scans) into strictly formatted Markdown for ingestion into the broader DH SQLite databases.

## Architectural Notes
* **Projects Included**: Targeted conversions of scholarly texts, such as extracting the epub for *A Stain in the Blood: The Remarkable Voyage of Sir Kenelm Digby* into Markdown.
* **Significance**: This is the unglamorous but utterly necessary foundation of the "Cathedral" database theory. Before the LLM can act as a Dungeon Master, the primary texts must be deterministically parsed, stripped of formatting artifacts, and stored as clean Markdown. 

## Integration with the Memory System
These scripts ensure that the texts ingested into `RenMagDB` or the Almagest Construction Kit are free of OCR garbage and correctly formatted, preserving the strict textual provenance required by the Deckard Boundary.
