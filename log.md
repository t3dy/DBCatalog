# Wiki Operations Log

Chronological, append-only record of operations performed on the wiki. 

## [2026-06-08] ingest | GoetiaRevEng — Ontology page + scripts 30-31
- Created `goetia_sigil_analysis.md`: full ontology for the Goetia sigil reverse-engineering project at `C:\Dev\GoetiaRevEng\`. Covers data entities (Sigil, AnalysisFeature, Cluster, PrecedentImage, GridScore), key relationships, four construction method hypotheses (kamea_path, letter_grid, freehand_scribal, corrupted_kamea), data file inventory, and current findings summary.
- Wrote `30_gematria_path_test.py`: kamea-path gematria test — decomposes each spirit's gematria into a cell sequence on its assigned magic square, compares theoretical path to actual skeleton via Hausdorff + mean-NN distance across 8 isometries.
- Wrote `31_grid_synthesis.py`: synthesis script combining gridness, waypoint alignment, angle coverage, and gematria path quality into a composite score with "likely / possible / unclear" classification.
- Updated `index.md` with new page entry.

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

## [2026-06-11] update | GoetiaRevEng grid calibration (script 32): instrument AUC 0.957; Venus best-fit result falsified as grid-density artifact; real corpus at 94th pctile of freehand null, 26th of kamea walks; 32/78 exceed null p<0.05. Cluster k=8 claim marked revised per script 24.

## [2026-06-13] ingest | Initialized Pico della Mirandola Knowledge Portal
- Created `E:\pdf\renaissance magic\Pico\scripts\init_pico_portal.py` to convert the local Pico PDF/EPUB corpus into Markdown, SQLite, manifest JSON, reading-system docs, templates, and a static viewer.
- Converted 73 source files into 73 Markdown full-text files in `E:\pdf\renaissance magic\Pico\Markdown`.
- Built `E:\pdf\renaissance magic\Pico\db\pico.db` with 73 document records, 10,538 page/EPUB-section records, 1,829 section records, 25 scholar seeds, 207 reading tasks, 5 Pico text gap records, and an FTS5 index.
- Created `project_pico.md` and `ontology_pico.json`; indexed the project and ontology in `index.md`.

## [2026-06-14] update | Added PicoDB artifact system, timeline, and map layer
- Updated `C:\Dev\PicoDB` with `docs/ARTIFACT_SYSTEM.md`, `data/reading_artifact_ontology.json`, artifact templates, and `scripts/seed_research_artifacts.py`.
- Added SQLite tables for artifact types, reading artifacts, claims, website cards/pages, timeline events, locations, and map routes.
- Seeded 8 draft website notes, 6 source-tethered claims, 7 website cards, 8 website page records, 63 timeline events, 18 mapped locations, and 4 route layers.
- Expanded `site/index.html` with Overview, Research Artifacts, Timeline, Map, and Catalog sections.

## [2026-06-14] study | PicoDB study pass 002
- Added close-reading source packets for Howlett, Copenhaver, Farmer, Wirszubski/Kristeller, and Akopyan.
- Added website-facing notes for Pico biography, Oration-centered historiography, Christian Kabbalah, astrology, and scholar cards for Farmer, Wirszubski, and Akopyan.
- Expanded PicoDB to 18 reading artifacts, 18 source-tethered claims, 13 website cards, 72 timeline events, and 20 mapped locations.
- Verified the static viewer at `http://localhost:8877/index.html` after regenerating `db/pico.db`, JSON exports, and `site/index.html`.

## [2026-06-14] study | PicoDB study pass 003
- Added primary-text source packets for the Oration opening/ascent, *On Being and the One*, and the *Heptaplus* proems.
- Added Farmer-based source packets for the 900 Conclusions as a hidden-connection thesis system and for the Gianfrancesco/Savonarolan Anti-Pico textual-transmission problem.
- Expanded PicoDB to 29 reading artifacts, 35 source-tethered claims, 18 website cards, 17 website pages, and 77 timeline events.
- Verified the static viewer at `http://localhost:8877/index.html`; it now exposes primary-text cards for Oration, *On Being and the One*, *Heptaplus*, the 900 Conclusions, and the Anti-Pico problem.

## [2026-06-14] system | PicoDB section-summary style guides
- Added `SECTION_SUMMARY_STYLE_GUIDE.md`, `ARGUMENT_REFERENCE_STYLE_GUIDE.md`, and `SUMMARY_COVERAGE_PROTOCOL.md` to make exhaustive section summaries operational.
- Expanded the section-summary template to require section function, argument map, reference register, claims/subclaims, philological notes, knowledge hooks, and coverage checklist.
- Updated the reading artifact ontology to version 0.3.0 with coverage levels and argument-move vocabulary.
- Seeded 6 formal section-summary artifacts and expanded PicoDB to 35 reading artifacts, 41 source-tethered claims, and 20 website cards.

