---
title: "Project: Pico della Mirandola Knowledge Portal"
type: project
description: "A digital humanities knowledge portal for Giovanni Pico della Mirandola, his primary texts, modern scholarship, and debates around magic, Kabbalah, Platonism, Aristotelianism, astrology, and human dignity."
tags: [pico, renaissance, magic, kabbalah, platonism, digital-humanities, knowledge-portal]
---

# Project: Pico della Mirandola Knowledge Portal

**Location**: `C:\Dev\PicoDB`  
**Type**: Digital Humanities Knowledge Portal  
**Status**: Initialized corpus, database, ontology, artifact system, reading system, timeline/map layer, and active study-pass writing

## Overview

The Pico portal is a source-grounded research environment for Giovanni Pico della Mirandola and Pico studies. It is designed to support close reading of Pico's works, systematic synthesis of modern scholarship, scholar biographies, historiographical mapping, and future knowledge products on Pico's philosophy, magic, Kabbalah, astrology, theology, and reception.

The project follows the broader knowledge-portal pattern used by RenMagDB and the other `C:\dev\wiki` projects: deterministic extraction first, SQLite as the stable evidence layer, then reviewed LLM-assisted summaries and interpretive pages.

## Current Corpus State

- **73 source files processed** from the Pico folder.
- **73 Markdown full-text files** created in `E:\pdf\renaissance magic\Pico\Markdown`.
- **Project repository** created at `C:\Dev\PicoDB` and deployed to `https://github.com/t3dy/PicoDB`.
- **SQLite database** created at `C:\Dev\PicoDB\db\pico.db`.
- **10,538 page / EPUB-section records** stored in `pages`.
- **1,829 section or generated reading-unit records** stored in `sections`.
- **25 scholar-profile seed records** created.
- **207 reading tasks** queued for close reading, section summaries, and Pico work dossiers.
- **5 primary-text gap records** created.
- **FTS5 search index** created for all 73 documents.
- **11 artifact types** defined for systematic reading and writing.
- **35 reading artifacts** created for source packets, section summaries, biography, historiography, concepts, scholars, and work dossiers.
- **41 seed claims** extracted into the claims table.
- **77 Pico life/reception/scholarship timeline events** seeded.
- **20 map locations** and **4 route layers** seeded for Italy-France geography.

## Core Files

- `scripts/init_pico_portal.py`: idempotent bootstrap script for extraction, database creation, ontology seeding, and static-site generation.
- `Markdown/`: full-text Markdown conversions of every PDF/EPUB source.
- `db/pico.db`: SQLite catalog, page text, sections, scholars, ontology terms, reading tasks, text gaps, and FTS5.
- `data/pico_manifest.json`: top-level manifest with corpus counts and paths.
- `data/pico_ontology.json`: seed ontology for Pico reading and scholarship synthesis.
- `data/corpus_catalog.json`: portable JSON catalog for the viewer.
- `docs/READING_SYSTEM.md`: operating system for systematic reading.
- `docs/ARTIFACT_SYSTEM.md`: markup-and-writing system for turning readings into reusable scholarship.
- `docs/PICO_TEXT_GAPS.md`: living register of missing or uncertain Pico texts.
- `data/reading_artifact_ontology.json`: artifact ontology for source packets, claims, section summaries, scholar profiles, work dossiers, concept dossiers, historiography nodes, timeline events, map records, and website outputs.
- `data/pico_life_timeline.json`: seeded life/reception/scholarship timeline.
- `data/pico_locations.json` and `data/pico_map_routes.json`: geocoded map data.
- `artifacts/website_notes/`: initial notes for biographies, scholar profiles, and Pico work dossiers.
- `templates/`: section summary, scholar profile, and Pico work dossier templates.
- `site/index.html`: static viewer for corpus overview, reading artifacts, claims, timeline, map, catalog, and Markdown links.

## Data Model

- `documents`: physical source files, hashes, Markdown paths, type, themes, Pico works, duplicate links, extraction status.
- `pages`: page- or EPUB-section-level extracted text.
- `sections`: PDF bookmarks or generated reading units with pending summary fields.
- `scholars`: detected scholar names and biography/profile status.
- `ontology_terms`: entity classes, themes, relationships, and evidence statuses.
- `reading_tasks`: queue for close reading and synthesis work.
- `pico_text_gaps`: living accounting of Pico primary texts or editions still to locate or verify.
- `document_fts`: full-text search over the corpus.
- `artifact_types`: controlled vocabulary for reading and writing artifacts.
- `reading_artifacts`: file-backed working notes with target entity, status, and evidence status.
- `claims`: atomic source-tethered claims with type, theme, evidence page, confidence, and review status.
- `website_cards` / `website_pages`: promoted public-facing cards and draft long-form pages.
- `timeline_events`: dated life, controversy, writing, reception, and scholarship events.
- `locations` / `map_routes`: geocoded map entries and named route layers.

