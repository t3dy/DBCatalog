---
name: project_esofeed
description: Active expansion fork of EsotericBeatNews — a dark-academic static aggregator of esoteric-studies podcasts/YouTube into one feed.
type: project
status: ACTIVE
tags: [aggregator, static-site, esoteric, python, dh]
---

# Project: ESOFEED

**Location** · `C:\Dev\ESOFEED` — **Type** · static-site content aggregator — **Stack** · Python 3 stdlib + yt-dlp fetcher, hand-written "SHWEP" CSS, GitHub Pages + Actions — **Verified** · committed `catalog.json` + built `site/` present (CI deploys; not re-run this session)

## What it is
The active, more-advanced working copy of [[project_esotericbeatnews]]: collects full back-catalogues of esoteric-studies podcasts/YouTube channels (25 sources, 20 topics, Featured Scholars) into one auto-tagged card feed. No framework, no API keys.

## Architecture
Two-stage split — the exact "fetch separate from build" pattern that prevents silent staleness: `fetch_catalog.py` (network, yt-dlp/RSS → `data/catalog.json`, run **locally**) and `build.py` (offline stdlib render → `site/`, runs in **CI**). `sources.json` declares sources/topics/scholars/branding; `tags.json` holds manual tag overrides. Auto-tagging by title/summary keyword + playlist membership at build time.

## Fragile parts
`yt-dlp` scraping breaks on YouTube changes/IP blocks — precisely why fetch is kept out of CI (run locally, commit the catalog). SoundCloud needs `curl_cffi`. **Editing `sources.json` alone won't change the feed until `fetch_catalog.py` then `build.py` run** — the canonical two-stage trap (see [[environment-health]]).

## Status & next
Active; deploys to the EsotericBeatNews Pages URL (its `sources.json` still targets it). Consider consolidating naming with EsotericBeatNews.

## Related
- [[project_esotericbeatnews]] — same codebase, earlier copy
- [[strategy_esoteric_platform]] — the Feed layer of the commons