## [2026-06-14] study | PicoDB scholarly-values and Allen/Ficino passes
- Added study pass 005 for Copenhaver, Edelheit, Dougherty, Howlett, Busi, and Wirszubski as guide scholars for scholarly values, ontology updates, and Kabbalah reading protocols.
- Added study pass 006 after copying Allen's *Studies in the Platonism of Marsilio Ficino and Giovanni Pico* from Downloads into `C:\Dev\PicoDB`, converting it to Markdown, and ingesting it into `db/pico.db`.
- Added `FICINO_PICO_READING_PROTOCOL.md`, Allen scholar/source artifacts, primary rereads of *On Being and Unity*, the *Oration*, and the 900 Conclusions, plus a longform essay seed on Pico's dispute with Ficino.
- Expanded PicoDB to 74 documents, 57 reading artifacts, 61 claims, 29 website cards, and ontology version 0.5.0; verified the static viewer at `http://localhost:8877/index.html`.

## [2026-06-14] study | PicoDB Kabbalah longform synthesis
- Added study pass 007 with a longform essay seed, `artifacts/essays/pico_kabbalah_synthesis_longform_draft.md`, synthesizing Wirszubski, Busi, Copenhaver, Farmer, Howlett, Edelheit, Dougherty, and Allen.
- Added `artifacts/historiography/kabbalah_scholar_synthesis_matrix.md` and a scholar synthesis overlay to `docs/KABBALAH_READING_PROTOCOL.md`.
- Updated the reading ontology to version 0.6.0 with Kabbalah synthesis fields, a Kabbalah taxonomy, and a scholar-role map.
- Expanded PicoDB to 59 reading artifacts, 69 claims, and 31 website cards; verified the static viewer at `http://localhost:8877/index.html`.

## [2026-06-14] study | PicoDB biographical synthesis
- Added study pass 008 with `docs/BIOGRAPHICAL_READING_PROTOCOL.md`, a biographical method matrix, a biographical source-gap packet, and a scholar-synthesis biography draft.
- Updated the ontology to version 0.7.0 with biographical reading fields, life-register taxonomy, and a scholar-role synthesis keyed to Howlett, Edelheit, Copenhaver, Dougherty/Borghesi, Farmer, Busi/Wirszubski, and Allen.
- Marked major source gaps: letter-by-letter work on Borghesi's `Lettere`, Gianfrancesco's `Vita`, Vatican Capponi 235, the 1496 print tradition, PRDL public-domain Pico titles, and the Elijah del Medigo letter.
- Expanded PicoDB to 62 reading artifacts, 78 claims, 34 website cards, and 18 website pages; verified the static viewer at `http://localhost:8877/index.html`.

## [2026-06-14] study | PicoDB Crofton Black and parallel Heptaplus essays
- Copied Crofton Black's *Pico's Heptaplus and Biblical Hermeneutics* plus two reviews from Downloads into `C:\Dev\PicoDB\sources\crofton_black_heptaplus`; raw PDFs remain locally available and ignored by git, while Markdown full text is tracked.
- Ingested the three Black-related PDFs into PicoDB, expanding the corpus to 77 documents and about 4.21M extracted words.
- Added `HEPTAPLUS_BLACK_READING_PROTOCOL.md`, a Black scholar-values profile, a Heptaplus structure source packet, and a chapter-summary artifact for Black's monograph.
- Updated the Heptaplus essay and seeded parallel essay drafts on Plato/Aristotle, Aquinas/Dionysius, own-opinion theses, Neoplatonist and Arabic authors in the 900, Arabic intellect/felicitas, Dionysian anagogy, and Heptaplus after the Oration.
- Updated ontology to version 0.8.0 and expanded PicoDB to 73 reading artifacts, 87 claims, 44 website cards, and 26 website pages; verified the static viewer at `http://localhost:8877/index.html`.

## [2026-06-14] study | PicoDB astrology synthesis
- Copied six Pico-and-astrology PDFs into `C:\Dev\PicoDB\sources\pico_astrology_pass010`; raw PDFs remain locally available and ignored by git, while Markdown full text is tracked.
- Ingested Rabin, Rutkin, Akopyan, Vanden Broecke, Boner, and Azzolini-related materials, expanding the corpus to 83 documents and about 4.37M extracted words.
- Added `ASTROLOGY_READING_PROTOCOL.md`, an astrology scholar matrix, an astrology source packet, an astrology chapter-summary artifact, and an astrology taxonomy.
- Added the Pico and astrology synthesis essay draft, treating Pico's position as a developmental, genre-sensitive movement from early celestial causation and poetic/natural astrology to the late attack on divinatory astrology.
- Updated ontology to version 0.9.0 and expanded PicoDB to 78 reading artifacts, 95 claims, 48 website cards, and 27 website pages; verified the static viewer at `http://localhost:8877/index.html`.

## [2026-06-14] study | PicoDB angelology synthesis
- Searched PicoDB for angelology across the Oration, Heptaplus, 900 Conclusions scholarship, Kabbalah notes, Ficino/Pico materials, Dionysian anagogy, Thomistic metaphysics, and Arabic intellect/felicitas materials.
- Added `ANGELOLOGY_READING_PROTOCOL.md`, an angelology taxonomy, a primary/source map, a passage matrix, and an angelology scholar matrix.
- Added the Pico angels and angelology synthesis essay draft, connecting angelic imitation, angelic/intellectual world, Kabbalistic angel names, Dionysian hierarchy, Proclean/Plotinian metaphysics, Ficinian intelligences, Thomistic separate substances, and Arabic Active Intellect/conjunction traditions.
- Updated ontology to version 0.10.0 and expanded PicoDB to 83 reading artifacts, 103 claims, 52 website cards, and 28 website pages; verified the static viewer at `http://127.0.0.1:8877/site/index.html`.

