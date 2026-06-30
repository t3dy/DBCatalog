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

Last swept: **2026-06-29** (12-agent sweep of recently-modified dirs → 4-agent gap pass for named-active/alchemy-game projects → 3-agent closing pass + 8-dir triage). Every C:\Dev dir has now been triaged at least once.

## Coverage snapshot

- **71 projects** in the registry (`registry.tsv`); ~60 concept/strategy/system pages besides.
- **23 project pages added 2026-06-29** (13 main sweep + 4 gap pass + 6 closing pass) — see `log.md`.
- **0 known real projects un-ingested.** Remaining un-paged dirs are scratch/empty (see Skipped).

## Ingested this sweep (17)

Main sweep (13): [[project_hpin3d]] · [[project_emblemsin3d]] · [[project_fuguejukebox]] ·
[[project_audiobookcleaner]] · [[project_memorypalace]] · [[project_nesmusictools]] ·
[[project_esofeed]] · [[project_pkdfestsite]] · [[project_pkdplanningsite]] ·
[[project_tarotmeditation]] · [[project_barton]] · [[project_bookstore]] ·
[[project_smwebmastersite]]

Gap pass (4): [[project_mtgslider]] · [[project_dogsgame]] · [[project_alchemybeatemup]] ·
[[project_alchemytetris]] (cluster: AlchemyBalanceTetris / BALANCETETRIS / TILTRIS / TetrisCodex)

Closing pass (6): [[project_promptarchaeology]] · [[project_shwep]] · [[project_glitchmario]] ·
[[project_ubiktrainings]] · [[project_oldragdonald]] · [[project_mapresearch]]

## Deliberately skipped (with reason)

| Dir | Reason |
|---|---|
| `ANTIGRAVEMBLEMSIN3D` | Scratch Vite fork of EMBLEMSIN3D; noted inside [[project_emblemsin3d]] |
| `antigravbeadgame` | Unversioned copy trailing [[project_glassbeadgame]]; no distinct identity |
| `NESARPEGDESIGNS` | Empty stub; noted in [[project_nesmusictools]] |
| `membership-site-guide` | Stock `create-next-app` + tutorial shell; revisit if content fills in |
| `CDevTarotMeditation` | Does not exist on disk |
| `AlchemyProtos` | Dormant archive of 8 standalone HTML alchemy-mechanic prototypes; one line under the alchemy-games cluster, not a full page |
| `mtg-research` | Scratch — a single un-frozen `PARKING_LOT.md` brainstorm; revisit when scope freezes |
| `VCG_DOCS` | Meeting notes / concept dumps for [[project_vibecoding]] (Vibe Coding Garage) — fold into that page, not its own |
| `CDevsm-webmaster-site` | **Empty dir** — likely a stray duplicate of [[project_smwebmastersite]] / [[project_socmagweb]]; flagged for deletion |
| `game`, `games`, `roguelike`, `portal`, `output`, `5174`, `GPTmarch172026`, `GPTREAPERPRODUCTS_chunks` | Scratch / build-output / experiment dirs |

## Not yet ingested (next sweep queue)

Empty — every C:\Dev directory has been triaged. New projects get added here as they appear;
re-run the sweep below periodically.

## How to run a coverage sweep

1. `Get-ChildItem C:\Dev -Directory | Sort LastWriteTime -Desc` → find recently-touched dirs.
2. Diff against `index.md` project list + this page's three lists.
3. Fan out one survey agent per new dir/cluster (return the [[style]] template fields + a
   real-or-scratch verdict). Don't dump file contents back.
4. Write lean pages for the real ones; move the rest into Skipped or Not-Yet-Ingested here.
5. Update `index.md`, append to `log.md`, and re-date the "Last swept" line above.
