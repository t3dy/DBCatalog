# Wiki Operations Log

Chronological, append-only record of operations performed on the wiki. 

## [2026-06-29] synthesize | The Opportunity Audit method (from HPin3D session)
- Filed [[concept_opportunity_audit]] — a reusable method for auditing a *shipped* project to find improvements (render-and-look · unsurfaced data · asset reality · dead-end interactions). The "what to build next" counterpart to [[audit-failures]] and [[concept_auditing_writing]]. Indexed under Master Concepts & Architecture.
- Sourced from an HPin3D ([[project_hpin3d]]) work session: probe 1 caught a WebGL `<canvas>` rendering the whole app into a 300×150 box (invisible to console/snapshot — only a screenshot revealed it); probe 2 found 51 hidden `discourse_summary` scholarship blocks → built a **Tours** feature connecting the 3-D models to the research; probe 3 found `emblems.json` referencing absent images (self-hosted from AlchemyBeatEmUp); probe 4 found the gallery unlit + the HP fountain non-orbitable.
- Added two `environment-health.md` silent-failure rows: the canvas-sizing trap and the missing-referenced-assets trap.

## [2026-06-29] ingest + maint | Closing coverage pass, git-init, system.md rename
- **Closing pass (6 pages)**: 3-agent survey + 8-dir triage. Created [[project_promptarchaeology]] (1.45M-prompt distant reading over megabase.db, ACTIVE), [[project_shwep]] (dark-academic style kit + skill, STABLE), [[project_glitchmario]], [[project_ubiktrainings]] (PKD planning skill system behind [[project_pkdplanningsite]]), [[project_oldragdonald]] (Android field tool), [[project_mapresearch]] (map R&D for [[project_alchemytimelinemap]]). Last four are honest stubs (one-liner + status; architecture not surveyed in depth).
- Triage outcomes folded into `coverage.md` Skipped: AlchemyProtos (dormant), mtg-research (scratch), VCG_DOCS (fold into [[project_vibecoding]]), **CDevsm-webmaster-site (empty dir — deletion candidate)**. Coverage queue now empty: every C:\Dev dir triaged. Registry: 71 projects.
- **Loss-risk git-init**: `git init` + tailored `.gitignore` (deps/venv/media excluded) on Bookstore (0.4 MB), antigravbeadgame (4 MB), REAPERBEYONDNES (8 MB) — committed. NESjamtools left uncommitted (177 MB of `.rpp`/MIDI/NSF even after ignoring `.wav`) — needs a Git LFS decision.
- **Consistency**: renamed `SYSTEM.md` → `system.md` (lowercase, matching sibling system files) so `[[system]]` wikilinks resolve in MemoryPalace; updated refs in `index.md`, `C:\Dev\CLAUDE.md`, internal memory. Rebuilt MemoryPalace (123 → 129 pages, 163 loci).
- Updated `environment-health.md` (promptarchaeology → external `megabase.db`), `registry.md` theme map (+6, new Mobile-apps and Design-references themes), `index.md`.

## [2026-06-29] ingest | Gap pass — named-active + alchemy-game projects (4)
- 4-agent survey of dirs the registry's theme map flagged as un-ingested. Created lean pages: [[project_mtgslider]] (MTG theme→slideshow Python pipeline, STABLE), [[project_dogsgame]] (4DOGS noir text-adventure, ACTIVE), [[project_alchemybeatemup]] (alchemical-engraving → pixel-sprite DH pipeline, STABLE), [[project_alchemytetris]] (cluster: AlchemyBalanceTetris / BALANCETETRIS / TILTRIS / TetrisCodex).
- Regenerated `registry.tsv` (65 projects). Updated `registry.md` theme map (Alchemy-games, MTG, Games-general) — removed the "not yet ingested" caveats. Updated `index.md`, `coverage.md` (queue ~15 → ~10), and the hardcoded-path row in `environment-health.md` (AlchemyBeatEmUp → `Claudiens/site/images/emblems`).

