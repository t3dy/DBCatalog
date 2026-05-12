# Project: Shakespeare Sonnets DH Site

**Location**: `C:\Dev\Shakespeare`
**Type**: Digital Humanities Website

## Overview
A digital humanities website presenting Shakespeare's 154 Sonnets through four scholarly pillars: close-reading Analyses, line-by-line Directing notes, historical Contexts, and thematic Essays. It is deeply focused on the dramatic love triangle of the Fair Young Man (FYM), Dark Lady (DL), and the Speaker.

## Architecture & Deckard Boundary
Uses the standard DH Pipeline: SQLite → Python static generator → HTML. 
It operates under strict "Deckard Boundary" rules, cleanly separating what deterministic Python scripts do (parsing, schema, template assembly, validation) from what LLMs do (close reading, rhetorical device ID, directing notes).

## System Invariants & Provenance
- **Immutable Seed**: The canonical 1609 Quarto text is sacred and cannot be overwritten.
- **Data Flow**: Seed JSON → Database → HTML (one direction only).
- **Controlled Vocabularies**: Strict ENUM lists for rhetorical devices, analytical modes, and volta types.
- **Provenance**: Every datum tracks `source_method` (Deterministic vs LLM_Assisted), `review_status` (Draft → Reviewed → Verified), and `confidence` (High/Medium/Low). LLM-generated output defaults to DRAFT/MEDIUM.

## Related Entities & Concepts
- [[William Shakespeare]]
- [[Digital Humanities]]
- [[Deckard Boundary]]
- [[DH Framework]]
