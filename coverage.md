---
name: coverage
description: Living audit of wiki coverage across C:\Dev — what's ingested, what's deliberately skipped, and what still needs a sweep. The wiki's self-check.
type: reference
status: ACTIVE
tags: [coverage, audit, lint, meta]
---

# Wiki Coverage Audit

Honest accounting of how much of `C:\Dev` the wiki actually documents. Update the three
lists when you ingest, skip, or discover a project. This is the wiki checking its own work —
**it should never read as "100% done" unless the Not-Yet-Ingested list is genuinely empty.**

Last swept: **2026-06-29** (12-agent sweep of recently-modified dirs, then a 4-agent gap pass for the named-active and alchemy-game projects).

## Coverage snapshot

- **65 projects** in the registry (`registry.tsv`); ~60 concept/strategy/system pages besides.
- **17 project pages added 2026-06-29** (13 in the main sweep + 4 in the gap pass) — see `log.md`.
- **~10 dirs still un-ingested** (list below) — coverage is partial by design, not complete.

## Ingested this sweep (17)

Main sweep (13): [[project_hpin3d]] · [[project_emblemsin3d]] · [[project_fuguejukebox]] ·
[[project_audiobookcleaner]] · [[project_memorypalace]] · [[project_nesmusictools]] ·
[[project_esofeed]] · [[project_pkdfestsite]] · [[project_pkdplanningsite]] ·
[[project_tarotmeditation]] · [[project_barton]] · [[project_bookstore]] ·
[[project_smwebmastersite]]

Gap pass (4): [[project_mtgslider]] · [[project_dogsgame]] · [[project_alchemybeatemup]] ·
[[project_alchemytetris]] (cluster: AlchemyBalanceTetris / BALANCETETRIS / TILTRIS / TetrisCodex)

## Deliberately skipped (with reason)

| Dir | Reason |
|---|---|
| `ANTIGRAVEMBLEMSIN3D` | Scratch Vite fork of EMBLEMSIN3D; noted inside [[project_emblemsin3d]] |
| `antigravbeadgame` | Unversioned copy trailing [[project_glassbeadgame]]; no distinct identity |
| `NESARPEGDESIGNS` | Empty stub; noted in [[project_nesmusictools]] |
| `membership-site-guide` | Stock `create-next-app` + tutorial shell; revisit if content fills in |
| `CDevTarotMeditation` | Does not exist on disk |
| `game`, `games`, `roguelike`, `portal`, `output`, `5174`, `GPTmarch172026`, `GPTREAPERPRODUCTS_chunks` | Scratch / build-output / experiment dirs |

## Not yet ingested (next sweep queue)

These are real-looking projects the sweep did **not** cover. Coverage is incomplete here.

- **promptarchaeology** — the megabase prompt-archaeology tool (has a Claude skill; real).
- **SHWEP** — dark-academic site design reference (has a `shwep-build` skill).
- **AlchemyProtos** — prototype collection (triage for real vs. scratch).
- **mtg-research**, **GlitchMario**, **OldRAGDonald**, **UbikTrainings**, **MAPRESEARCH**, **VCG_DOCS**, **CDevsm-webmaster-site** — unsurveyed; status unknown.

## How to run a coverage sweep

1. `Get-ChildItem C:\Dev -Directory | Sort LastWriteTime -Desc` → find recently-touched dirs.
2. Diff against `index.md` project list + this page's three lists.
3. Fan out one survey agent per new dir/cluster (return the [[style]] template fields + a
   real-or-scratch verdict). Don't dump file contents back.
4. Write lean pages for the real ones; move the rest into Skipped or Not-Yet-Ingested here.
5. Update `index.md`, append to `log.md`, and re-date the "Last swept" line above.
