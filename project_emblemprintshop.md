---
title: Emblem Print Shop
type: project
description: A local, no-API computer-vision pipeline that cuts every figure out of early modern alchemical emblems into a tagged, citable library of 7,097 transparent-PNG "image parts" with a scholarly browsing layer.
tags: [project, alchemy, emblems, computer-vision, extraction, grounding-dino, sam, dh, catalog, iconography]
updated: 2026-06-27
---

# Emblem Print Shop

A consolidation hub and extraction pipeline for early modern alchemical imagery, living at `C:\Dev\EmblemPrintShop`. It is **not** a print-on-demand storefront and not (yet) a poster generator: it is an **emblem image-parts extraction pipeline plus a scholarly browser**. The practical goal is to turn existing emblem-book catalog work into a searchable library of reusable visual elements — dragons, lions, hermaphrodites, vessels, furnaces, suns, moons, kings, queens — each cut out as a transparent PNG, tagged against a controlled iconographic vocabulary, sourced, and citable, so they can later be recomposed into "print-shop style" outputs. The "print shop" is aspiration; the built reality is the cutout library and catalog.

## What it is
Three things stacked:
1. **A consolidation of nearby projects.** `sources/` snapshots 17 corpus folders (claudiens / Atalanta Fugiens, cramer, rosarium, splendor_solis, khunrath, stolcius, mylius_philosophia, mclean_second, maier_arcana, maier_viatorium, maier_af_mellon, fludd, hall_manuscripts, hypnerotomachia-polyphili, obrist_medieval, paul_marshall, theosophical-alchemy-db). The README is explicit that `sources/` is raw material, not the final architecture; canonical work happens in top-level `data/`, `assets/`, `scripts/`, `prototype/`.
2. **A CV extraction pipeline** (`scripts/`, `scripts/pipeline/`) that detects, segments, and cuts out every object in an emblem plate.
3. **A static scholarly browser** (`prototype/`) — gallery, emblem catalog, motif atlas, concept index, and a standalone "Complete Alchemical Images" reference site covering ~30 image sequences from ancient Egypt to 1788.

## Architecture / Pipeline
Open-source, **CPU-only, no API keys** for the core extraction (Claude Vision is used only as an optional re-ID pass). Six-stage flow, documented in `docs/VISUAL_ELEMENT_EXTRACTION_STRATEGY.md`:

1. **Detect** — `pipeline/comprehensive_detector.py` runs **GroundingDINO-tiny** in six text-prompted passes, one per semantic category (figures / animals / plants / landscape / architecture / objects-weapons-equipment), then NMS-deduplicates (IoU > 0.5).
2. **Segment** — `pipeline/segmenter.py` feeds each bbox to **SAM ViT-base** for a pixel mask.
3. **Postprocess** — `pipeline/postprocessor.py` removes paper background (Otsu ink detection), severs thin hatching "bridges" to the background, and keeps only bbox-overlapping components. Output is a transparent RGBA PNG plus reference crop JPG and a red-mask review overlay.
4. **Overlap analysis** — `pipeline/overlap_analyzer.py` builds a pairwise containment matrix and union-find groups, so an overlapping pair (man-holding-sword, dragon-coiling-tree) is extracted **both individually and as a composite**.
5. **Catalog build** — `build_object_catalog.py` reads each emblem's `summary.json` and writes a structured `object_catalog` into `data/emblems.json` (label, motif_id, category, detection_score, appearance, iconographic_meaning, alchemical_valence, png paths); `build_catalog.py` / `build_emblem_catalog.py` aggregate `prototype/gallery_catalog.json`.
6. **Refine + browse** — heuristic junk filtering (`flag_junk_crops.py`, drops text-pages and full-scene crops), optional Claude-Vision re-identification of mislabeled animal crops (`reidentify_objects.py`, rubric in `docs/ANIMAL_RECOGNITION_SYSTEM.md`), text-to-emblem linking (`build_text_visual_links.py`), and a concept index (`build_concept_index.py`). A `watch_and_rebuild.py` monitor auto-rebuilds the catalog when an extraction job goes idle.

**Data ontology** (`data/`): `works.json` (source books), `emblems.json` (whole-plate records + `object_catalog`), `motifs.json` (controlled vocabulary), `visual_elements.json` (individual extracted records). This domain-model-vs-extraction-output split is a small instance of the [[architecture_deckard_boundary]] discipline seen elsewhere in the workspace.

## Status (2026-06-27) — honest accounting
Built and real, last major work ~2026-06-14 (the data files are not API metadata; counts below are read from the files):

