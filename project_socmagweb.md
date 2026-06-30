---
title: Societas Magica Webmaster (SocMagWeb)
type: project
description: Modernization of the 14-year-old societasmagica.org admin platform — Next.js + Postgres, built test-first under an in-repo agile+wiki orchestrator.
tags: [project, nextjs, postgres, drizzle, tdd, orchestrator, admin-panel, scholarly-society]
updated: 2026-06-27
---

# Societas Magica Webmaster (SocMagWeb)

Modernization of **societasmagica.org**, the site of an international scholarly society (~494 members studying the history of magic, esotericism, and the occult). The legacy stack is a custom **PHP/Bonfire + MySQL** app on shared hosting whose admin control panel is glitchy and times out (Members/Accounts/Pages/Newsletters tabs 500 or hang). The user inherited the webmaster role and is rebuilding the site in **Next.js 16 + Postgres** — initially scoped to the **admin control panel** (so the treasurer Claire Fanger gets her familiar functions back without lag), since broadened into a **full-functionality mirror** of the whole public + member-facing site, deployed live to Vercel. The original PHP site stays live and authoritative until the board signs off on cutover.

Located at `C:\Dev\SocMagWeb` (docs + orchestrator) and `C:\Dev\SocMagWeb\socmagweb-app` (the Next.js app).

## What it is
A faithful, modern reimplementation of a 10-tab admin panel (Dashboard, Invoices, Members, Export, Pages, Newsletters, Contacts, Dues, Stats, Emails, Accounts), preserving **all** legacy data (494 members, 485 invoices, 44 newsletters) and the **Bonfire `sha1(salt+password)` login** so members log in day one. Design choices for every tab are captured in `ADMIN_*.md` design docs (each feature has 3–5 evaluated options + an interactive HTML mockup playground).

## Architecture (ports & adapters)
Domain-first hexagonal layering so business rules are pure and testable without a DB:
- `lib/domain/*` — **pure** rules: `pagination`, `validation`, `password` (timing-safe, fail-closed), `permissions` (data-driven RBAC), `invoices` (defaults/status/draft), `renewal` (per-type academic-calendar dues), `export` (RFC-4180 + CSV-injection defense), `staleness` (6mo/12mo content rot).
- `lib/ports/*` — interfaces: `Clock, InvoiceRepo, Mailer, AuditLog`.
- `lib/services/*` — use-cases orchestrating domain over ports (exemplar: `createInvoice`, with authz→validate→persist→conditional-email→audit and mailer-failure resilience).
- `app/**` — Next.js App Router adapter (routes + admin UI).

## Process innovation: the in-repo orchestrator (Karpathy-wiki × agile)
`C:\Dev\SocMagWeb\orchestrator/` fuses the **LLM-Wiki pattern** with **agile TDD**: `ORCHESTRATOR.md` (schema/control), `backlog.md` (epics→stories), `sprints/`, `tickets/SM-NNN.md` (Given/When/Then AC + test plans), `architecture/` (ADRs + reviews), `index.md`, append-only `log.md`, `[[wikilinks]]`. The agent works in three hats (Orchestrator/Builder/Reviewer), every ticket built red→green→refactor. This is a concrete instance of the workspace [[architecture_prompt_archaeology_machines]] / [[concept_vibecoding]] ethos applied to a production rebuild.

