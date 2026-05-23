# Wiki Field Guide: Getting the Most From Your Memory System

*A practical handbook of techniques for using the wiki as an active tool for building and querying databases — not just documentation, but a system you drive.*

---

## Part 1: The Session Startup Ritual

The biggest waste of a wiki is opening a session and asking the LLM a question before it has read anything. A blank-slate LLM that happens to have access to your files is not the same as an LLM that has been primed with your constraints. The session startup ritual fixes this.

**The minimum viable context load — do this every session:**
1. Feed `index.md` — so the LLM knows the full map of what exists
2. Feed `log.md` — so the LLM knows what was last done and can avoid repeating it
3. Feed the one or two project files most relevant to today's work
4. Feed `architecture_deckard_boundary.md` if you are about to write any code

That is it. Do not dump the entire wiki into context on every session. More is not better — diluted context produces diluted work.

**The opening prompt matters more than you think.** Compare these two:

*Weak*: "Help me work on HermeticDB."

*Strong*: "You have read index.md, log.md, and project_emeraldtablet.md. The last session added 200 new claims to the provenance pipeline. Today I want to build the recursive join that maps how a specific mistranslation lineage spawned a new esoteric tradition. The Deckard Boundary applies: Python handles the JOIN logic, you handle the scholarly framing of what to display. Start by reviewing the current schema and telling me what the JOIN structure should look like."

The strong prompt hands over the constraints, the history, the specific task, and the boundary — before any code is written. The LLM cannot drift if you have already drawn the fence.

**The handover pattern.** At the END of every productive session, ask the LLM to write a brief handover note: what was done, what was decided, what the next concrete step is. Store it in `log.md`. Future you (and future LLMs) will thank you. The existing `handover_session_end.md` is a template for this.

---

## Part 2: Write the Profile Before You Build

Every project profile in this catalog was written *after* the project already existed. That is useful for documentation, but it misses the most powerful use of the wiki: as a **design tool**.

Writing the profile before you write a single line of code forces you to answer the hardest questions up front:
- What are the System Invariants? (If you cannot write them, the architecture is not clear enough to build.)
- What is the exact data model? (If you cannot describe the tables and their relationships in plain English, you do not know what you are building yet.)
- What is the Deckard Boundary for this specific project? (Write it out before you discover it by accident.)
- What is the one concrete Next Step? (If there are five, you do not have a clear goal.)

**The pre-mortem profile technique.** Before starting WitcherFolkloreDB, write the profile as if the project already exists and you are explaining it to a colleague. The act of writing "Every mapping requires three fields: `witcher_text_ref`, `folklore_source_ref`, `scholarly_authority`" reveals a constraint you might not have thought of during actual coding — and finding it in a Markdown file costs nothing, while finding it in production costs a refactor.

**The System Invariants section is the most important section on any page.** If you cannot write at least two genuine invariants for a project, you do not know the project well enough to build it. Invariants are not aspirations ("we hope to maintain provenance") — they are hard rules that, if violated, mean the project is broken ("data flows ONE direction; the HTML is never edited directly").

---

## Part 3: Querying the Wiki Itself

The wiki is a corpus of text files. It is queryable — not through SQL, but through the same grep and text search tools you use everywhere else. Most people never think to search their own wiki, but it is one of the highest-value operations you can do.

**Find every page that mentions a concept:**
```bash
grep -rl "Deckard Boundary" /path/to/wiki/
grep -rl "Jabir ibn Hayyan" /path/to/wiki/
grep -rl "DRAFT" /path/to/wiki/ | wc -l   # how many pages have unverified content?
```

**Find concepts that are mentioned but do not have their own page** (orphaned Related Entities):
```bash
# Extract all [[WikiLinks]] from all files
grep -roh '\[\[[^\]]*\]\]' /path/to/wiki/ | sort | uniq -c | sort -rn
# Then check which ones have no corresponding file
```
Any concept that appears in five or more Related Entities sections and has no dedicated page is a wiki gap — a concept important enough to have its own treatment.

**The log.md as a decision audit.** The log is append-only, which means it is a chronological record of every decision. When you cannot remember why you structured something a certain way, read the log entry for that session. It will tell you what was attempted, what failed, and what was decided. This is worth far more than code comments.

