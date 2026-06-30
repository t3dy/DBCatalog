---
name: project_barton
description: Client/commercial work — a three-part consulting pitch package for Barton Springs Moving, an Austin moving company.
type: project
status: STABLE
tags: [client, commercial, react, vite, moving-company]
---

# Project: Barton Moving (client work)

**Location** · `C:\Dev\` (4 dirs) — **Type** · commercial pitch package — **Stack** · React 19 + Vite + Tailwind (recharts, react-router, lucide) — **Verified** · all four deployed to t3dy GitHub Pages

## What it is
**Client / commercial work** (distinct from the esoteric/DH hobby portfolio): a consulting pitch package for *Barton Springs Moving*, a small Austin moving company. `barton-catalog`'s README frames it as a "Three-Part Pitch Package" naming the sibling repos.

## Members
| Dir | Role | Status |
|---|---|---|
| `moving-company-demo` (BizSolutionsBarton) | Interactive sales-prototype of a moving-ops platform (landing, pricing, dashboards) | built, deployed |
| `barton-catalog` | Solutions catalog + pitch hub (quiz, pitch script, docs) — the index | built, deployed |
| `barton-hiring` | Mover hiring-lifecycle guide; also hosts "Claude Code lessons" + quote wizard | built, deployed, most active (Jun 2026) |
| `BartonMovingFORMfinal` | One-file job-application intake form | built; default Vite README only |

## Fragile parts
None structural. `BartonMovingFORMfinal` ships the stock Vite README (no docs); had a recent CI lockfile fix (npm install vs ci on Node 22).

## Status & next
One coherent engagement, four deployed artifacts.

## Related
- The only commercial cluster in the workspace; unrelated to the DH/esoteric portfolio.