## [2026-06-29] system | Project registry for cross-project discovery
- Added `build_registry.py` → generates `registry.tsv` (slug · name · type · status · path · live · tags · desc) by harvesting every `project_*.md`. Resolves real directory paths against the filesystem, so dir names with spaces ("renaissance magic", "Tarot Dev", "hypnerotomachia polyphili") and prose that merely mentions `C:\Dev\wiki` (PicoDB, Illuminatus) no longer mis-resolve. 61 projects harvested.
- Added `registry.md` — hand-curated theme/alias map (the semantic layer; Deckard split from the deterministic harvest). Resolves fuzzy references like "my alchemy databases" → explicit slug sets, distinguishing databases from games. ~18 themes.
- **Cross-project hook**: added a pointer in the always-loaded `C:\Dev\CLAUDE.md` so a session in *any* project resolves theme references via `registry.md` + `registry.tsv`. Also linked from `SYSTEM.md` and `index.md`.

## [2026-06-29] system + ingest | Self-healing system files + 13-project sweep
- **System files** (new): `SYSTEM.md` (operating principles, four operations, verify-before-done gate), `style.md` (voice + markdown conventions + lean ~1.5 KB project-page template), `environment-health.md` (living fragility/silent-failure registry, seeded from the 2026-06-29 usage report + agent sweep), `audit-failures.md` (append-only failure log). Motivated by the usage report's top friction patterns: overclaiming completion, missing project context, silent-failure traps. Designed lean to avoid context bloat (4 files, one source of truth each, no checklist duplication).
- **Ingest sweep**: fanned out 12 parallel survey agents over recently-modified `C:\Dev` dirs not yet in the wiki. Created 13 lean project pages: `project_hpin3d`, `project_emblemsin3d`, `project_fuguejukebox`, `project_audiobookcleaner`, `project_memorypalace`, `project_nesmusictools` (cluster: NESMusicStudio/REAPERBEYONDNES/NESjamtools/ReapNES-Studio/nes-music-lab/arpeggiator-composer/NESARPEGDESIGNS), `project_esofeed`, `project_pkdfestsite`, `project_pkdplanningsite`, `project_tarotmeditation`, `project_barton` (client cluster, 4 repos), `project_bookstore` (Bookstore+SHOPSITE), `project_smwebmastersite`.
- **Flagged, not paged**: `ANTIGRAVEMBLEMSIN3D` (scratch Vite fork → noted in [[project_emblemsin3d]]), `antigravbeadgame` (unversioned copy trailing [[project_glassbeadgame]]), `NESARPEGDESIGNS` (empty stub), `membership-site-guide` (stock scaffold), `CDevTarotMeditation` (does not exist).
- **New fragility recorded** in `environment-health.md`: cross-project hardcoded `C:\Dev` paths (emblem-3D family, FUGUEJUKEBOX, MemoryPalace); stale planning docs vs. shipped code (HPin3D); non-git working copies at loss risk (NESjamtools, REAPERBEYONDNES, Bookstore, antigravbeadgame); `vite fs.allow:['..']` drive exposure.
- Updated `index.md` (new "System & Maintenance" section + 13 project entries). Internal Claude memory seeded with operating discipline (verify-before-done, check-context-before-asking, user profile, wiki protocol).

