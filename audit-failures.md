---
name: audit-failures
description: Append-only record of failure patterns (what broke, root cause, how the LLM failed, prevention) so future sessions don't repeat them. Seeded from the 2026-06-29 usage report.
type: reference
status: ACTIVE
tags: [audit, failures, learning, meta]
---

# Failure Audit Trail

Append-only. One entry per pattern. Each entry should make a future session faster or
safer. When a fix becomes a standing rule, also encode it in [[environment-health]] or
the verify gate in [[system]].

**Entry shape:** `### [YYYY-MM-DD] Project | Failure type` → What happened · Root cause ·
How the LLM failed · Prevention.

---

### [2026-06-29] (seed) HPMarginalia | Silent edit didn't propagate
- **What:** Scholar/toolbar edits to source data didn't change the live site.
- **Root cause:** `build_site.py` carries a hardcoded list and depends on an unrun fetch step.
- **LLM failure:** Assumed a single-file edit would propagate; claimed done without rebuilding.
- **Prevention:** [[environment-health]] silent-failure row; verify-gate "trace hidden coupling".

### [2026-06-29] (seed) Deploy | Overclaimed completion
- **What:** Reported a deploy/catalog/enrichment batch complete before it was.
- **Root cause:** Success reported against the edit, not against live output.
- **LLM failure:** No live-URL check, no screenshot, no row-count confirmation.
- **Prevention:** Verify-before-done gate in [[system]]; paste evidence, don't assert.

### [2026-06-29] (seed) Discord setup | Destructive script + false reassurance
- **What:** Setup script created duplicate empty channels; LLM reassured that posts weren't lost before confirming.
- **Root cause:** Ran a service-mutating script without a check-in; spoke before verifying.
- **LLM failure:** Premature autonomy on an outward-facing, hard-to-reverse action.
- **Prevention:** Pause and confirm before scripts that mutate external services (Discord/GitHub/Vercel).

### [2026-06-29] (seed) Multiple | "I lack access" when credentials were provided
- **What:** Insisted on missing DB/Supabase access; re-asked for a URL of a site it built.
- **Root cause:** Didn't check existing env/secrets or prior context.
- **LLM failure:** Asked instead of looking.
- **Prevention:** [[environment-health]] credentials-trap row; check `.env*` and project page first.

### [2026-06-29] (seed) Catalog | Built the wrong artifact type
- **What:** Built a concept catalog when a bibliographical/citation tracker was wanted.
- **Root cause:** Deliverable type assumed, not confirmed.
- **LLM failure:** Acted on an under-specified request without a one-line confirmation.
- **Prevention:** Confirm exact artifact type before building when it's ambiguous.
