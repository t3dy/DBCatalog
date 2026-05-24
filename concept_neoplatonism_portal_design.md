# NeoplatonismDB: Portal Design & Implementation Plan

*A comprehensive knowledge portal on Neoplatonic philosophy from Plotinus through the Renaissance, organized concept-first with encyclopedic essays and a full reception-history treatment.*

---

## 1. Core Design Philosophy

**The Portal as Encyclopedia + Database Hybrid**

NeoplatonismDB differs fundamentally from HermeticDB in its organizing principle:
- **HermeticDB**: Textual transmission-first. Start with a text (the Emerald Tablet), trace its lineage across languages and centuries.
- **NeoplatonismDB**: Concept-first. Start with an idea (emanation, henology, theurgy), trace how philosophers developed it, what texts articulated it, how Renaissance thinkers transformed it.

This concept-first architecture demands:
1. A rich **concept ontology** (200+ concepts organized in categorical groups)
2. **Relational browsing** where clicking "henology" shows all philosophers who contributed to it, all texts that discuss it, a thematic essay on its history
3. **Multi-layered content**: structured metadata + entity essays + cross-cutting thematic essays
4. **Reception history as primary structure**: not just "what Plotinus said" but "how Ficino reinterpreted it"

---

## 2. Data Model & Ontology

### Entity Types

**Core Tables:**

#### 1. Concepts
The organizing spine. Each concept is a rich entity with provenance.

| Field | Type | Notes |
|-------|------|-------|
| `id` | INTEGER | Primary key |
| `name` | TEXT | "henology", "emanation", "apophasis" |
| `category` | TEXT | "Metaphysical", "Epistemological", "Practical/Theurgical" |
| `greek_term` | TEXT | Original Greek if applicable |
| `definition` | TEXT LONG | Structured definition, 200-500 words |
| `first_articulation` | TEXT | Which philosopher/text first developed this? |
| `etymology` | TEXT | Linguistic background if relevant |
| `related_concepts` | TEXT | Comma-separated IDs of related concepts (many-to-many) |
| `review_status` | TEXT | DRAFT, Reviewed, Verified |
| `confidence` | TEXT | LOW, MEDIUM, HIGH |
| `source_method` | TEXT | Deterministic, LLM_Assisted, Human_Verified |

**Concept Categories** (~5-8 major groups):
- **Metaphysical**: The One, Nous, Soul, Matter, emanation, procession, return
- **Epistemological**: Henosis, theoria, intellection, noesis, apophasis (via negativa)
- **Theological**: The Good, the Beautiful, the Demiurge, divine providence
- **Soteriological**: Theurgic salvation, participation (methexis), divinization (theosis)
- **Ethical**: Virtue, the sage, apatheia, the contemplative life
- **Cosmological**: The cosmic hierarchy, the All, universal soul, daemons
- **Practical/Magical**: Theurgy, sunthema (sacred symbol), symbola, ritual practice, sympatheia

#### 2. Philosophers
Contextualized under concepts. Each philosopher has biographical data, a school affiliation, and a central contribution.

| Field | Type | Notes |
|-------|------|-------|
| `id` | INTEGER | Primary key |
| `name` | TEXT | "Plotinus", "Porphyry", "Ficino" |
| `dates` | TEXT | "204–270 AD" |
| `era` | TEXT | "Ancient", "Late Antique", "Byzantine", "Islamic", "Medieval", "Renaissance" |
| `school` | TEXT | FK to Schools table (see below) |
| `tradition` | TEXT | "Roman", "Syrian", "Athenian", "Alexandrian", "Islamic", "Christian Neoplatonism", "Renaissance Humanism" |
| `central_claim` | TEXT LONG | What is this philosopher's unique contribution? |
| `methodological_stance` | TEXT LONG | How do they approach philosophy? (contemplative vs. theurgic, etc.) |
| `key_texts` | TEXT | Comma-separated list of their major works |
| `disputes_with` | TEXT | Other philosophers they disagreed with (many-to-many) |
| `influenced_by` | TEXT | List of predecessors |
| `influenced` | TEXT | List of successors/students |
| `quotable_evidence` | TEXT LONG | A key passage that exemplifies their position |
| `review_status` | TEXT | DRAFT, Reviewed, Verified |
| `confidence` | TEXT | LOW, MEDIUM, HIGH |
| `source_method` | TEXT | Deterministic, LLM_Assisted, Human_Verified |