## Artifact System

The portal now has a formal intermediate layer between raw corpus text and public writing:

1. source packet
2. claim record
3. section summary
4. scholar profile
5. Pico work dossier
6. concept dossier
7. historiography node
8. timeline event
9. location record
10. website card/page

This is meant to prevent summary drift. Website prose should be promoted from source packets, claims, section summaries, scholar profiles, and work dossiers rather than written directly from memory.

## Timeline and Map

The current timeline has 77 draft entries from Pico's birth in 1463 through twentieth- and twenty-first-century Pico scholarship. Entries are explicitly marked as verified, likely, interpretive, placeholder, or needs-review.

The map layer currently includes Mirandola, Bologna, Ferrara, Padua, Pavia, Milan, Florence, Careggi/Fiesole, San Marco, Reggio Emilia, Arezzo, Rome, Perugia, La Fratta, Paris, Vincennes, and provisional France-Italy corridor nodes. The website viewer has sections for Overview, Research Artifacts, Timeline, Map, and Catalog.

## Study Pass 002

The second close-reading pass created source packets and website notes for Howlett, Copenhaver, Farmer, Wirszubski/Kristeller, and Akopyan. It emphasizes:

- Howlett's re-evaluation of Pico against simple Oration-centered, Ficinian, or proto-modern myths.
- Copenhaver's critique of the modern "dignity" Pico and his relocation of the trial material in scholastic, theological, and heresy contexts.
- Farmer's claim that the 900 Theses, not the Oration, are the center of the Roman debate project.
- Wirszubski and Kristeller's account of Pico's Kabbalah through Hebrew study, Mithridates' translations, and the founding of Christian Kabbalism.
- Akopyan's structure for treating Pico's astrology as a developmental problem before, within, and after the Disputationes.

New website-facing notes now cover an expanded Pico biography, the "Against the Oration-Only Pico" historiography page, Christian Kabbalah, Pico and astrology, and scholar cards for Farmer, Wirszubski, and Akopyan.

## Study Pass 003

The third pass began sustained primary-text and textual-transmission work. It created source packets and work-dossier notes for:

- the Oration opening as indeterminacy, philosophical discipline, angelic imitation, and ascent;
- *On Being and the One* as a concordist and apophatic text reconciling Plato and Aristotle by semantic distinction;
- the *Heptaplus* proems as a Genesis hermeneutics project organized by hidden wisdom, sevenfold interpretation, the three worlds, and man as a fourth lesser world;
- Farmer's treatment of the 900 Conclusions as a debate database with hidden connections, edition risk, thesis clusters, and oral-disputational logic;
- Farmer's Anti-Pico problem: Gianfrancesco/Savonarolan textual tampering risk, especially for late printed Pico and the *Disputationes*.

This pass added the portal rule that late doctrinal claims from printed Pico texts need explicit `transmission_status` or equivalent risk annotation before promotion.

## Study Pass 004

The fourth pass created formal style and coverage standards for exhaustive section-by-section work:

- `docs/SECTION_SUMMARY_STYLE_GUIDE.md`
- `docs/ARGUMENT_REFERENCE_STYLE_GUIDE.md`
- `docs/SUMMARY_COVERAGE_PROTOCOL.md`
- expanded `templates/section_summary_template.md`
- updated `data/reading_artifact_ontology.json` to version 0.3.0
- created `data/section_summary_coverage.json`

It also seeded six formal section-summary artifacts covering the Oration opening, the Oration discipline ladder, the opening of *On Being and the One*, two *Heptaplus* proem units, and Farmer's substance/accident section in the 900 Conclusions chapter.

## Study Pass 005

The fifth pass created a scholarly-values layer for close reading:

- `docs/SCHOLARLY_VALUES_STYLE_GUIDE.md`
- `docs/KABBALAH_READING_PROTOCOL.md`
- updated ontology to version 0.4.0
- created guide-scholar source packets and profiles for Copenhaver, Edelheit, Dougherty, Howlett, Busi, and Wirszubski
- added a Busi-Wirszubski Kabbalah protocol for the *Oration*, 900 Conclusions, and *Heptaplus*

The pass treats Copenhaver as anti-myth/trial guide, Edelheit as scholastic-source guide, Dougherty as corpus/genre/edition guide, Howlett as three-pillar/concord guide, Wirszubski as Kabbalah source-control guide, and Busi as qabbalah-praxis/correspondence guide.

