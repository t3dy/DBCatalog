# Master Concept: Auditing the Writing

**Goal**: Systematically review, flag, and elevate LLM-generated prose across massive DH databases (QueryPat, HermeticDB, Shakespeare) without blowing through context windows, burning API budgets, or losing the human academic voice.

## 1. The Challenge of Massive Databases
Projects like `QueryPat` and `MarxistPortal` contain thousands of entities, timeline events, and essays. Running full-text LLM rewrites on 10,000 JSON entries is neither token-efficient nor epistemologically sound. Mass automation inevitably causes "flattening"—the LLM smooths out contradictions, erases scholarly disputes, and defaults to "vague praise." You need a way to audit the database surgically.

## 2. Pros & Cons of Current Approaches

### Approach A: Automated Batch Overrides (e.g., QueryPat v2.0 pipelines)
* **Pros**: Incredibly fast; scales across 1,100 segments instantly.
* **Cons**: Massive token consumption. Without a human in the loop, the LLM quickly drifts away from your strict templates. It violates *Prompt Archaeology Value #7* (Methodology emerges under pressure) by favoring theoretical, over-engineered automation instead of deep reading.

### Approach B: The "Q-Log" Manual Method (e.g., MTGSLIDER)
* **Pros**: Extremely high quality. Captures verbatim text, explicitly surfaces contradictions, and strictly adheres to the Deckard Boundary.
* **Cons**: Does not scale to thousands of records quickly.

## 3. A Token-Efficient Auditing Strategy
To merge the speed of batch scripts with the rigor of manual Q-Logs, we must build a **Lint-and-Sample Pipeline**:

1. **Deterministic Linting (Zero Tokens)**
   Do not use an LLM to read for structural compliance. Use Python scripts to flag bad writing structurally. A script can easily check if an `interpretive_stance` is under 120 words, or if an essay lacks citation brackets like `(Sutin 1989)`. Flag these rows as `review_status: FAILED_LINT` in SQLite.
2. **Semantic Sampling (Low Tokens)**
   Instead of rewriting the whole database, extract a random sample of 50 profiles currently flagged as `DRAFT`. Pass them to the LLM with the prompt: *"Rate these profiles 1-5 against the rules in `concept_scholarly_writing.md`. Only rewrite the ones that score a 1 or 2."*
3. **The Human Dashboard (The "Reading Environment")**
   Surface the `FAILED_LINT` and `DRAFT` entries in a dedicated local HTML dashboard for manual review. This honors the framework's core design philosophy: it is a "one-click reading environment," not a magical auto-writer.

## 4. How the Wiki Memory System Helps
* **The Global Benchmark**: The auditing script doesn't need to carry a bloated 2,000-word prompt. It simply references the wiki's `concept_scholarly_writing.md` master template as the absolute benchmark for quality.
* **The Critique Ledger**: By maintaining this document, the wiki acts as institutional memory. It remembers *why* we stopped using "Approach A" (Batch Overrides). Future AI agents will no longer suggest expensive, full-database rewrites because the wiki explicitly forbids it.
* **Cross-Project Triage**: The wiki can host a script that routinely reads all 10 SQLite databases in `C:\Dev` and outputs a weekly `vault/audit_report.md` tracking the ratio of `DRAFT` vs `VERIFIED` content across your entire scholarly ecosystem.

## 5. Next Steps
1. Build `scripts/lint_writing.py` in the `DH Framework` to perform the zero-token structural checks.
2. Build an `Audit Report` dashboard into the `DBCatalog` HTML portal so you can see exactly which databases need manual Q-log attention.