**Key philosophers to start with:**
- Plotinus (Roman school founder)
- Porphyry (systematizer)
- Iamblichus (theurgist, Syrian school)
- Proclus (synthesizer, Athenian school)
- Damascius (final Athenian school head)
- Ficino (Renaissance translator, Platonist Academy)
- Pico della Mirandola (syncretist, kabbalist)

#### 3. Schools
Organizational hierarchy. Each school has a location, time period, key figures, and methodological character.

| Field | Type | Notes |
|-------|------|-------|
| `id` | INTEGER | Primary key |
| `name` | TEXT | "Roman School", "Apamea (Iamblichean)", "Athenian School", "Ficino's Platonic Academy" |
| `location` | TEXT | Geographic center |
| `period_start` | INTEGER | Year CE or Islamic calendar |
| `period_end` | INTEGER | Year CE or Islamic calendar |
| `founder` | TEXT | FK to Philosopher |
| `key_figures` | TEXT | Comma-separated IDs of major representatives |
| `methodological_character` | TEXT | "Contemplative", "Theurgic", "Syncretist", "Exegetical" |
| `next_school` | TEXT | What school followed this one? (successor relationship) |
| `primary_location` | TEXT | "Rome", "Apamea", "Athens", "Constantinople", "Baghdad", "Florence" |

**Schools to model:**
1. Roman School (Plotinus, Porphyry) — 3rd c. AD
2. Iamblichean School (Apamea, Damascus) — 4th c. AD, theurgic turn
3. Athenian School (Proclus, Damascius) — 5th-6th c. AD, systematic synthesis
4. Neoplatonic transmission in Islamic philosophy — 9th-11th c. (Kindi, Farabi, Avicenna)
5. Christian Neoplatonism — Pseudo-Dionysius, medieval mystics
6. Ficino's Platonic Academy — Renaissance, 15th c. Florence
7. Pico and Christian Kabbalah syncretism — 15th-16th c.

#### 4. Texts
Primary sources and major secondary works. Keyed to the philosophers and concepts they treat.

| Field | Type | Notes |
|-------|------|-------|
| `id` | INTEGER | Primary key |
| `title` | TEXT | "Enneads", "Platonic Theology", "Metaphysics of Light" |
| `author_id` | INTEGER | FK to Philosopher (who wrote it) |
| `date` | TEXT | "3rd century AD" or range |
| `original_language` | TEXT | "Greek", "Syriac", "Arabic", "Latin", etc. |
| `translation_status` | TEXT | "Original", "Medieval Latin", "Modern Translation Available" |
| `major_concepts` | TEXT | Comma-separated concept IDs discussed in this text |
| `reception_history` | TEXT LONG | How was this text interpreted over time? |
| `key_passages` | TEXT LONG | Notable quotations with line references |
| `scholarly_importance` | TEXT | Why does a historian of philosophy care about this text? |
| `review_status` | TEXT | DRAFT, Reviewed, Verified |
| `confidence` | TEXT | LOW, MEDIUM, HIGH |

**Primary texts:**
- Plotinus: Enneads (Ennead 1-6)
- Porphyry: Isagoge, Against the Christians, Life of Plotinus
- Iamblichus: De Mysteriis, On the Mysteries, On Pythagorean Life
- Proclus: Platonic Theology, Elements of Theology, Timaeus Commentary
- Damascius: Problems and Solutions, Life of Isidore
- Pseudo-Dionysius: Mystical Theology, Celestial Hierarchy
- Ficino: Theologia Platonica, Platonic Commentaries
- Pico: Heptaplus, Oration on the Dignity of Man

#### 5. Many-to-Many Relationship Tables

```sql
CREATE TABLE philosopher_concepts (
  philosopher_id INTEGER,
  concept_id INTEGER,
  contribution TEXT,  -- "developed", "critiqued", "extended", etc.
  PRIMARY KEY (philosopher_id, concept_id)
);

CREATE TABLE concept_concepts (
  concept_id_1 INTEGER,
  concept_id_2 INTEGER,
  relationship TEXT,  -- "derives from", "opposes", "precedes", etc.
  PRIMARY KEY (concept_id_1, concept_id_2)
);

CREATE TABLE text_concepts (
  text_id INTEGER,
  concept_id INTEGER,
  treatment TEXT,  -- "central", "mentioned", "disputed", etc.
  PRIMARY KEY (text_id, concept_id)
);

CREATE TABLE philosopher_influences (
  influencer_id INTEGER,
  influenced_id INTEGER,
  nature TEXT,  -- "direct student", "textual influence", "reaction against", etc.
  PRIMARY KEY (influencer_id, influenced_id)
);
```