## Study Pass 006

The sixth pass ingested the Allen EPUB from Downloads and made Michael J. B. Allen the guide scholar for the Pico-Ficino relation:

- copied Allen's *Studies in the Platonism of Marsilio Ficino and Giovanni Pico* into `C:\Dev\PicoDB`
- converted it to Markdown and ingested it as document `Studies_in_the_Platonism_of_Marsilio_Ficino_and_Giovanni_PicoMichael_J._B._AllenRoutledge1080299_epub_65585d05`
- added `docs/FICINO_PICO_READING_PROTOCOL.md`
- updated ontology to version 0.5.0 with Ficino-Pico reading fields
- created Allen source packets for "Cultura hominis," "The Birth Day of Venus," and the second Ficino-Pico controversy
- added primary reread artifacts for *On Being and Unity*, the metaphysics of the *Oration*, and the metaphysical system of the 900 Conclusions
- started `artifacts/essays/pico_ficino_dispute_longform_draft.md`

Allen's governing value is "contentious co-Platonism": Pico should not be reduced to Ficino's disciple, Ficino's enemy, or a non-Platonic scholastic. Pico uses Ficino's recovered Plato and revises it through Aristotle, scholasticism, Christology, Kabbalah, and disputational method.

## Study Pass 007

The seventh pass created the companion longform Kabbalah synthesis:

- added `artifacts/essays/pico_kabbalah_synthesis_longform_draft.md`
- added `artifacts/historiography/kabbalah_scholar_synthesis_matrix.md`
- updated `docs/KABBALAH_READING_PROTOCOL.md` with a scholar synthesis overlay
- updated ontology to version 0.6.0 with `kabbalah_synthesis_fields`, `kabbalah_taxonomy`, and a scholar-role synthesis map
- added website cards for "Pico's Kabbalah" and "Kabbalah Scholar Matrix"

The pass synthesizes Wirszubski, Busi, Copenhaver, Farmer, Howlett, Edelheit, Dougherty, and Allen. Its governing position is that Pico's Kabbalah is a source-critical, translational, Christianizing, magical, apologetic, scholastic, thesis-cluster, and historiographical problem at once.

## Study Pass 008

The eighth pass created a biographical synthesis layer:

- added `docs/BIOGRAPHICAL_READING_PROTOCOL.md`
- added `artifacts/essays/pico_biography_scholar_synthesis_draft.md`
- added `artifacts/historiography/pico_biography_scholar_method_matrix.md`
- added `artifacts/source_packets/pico_biographical_source_gaps_pass008.md`
- updated ontology to version 0.7.0 with biographical reading fields, life-register taxonomy, and biography scholar-role synthesis
- added website cards for "Pico Biography," "Biography Method Matrix," and "Biography Source Gaps"

The pass treats Pico's life as a source-controlled intellectual geography rather than a prodigy myth. Howlett governs mobility, elite networks, and the critique of "St. Pico"; Edelheit governs scholastic formation; Copenhaver governs Roman trial danger and Oration myth; Dougherty/Borghesi govern works, letters, genre, and editions; Farmer governs the Roman debate; Busi/Wirszubski govern Kabbalah source infrastructure; Allen governs Ficino affinity and dispute.

## Study Pass 009

The ninth pass copied Crofton Black's *Pico's Heptaplus and Biblical Hermeneutics* and two reviews from Downloads into `C:\Dev\PicoDB\sources\crofton_black_heptaplus`, converted/ingested them, and added a Black-centered Heptaplus research layer:

- added `docs/HEPTAPLUS_BLACK_READING_PROTOCOL.md`
- added `artifacts/scholar_profiles/crofton_black_values_profile.md`
- added `artifacts/source_packets/black_heptaplus_structure_packet.md`
- added `artifacts/section_summaries/black/black_heptaplus_chapter_summaries_pass009.md`
- added the Black-guided Heptaplus essay draft
- seeded parallel essay drafts on Plato/Aristotle, Aquinas/Dionysius, Pico's own-opinion theses, Neoplatonist and Arabic authors in the 900, Arabic intellect/felicitas, Dionysian anagogy, and the Heptaplus after the Oration
- updated ontology to version 0.8.0 with `heptaplus_black_reading_fields` and `parallel_essay_program_fields`

Black now governs Heptaplus readings as structured biblical hermeneutics: Genesis 1.1-27, sevenfold architecture, Moses, Aquinas, Pseudo-Dionysius, Arabic intellect traditions, Jewish/Kabbalistic sources, Bereshit, sabbath, jubilee, and the forty-nine gates.