**Track which projects have not been touched recently:**
```bash
grep "^\#\# \[" log.md | tail -20
```
Any project that does not appear in the last ten log entries has likely drifted — the profile may no longer match the code.

---

## Part 4: Cross-Pollination Sessions

The wiki describes cross-pollination as a benefit, but it does not describe how to actually do it. Here is the workflow.

**Step 1: Find collision candidates.** Two projects should be deliberately collided if their Related Entities sections share two or more entries. CrowleyDB and HermeticDB both link to `[[Kabbalah]]`, `[[Hermeticism]]`, and `[[Alchemy]]` — they are collision candidates. WitcherFolkloreDB and WitchcraftStudiesDB both link to `[[Folk Magic]]` and `[[RenMagDB]]` — collision candidates.

**Step 2: Run a dedicated bridge session.** Load BOTH project profiles into context alongside `index.md`. Ask the LLM one specific question: *"What does project A know that project B is missing, and what connection between them would most improve both?"* Do not ask for a full synthesis — ask for a single concrete bridge.

For example, loading CrowleyDB and HermeticDB together should produce: "CrowleyDB's 777 correspondence tables reference Kabbalistic Sephiroth that are already defined as entities in HermeticDB. A `sephiroth_id` foreign key in CrowleyDB's correspondence table would enable a single query to pull the full historical Kabbalistic lineage of any Thelemic attribution — something neither database can do alone."

**Step 3: Write the bridge as a System Invariant.** Do not just note the connection in a conversation — add it as a cross-reference requirement to both project profiles. The connection is only real when both pages acknowledge it.

**Step 4: AlchemyTimelineMap as the navigation layer.** The timeline project is not just a standalone visualization — it is the logical navigation hub for HermeticDB, RenMagDB, CrowleyDB, and WitcherFolkloreDB. Any figure node in the timeline that links to multiple portals is a cross-pollination point. When you click Paracelsus in AlchemyTimelineMap, you should be able to jump to his entry in HermeticDB, his appearances in RenMagDB, and his relevance to the Witcher folk medicine tradition. Design the timeline with this in mind from the start.

---

## Part 5: Building a SQL Query Arsenal

Every database you build will be queried in the same ten ways over and over. Writing those queries once, storing them as named files, and reusing them is the single highest-leverage data engineering habit you can develop.

**Create a `queries/` folder in every project.** Store your most useful SQL as `.sql` files with descriptive names: `provenance_audit.sql`, `draft_count_by_table.sql`, `figures_with_no_primary_source.sql`. Running `python -c "import sqlite3; ..."` against a named query file takes seconds; re-writing the query from memory takes minutes and introduces bugs.

**The five queries every DH project needs:**

**1. The provenance audit** — how much of your data is still DRAFT?
```sql
SELECT source_method, review_status, confidence, COUNT(*) as count
FROM scholars
GROUP BY source_method, review_status, confidence
ORDER BY count DESC;
```
Run this at the start of every session. If more than 30% of entries are DRAFT, the data pipeline is ahead of the review pipeline.

**2. The coverage gap finder** — what is in your corpus but not in your database?
```sql
-- For RenMagDB: which documents are ingested but have no extracted figures?
SELECT d.title FROM documents d
LEFT JOIN document_figures df ON d.id = df.document_id
WHERE df.document_id IS NULL;
```
This reveals ingestion gaps — PDFs that were processed but whose contents were not extracted.

**3. The orphan detector** — entities referenced in text but not defined as rows:
```sql
-- Find claims that reference a figure_id that doesn't exist
SELECT c.figure_ref FROM claims c
LEFT JOIN figures f ON c.figure_ref = f.id
WHERE f.id IS NULL;
```
Orphaned references are broken links waiting to cause confusing results.

**4. The cross-project query using ATTACH DATABASE** — before `entities.db` exists, SQLite lets you query two databases in the same command:
```sql
ATTACH DATABASE 'C:/Dev/EmeraldTablet/emerald_tablet.db' AS hermeticdb;
ATTACH DATABASE 'C:/Dev/renaissance magic/renmagdb.db' AS renmagdb;

SELECT h.figure_name, r.figure_name
FROM hermeticdb.figures h
JOIN renmagdb.figures r ON LOWER(h.figure_name) = LOWER(r.figure_name);
```
This is the manual version of entity federation — it works today, without `entities.db`, and every result is a candidate entry for the shared namespace when you do build it.