---

## 3. Content Layers

The portal has three distinct content layers, each serving different needs:

### Layer 1: Structured Metadata
Tables as described above. Deterministic, provenance-tracked, the database layer. Enables querying ("show all texts discussing theurgy") and relational navigation.

### Layer 2: Entity Essays
A rich essay on each major concept, each philosopher, and each school. These are authored as LLM syntheses from the corpus, tagged DRAFT, reviewed and promoted to Verified by you.

**Concept Essay** (for "henology"):
- Definition and history of the term
- Its role in Plotinus's system
- How later philosophers reinterpreted it
- Key texts that discuss it
- Modern scholarly debates
- Recommended reading
- Length: 800–1500 words

**Philosopher Essay** (for "Proclus"):
- Life and historical context
- Central philosophical positions
- Major works and their importance
- Relationship to predecessors (esp. Plotinus, Iamblichus)
- Influence on successors
- Theurgic practice (if applicable)
- Scholarly assessment
- Length: 1000–2000 words

**School Essay** (for "Athenian School"):
- Historical period and geographic context
- Key figures and their relationships
- Distinctive methodological character
- How they transformed Neoplatonism from their predecessors
- Their reception by later traditions
- Length: 1000–1500 words

### Layer 3: Thematic Essays
Cross-cutting essays addressing topics that span multiple philosophers, concepts, and texts. These are synthesized LLM outputs from the corpus, reviewed by you.

**Examples:**
- "The Problem of Evil and Unjust Suffering in Neoplatonism" — how Plotinus, Iamblichus, and Proclus each grapple with theodicy
- "Theurgy vs. Contemplation: Two Paths to Henosis" — contrasting the Syrian and Athenian schools
- "Neoplatonism and Gnosticism: Philosophical and Theological Tensions" — the famous debate between Plotinus and Gnostics
- "Emanation vs. Creation: How Medieval Christian Thinkers Transformed Neoplatonic Ontology" — Pseudo-Dionysius, Aquinas, Eckhart
- "The Renaissance Recovery of Plato: Ficino's Translation Project and its Philosophical Consequences"
- "Henosis in Christian Mysticism: Pseudo-Dionysius and Neoplatonic Union with the Divine"
- "Islamic Neoplatonism: How al-Farabi and Avicenna Reinterpreted the Enneads"

Each thematic essay:
- Identifies 3–6 key philosophers/texts it centers on
- Treats a philosophical problem or historical transformation
- Surfaces scholarly disagreements
- Recommends primary and secondary sources
- Length: 2000–4000 words (ambitious but essential for encyclopedic depth)

---

## 4. Architecture & Tech Stack

### Frontend: Next.js 15 SSG (like HermeticDB)

**Why Next.js over static HTML:**
- Concept-first navigation benefits from relational previews (click "henosis," see a side panel of philosophers who theorized it)
- Component reuse: scholar profile, concept card, text card, school timeline are each a component rendered across many pages
- Advanced data flow: JSON exports by concept, by philosopher, by school enable sophisticated filtered views

**Core Views:**

1. **Concept Browser** → concept list with category filtering → individual concept page
   - Show philosopher network (who developed this concept?)
   - Show texts that discuss it
   - Show related concepts
   - Display the entity essay
   - Link to thematic essays mentioning this concept

2. **Philosopher Browser** → philosopher list → individual philosopher page
   - Show concepts they contributed to
   - Show their texts
   - Show their school and relationships (students, mentors, critics)
   - Display the entity essay
   - Include quotable evidence sidebar

3. **School Timeline** → interactive timeline (Ancient → Late Antique → Islamic → Medieval → Renaissance)
   - Show key figures per school
   - Show conceptual developments per era
   - Link to thematic essays on "Neoplatonism in the Islamic Golden Age" etc.

4. **Thematic Essay Index** → list of all thematic essays with tags (concept-centered, philosopher-centered, period-centered)
   - Each thematic essay links back to the entities it discusses

