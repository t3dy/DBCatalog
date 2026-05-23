# Project: AlchemyTimelineMap

**Location**: `C:\Dev\AlchemyTimelineMap`
**Type**: Procedural Engine (Interactive Visualization)

## Overview
An interactive chronological visualization mapping 2,500 years of alchemical history — from Hellenistic proto-chemistry and Zosimos of Panopolis through the Islamic golden-age transmission (Jabir ibn Hayyan, al-Razi) into European Renaissance practice and the eventual dissolution into modern chemistry. Designed as a navigational companion layer cross-referenced with HermeticDB and RenMagDB.

## Core Content
- **Timeline Events**: 300+ dated milestones covering key texts, figures, experimental discoveries, and regional transmission arcs.
- **Figure Nodes**: 80 alchemists with brief biographical sketches, primary texts, and lineage connections.
- **Transmission Arcs**: Visual lineage mapping showing how specific doctrines and laboratory techniques migrated across Arabic, Latin, Byzantine, and vernacular traditions.
- **Era Zones**: Five discrete periods — Antiquity, Islamic Golden Age, Medieval Latin, Renaissance, Early Modern — each with distinct color coding and navigational filter.

## Architecture
- **Stack**: D3.js force-directed timeline SVG, SQLite backend, Python ingestion pipeline.
- **Data Model**: `events` table with `figure_id`, `era`, `tradition`, `geo_origin`, `text_refs` linking to HermeticDB and RenMagDB entity IDs.
- **Frontend**: Interactive SVG canvas; click-through to linked entity profiles in companion portals.

## System Invariants
- **Cross-Reference Integrity**: All `figure_id` and `text_ref` values must resolve to valid entities in `HermeticDB` or `RenMagDB` — no orphaned links.
- **Date Discipline**: Uncertain dates stored as range fields (`date_min`, `date_max`) rather than false-precision point values.

## Related Entities & Concepts
- [[Alchemy]]
- [[Hermeticism]]
- [[Zosimos of Panopolis]]
- [[Jabir ibn Hayyan]]
- [[Paracelsus]]
- [[HermeticDB]]
- [[RenMagDB]]
- [[AtalantaClaudiens]]