- **Catalog**: `prototype/gallery_catalog.json` reports **`total: 7097` elements, 124 tags, 16 projects** — this matches the latest commit (`539f09f Update gallery catalog with filtered extractions (7,097 elements)`). 268 junk crops were dropped to reach this number.
- **Extracted assets on disk**: `assets/extracted_all/` holds **1,653 per-emblem directories** (comprehensive mode); legacy `assets/extracted/` holds ~8,315 entries. Neither is in git (README notes 25GB+, regenerate locally).
- **Data files**: `data/motifs.json` has **79 entries** (README/strategy doc say "65" — the vocabulary has grown past its own documentation); `data/visual_elements.json` has **738 records** (a partial slice, not the full 7,097 — the gallery catalog, not this file, is the authoritative element list); `data/works.json` currently defines only **2 works** (Atalanta Fugiens, Hypnerotomachia) despite 17 source corpora, i.e. `works.json` is under-populated relative to what has been extracted.
- **Scholarly layer**: concept index = **140 concepts** over 7,097 records (`concept_index.json`); text linking = **56 emblems** mapped to source chapters (`emblem_text_links.json`) — the linker is keyword-based and the docs admit only ~0.8% of elements got links. Text extraction covers ~140 chapters from 8–9 books (`Markdown/`); the Maier Atalanta Fugiens Mellon copy is image-only and still **needs OCR (not done)**.
- **Re-identification**: only **121 animal crops** were vision-verified — human-scale, not corpus-scale; the other ~7,000 elements carry raw detector labels.
- **Corpus table caveat**: the README marks **Obrist Medieval (319 plates) as "extraction in progress,"** but `obrist_extraction.log` ends with `Batch complete: 305 ok, 14 skipped, 0 failed / 944 individual, 162 composite` — so Obrist extraction has in fact finished; the README table is stale on this row. Equipment-category re-runs for Rosarium/Splendor Solis also completed per `equipment_*.log`.
- **Tests**: a pytest suite exists (`tests/`, README cites "28 behavioral tests"; pipeline-integration test runs real model inference, ~3 min). Many files under `tests/` are actually ad-hoc IIIF/Internet-Archive sourcing scripts (`search_ia_*.py`, `check_iiif_manifests.py`), not unit tests.
- **Build system**: **no `package.json`, no JS build** — the prototype is static HTML served by `prototype/serve.py` (port 8765, with `POST /api/save-edit` and `/api/save-review` for the review/editor pages). Python is the only toolchain.
- **Print-shop output stage**: **not built.** Recomposition of cutouts into print-shop artifacts is stated as the eventual goal; nothing in `scripts/` or `prototype/` yet composes new images from the parts.

Bottom line: the extraction-and-catalog half is genuinely done and substantial (7,097 cataloged elements, multi-corpus); the "print shop" (recomposition/output) and the scholarly-linkage polish (full re-ID, full text linking, OCR of image-only sources, populated `works.json`) are partial or unstarted.

## Tech
Python only. GroundingDINO-tiny + SAM ViT-base via HuggingFace `transformers` (CPU), OpenCV for postprocessing, PyMuPDF for PDF→Markdown text extraction, optional Claude Vision (Opus) for animal re-ID. Static HTML/JS prototype served by a stdlib `http.server` script. pytest for the behavioral suite. Git-tracked except the multi-GB extracted-asset directories.

## Relation to the ecosystem
Emblem Print Shop is the **image-infrastructure layer** under the user's emblem cluster. It ingests the Atalanta Fugiens corpus from [[project_claudiens]] (its `sources/claudiens` snapshot, 51 AF plates, furnaceandfugue.org provenance) and the broader Rosicrucian/Rosarium material from the TheosophicalAlchemyDB project, then turns whole plates into reusable cut-out parts. Those parts are the natural raw asset supply for the two emblem **consumer** projects in this workspace — **EmblemRoguelike** (browser roguelike on Maier's *Atalanta Fugiens* with an alchemy-lab sim) and **EmblemNovel** (graphical narrative adventure built from emblems) — both of which need emblem-drawn visual elements; the handover even notes "EmblemRoguelike is canonical" game repo. Thematically it sits alongside the Hermetic/alchemical material in [[project_emeraldtablet]], and shares the pure-data-model-vs-IO-adapter instinct catalogued as [[architecture_deckard_boundary]]. Where Claudiens is a finished DH **reading** site for one book, Emblem Print Shop is the cross-corpus **parts foundry** spanning Atalanta, Rosarium, Splendor Solis, Khunrath, Stolcius, Mylius, Cramer, and more.

## Pointers
- Overview / run commands: `C:\Dev\EmblemPrintShop\README.md`
- Latest state & roadmap: `C:\Dev\EmblemPrintShop\docs\CURRENT_HANDOVER.md`, `docs\SESSION_SUMMARY_2026_06_14.md`
- Pipeline design: `C:\Dev\EmblemPrintShop\docs\VISUAL_ELEMENT_EXTRACTION_STRATEGY.md`
- Re-ID rubric: `C:\Dev\EmblemPrintShop\docs\ANIMAL_RECOGNITION_SYSTEM.md`
- Sourcing inventory (IIIF/IA provenance): `C:\Dev\EmblemPrintShop\docs\IMAGES_TO_SOURCE.md`
- Core CV code: `C:\Dev\EmblemPrintShop\scripts\pipeline\` (`comprehensive_detector.py`, `segmenter.py`, `postprocessor.py`, `overlap_analyzer.py`)
- Canonical data: `C:\Dev\EmblemPrintShop\data\` (`works.json`, `emblems.json`, `motifs.json`, `visual_elements.json`)
- Browser entry: `C:\Dev\EmblemPrintShop\prototype\index.html` (serve via `prototype\serve.py`, port 8765)
- Catalog: `C:\Dev\EmblemPrintShop\prototype\gallery_catalog.json`
- Reference site: `C:\Dev\EmblemPrintShop\prototype\alchemical-images\index.html`