5. **Full-Text Search** (Fuse.js client-side) searching:
   - Concept names and definitions
   - Philosopher names and essays
   - Text titles
   - Thematic essay titles and content

### Backend: SQLite + Python Ingestion Pipeline

**Ingestion flow:**

1. **Source collection**: PDFs of Plotinus, Proclus, Ficino; academic monographs on Neoplatonism; secondary literature
2. **Text parsing** (PyMuPDF): Extract text, structure (chapters, sections), metadata
3. **Entity extraction** (spaCy NER): Identify philosopher names, text titles, place names, concepts
4. **Concept mapping** (manual + LLM-assisted): Which concepts does a passage discuss?
5. **Multi-pass synthesis** (LLM): Generate entity essays (concept, philosopher, school) and thematic essays, tagged DRAFT
6. **Human review** (via DH Admin Panel): Promote entries from DRAFT → Reviewed → Verified
7. **Build step** (Next.js): Generate all HTML from SQLite, output to GitHub Pages

**Database schema:** ~500–1000 entities total (200+ concepts, 50–70 philosophers, 7 schools, 100–150 texts, 20–40 thematic essays)

---

## 5. The Deckard Boundary for NeoplatonismDB

**What Python Handles (Deterministic):**
- Scholar metadata: name, dates, school affiliation, era
- Text metadata: title, author, language, date, major concepts covered
- School definitions: location, period, founder, successor
- Many-to-many relationships: which philosopher contributed to which concept?
- Concept hierarchy: which concepts are related to which?
- Timeline rendering: chronological placement of philosophers and schools
- Search indexing

**What the LLM Handles (Judgment):**
- Entity essays: synthesizing the philosophical position from primary and secondary sources
- Thematic essays: connecting disparate philosophers around a common problem
- Interpretive stances: what is the scholarly consensus on a controversial point?
- Quotable evidence selection: finding the most eloquent or representative passage
- Reception history narrative: how did each tradition transform Neoplatonism?

**Provenance discipline:**
- Every LLM-synthesized essay starts as DRAFT/MEDIUM
- You read the source material (primary + secondary)
- You either promote it to Verified (you agree with the synthesis) or rewrite it and promote it as Human_Verified
- The goal: no DRAFT essays ship to the site

---

## 6. Connection to Existing Projects

### HermeticDB
- **Shared figures**: Plotinus, Porphyry, Iamblichus, Proclus appear in both portals
- **Authority**: NeoplatonismDB becomes the authoritative entry for these figures
- **Linking**: HermeticDB entries on "Hermetic transmission" link out to NeoplatonismDB entries on "Plotinus" and "emanation"
- **Cross-reference IDs**: Eventually (when `entities.db` exists), both databases reference Plotinus by the same canonical ID

### RenMagDB
- **Renaissance figures**: Ficino and Pico appear in both
- **Same authority pattern**: NeoplatonismDB is authoritative for Neoplatonic content; RenMagDB links out
- **Methodological affinity**: Both use the scholarly lineage / dispute model

### AlchemyTimelineMap
- **Timeline integration**: The "era zones" on AlchemyTimelineMap include "Neoplatonism" as a major era
- **Concept transmission**: Trace how Neoplatonic concepts (henosis, emanation, the Beautiful) influenced alchemical thought
- **Philosopher nodes**: Plotinus, Iamblichus, Proclus appear on the timeline with links to NeoplatonismDB

### Future WitcherFolkloreDB Extension
- **Theurgy layer**: The Iamblichean theurgy content here becomes the foundation for a future "Witcher Theurgy Laboratory" mode
- **Correspondence tables**: The "sacred symbols" (sunthema, symbola) documented in the Neoplatonism essays feed into grimoire-style correspondence tables

---

## 7. Roadmap & Phase Strategy

### Phase 1: Schema & Core Ingestion (Weeks 1–3)
- Build the SQLite schema (Concepts, Philosophers, Schools, Texts tables + many-to-many)
- Ingest primary texts (Enneads, Platonic Theology, De Mysteriis, Elements of Theology) via PyMuPDF
- Extract and manually map ~70 philosophers, ~150 texts, ~200 concepts into the database
- Mark all as Deterministic (structural data, no interpretation)

