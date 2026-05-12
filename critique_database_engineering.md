# Critique of Database Engineering & Web Writing

## 1. The Over-Engineering of QueryPat
Looking across the landscape of our DH projects, there is a looming risk that LLMs have begun to over-engineer the database architectures. **QueryPat**, for example, employs a massive, multi-stage ingestion pipeline (Pre-Processing, Swarm Extraction, Heuristic Linking, Editorial Overrides, and 20 automated "Corpus Improvement" scripts). 

While technically impressive, this violates **Prompt Archaeology Value #7: Methodology emerges under pressure, not from theory.** 

When we let LLMs dictate the architecture, they tend to build sprawling, highly theoretical frameworks that prioritize dense cross-linking over actual readability. The DB schema becomes the goal, rather than the insight. As **Prompt Archaeology Value #10** reminds us: *The water keeps what's heavy. Frameworks and platforms flicker.* The architecture in QueryPat began to flicker—becoming so complex that generating the React components overshadowed the actual scholarly reading of Philip K. Dick.

## 2. The Web Writing Problem: Flattening
There is a stark contrast between the *design* of our templates and the *reality* of the LLM-generated web writing. 

We built master classes in data structuring—like the `template_scholar.md` in QueryPat, which explicitly demands an `interpretive_stance`, `scholarly_lineage`, and documented `disputes`. Yet, when automated batches run, the LLM writing often degrades into "vague praise." 
- **The Issue**: LLMs naturally want to resolve tension, synthesize smoothly, and avoid taking definitive, critical stances.
- **The Result**: We get thin wiki profiles that say a scholar "provided valuable insights into PKD's theology" instead of "advanced a Marxist/Althusserian critique of *Ubik* that explicitly disputed Sutin's biographical timeline."

## 3. The Prompt Archaeology Remedy
To fix the writing and the engineering moving forward, the Wiki Memory System will enforce the values uncovered in **Promptarchaeology-Heldscalla**:

* **Treat the Corpus as a Primary Source (Value 4)**: The Q-log convention from MTGSLIDER proved that capturing verbatim input and manually annotating interpretations is superior to automated batch summarization. 
* **Earnestness Through Irony (Value 3)**: Stop writing generic academic slop. The writing should be dense, highly specific, and unafraid of pulp aesthetics or idiosyncratic framing.
* **Refuse Closure (Value 8)**: Stop running scripts that try to finish 10,000 segments at once. Leave the manuscripts open. It is better to have 37 hand-verified, intensely rich scholar profiles than 119 thin, machine-generated ones.

## 4. Next Steps
Going forward, no agent is allowed to execute automated batch-summarization without passing the output through the **Scholarly Voice Master Template**. Database schemas should be pruned to exactly what is needed for the user to query the text, resisting the LLM impulse to add "just one more join table."