## [2026-06-27] synthesize | Platform + Discord strategy for esoteric studies
- Created `strategy_esoteric_platform.md`: synthesis of the whole C:\Dev ecosystem into one (currently unbundled) platform/commons for esoteric-studies scholars. Five layers — Feed (EsotericBeatNews) · Library (the knowledge portals) · Workshop (EmblemPrintShop/Goetia/games) · Commons (Discord) · Society (SocMagWeb). Distills the transferable doctrine (3+1 DB archetypes, Deckard Boundary, over-engineering trap, static-first, fan-index ethics, provenance-strict scholarship), an outreach funnel for SocMag (Matthew's concern: feed → Discord → membership), guardrails (sustainable solo labor, co-stewards), and a 5-phase plan.
- Created `strategy_esoteric_discord.md`: concrete Discord blueprint modeled on the Vibe Coding Garage — ~10 channels, lean role set incl. @SocMag Member (verified on-ramp), the feed-bot keystone (webhook off the existing EsotericBeatNews catalog.json), a Megaphone digest bot for SocMag outreach content, governance/safety, and anti-empty-room seeding.
- Linked to [[concept_database_theories]] (the archetype taxonomy, now +Institutional Infrastructure), [[project_vibecoding]], [[concept_dh_evaluation]]. Cross-refs `SocMagWeb/docs/WEBDEV_FOR_HIRE.md`.
- Updated `index.md` (new "Strategy & Synthesis" section).

## [2026-06-18] ingest | SocMagWeb — Societas Magica admin rebuild
- Created `project_socmagweb.md`: Next.js 16 + Postgres rebuild of societasmagica.org's PHP/Bonfire admin panel for a ~494-member scholarly society.
- Captures the ports-and-adapters architecture (pure `lib/domain/*` + `lib/services` over `lib/ports`), the in-repo agile+Karpathy-wiki orchestrator (`C:\Dev\SocMagWeb\orchestrator/`), and current status: 70 Vitest tests green, 99.65% domain stmt coverage, typecheck clean; Sprints 00/01/02/04 done.
- Notes the 🔴 launch-blocker found in code review (unsigned forgeable session cookie → privilege escalation, ticket SM-024) and four defects fixed in-review.
- Linked to [[concept_database_theories]] (transactional admin vs. read-mostly DH portals) and [[architecture_deckard_boundary]] (pure domain vs. I/O adapters).
- Updated `index.md` Projects list.

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

## [2026-06-27] ingest | OCCULTIMGDB (Occult Image DB) project spun up
- New project `C:\Dev\OCCULTIMGDB\`: static-site archive of WHOLE alchemical/occult illustrations for game-devs/artists. Deliberately whole-image (no element extraction — that distinguishes it from EmblemPrintShop).
- Inventoried ~3,700 public-domain scans already on disk under EmblemPrintShop/sources (16 source books); reuses them in place, nothing re-downloaded.
- Built: source registry (config.py), idempotent Pillow importer (build_catalog.py → catalog.json + thumb/card derivatives), static site (gallery with era/tradition/work/motif facets + motif-aware search, detail pages, about/licensing).
- V1 = 687 curated illustrations across 8 works (Atalanta, Hypnerotomachia, Rosarium, Splendor Solis, Stolcius, Mylius plates, Khunrath, Cramer); 12 flagship Atalanta emblems given web-sourced scholarly summaries with searchable motifs (dragon, wolf, ouroboros, toad, egg, green lion, squared circle).
- Wrote wiki page project_occultimgdb.md; updated index.md.

## [2026-06-27] ingest | Memory Palace batch — 3 deep pages, 1 refresh, 19 stubs
- Wrote 3 new deep project pages: `project_glassbeadgame.md` (Glass Bead Game — browser Glasperlenspiel placing esoteric-history "beads" with alchemical glyph attributes, engine-derived relations scored for reconciling opposites and spanning disciplines), `project_emblemprintshop.md` (Emblem Print Shop — local no-API CV pipeline cutting figures from alchemical emblems into 7,097 tagged transparent-PNG "image parts" with a scholarly browse layer), and `project_esotericbeatnews.md` (Esoteric Beat News — dependency-free static site aggregating ~30 esoteric podcasts/channels / ~3,000 episodes into a topic-tabbed card feed from a committed JSON catalog).
- Refreshed `project_socmagweb.md`: now live on Vercel, test suite up to 153 tests, SM-024 fixed; updated its index.md description accordingly.
- Added 19 new stub pages and indexed them: EmblemRoguelike, EmblemNovel, ALCHEMYTIMELINEMAP, audiobook-app, AlchemyBlockInvaders, CrowleyDB, AgrippaDOP, EsotericProjectsShowcase, ChristianCabalaDB, MagicalLatin, MedievalMagicDB, WitchcraftStudiesDB, TheosophicalAlchemyDB, ZorziHarmoniaMundi, neoplatonism-portal, Draft Academy, dungeon-architect, Tarot Dev, WitcherPortal.
- Added 22 new bullets total under index.md "### Projects" (3 deep + 19 stubs) and updated the existing SocMagWeb bullet.
- Ted's Memory Palace site (`C:\Dev\MemoryPalace`) was built over this wiki as a navigable front-end to the compiled knowledge synthesis.