### Phase 2: Entity Essays (Weeks 4–6)
- Run the LLM pipeline: synthesize concept essays from the corpus (200 concepts × ~1000 words = 200K tokens)
- Run philosopher essays (50–70 philosophers × ~1500 words)
- Run school essays (7 schools × ~1200 words)
- Tag all as DRAFT
- You review and promote ~50% to Verified; rewrite and promote the rest

### Phase 3: Thematic Essays (Weeks 7–8)
- Identify 15–20 thematic topics (see examples above)
- LLM synthesizes thematic essays from the corpus + entity essays (as context)
- Review and promote the same way

### Phase 4: Frontend & Deployment (Week 9)
- Build Next.js views (concept browser, philosopher timeline, thematic essay index, search)
- Export JSON bundles from SQLite
- Deploy to GitHub Pages

### Phase 5: Post-Launch Maintenance
- Use DH Admin Panel to push any remaining DRAFT entries to Verified
- Add new thematic essays as scholarship evolves
- Maintain links to HermeticDB, RenMagDB as they add Neoplatonic content

---

## 8. Success Metrics & Audience Alignment

### For the Academic Researcher
- Full provenance on every claim (source passage, scholarly authority, confidence level)
- Comprehensive bibliography (who wrote what about Neoplatonism?)
- Relational browsing (from concept → philosophers who developed it → their disagreements)
- Thematic essays surfacing scholarly debate

### For the Gamer (Future Laboratory Layer)
- The theurgy essays become the foundation for interactive "ritual design" mechanics
- The Sacred Symbols (sunthema) become collectible/combinable game elements
- The concept hierarchy becomes a "skill tree" (unlock henosis by mastering the hypostatic levels)

### For the Practitioner (Future Foundation)
- The Iamblichean theurgy essays document actual ritual practice
- Correspondence tables (planets → divine names → symbols) are queryable
- The full ancient-through-Renaissance documentation of how practitioners invoked these systems

---

## 9. Key Design Constraints & Risks

**Constraint 1: The 200+ Concept Ontology**
Creating, vetting, and writing essays for 200+ concepts is ambitious. Mitigation: start with 50 core concepts, expand incrementally. Phase 1 focuses on the inner circle.

**Constraint 2: Reception History Across Eras**
Tracking how each concept transforms across 1,400 years (Plotinus → Renaissance) requires deep domain knowledge. Mitigation: focus heavily on the LLM DRAFT → Human Review cycle. You're the expert reviewer.

**Constraint 3: Multi-Language Sources**
Greek, Syriac, Arabic, Latin, Italian sources. Mitigation: prioritize English translations for Phase 1; add original languages as secondary research.

**Constraint 4: Overlap with HermeticDB**
Be clear about boundaries. NeoplatonismDB is "What is Neoplatonism?"; HermeticDB is "How did Hermetic texts transform through history?" Mitigation: clean referential integrity and explicit linking.

---

## 10. First Actions

1. **Define the core 50 concepts.** Create a spreadsheet:
   - Concept name
   - Greek term
   - Category (Metaphysical, Epistemological, etc.)
   - Plotinus reference (which Ennead?)
   - Proclus reference (Platonic Theology chapter?)
   - Renaissance reference (Ficino essay?)

2. **Collect the corpus.** PDFs of:
   - Plotinus Enneads (Armstrong or Wakefield translation)
   - Porphyry: Isagoge, Against the Christians
   - Iamblichus: De Mysteriis
   - Proclus: Platonic Theology, Elements of Theology
   - Ficino: Theologia Platonica, letter summaries

3. **Sketch the thematic essays.** List 10–15 crossing-cutting problems that span multiple philosophers:
   - "The Nature of the One"
   - "Emanation vs. Creation"
   - "Theurgy: Salvation Through Ritual"
   - "Beauty as a Metaphysical Principle"
   - etc.

4. **Plan the schema** (SQLite design workshop). Test the Many-to-Many relationships with dummy data.

5. **Test one LLM pipeline cycle**: Feed Plotinus Enneads to the model, ask it to synthesize an essay on "henosis," review the output, note what works and what needs human rewriting.

This is the most sophisticated DH project in your ecosystem. It's ambitious but achievable given your existing infrastructure (admin panel, Deckard Boundary discipline, scholar profile standard, multi-pass pipelines). Start with the core 50 concepts and expand iteratively.
