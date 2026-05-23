# Wiki Operations Log

Chronological, append-only record of operations performed on the wiki. 

## [2026-05-11] ingest | Initialized LLM-Wiki System
- Created the wiki structure and index file.
- Updated `CLAUDE.md` to establish the schema and agent rules for maintaining the wiki.

## [2026-05-11] ingest | Ingested Claudiens and Megabase
- Extracted architectural and thematic details from `C:\Dev\Claudiens` (AtalantaClaudiens) and `C:\Dev\megabase` (Dreambase).
- Created `project_claudiens.md` and `project_megabase.md` summaries.
- Indexed the new project pages in `index.md`.

## [2026-05-11] ingest | Ingested RenMagDB, Hypnerotomachia, EmeraldTablet, BachStudies
- Extracted summaries, tech stacks, and invariants from `C:\Dev\renaissance magic`, `C:\Dev\hypnerotomachia polyphili`, `C:\Dev\EmeraldTablet`, and `C:\Dev\BachStudies`.
- Created `project_renaissancemagic.md`, `project_hypnerotomachia.md`, `project_emeraldtablet.md`, and `project_bachstudies.md`.
- Indexed the 4 new project pages in `index.md`.

## [2026-05-11] ingest | Ingested SocialsDB, MarxistPortal, Shakespeare, and QueryPat
- Extracted summaries, data models, and theoretical approaches from `C:\Dev\SocialsDB`, `C:\Dev\MarxistPortal`, `C:\Dev\Shakespeare`, and `C:\querypat`.
- Created `project_socialsdb.md`, `project_marxistportal.md`, `project_shakespeare.md`, and `project_querypat.md`.
- Indexed the 4 new project pages in `index.md`.

## [2026-05-11] synthesis | Extracted Master Concepts & Critiques
- Extracted `concept_scholarly_writing.md` from the QueryPat scholar templates and Prompt Archaeology values.
- Extracted `architecture_deckard_boundary.md` from the Shakespeare project rules.
- Authored `critique_database_engineering.md` evaluating LLM over-engineering risks and web writing failures against the 10 values of prompt archaeology.
- Updated `index.md` to catalog the new structural documents.

## [2026-05-11] ingest | Ingested DH Framework Scaffolder
- Evaluated `C:\Dev\framework\new_project.py` and its templating system.
- Authored `project_framework.md` with critiques and next steps concerning the over-automation of the Judgment Zone.
- Added the Framework to `index.md` and `index.html`.

## [2026-05-11] synthesis | Authored Wiki Utility Report
- Authored `report_wiki_utility.md` mapping the wiki's structure (Deckard Boundary, Scholar Templates, Prompt Archaeology) directly to the user's goals of defeating LLM drift and enforcing scholarly density.
- Indexed the report in `index.md`.

## [2026-05-11] synthesis | Authored Prompt Archaeology Machines
- Authored `architecture_prompt_archaeology_machines.md` outlining the pipeline for extracting game, app, and book ideas from megabase LLM chats.
- Indexed the new architecture document in `index.md`.

## [2026-05-11] synthesis | Authored Auditing the Writing Strategy
- Authored `concept_auditing_writing.md` defining a token-efficient Lint-and-Sample pipeline to audit LLM prose.
- Added an explicit Auditing section to the HTML website and `index.md`.

## [2026-05-11] synthesis | Authored Database Theories
- Authored `concept_database_theories.md` classifying all projects into three distinct database theories: Knowledge Portals, Procedural Engines, and Social Megaphones.
- Indexed the theory document in the HTML website and `index.md`.

## [2026-05-11] synthesis | Authored Audience Evaluation
- Authored `concept_dh_evaluation.md` critiquing how well the databases serve the triple audience of Academics, Gamers, and Practitioners.
- Indexed the evaluation in the HTML website and `index.md`.

## [2026-05-11] synthesis | Authored DH Methodological Analysis
- Authored `report_dh_project_analysis.md` providing a strict DH critique of the corpus (ontology, textual transmission, IIIF standards, and distant reading).
- Indexed the analysis in the HTML website and `index.md`.

## [2026-05-11] synthesis | Authored Digby, Scryfall, and NSFRIPPER Profiles
- Authored `project_digby.md`, `project_alchemyscryfall.md`, and `project_nsfripper.md`.
- Evaluated these projects as Procedural Engines and technical boundaries.
- Added cards to the HTML dashboard.

