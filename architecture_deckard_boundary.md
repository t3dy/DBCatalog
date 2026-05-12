# Architecture: The Deckard Boundary

The **Deckard Boundary** is the absolute dividing line between deterministic execution and LLM judgment. Originally defined in the `Shakespeare Sonnets` DH Site, this boundary ensures that the architecture remains stable while the LLM is restricted exclusively to literary and qualitative analysis.

## 1. Deterministic Zone (Python / Code)
**No LLM judgment is needed or allowed here.**
- Parsing texts into lines, stanzas, or chunks.
- Syllable counting and exact rhyme positioning.
- Schema creation, database migrations, and structural seeding.
- Loading validated JSON into SQLite.
- Template assembly (compiling DB into HTML/Next.js).
- Validation scripts (Foreign Key checks, enum compliance).

## 2. Judgment Zone (LLM)
**Requires literary interpretation and scholarly synthesis.**
- Addressee classification and tone analysis.
- Rhetorical device identification (e.g., identifying irony, paradox, metaphor).
- Close-reading synthesis and tracking emotional arcs.
- Scholar profiling and mapping disputes.
- Generating directing/performance notes.

## 3. The Danger Zone (Violations)
Under no circumstances should an agent cross the Deckard Boundary in the wrong direction:
- **DO NOT** allow LLM output to bypass validation scripts and go directly into the database.
- **DO NOT** allow LLMs to overwrite canonical seed texts (e.g., the 1609 Quarto of Shakespeare, or the exact text of PKD's Exegesis).
- **DO NOT** allow LLMs to invent vocabulary that is not explicitly in the controlled Enum lists (`device_ids`, `analytical_modes`).
- **DO NOT** use deterministic Python code to try to detect irony or aesthetic value.