## Status (2026-06-27)
The project crossed from "tested domain core + mockup" to a **live, data-backed deployment** between 2026-06-18 and 2026-06-27.
- **Live**: deployed to Vercel at **https://societas-magica-webmaster.vercel.app** (manual CLI deploy; no GitHub auto-deploy). Private GitHub repo `tedhand-2181s-projects/societas-magica-webmaster`.
- **Testing**: Vitest; **153 tests green across 20 test files** (up from 70); `npm run lint`, `tsc --noEmit`, and `npm run build` all clean (~32 routes). Domain layer grew from 8 to ~17 modules (added `session`, `passwordHash`, `passwordReset`, `privacy`, `registration`, `membership`, `dues`, `sanitize-html`, `legacyText`, `files`) plus the `accounts` service, `memberRepo`/`mailer`/`paypal` adapters, and a `schema.parity.test.ts` static guard.
- **🔴 SM-024 launch blocker RESOLVED (signed sessions)**: `lib/domain/session.ts` now issues HMAC-SHA256 signed, expiring tokens (timing-safe verify, fail-closed); `lib/session-cookie.ts` resolves the secret fail-fast in prod; the login route sets the signed cookie and `roleId` is authoritative only after `verifySession`. Tamper / wrong-secret / expiry / malformed all rejected. Modern hash is **scrypt** (Node built-in), not argon2id — chosen against [[adr-003-auth-compat]], scheme inferred from the hash prefix so no schema column is needed; legacy SHA-1 transparently upgrades on login. **Live successful-login round trip verified 2026-06-27** (`scripts/e2e-auth-test.ts`, 15 checks green against prod, throwaway account auto-deleted).
- **Full data import (not just users)**: the entire `socmag.sql` MySQL dump (24 tables) was reconciled and imported to Supabase Postgres — **494 members, 2,486 dues invoices, 233 ledger entries, 25 year-end balances, 44 newsletters, 8 officers, 15 contacts**, dues pricing. Blog (19 posts / 11 categories / 14 comments) and `bf_users_year_end` cutoff dates loaded 2026-06-27 via the session pooler. "Current member" (≈92) is redefined as *having a paid dues invoice for the current year* (`lib/domain/membership.ts`), not the legacy `active` flag (≈483). SM-030 reconciled three latent schema↔migration drift defects (boolean→smallint columns, `GENERATED BY DEFAULT AS IDENTITY`, unique `user_id` index) caught by the parity guard.
- **Parity build-out**: public site (home/membership/publications/newsletters/conferences/manuscripts/syllabus/contact/privacy), member account + profile edit + consent-honoring directory, full `/admin/*` control panel on real data, and a `/register` email-list/membership form. A **fabricated-roster data shroud** (`lib/data/fabricated.ts`, ~40 historical-magic figures in tradition "packs") de-identifies all demo/public surfaces; real PII lives only in Supabase. Secrets envelope (`_SECRETS/`, `_legacy_site/`, the dump) sits outside the git repo, gitignored, enforced by a PreToolUse hook.
- **Pending / blocked on external input**: PayPal activation (modern Orders-v2 integration built & tested but needs REST keys + sandbox test — *not* a port of Paul Coyne's live fix), an email provider (Resend/Postmark) to unblock contact-form send + dues receipts, fleshing out `/membership` + `/travel-bursary` content, and the eventual domain cutover (the original PHP/MySQL site stays live and authoritative until then). Still-open security follow-ups: login lockout ([[SM-026]]).

## Tech
Next.js 16 (App Router, React 19) · TypeScript · Drizzle ORM · Postgres (`pg`) · Vitest + Testing Library · CSS-variable theming (classic navy/gold + modern skins).

## Relation to the ecosystem
Unlike the DH **Knowledge Portals** in this wiki (read-mostly scholarship), SocMagWeb is a **transactional admin system** (auth, dues, email) for a scholarly society — a different quadrant of [[concept_database_theories]]. It shares the workspace's TDD/provenance discipline and the [[architecture_deckard_boundary]] instinct (here: pure domain vs. I/O adapters).

## Pointers
- Current state / parity scorecard: `C:\Dev\SocMagWeb\socmagweb-app\HANDOVER_CURRENT.md`
- Orchestrator control doc + log: `C:\Dev\SocMagWeb\orchestrator\ORCHESTRATOR.md`, `orchestrator\log.md`
- Architecture: `orchestrator/architecture/architecture-overview.md` (+ `socmagweb-app/ARCHITECTURE.md`)
- Code review: `orchestrator/architecture/code-review-2026-06-18.md`
- Data map: `C:\Dev\SocMagWeb\socmagweb-app\DATA_ACCOUNTING.md`
- Design package: `C:\Dev\SocMagWeb\ADMIN_PANEL_README.md`
- Live mirror: https://societas-magica-webmaster.vercel.app