## Study Pass 010

The tenth pass copied six astrology-related PDFs from Downloads into `C:\Dev\PicoDB\sources\pico_astrology_pass010`, converted/ingested them, and added an astrology synthesis layer:

- added `docs/ASTROLOGY_READING_PROTOCOL.md`
- added `artifacts/historiography/pico_astrology_scholar_matrix.md`
- added `artifacts/source_packets/astrology_new_documents_pass010.md`
- added `artifacts/section_summaries/astrology/astrology_new_documents_chapter_summaries_pass010.md`
- added `artifacts/concepts/pico_astrology_taxonomy_pass010.md`
- added the Pico and astrology synthesis essay draft
- updated ontology to version 0.9.0 with astrology reading fields, taxonomy, and scholar-synthesis guidance

Akopyan now governs developmental chronology; Rabin governs historiographical correction; Rutkin governs the early Commento/desire problem; Vanden Broecke governs reform, rejection, and Louvain reception; Farmer governs posthumous and Savonarolan textual risk; Allen and Black keep astrology tied to Ficinian Platonism, Heptaplus cosmology, and the broader metaphysical program.

## Study Pass 011

The eleventh pass collected Pico's angelology across the Oration, 900 Conclusions, Heptaplus, and related scholarship:

- added `docs/ANGELOLOGY_READING_PROTOCOL.md`
- added `artifacts/concepts/pico_angelology_taxonomy_pass011.md`
- added `artifacts/source_packets/pico_angelology_source_map_pass011.md`
- added `artifacts/section_summaries/angelology/pico_angelology_passage_matrix_pass011.md`
- added `artifacts/historiography/pico_angelology_scholar_matrix.md`
- added the Pico angels and angelology synthesis essay draft
- updated ontology to version 0.10.0 with angelology reading fields, taxonomy, and scholar-synthesis guidance

The pass treats angels as a hinge between anthropology, hierarchy, intellect, exegesis, Kabbalah, Ficinian/Neoplatonic metaphysics, Arabic theories of separate intellect and felicitas, Thomistic limits on created knowledge, and grace.

## Study Pass 012

The twelfth pass copied six reviews of Pico Opera, Garin's Mirandola congress volumes, and Speyer's *Carmina latina* from Downloads into `C:\Dev\PicoDB\sources\pico_opera_reviews_pass012`, converted/ingested them, and added a primary-text acquisition layer:

- added `docs/PICO_PRIMARY_TEXT_ACQUISITION_PROTOCOL.md`
- added `artifacts/source_packets/opera_reviews_pass012_source_packet.md`
- added `artifacts/section_summaries/opera_reviews/opera_reviews_section_summaries_pass012.md`
- added `artifacts/concepts/pico_missing_writings_taxonomy_pass012.md`
- added the Pico missing-writings / next-steps essay draft
- updated ontology to version 0.11.0 with primary-text acquisition fields and a missing-writings priority queue

The pass makes Basel Opera control, the Bologna 1496 posthumous collection, the Commento, Disputationes, De imaginatione, Carmina/poem witnesses, letters, Apologia/condemned theses, Gianfrancesco's Vita, More's Life, and related source-ecology texts the next primary-corpus priorities.

## Study Pass 013

The thirteenth pass continued the missing-writings work by acquiring and converting two corpus-control/reception witnesses:

- ingested the Internet Archive OCR of the 1557 Basel *Opera omnia Ioannis Pici* as a searchable Markdown and database control witness
- ingested the public-domain More/Rigg *Life of Pico* PDF as a reception witness for biography and English devotional Pico
- added `docs/MISSING_WRITINGS_ACQUISITION_LOG.md`
- added source packets for the web acquisition pass, Basel Opera witness, and More/Rigg Life witness
- added `artifacts/concepts/pico_corpus_control_dashboard_pass013.md`
- revised the missing-writings essay and gap register
- updated ontology to version 0.12.0 with corpus-control acquisition statuses

The main correction is that `De imaginatione` should be treated as Gianfrancesco Pico's related 1501 work, not as a missing Giovanni Pico primary text unless new evidence says otherwise. The highest current missing-writing priorities are structural segmentation of the Basel Opera, acquisition/control of the Commento, reliable witness control for the Disputationes, poem-manuscript control, letter-by-letter summary, and reception-aware reading of More/Gianfrancesco.

## Study Pass 014

The fourteenth pass answered the Commento access question and upgraded the work from a gap/lead to controlled primary text:

