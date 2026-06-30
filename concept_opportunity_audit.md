---
name: concept_opportunity_audit
description: Reusable method for auditing a *shipped* project to find improvements — latent display bugs, unsurfaced data, missing/relocatable assets, dead-end interactions. The "what to build next" counterpart to audit-failures.
type: concept
status: ACTIVE
tags: [audit, method, improvement, frontend, data, meta]
---

# The Opportunity Audit

A method for pointing at a project that already *runs* and finding what to improve.
Distinct from [[audit-failures]] (what broke) and [[concept_auditing_writing]] (auditing
prose): this hunts **latent value** — things already present in the code or data that
the user can't yet see or reach.

Run it when a project is "shipped" but underwhelming, between phases, or when the user
says *audit it / find improvements / why can't I see X / make sure it displays properly*.

## The four probes

Run all four; they catch different misses. Order matters — probe 1 first, it finds the
invisible.

1. **Render-and-look.** Actually start the app and **screenshot every view**, at real
   viewport size. The highest-impact bugs are invisible to a clean console, an
   accessibility snapshot, or `eval` of DOM state — only pixels reveal them. (Canonical
   case: a WebGL `<canvas>` silently rendering the *entire app* into a 300×150 box; see
   [[environment-health]]. Also over-aggressive shader/bloom passes blacking out a frame.)
   If you only verify by reading state, you will ship the invisible bug.

2. **Unsurfaced data.** Grep the data/DB for rich fields the UI never shows. Compute
   *coverage*: fields present vs. fields actually rendered. Rich text sitting in the data
   and shown nowhere is the single best source of new features. (Case: 51 emblems each
   carried a ~700-char `discourse_summary` of real scholarship surfaced on no screen —
   it became three guided tours.)

3. **Asset reality.** Do the assets the code references actually exist in-repo? Are
   cleaner/web-optimized versions sitting in a sibling project? Missing assets fail
   silently under a canvas or as broken `<img>`. Self-host them and use **relative**
   paths (GitHub Pages project URLs break on a leading `/`).

4. **Dead-end interactions.** Can the user actually explore and complete the loop? Look
   for static cameras with no controls, models you can't rotate, content with no entry
   point, games with no win/again state. Every primary object should be reachable and
   manipulable.

## Output

A short **prioritized** list, invisible-first: (1) display bugs that hide everything,
(2) unsurfaced data → new surfaces, (3) missing assets, (4) dead ends. Prefer
**outward not deeper** — connect what already exists (data, research, sibling assets)
before specifying anything new. Then build the top item and re-run probe 1 to confirm.

## Worked example

HPin3D / [[project_hpin3d]], 2026-06: probe 1 found the 300×150 canvas (whole app tiny);
probe 2 found the hidden `discourse_summary` + a 10-symbol table → the **Tours** feature
connecting models to scholarship; probe 3 found `emblems.json` referencing absent images
that existed in AlchemyBeatEmUp → self-hosted; probe 4 found the gallery unlit and the HP
fountain non-orbitable → textured plates + OrbitControls. One audit, a session of work.