**5. The confidence distribution check** — are you promoting claims too aggressively?
```sql
SELECT confidence, review_status, COUNT(*) as count
FROM claims
WHERE source_method = 'LLM_Assisted'
GROUP BY confidence, review_status;
```
If any LLM-assisted claim has `confidence = 'HIGH'` and `review_status != 'Verified'`, something bypassed the review pipeline. This should return zero rows.

---

## Part 6: The DRAFT Review Cycle

Every LLM-assisted entry starts as DRAFT/MEDIUM. Without a review discipline, DRAFT entries accumulate until the database is full of unverified content that you are too intimidated to touch. Here is a realistic cycle.

**Set a review quota, not a review deadline.** "I will review 20 entries per session" is achievable. "I will clear all DRAFTs by Friday" is not. The quota approach means every session makes measurable progress regardless of how much time you have.

**Batch by type, not by project.** Reviewing all scholar profiles across every project in a single session is more efficient than reviewing all entries in a single project. You develop a rhythm for the Scholar Profile format; your judgments become faster and more consistent.

**The three-question test for promoting DRAFT to Verified:**
1. *Can I trace this claim to a specific page in a specific source?* If yes, `confidence = HIGH`.
2. *Would a specialist in this field immediately recognize this as accurate?* If uncertain, leave at MEDIUM.
3. *Did an LLM add any detail not present in the source material?* If yes, mark the hallucinated addition as a separate DRAFT entry, not part of the verified claim.

**Run `lint_writing.py` before human review, not after.** The linter catches surface-level problems (vague praise, missing fields, no quotable evidence) at zero token cost. A human reviewer's attention is too valuable to spend on entries that a script could have flagged as structurally deficient.

**The promotion pipeline:**
```
LLM generates → DRAFT/MEDIUM → lint_writing.py audit → human reads source → Reviewed/HIGH or MEDIUM → Published
```
Any entry that skips a step is not verified, regardless of what the database says.

---

## Part 7: Defeating Staleness

A wiki that does not match reality is worse than no wiki — it actively misleads the LLM in future sessions. Staleness is the slow entropy that kills all knowledge systems, and the only cure is a deliberate maintenance practice.

**The actuality check: compare the profile to the code.** Once a month, open a project profile and the actual project side by side. Ask: is every Architecture bullet still accurate? Has the tech stack changed? Are the System Invariants still enforced? Has the row count in Core Content grown significantly? If any answer is yes, the profile needs updating before the next session that touches that project.

**The Next Step field is a staleness sensor.** If a project's Next Step entry is more than three months old and the project is still active, either the step was completed (update the profile) or the project is stuck (note why in log.md). A Next Step that is never acted on and never updated is evidence of a dead profile.

**When to UPDATE a page vs. create a new synthesis:**
- **Update the page** when the underlying facts changed: new tech stack, new data counts, new System Invariants discovered.
- **Create a new synthesis doc** when your *understanding* of the project changed: a new architectural insight, a new relationship to other projects, a critique that deserves its own treatment.

Never delete old synthesis documents. Mark them with a header noting when they were superseded and why. The history of how your understanding evolved is itself a scholarly record.

**The "divergence signal" in log.md.** Run this mental check: take the most recent log entry that mentions a given project, and compare its description of the project to the current profile. If they describe meaningfully different things, the profile has diverged from reality. Divergence is normal — it is undetected divergence that causes problems.

---

## Part 8: Context Window Discipline

The wiki will grow. Context windows are finite. At some point you will have more wiki than fits in a single prompt, and you will need to choose what to include. Here is how to make that choice well.

**The minimum viable context rule.** For any task, you need at most: `index.md` + `log.md` + the single most relevant project profile + the one architecture doc that governs the task. Five files, maybe six. Everything else is noise that dilutes the LLM's attention.

**Write every page to be useful in isolation.** Never write "as mentioned in the architecture document above" or "following the pattern established earlier." A wiki page will be read without its neighbors. Every page must stand alone: state its own constraints, name its own related entities, describe its own invariants. References to other pages should be [[WikiLinks]], not prose dependencies.

