---
name: project_shwep
description: Dark-academic site style kit — a study/clone of shwep.net packaged as reusable HTML templates and the shwep-build Claude skill.
type: project
status: STABLE
tags: [design, templates, static-site, style-guide, skill]
---

# Project: SHWEP (style kit)

**Location** · `C:\Dev\SHWEP` — **Type** · design-study + template kit — **Stack** · static HTML/CSS + a tiny Node `serve.js`; no build, no DB — **Verified** · templates viewable via `templates/serve.js`

## What it is
A learning project replicating the dark-academic aesthetic of shwep.net (the Secret History of Western Esotericism Podcast) as reusable static templates, packaged as the `/shwep-build` Claude skill. **Not** the real podcast site — a study and style clone.

## Architecture
Doc-driven design study with four pillars: `docs/` (STYLE_GUIDE, SITE_ANALYSIS, EDITORIAL_VOICE), `templates/` (blog-post / episode / episode-listing HTML+CSS, `serve.js` entry), `lessons/` (13 numbered web-dev tutorials), `skills/shwep-build.md` (source for the global skill). The skill is the operational deliverable; templates are exemplars.

## Fragile parts
None observed — no build pipeline, dependencies, or runtime state. Documents WordPress + Memberful + WooCommerce as the *reference* site's stack (not used locally).

## Status & next
Stable reference kit; consumed via the `/shwep-build` skill when building dark-academic scholarly sites.

## Related
- [[strategy_esoteric_platform]] — the esoteric commons these aesthetics serve
- Sibling esoteric/DH sites (Atalanta/Claudiens, EsotericBeatNews)
