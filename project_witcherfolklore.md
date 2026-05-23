# Project: WitcherFolkloreDB

**Location**: `C:\Dev\WitcherFolkloreDB`
**Type**: Fictional-Historical Bridge (Knowledge Portal + Procedural Engine)

## Overview
A DH portal mapping the Slavic folklore, medieval bestiary traditions, and early modern folk magic sources underlying Andrzej Sapkowski's Witcher universe. Each monster, potion, ritual, and place in the Witcher corpus is traced back to documented Slavic mythology, medieval Polish chronicles, Latin bestiary traditions, and the scholarly folklore literature. Designed as a "Scholarly Bridge" serving the academic folklorist, the engaged Witcher reader, and the magical practitioner simultaneously — the canonical example of the triple-audience ideal.

## Core Content
- **Monster Mappings**: 60+ Witcher entities (striga, kikimora, leshy, drowner, bruxa, wyvern) traced to specific folklore sources with Aarne-Thompson-Uther tale-type classifications where applicable.
- **Folklore Corpus**: 40+ documented Slavic and Central European traditions, drawing on Afanasyev's Russian fairy tale collection, Kolberg's *Lud*, Moszyński's *Kultura ludowa Słowian*, and Szyjewski's *Religia Słowian*.
- **Medieval Sources**: 25 bestiary and chronicle entries (*Aberdeen Bestiary*, *Physiologus*, Gallus Anonymus's *Gesta principum Polonorum*, Vincentius Kadlubek's *Chronica Polonorum*) with direct comparison to Sapkowski's creature designs.
- **Sapkowski Texts**: All eight Witcher short story collections and the five-novel saga, with passage-level citation references indexed by creature/practice type.
- **Scholars**: 20 folklorists and Slavic studies scholars profiled — Propp's narrative morphology, Biegeleisen's folk magic documentation, Zowczak's witchcraft ethnography — with methodological stances and lineages.
- **ATU Classifications**: Aarne-Thompson-Uther tale-type index entries applied to Sapkowski's fairy-tale retellings (*A Grain of Truth* as ATU 428: The Wolf, *The Last Wish* as ATU 555: The Fisherman and His Wife).

## Architecture
- **Data Model**: Three-tier citation chain — `witcher_entities` → `folklore_sources` → `medieval_texts` — joined by a `citation_chains` table that enforces the three-field citation requirement.
- **Pipeline**: SQLite → Python → Next.js 15 SSG (following the HermeticDB model for relational browsing and provenance tooltips).
- **Frontend**: Relational browse views — clicking a Witcher monster surfaces its full citation chain, from Sapkowski's passage through to the medieval bestiary entry. Provenance tooltips on every claim.
- **Cross-Links**: Entity IDs resolve against WitchcraftStudiesDB (shared folk magic traditions), RenMagDB (shared herbalism and ritual traditions), and CrowleyDB (shared Slavic magical correspondences).

## System Invariants
- **Three-Field Citation Requirement**: Every mapping requires all three fields to be present: `witcher_text_ref` (specific passage, story/novel title, chapter), `folklore_source_ref` (documented tradition, publication, page), `scholarly_authority` (the folklorist or Slavic studies academic who identified the connection in print).
- **Deckard Boundary**: Sapkowski's published texts and documented folklore sources are immutable seed data. The LLM generates only the connecting scholarly commentary, which defaults to DRAFT/MEDIUM pending review.
- **No Speculative Mappings**: Connections without a `scholarly_authority` citation are tagged HYPOTHETICAL and rendered with a distinct visual badge — separating serious DH work from fan wiki interpretation.
- **ATU Tagging Discipline**: ATU classifications are drawn verbatim from Uther's 2004 revised index; no LLM assignment of tale types without a published scholarly precedent.

## Audience Analysis
- **Academic Folklorist**: The three-field citation chain and ATU classification system provide the methodological rigor expected of a serious Slavic studies resource. The project sits alongside — and cites — the same scholarly literature used in peer-reviewed journals.
- **Witcher Reader / Gamer**: The monster-page view (what Sapkowski wrote → what the folk tradition says → what the medieval text records) turns casual curiosity about creature lore into a guided scholarly journey without imposing academic friction.
- **Occult Practitioner**: The folk magic sections (herbalism, warding rituals, the practice of *znachorstwo* — folk healing) are documented as living traditions with Biegeleisen and Zowczak as authorities, making the database a genuine folkloric grimoire resource.

## Related Entities & Concepts
- [[Andrzej Sapkowski]]
- [[Slavic Folklore]]
- [[Vladimir Propp]]
- [[Aarne-Thompson-Uther Index]]
- [[Medieval Bestiary]]
- [[Folk Magic]]
- [[WitchcraftStudiesDB]]
- [[RenMagDB]]
- [[CrowleyDB]]
- [[Digby Game]]
- [[Fictional-Historical Bridge]]
