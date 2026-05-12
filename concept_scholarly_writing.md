# Master Concept: Scholarly Writing & Voice

This is the global style guide for all LLM-assisted generation within the DBCatalog ecosystem. It extracts the rigorous standards developed in the `QueryPat` scholar templates and the epistemological values of `Prompt Archaeology`.

## 1. The Epistemological Stance
- **Never Flatten Contradictions**: If Scholar A says the text is literal and Scholar B says it is allegorical, do not synthesize them into a "nuanced middle ground." Explicitly name the dispute.
- **Lower Heaven into Reach**: Academic rigor does not require academic stiffness. Write with high density but clear, declarative momentum.
- **Methodology Must Be Visible**: The reader must know *how* a claim was derived. Attribute claims to specific methods (e.g., Marxist, psychoanalytic, formalist).

## 2. The Scholar Profile Standard
Whenever generating a profile or summary of a researcher, thinker, or author, you MUST adhere to the following structure:

* **Central Claim (1 sentence)**: What is the one thing this scholar most distinctively argues?
* **Methodological Frame (1 sentence)**: e.g., Marxist, psychoanalytic, postmodern, formalist, deconstructive.
* **Specific Moves (2-4 sentences)**: What concepts did they introduce? What errors did they correct? Name their works and the prior scholars they reference.
* **Scholarly Lineage & Disputes**: Who do they descend from intellectually? Who did they explicitly disagree with? (e.g., "Disputes: Sutin over the chronology of the Vancouver trip.")
* **Relevance**: Tell the researcher what specific classes of questions this scholar answers. (e.g., "Consult for ideological-critique readings of the mid-1960s novels.")
* **Quotable Lines**: Provide 2-5 specific text excerpts as evidence.

## 3. The Lint Checklist for Agents
Before an agent commits writing to the database, it must pass this internal check:
- [ ] Is the tone critical-reportorial rather than universally praising?
- [ ] Did I name specific question-classes rather than using generic phrases like "provides valuable insights"?
- [ ] Are all disputes explicitly attributed to named opponents?
- [ ] Is there verbatim textual evidence?
