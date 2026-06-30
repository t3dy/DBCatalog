---
title: OCCULTIMGDB (Occult Image DB)
type: project
tags: [project, alchemy, occult, image-archive, static-site, game-assets, public-domain]
---

# OCCULTIMGDB — Occult Image DB

**Location:** `C:\Dev\OCCULTIMGDB\` · **Entry:** `OCCULTIMGDB/CLAUDE.md` · **Scope:** `OCCULTIMGDB/SCOPE.md`
**Started:** 2026-06-27 · **Status:** V4 — **DB-backed** archive with a **tabbed Explore viewer**, occult breadth begun. Canonical SQLite store `db/occultimgdb.db` (22 tables incl. `wanted` discovery queue) via `build_all.py`. **918 images · 31 works · 5 eras antiquity→MODERN · 71 deep academic entries · 10 traditions · 9/11 topics live · 10/13 collections live.** No longer alchemy-only: now spans alchemy, hermeticism, Kabbalah, ceremonial/goetic magic, astrology, witchcraft, divination (tarot), Rosicrucian, Enochian, theosophy, biblical-magic. Homepage `index.html` = Explore (Timeline/Eras/Regions/Topics/Figures/Collections tabs, image-forward masonry, lightbox+zoom); `gallery.html` = faceted gallery. Browsing taxonomy mined from the user's own esoteric-studies DBs. `RESEARCH_PLAN.md` + `data/wanted.json` drive systematic sourcing (engines: compendium-harvest, Iconclass enumeration, IIIF crawl, local mining, reception tracing); `scripts/fetch_commons.py` = Wikimedia-API sourcing tool.

## What it is

A browsable, scholarly-cataloged archive of **whole illustrations** from the alchemical and occult
tradition (late antiquity → early modern, later extending to Victorian/modern), built for
**game developers and artists** sourcing public-domain visual assets. Each entry is a complete image
(an emblem plate, a woodcut, a diagram, a portrait) with sourced metadata, a downloadable scan, and a
scholarly summary capped at 5,000 words.

Spun off from [EmblemPrintShop](#) as a deliberately **whole-image** project: it does **not** do the
atomic element-extraction that EmblemPrintShop pursued (cutting the dragon out of the emblem). The
distinction is the core design constraint.

## Architecture

Plain static **HTML/CSS/vanilla JS** (no build step; deploys to GitHub Pages/Netlify). A Python
importer (`scripts/build_catalog.py`, idempotent, Pillow) reads a source registry
(`scripts/config.py`), reuses the ~3,700 public-domain scans already on disk under
`C:\Dev\EmblemPrintShop\sources\` (nothing re-downloaded), generates thumb/card derivatives, and
emits `data/catalog.json`. Hand-authored scholarship lives in `data/overrides.json`, merged by id.
This follows the workspace's [Deckard Boundary](architecture_deckard_boundary.md): deterministic
Python builds the catalog; LLM/human judgment supplies the per-image essays.

## V1 corpus (curated "illustration" tier — 687 images, 8 works)

Atalanta Fugiens (Maier, 1618, 51) · Hypnerotomachia Poliphili (Colonna, 1499, 162) · Rosarium
Philosophorum (1550, 19) · Splendor Solis (Trismosin, 1532–35, 46) · Viridarium Chymicum (Stolcius,
1624, 108) · Philosophia Reformata plates (Mylius, 1622, 134) · Amphitheatrum Sapientiae (Khunrath,
1595/1609, 92) · Emblemata Sacra (Cramer, 1624, 75).

A second **page-scan tier** (Fludd, Hall, Marshall/Dee, Obrist medieval, McLean — ≈3,000 more) is
registered and available with `--all`, pending illustration-vs-text curation.

**V2 additions (2026-06-27 build-out):** ingested 10 by-text works from `C:\Dev\AlchemyBeatEmUp\staging\
raw_images\` — pushing coverage into the **medieval stratum** (Aurora Consurgens c.1420, pseudo-Geber
*Summa*), plus Ripley Scroll, Mutus Liber, Lambspring, Maier's *Symbola Aureae Mensae*, Agricola, Glauber,
Libavius, Biringuccio. Built a **relational hyperlinking layer** (`entity.html` profiles for creator/work/
tradition/motif/era, `browse.html` themes directory, `history.html` timeline) over a hand-authored
`entities.json`. Imported local scholarship: `Claudiens/site/data.json` discourse → all 51 Atalanta
emblem summaries; `EmblemPrintShop/data/emblems.json` → motif tags. System files now encode
context-engineering/agentic working rules (layered context, persist-every-step, Deckard seam).
Full sourcing account in `OCCULTIMGDB/SOURCINGIMAGES.md`.

## UX bet

Optimised for artists/game-devs who search by **motif** ("dragon", "furnace", "magic circle"),
not bibliography. Faceted browse (era / tradition / source work / motif), motif-aware text search,
one-click download, explicit per-item rights. Scholarly depth sits on the detail page. Aesthetic:
dark-academic / alchemical (gold-on-ink, Cormorant Garamond display).

## Research plan (path to "everything occult")

`OCCULTIMGDB/RESEARCH_PLAN.md` (2026-06-27) sets the strategy to source *every* extant occult image:
a universe-map on 3 axes (subject domain × period × medium/object), explicit blind spots (Iconclass/
Warburg classification, reception-vs-origin à la Apuleius, the bible as occult image-source, objects
beyond books, compendia-as-wanted-lists, image-vs-witness model, rights-as-data), and **5 discovery
engines** (compendium-harvest, Iconclass enumeration, IIIF crawl, local mining, reception tracing) feeding
a convergence loop. `data/wanted.json` is the machine-actionable discovery queue (33 seed targets, compiled
into the DB `wanted` table for gap reporting). Highest-yield next harvests: the Obrist alchemical corpus,
the *Geheime Figuren der Rosenkreuzer*, the Goetia 72 seals, witchcraft woodcuts.

## Sourcing gaps (human TODO)

The antiquity & grimoire stratum the user wants is **not yet downloaded**: Kleopatra *Chrysopoeia*
ouroboros, Zosimos/furnace diagrams, Solomonic circles, the 72 Goetia seals (already analysed in
[goetia_sigil_analysis.md](goetia_sigil_analysis.md) — wire those in), Theban alphabet, portraits
(Dee, Paracelsus, Agrippa), Aurora Consurgens, Mutus Liber, Ripley Scroll. 675/687 V1 images still
carry placeholder summaries by design.

## Related projects

[AtalantaClaudiens](project_claudiens.md) (Atalanta scholarship to reuse) ·
[HPMarginalia](project_hypnerotomachia.md) ·
[HermeticDB / Emerald Tablet](project_emeraldtablet.md) ·
[RenMagDB](project_renaissancemagic.md) ·
[Goetia Sigil Analysis](goetia_sigil_analysis.md) ·
[Alchemy Scryfall](project_alchemyscryfall.md).