## [2026-05-12] synthesis | Authored Legacy & Pipeline Profiles
- Authored `project_treetapper.md`, `project_mtgoverlay.md`, `project_ack.md`, `project_bookhistory.md`, and `project_vibecoding.md`.
- Documented projects from `C:\olddevprojects` and previous Antigravity workflows.
- Added their respective cards to the HTML dashboard.

## [2026-05-23] ingest | Ingested CrowleyDB, WitchcraftStudiesDB, AlchemyTimelineMap
- Authored `project_crowleydb.md`: Knowledge portal for Aleister Crowley's corpus, Thelemic doctrine, and 777 correspondence tables. Strict Deckard Boundary on all symbolic attributions.
- Authored `project_witchcraftstudies.md`: DH corpus for European witchcraft historiography; 500+ trial records, 45 demonological treatises, Leaflet.js geospatial mapping (first geospatial project in catalog).
- Authored `project_alchemytimelinemap.md`: D3.js interactive timeline mapping 2,500 years of alchemical transmission; introduces cross-portal entity resolution with HermeticDB and RenMagDB (first federated data layer in ecosystem).
- Indexed all three projects in `index.md` and added cards 19–21 to `index.html`.

## [2026-05-23] synthesis | Authored New Directions Architecture & WitcherFolkloreDB
- Authored `architecture_new_directions.md`: Full synthesis of context engineering, coding environment, and data engineering directions across the ecosystem. Covers entity federation (`entities.db`), D3.js visualization-as-argument, geospatial modeling, FTS5 → semantic search evolution, the Engine + Portal dual-frontend, and alternative approaches (Neo4j, SQLite-vec, Wikidata QIDs, IIIF, DuckDB, Observable, Svelte).
- Defined the **Fourth Database Theory**: the Fictional-Historical Bridge — comparative citation chain projects (Fictional Entity → Folklore Source → Medieval Text) with a Three-Field Citation Requirement.
- Authored `project_witcherfolklore.md`: Fictional-Historical Bridge tracing Witcher monsters and folk practices to Slavic folklore, medieval Polish chronicles, and Latin bestiary traditions. Introduces three-tier `citation_chains` data model; cross-linked to WitchcraftStudiesDB, RenMagDB, and CrowleyDB.
- Added card 22 (WitcherFolkloreDB) and New Directions rabbit-hole section to `index.html`.
- Indexed both new documents in `index.md` under Projects and Master Concepts & Architecture.

## [2026-05-23] synthesis | Authored Beginner's Glossary
- Authored `concept_beginners_glossary.md`: Plain-English definitions for every CS, DH, and wiki-specific term across the full catalog. Seven parts covering core CS building blocks, the data pipeline, the frontend tech stack, AI/LLM terms, this wiki's special vocabulary, digital humanities terminology, and advanced architecture concepts. Every definition includes a real example from a catalog project.
- Added "New Here? Start With the Glossary" rabbit-hole section to `index.html` as the first rabbit-hole entry.
- Indexed in `index.md` under Master Concepts & Architecture.

## [2026-05-23] synthesis | Authored Wiki Field Guide
- Authored `report_wiki_field_guide.md`: Ten-part practical handbook covering session startup rituals (minimum viable context load, strong opening prompts, handover pattern), writing project profiles before building, querying the wiki itself as a corpus (grep patterns, orphan detection, log as decision audit), cross-pollination sessions (collision candidates via shared Related Entities, bridge sessions, AlchemyTimelineMap as navigation hub), SQL query arsenals (five essential queries, ATTACH DATABASE for cross-project joins), the DRAFT review cycle (quota-based, three-question test, lint before human review), defeating staleness (actuality check, Next Step as staleness sensor, update vs. synthesis discipline), context window discipline (minimum viable context rule, density over volume), anti-patterns (wall of text, terminology drift, orphan pages, confidence inflation, stale Next Step, meta-wiki trap, batch synthesis dump), and extending the wiki with a query console (entity browser, coverage gap report, missing pages detector, live database wiring).
- Added "Wiki Field Guide" rabbit-hole section to `index.html`.
- Indexed in `index.md` under Meta & Reports.
