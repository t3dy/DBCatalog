---
name: project_pkdfestsite
description: Official site for the 4th International Philip K. Dick Festival (Aug 20–23, 2026, Cal State Fullerton).
type: project
status: STABLE
tags: [pkd, event-site, nextjs, vercel]
---

# Project: PKD Fest Site

**Location** · `C:\Dev\pkd-fest-site` — **Type** · Next.js web app (public event site) — **Stack** · Next 16 App Router, React 19, TS 5, Tailwind v4, Vercel — **Verified** · live on Vercel (philipkdickfest.com) per project status doc

## What it is
The official public site for the 4th International Philip K. Dick Festival (Aug 20–23, 2026, Cal State Fullerton); run by Pat Shelton (Sound Legacy) + David Agranoff/PRRIC.

## Architecture
App Router under `src/app/`: route pages (schedule, speakers, publishers, register, contact) plus API handlers (`api/register`, `api/contact`, `api/signup`). Data in `src/data`, helpers in `src/lib`, UI in `src/components`. Entry `src/app/page.tsx`.

## Fragile parts
`.env.local` holds registration/email secrets (see `REGEMAIL.md`); the env-dependent API routes won't run without it. Check that env before assuming missing access (see [[environment-health]] credentials trap).

## Status & next
Built and deployed (`.next/`, `.vercel/`, live domain).

## Related
- [[project_querypat]] — Philip K. Dick scholarship portal (shared author/topic)
- [[project_pkdplanningsite]] — sibling by PKD theme, different purpose
