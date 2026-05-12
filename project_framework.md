# Project: DH Framework Scaffolder

**Location**: `C:\Dev\framework`
**Type**: CLI Tool / Project Template

## Overview
A Python-based CLI tool (`new_project.py`) designed to automatically scaffold new digital humanities projects. It replicates the battle-tested architecture pattern (SQLite → Python → static HTML → GitHub Pages) originally developed across the *HPMarginalia*, *AtalantaClaudiens*, and *Shakespeare Sonnets* projects.

## Architecture
- **Templating**: Uses a `template/` directory containing the full DH project skeleton (`scripts/`, `docs/`, `site/`, `db/`).
- **Automation Pipeline**: 
  1. **Convert PDFs**: Extracts text from source documents.
  2. **Init DB**: Builds the SQLite schema.
  3. **Seed from Corpus**: Ingests the data (with AI stubs).
  4. **Build Site**: Generates static HTML.
  5. **Validate DB**: Runs structural integrity checks.

## Critique & Insights (Prompt Archaeology)
* **Methodology Under Pressure (Value #7)**: The creation of this framework is a perfect example of methodology emerging organically. Instead of theorizing a framework first, the architecture was built by hand across three distinct projects before being codified into a reusable script.
* **The Over-Automation Risk**: The CLI attempts to run the full 5-stage pipeline with a single command. While excellent for the *Deterministic Zone*, there is a high risk that the `seed_from_corpus.py` script attempts to automate the *Judgment Zone* (LLM synthesis). Automating the judgment phase leads to the "flattening" of writing critiqued in our database engineering review.

## Next Steps
1. **Enforce the Deckard Boundary**: Update the `template/scripts/seed_from_corpus.py` to ensure that any LLM-generated entries are strictly flagged as `review_status="DRAFT"`.
2. **Inject the Master Style Guide**: The scaffolding should automatically copy `concept_scholarly_writing.md` into the new project's `.claude/` or `docs/` directory so that any future LLM runs inherit the critical-reportorial voice.
3. **Shift the Goal**: The framework should be framed not as a "one-click site builder," but as a "one-click reading environment." The goal is to get the PDFs into SQLite quickly so the manual, iterative "Q-log" interpretation can begin.

## Related Entities
- [[Deckard Boundary]]
- [[Database Engineering Critique]]
