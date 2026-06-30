---
title: Esoteric Beat News
type: project
description: A dependency-free static site that aggregates the complete back catalogues of ~30 esoteric-studies podcasts/YouTube channels (~3,000 episodes) into one card feed, auto-sorting every episode into thematic topic tabs from a committed JSON catalog — no database, no framework, no API keys.
tags: [project, static-site, aggregator, esoteric-studies, python, yt-dlp, github-pages, json-catalog]
updated: 2026-06-27
---

# Esoteric Beat News

A **dark-academic static-site news aggregator** for Western-esotericism media. It scrapes the *complete* upload histories of a few dozen scholarly esoteric podcasts and YouTube channels, snapshots them into a committed JSON catalog, and renders them as scrollable **cards** that link back out to each creator — "Latest Emanations" (the marquee chronological feed), per-podcast/scholar landing pages, **20 auto-sorted topic tabs**, and Esoterica's 28 curated playlists. Live at **https://t3dy.github.io/EsotericBeatNews/**, GitHub repo `github.com/t3dy/EsotericBeatNews`, maintained by Ted Hand (`ted.hand@gmail.com`).

It lives in **two sibling directories that are clones of the same GitHub repo**: `C:\Dev\ESOFEED\` is the **earlier iteration** (its git tip ends 2026-06-13 at the Adam McLean import; its README documents only ~8 topics and ~23-25 sources) and `C:\Dev\EsotericBeatNews\` is the **current canonical clone** that continues past it (Robert Fludd / David Litwa / Dylan Burns sources, an "esotericists" toolbar, source pruning; 33 sources, 19 topics). Both `git remote`s point to the same `t3dy/EsotericBeatNews` origin. `EsotericBeatNews/CLAUDE.md` makes the verdict explicit: *"Not NSFRIPPER / ESOFEED. Any doc that references those paths is stale."* Treat **ESOFEED as a stale duplicate**; EsotericBeatNews is authoritative.

## What it is
A fan-made discovery index — it stores only titles, links, thumbnails, durations, and summaries pulled from public feeds, rehosting nothing and linking every card back to the creator. The surfaces:
- **Latest Emanations** — paginated chronological feed of *every* episode from every source (cards).
- **Featured Podcasts** toolbar — a tab/landing page per show.
- **Topics** toolbar — ~20 curated cross-channel currents (Neoplatonism, Grimoires, Kabbalah, Renaissance/Ancient/Medieval Magic, Agrippa, Ficino, Alchemy, Hermeticism, Occultism, Witchcraft, Gnosticism, Demonology, Astrology, …), each populated automatically at build time.
- **Featured Scholars** / **Esotericists** toolbars — per-figure pages (Hutton, Yates, Forshaw, Newman, Principe, Dzwiza; Robert Fludd as a pinned esotericist).
- **Curated Playlists** — a section per Esoterica thematic playlist (28).
- Client-side full-text **search** (`site/data.json`) and **browse-by-date**.

## Architecture / Data pipeline
A deliberately minimal **two-stage** pipeline, framework-free, Python-stdlib render:

```
sources.json ──> fetch_catalog.py ──> data/catalog.json ──> build.py ──> site/
  (config)        (network, LOCAL)       (committed JSON)     (offline, CI)   (deployed)
