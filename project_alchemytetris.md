---
name: project_alchemytetris
description: A family of alchemy-themed Tetris / tilting-balance browser games — BALANCETETRIS → TILTRIS → TetrisCodex arcade, plus element-themed AlchemyBalanceTetris.
type: project
status: ACTIVE
tags: [game, tetris, alchemy, balance, vanilla-js, cluster]
---

# Project: Alchemy Tetris (cluster)

**Location** · `C:\Dev\` (4 dirs) — **Type** · browser game family — **Stack** · vanilla HTML/JS canvas (no build) — **Verified** · several deployed to GitHub Pages; not re-run this session

## What it is
One game family exploring alchemy-themed Tetris and tilting-balance puzzles. The alchemy theming is sourced from real scholarship (Valentine's *Twelve Keys*, *Atalanta Fugiens*, Ripley, Paracelsus; a 40-item interaction matrix, zodiac × Tria Prima palette) — not cosmetic.

## Members
| Dir | Role | Status |
|---|---|---|
| `BALANCETETRIS` | Stack tetrominoes on a tilting fulcrum without tipping; alchemy mode layered on | working v1 + ~9 prototypes, deployed |
| `TILTRIS` | Stripped-down tilting-platform Tetris that reliably works; **no alchemy** | stable lean build (~20 KB) |
| `TetrisCodex` | "Alchemical Game Arcade" — ~40 alchemy block games + tarot/Golden Dawn tools + editors (the superset) | large active hub, deployed |
| `AlchemyBalanceTetris` | Element-themed offshoot — alchemical-element blocks, XP/initiation progression | working v1 + GLYPH_DESIGNS doc |

Lineage: `BALANCETETRIS` → `TILTRIS` (stable fork) → `TetrisCodex` (arcade superset, absorbs the others); `AlchemyBalanceTetris` is a parallel element-themed branch.

## Fragile parts
`TetrisCodex` is sprawling (~40 pages, many "planned"); its README names `TILTRIS` as "the version that reliably works", implying the richer balance/alchemy builds are less stable.

## Status & next
Active. Consolidating into `TetrisCodex` as the hub.

## Related
- [[project_alchemyblockinvaders]], [[project_alchemybeatemup]] — sibling alchemy-game experiments
