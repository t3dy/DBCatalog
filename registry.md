---
name: registry
description: How to resolve a fuzzy project reference ("my alchemy databases", "the emblem games", "the PKD sites") to specific projects. Theme/alias map + pointer to the machine-readable registry.tsv.
type: system
status: ACTIVE
tags: [registry, discovery, themes, routing, meta]
---

# Project Registry — resolving "my X projects"

When the user refers to a group of projects by theme rather than by name —
**"my alchemy databases"**, "the emblem games", "the PKD sites", "the NES music tools" —
resolve it here. This works from *any* project because `C:\Dev\CLAUDE.md` points every
session to this file.

## How to resolve

1. **Match the phrase to a theme below** → you get the project slugs.
2. **Look up each slug in `registry.tsv`** (tab-separated, same folder) for its canonical
   `path`, `live` URL, `tags`, and one-liner. That file is generated — trust it for paths.
3. **No theme matches?** Grep `registry.tsv` by keyword/tag, e.g.
   `rg -i "tarot|alchemy" registry.tsv`. Tags are in column 7.
4. **Still unsure which the user means?** List the 2–4 candidates with one-liners and ask.

Slugs are wiki page names: `project_<slug>.md`. Themes overlap on purpose (a project can
belong to several). "Databases" excludes games; "games" excludes databases — keep that split.

## Theme / alias map

### Alchemy — databases & scholarly portals
*"my alchemy databases", "the alchemy DBs", "alchemy scholarship"*
`project_alchemytimelinemap` (+ `project_mapresearch`, map R&D) · `project_theosophicalalchemydb` · `project_emeraldtablet`
(Hermetic/alchemical) · `project_occultimgdb` (alchemical image archive) ·
`project_emblemprintshop` (alchemical-emblem CV library) · `project_claudiens` (Atalanta
Fugiens). *Adjacent magic/esoteric DBs, not strictly alchemy:* `project_renaissancemagic`,
`project_medievalmagicdb`, `project_christiancabaladb`, `project_witchcraftstudiesdb`,
`project_zorziharmoniamundi`, `project_neoplatonism`, `project_crowleydb`, `project_pico`,
`project_agrippadop`, `goetia_sigil_analysis`.

### Alchemy — games & interactive
*"the alchemy games", "alchemy game"*
`project_alchemyblockinvaders` · `project_alchemybeatemup` · `project_alchemytetris`
(cluster) · `project_alchemyscryfall` · `project_emblemroguelike` · `project_emblemnovel` ·
`project_glassbeadgame` · `project_magicallatin` (alchemy lab).

### Emblems / Atalanta Fugiens (cross-cutting)
*"the emblem projects", "Atalanta stuff", "the Maier projects"*
`project_claudiens` · `project_emblemprintshop` · `project_emblemroguelike` ·
`project_emblemnovel` · `project_hpin3d` · `project_emblemsin3d` · `project_fuguejukebox` ·
`project_occultimgdb`.

### 3D emblem viewers
*"the 3D emblem worlds", "emblems in 3D"*
`project_hpin3d` · `project_emblemsin3d`. (Scratch fork: ANTIGRAVEMBLEMSIN3D — see [[coverage]].)

### Hypnerotomachia Poliphili
`project_hypnerotomachia` (marginalia DB) · `project_hpin3d` (3D viewer).

### Esoteric / occult knowledge portals (DH)
*"the esoteric portals", "the magic databases", "the occult DBs"*
`project_renaissancemagic` · `project_medievalmagicdb` · `project_witchcraftstudiesdb` ·
`project_christiancabaladb` · `project_neoplatonism` · `project_theosophicalalchemydb` ·
`project_crowleydb` · `project_pico` · `project_agrippadop` · `project_zorziharmoniamundi` ·
`project_emeraldtablet` · `goetia_sigil_analysis`.

### Philip K. Dick
*"the PKD sites", "Philip K Dick projects"*
`project_querypat` (scholarship portal) · `project_pkdfestsite` (festival) ·
`project_pkdplanningsite` (slash-command showcase) · `project_ubiktrainings` (the skill system behind it).

### Tarot
`project_tarotdev` (knowledge DB) · `project_tarotmeditation` (annotator).

### NES / chiptune music
*"the NES music tools", "the chiptune projects", "the REAPER stuff"*
`project_nesmusictools` (cluster) · `project_nsfripper` (root ancestor) ·
`project_fuguejukebox` (Atalanta fugues) · `project_glitchmario` (Mario glitch-art).

### Magic: The Gathering
`project_mtgslider` (theme → slideshow) · `project_alchemyscryfall` · `project_draftacademy` ·
`project_mtgoverlay` (legacy).

### Societas Magica (the scholarly society)
`project_socmagweb` (admin-panel rebuild) · `project_smwebmastersite` (static replica + guide).

### Games — general (roguelike / narrative / learning)
`project_emblemroguelike` · `project_emblemnovel` · `project_glassbeadgame` ·
`project_dungeonarchitect` · `project_alchemyblockinvaders` · `project_magicallatin` ·
`project_digby` · `project_dogsgame` · `project_alchemytetris` (cluster).

### Esoteric platform / feed
*"the podcast aggregator", "the feed", "the showcase"*
`project_esofeed` · `project_esotericbeatnews` · `project_esotericshowcase` ·
see also [[strategy_esoteric_platform]].

### Memory / wiki / tooling
`project_memorypalace` (wiki front-end) · `project_framework` (DH scaffolder) ·
`project_megabase` · `project_socialsdb` · `project_promptarchaeology` (1.45M-prompt
distant reading) · this wiki ([[system]]).

### Mobile apps
`project_audiobookapp` (audiobook player) · `project_oldragdonald` (food-safety field tool).

### Design / style references
`project_shwep` (dark-academic site style kit + `shwep-build` skill).

### Client / commercial (not the DH portfolio)
`project_barton` (Barton Springs Moving).

### Personal e-commerce
`project_bookstore` (Bookstore / SHOPSITE).

## The machine list — `registry.tsv`

Columns: `slug · name · type · status · path · live · tags · desc`. Generated by
`python build_registry.py`, which harvests every `project_*.md` and resolves real
directory paths against the filesystem. **Regenerate it after adding or renaming a
project**, then add the new slug to the relevant theme(s) above (the theme map is
hand-curated — the script does not touch it).
