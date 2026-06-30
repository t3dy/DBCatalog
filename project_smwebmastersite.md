---
name: project_smwebmastersite
description: Webmaster field guide plus a full static replica of the Societas Magica society website.
type: project
status: STABLE
tags: [societas-magica, static-site, society, webmaster]
---

# Project: SM Webmaster Site

**Location** · `C:\Dev\sm-webmaster-site` — **Type** · static site + webmaster guide — **Stack** · plain HTML/CSS/JS, wired for Outseta/Stripe/Formspree/PayPal — **Verified** · deployed to GitHub Pages (14-page replica, active commits)

## What it is
A webmaster field guide plus a content-complete static replica of the Societas Magica website (societasmagica.org) — the academic society for history-of-magic scholars (founded 1994).

## Architecture
14-page static HTML replica, no framework, wired (not necessarily live) for Outseta membership / Stripe / Formspree / PayPal. Doubles as a how-to guide for maintaining the society site.

## Fragile parts
None observed. Payment/membership integrations are wired but depend on external service config.

## Status & next
Deployed replica; reference implementation for society web maintenance.

## Related
- [[project_socmagweb]] — the Next.js + Postgres admin-panel rebuild for the same society (Societas Magica)
- [[strategy_esoteric_platform]] — Society layer of the commons