```

1. **`fetch_catalog.py`** (network-bound, uses `yt-dlp` + `urllib`; run **locally only** because YouTube blocks CI/datacenter IPs). Reads `sources.json`, pulls every episode per source, writes `data/catalog.json`. Per-source caches land in `data/raw/` (gitignored). Each source declares a `kind` controlling the fetch: `podcast`/`podcast_rss` (RSS/Atom, e.g. SHWEP), `youtube` (full channel uploads via `UC…` id), `youtube_channel_filtered` (only titles matching `filter_title[]`, for mixed channels), `youtube_playlist`, `youtube_videos` (explicit id list for one-offs), and `composite` (merges channel + SoundCloud, de-duping the same episode across platforms). `fetch_playlists: true` also pulls a channel's playlists; `house: true` flags Ted's own shows. YouTube and SoundCloud are both scraped via `yt-dlp` (no API key).
2. **`build.py`** (~45 KB, offline, stdlib only; runs in CI). Reads `catalog.json` + `sources.json` + `tags.json`, **auto-tags** each episode into topics, emits static HTML, and cache-busts CSS by content hash.
3. **CI** — `.github/workflows/rebuild.yml` runs `build.py` on every push to `main` and deploys `site/` (gitignored; never committed) to GitHub Pages.

**The "database" for annotating video links is a JSON catalog, not SQL.** There is **no `.db`/`.sqlite`/schema/SQL file anywhere in either directory** — confirmed by search. The committed `data/catalog.json` is the authoritative episode store (items carry `source`, `title`, `url`, `video_id`, `published_iso`, `summary`, `thumb`, `duration`). "Annotation" today means **automated topic-sorting plus manual overrides**: `auto_tag()` in `build.py` assigns topics from three layers — (1) keyword match on title+summary against each topic's `keywords`, (2) Esoterica playlist membership, (3) per-URL `add`/`remove` overrides in `tags.json` (overrides win). `data/catalog.json` is regenerated and must never be hand-edited; all human annotation flows through `sources.json` keywords or `tags.json`. STRATEGY.md states the design goal plainly: *"No custom database or secrets in code."*

## Status (2026-06-27) — honest
Built and **live**; a working, deployed aggregator, not a prototype. Catalog numbers from the canonical `EsotericBeatNews/data/catalog.json` (generated 2026-06-14):
- **2,983 episodes counted / 3,004 catalog items, 28 playlists.** (ESOFEED's older catalog: 3,014 items, generated 2026-06-13 — a near-equal sibling snapshot, not "more.")
- **33 distinct sources** present in the catalog items; `sources.json` defines **33 sources, 19 topics, 12 scholars**. Largest sources: Esoterica (373), Religion for Breakfast (324), Angela's Symposium (305), Modern Hermeticist (249), Seekers of Unity (225), SHWEP (218), Glitch Bottle (202), Adam McLean (200), Arcanvm (150), Rejected Religion (146), Spiritus Mundi/Newman (131). A long tail of sources have 1-10 episodes (Hermitix, SHAC, SAS lectures, Kaz Rowe each = 1).
- **Built**: the full card site — Latest Emanations feed, Featured Podcasts/Scholars/Esotericists toolbars, ~20 auto-sorted topic tabs, 28 playlist pages, client-side search, browse-by-date, mobile breakpoints (375/820/1280px), content-hash CSS cache-busting, and **Tier-1 monetization** (Patreon + PayPal donate buttons — `patreon.com/esotericbeatnews`, `paypal.me/tedhand`).
- **Planned only (NOT built)**: transcript search (yt-dlp `.vtt` ingestion), email newsletter, per-episode landing pages with og: tags, per-topic RSS feeds, "Suggest a Source" form, analytics, and Patreon Tier-2/3 (patron-list sync, gated content). The PATREON.md/HANDOVER.md sync scripts (`scripts/sync_patrons.py`) are illustrative sketches, not shipped. **Do not read the roadmap revenue figures or the Tier-3 "database of patrons" as existing features.**
- **Caveat on doc figures**: HANDOVER.md (2,813 eps / 23 sources / 47 pages), SESSION_SUMMARY.md (3,014 / 25 / 51), and STRATEGY.md (3,070 / 25 / 52) each quote *different* counts from different sessions; CLAUDE.md flags them as direction, not current state. The catalog file itself is the ground truth quoted above.

## Tech
Python 3.9+ **standard-library-only render** (no Jinja, no JS runtime, no API keys) · `yt-dlp` + `urllib` for fetch (local) · `data/catalog.json` committed JSON snapshot as the data store · hand-written CSS with custom properties (the dark-academic ["SHWEP" design system](https://shwep.net) — Georgia headings, `#1a1a1a` palette, no web fonts/framework) · GitHub Pages hosting · GitHub Actions CI/CD (build + deploy on push).

## Relation to the ecosystem
Esoteric Beat News is the **discovery-feed layer** of Ted's would-be esoteric-studies platform: [[strategy_esoteric_platform]] already inventories it by name as "a discovery feed — *EsotericBeatNews*: ~3,000 episodes from 25 podcasts/channels," the asset to be given "one front door" alongside a community ([[strategy_esoteric_discord]]) and the SocMag institutional anchor. Within the workspace's [[concept_database_theories]] taxonomy it sits at the **opposite pole from [[project_socmagweb]]**: SocMagWeb is a transactional Postgres admin system, whereas EBN is the *minimal* quadrant — a read-only static index whose "database" is a committed JSON file and whose write path is a `git push`. It is a sibling, content-domain-wise, to the DH knowledge portals ([[project_claudiens]], the *Atalanta Fugiens* work) but architecturally far lighter, sharing only the dark-academic SHWEP aesthetic catalogued in [[architecture_frontend_patterns]]. The ~3,000-episode catalog is also a natural feedstock for the planned **Memory Palace** (see [[project_glassbeadgame]]): an interlinked spatial index of Ted's esoteric corpus would draw on exactly this kind of curated, topic-tagged media list.

## Pointers
- Canonical clone: `C:\Dev\EsotericBeatNews\` — entry `EsotericBeatNews\CLAUDE.md` (pipeline + source-kind reference, declares ESOFEED stale).
- Stale duplicate: `C:\Dev\ESOFEED\` — earlier iteration, same GitHub origin; do not edit.
- Config: `EsotericBeatNews\sources.json` (sources, topics, scholars, branding) · `tags.json` (per-URL overrides).
- Pipeline: `fetch_catalog.py` (network, local) · `build.py` (offline, CI) · data store `data\catalog.json`.
- Docs: `README.md` (overview + quickstart) · `HANDOVER.md` + `STRATEGY.md` (roadmap/monetization — figures predate current catalog) · `PATREON.md` · `SESSION_SUMMARY.md` · `DISCOVERING_ADAM_MCLEAN.md`.
- CI/deploy: `.github/workflows/rebuild.yml` → GitHub Pages → https://t3dy.github.io/EsotericBeatNews/.