## [2026-06-14] study | PicoDB Opera reviews and missing writings
- Copied six scholarly reviews of Pico Opera, Garin's Mirandola congress volumes, and Speyer's *Carmina latina* into `C:\Dev\PicoDB\sources\pico_opera_reviews_pass012`; raw PDFs remain locally available and ignored by git, while Markdown full text is tracked.
- Ingested the six reviews, expanding the corpus to 89 documents and about 4.38M extracted words.
- Added `PICO_PRIMARY_TEXT_ACQUISITION_PROTOCOL.md`, an Opera reviews source packet, an Opera reviews section-summary artifact, a missing-writings taxonomy, and the Pico missing-writings next-steps essay.
- Updated the gap register for Basel Opera, Bologna 1496, Commento, Disputationes, De imaginatione, Carmina, Lettere, Gianfrancesco's Vita, and Thomas More's Life of Pico.
- Updated ontology to version 0.11.0 and expanded PicoDB to 87 reading artifacts, 111 claims, 55 website cards, and 29 website pages; verified the static viewer at `http://127.0.0.1:8877/site/index.html`.

## [2026-06-14] study | PicoDB missing-writings acquisition pass
- Ingested the Internet Archive OCR of the 1557 Basel *Opera omnia Ioannis Pici* as a Markdown/database corpus-control witness.
- Ingested the More/Rigg public-domain *Life of Pico* as an English reception witness for biography, devotion, and the saintly Pico tradition.
- Added a missing-writings acquisition log, Basel Opera source packet, More/Rigg source packet, web-acquisition source packet, and corpus-control dashboard.
- Corrected `De imaginatione` from a presumed missing Giovanni Pico work to a related Gianfrancesco Pico text unless new evidence requires revision.
- Updated the ontology to version 0.12.0 and expanded PicoDB to 91 documents, 91 reading artifacts, 118 claims, 58 website cards, and 30 website pages; verified the portal at `http://127.0.0.1:8877/site/index.html`.

## [2026-06-14] study | PicoDB Commento access pass
- Found and ingested the full Italian *Commento sopra una canzone d'amore di Girolamo Benivieni* from Biblioteca Italiana TEI/XML as a controlled primary text.
- Found and ingested Thomas Stanley's early modern English translation witness via Edmund G. Gardner's 1914 Internet Archive reprint, *A Platonick discourse upon love*.
- Added Commento source packets, a structural summary, a Commento reading ontology, and a reading-plan essay for systematic chapter/stanza close reading.
- Updated `PICO_TEXT_GAPS.md`, `SECTION_SUMMARY_STYLE_GUIDE.md`, and ontology version 0.13.0 so the Commento is now governed by fields for Ficino dispute, love/beauty doctrine, hierarchy, celestial causality, poetic theology, Christian controls, Kabbalistic hints, and reception/translation differences.
- Expanded PicoDB to 93 documents, 96 reading artifacts, 123 claims, 62 website cards, and 32 website pages.

## [2026-06-14] study | PicoDB Jayne Commento translation access
- Opened the Internet Archive page for Sears Jayne's *Commentary on a Canzone of Benivieni*.
- Registered Jayne as a restricted modern translation witness, with a bibliographic Markdown stub instead of a transcript.
- Added a Jayne source packet and a Commento translation-collation protocol for page-level notes, short quotation anchors, and comparison against the Italian TEI and Stanley.
- Updated ontology to version 0.14.0 and expanded PicoDB to 94 documents, 98 reading artifacts, 125 claims, 64 website cards, and 33 website pages.

## [2026-06-14] study | PicoDB original Commento translation
- Confirmed that the project should translate Pico's Italian *Commento* directly from the controlled Italian TEI rather than reconstructing it from English translations.
- Added `COMMENTO_TRANSLATION_PROTOCOL.md`, a translation policy, a translation queue/glossary, and a draft original English translation of the title, Bonacursius dedication, and Benivieni's reader address.
- Registered translation artifacts in PicoDB, updated ontology to version 0.15.0, and exposed new portal cards for the Commento translation policy and opening translation.

## [2026-06-14] study | PicoDB Pugliese Benivieni pass
- Read Olga Zorzi Pugliese's article on Benivieni as Pico's friend, collaborator, and translator.
- Added a source packet, a Commento transmission note, and a source-gap packet for Pico's Pater Noster commentary and Benivieni's unpublished vernacular translation.
- Updated the gap register and section-summary guide: Commento passages involving Ficino now require explicit attention to Benivieni's possible softening/mediation.
- Updated ontology to version 0.16.0 and exposed new portal cards for Pugliese, the Commento softening problem, and Pico's Pater Noster commentary.