**The density rule: one dense page beats five thin ones.** A 400-word page with a real System Invariants section, a real architecture description, and a real Next Step is worth more as context than five 100-word stubs. The LLM extracts constraints from structure. If the structure is absent, it invents its own.

**The context prioritization order:**
1. `index.md` — always
2. `log.md` — always
3. The project profile for today's work — always
4. `architecture_deckard_boundary.md` — when writing code
5. `concept_scholarly_writing.md` — when generating prose
6. The profiles of any projects this one links to — when doing cross-pollination work
7. Everything else — only when directly relevant to a specific question

---

## Part 9: Anti-Patterns to Avoid

These are the failure modes that make wikis useless over time. Each one is drawn from patterns visible in or cautioned against in this catalog.

**The Wall of Text.** A page that is 2,000 words of undivided prose. The LLM processes the first third at full attention, the middle at partial attention, and the last third barely at all. Fix: every page must have structural headers, and no section should exceed ~200 words before a break.

**Terminology Drift.** The same concept under five different names: "Deckard Boundary," "the Python/LLM divide," "the deterministic boundary," "the judgment wall." Every name is a separate signal to the LLM; divergence causes it to treat them as different things. Fix: pick one canonical term per concept and enforce it across every page. The glossary (`concept_beginners_glossary.md`) is the authority.

**The Orphan Page.** A file added to `index.md` but not linked from any Related Entities section in any other page. The LLM finds it via the index but has no sense of how it connects to anything. Fix: every new page must add its title to the Related Entities section of at least two existing pages that are genuinely connected to it.

**Confidence Inflation.** Marking LLM-assisted entries as HIGH without running them through the three-question test. This is the most dangerous anti-pattern because it produces a database that looks verified but is not. Fix: LLM-assisted content is DRAFT until a human reads the source. No exceptions. The review pipeline exists precisely because this is tempting to skip.

**The Stale Next Step.** The Next Step field on a project card is the single highest-signal piece of information about the project's current state. An outdated Next Step tells the LLM the wrong thing to build. Fix: every time a project is opened in a session, the first thing updated is the Next Step — even if nothing else changes.

**The Meta-Wiki Trap.** Spending more time documenting the wiki than building the projects. This is easy to fall into when the wiki work is satisfying and the actual project work is hard. Fix: the log.md is the check. If the last ten entries are all "synthesis" and "docs" operations with no "ingest" or "build" operations, you are writing about building instead of building.

**The Batch Synthesis Dump.** Asking the LLM to synthesize ten new project profiles in a single session, producing ten thin, structurally complete but intellectually shallow pages. This violates the `critique_database_engineering.md` rule: 37 hand-verified rich profiles are worth more than 119 machine-generated thin ones. Fix: write one profile per session, write it slowly, and spend the review time to make it dense.

---

## Part 10: Extending the Wiki With a Query Console

The `build_ideas.py` script already demonstrates the core pattern: scan a folder of Markdown files, extract structured data, render it as a navigable HTML interface. This pattern can be extended to make the wiki itself queryable as an interface, not just a folder of files.

**A "cross-project entity browser"** — a page generated at build time that lists every entity mentioned in Related Entities sections across all project profiles, with links to every project that references it. Click on "Paracelsus" and see every project that considers him relevant. This is the manual version of `entities.db` and can be built today with 50 lines of Python.

**A "coverage gap report"** — a generated HTML page that shows, for each project, its DRAFT entry count, its last log entry date, and whether its Next Step is older than 90 days. This is a dashboard of wiki health, generated from the same data that already exists.

**A "missing pages detector"** — scan all `[[WikiLinks]]` across the wiki, compare against the list of actual files, and generate a list of concepts that are referenced but have no page. Every item on that list is a wiki debt — a concept important enough to be linked to but not yet important enough to have been written. Prioritize the ones with the most incoming links.

**Wiring the wiki to the actual databases.** The ultimate extension: when a figure's name appears in a wiki page's Related Entities section, the query console automatically runs `SELECT * FROM figures WHERE name LIKE '%Paracelsus%'` against every project database that has a `figures` table and displays the results inline. This requires a configuration file that maps wiki entity names to database table/column pairs — but it transforms the wiki from a documentation layer into a live query interface over all your databases simultaneously.

None of these require new technology. They require the same Python + SQLite + Static HTML pattern already in use in every project in this catalog.