- acquired the full Italian *Commento sopra una canzone d'amore di Girolamo Benivieni* through Biblioteca Italiana's TEI/XML endpoint
- converted the TEI into Markdown and SQLite sections: dedication, Benivieni's address, canzone, Book I, Book II, Book III, and *Commento particulare*
- acquired Thomas Stanley's early modern English translation witness through Edmund G. Gardner's 1914 reprint of *A Platonick discourse upon love*
- added Commento source packets, a structural summary, a Commento reading ontology, and a reading-plan essay
- updated the ontology to version 0.13.0 with Commento close-reading fields and translation/reception controls

The project now treats the Italian TEI as the controlling text and Stanley as a reception witness to collate, not as a substitute for Pico's Italian. Next work should summarize every Commento chapter and stanza while tagging Ficino agreement/correction, love and beauty doctrine, being modes, hierarchy, poetic theology, celestial causality, Dionysian/Christian controls, and any biblical or Kabbalistic hints.

## Study Pass 015

The fifteenth pass registered Sears Jayne's modern English translation of the *Commento* as a restricted translation witness:

- opened the Internet Archive item for Jayne's *Commentary on a Canzone of Benivieni*
- added a bibliographic/access stub rather than a transcript, because the item is under controlled digital lending
- added a source packet and a Commento translation-collation protocol
- updated ontology to version 0.14.0 with restricted-translation note fields

Jayne should be used for page-level notes, short quotation anchors, and translation collation against the Italian TEI and Stanley, not as a full-text repository source.

## Study Pass 016

The sixteenth pass began PicoDB's own English translation of Pico's Italian *Commento*:

- added `COMMENTO_TRANSLATION_PROTOCOL.md`
- added an original translation policy for the *Commento*
- translated the title, Bonacursius dedication, and Benivieni's address to the reader
- added a translation queue and glossary seeds for the next sections
- updated ontology to version 0.15.0 with original-translation fields

The translation is made from the controlled Italian TEI witness. Stanley and Jayne are comparison witnesses only, not source texts for reconstruction.

## Study Pass 017

The seventeenth pass studied Olga Zorzi Pugliese's article on Girolamo Benivieni as Pico's friend, collaborator, and translator:

- added a Pugliese source packet
- added a Commento transmission note focused on Benivieni's mediation and softening of anti-Ficinian criticism
- added Pico's *Expositio singularis in Orationem Dominicam* / Pater Noster commentary to the acquisition queue
- updated ontology to version 0.16.0 with Commento transmission fields

The article does not change the controlling Italian Commento text, but it reinforces the need to read the Commento as a mediated poem-commentary artifact shaped by Benivieni's collaboration, publication, and revision activity.

## Seed Themes

- Kabbalah / Cabala / Qabbalah
- Magic / magia
- Astrology
- Platonism and Neoplatonism
- Aristotelianism and scholasticism
- Human dignity and freedom
- Concord, syncretism, and prisca theology
- Philology, Hebrew, transmission, and translation
- Theology and biblical hermeneutics
- Historiography of Pico studies

## Pico Texts Detected

The first deterministic pass detected corpus material related to:

- *Heptaplus*
- *900 Theses / Conclusiones*
- *Commento* on Benivieni's canzone
- *Oration on the Dignity of Man*
- *On Being and the One*
- *Letters / Lettere*
- *Disputationes adversus astrologiam divinatricem*
- *Apologia*
- Poems

These detections are filename/text-pattern seeds, not final bibliographic judgments.

## Gap Register

The initialized gap register currently flags:

- *Disputationes adversus astrologiam divinatricem*: likely secondary-only in the current corpus; verify whether a standalone primary text is present.
- *Commento sopra una canzone d'amore composta da Girolamo Benivieni*: partial or uncertain; verify complete primary text coverage.
- *De imaginatione*: not identified from filenames.
- Complete correspondence corpus: partial; a `Lettere` file exists but completeness must be checked.
- Manuscript/critical-edition details for the anti-astrology text: metadata needed.

## Reading System

The portal uses a staged reading workflow:

1. Bibliographic audit.
2. Structure and section audit.
3. Exhaustive section summaries.
4. Scholar argument extraction.
5. Pico work dossiers.
6. Gap register updates.
7. Reviewed portal cards and pages.

All summaries must remain tethered to the extracted full text in `Markdown/` and `db/pages`.

## Related Projects

- [[RenMagDB (Renaissance Magic)]]
- [[HermeticDB (Emerald Tablet)]]
- [[QueryPat (Philip K. Dick)]]
- [[Book History Pipelines]]
- [[Progressive Context Engineering]]
- [[The Deckard Boundary]]
