# DBCatalog (LLM-Wiki Memory System)

Welcome to the **DBCatalog**, a personal knowledge base built using the [LLM-Wiki pattern popularized by Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). This repository serves as the compounding "memory" layer for a series of complex Digital Humanities (DH) databases, React web portals, and unified Python indexing pipelines.

## 🧠 The Method (Karpathy Pattern)

Traditional retrieval-augmented generation (RAG) relies on an LLM scanning raw files from scratch on every prompt. The LLM-Wiki pattern changes the paradigm by "compiling" the raw sources into an organized, heavily interlinked markdown wiki. The LLM reads the raw data, synthesizes it, maintains cross-references, updates catalogs, and manages timelines.

### Architecture
- **Raw sources**: The primary codebases and scholarly research documents (which remain immutable to the memory system).
- **The wiki**: This repository. It is a directory of LLM-generated markdown files containing project summaries, concept pages, entity profiles, and analyses.
- **`index.md`**: The central catalog of everything in the wiki, grouped by Entities, Concepts, and Projects. The LLM uses this file to navigate the memory space.
- **`log.md`**: A chronological, append-only record of every change made to the wiki (ingestions, queries, and maintenance lints).
- **Schema (`CLAUDE.md`)**: The root instruction set that dictates how the AI agent operates within the memory system (defining the Deckard Boundary, provenance rules, and operational workflow).

---

## 📚 Cataloged Database Projects

This memory system currently tracks 10 major projects, mostly centered around Digital Humanities, Western Esotericism, Game Design, and Intellectual History.

### 1. AtalantaClaudiens
A digital humanities website showcasing scholarship on Michael Maier's *Atalanta Fugiens* (1618). It features 50 alchemical emblems with comparative scholarly commentary, mapped textual sources, an alchemical dictionary, and a strict data provenance tracking system.

### 2. Dreambase (megabase)
A personal knowledge archaeology system that unified two years of LLM conversations, social media, and emails into a 1.3GB SQLite database. It indexes 4,308 conversations and 3.9M messages using FTS5, VADER sentiment analysis, and zero-cost chunked GPT summarization.

### 3. RenMagDB (Renaissance Magic)
A DH project cataloging a research corpus of 337 scholarly documents on Renaissance magic. It features a terminology dictionary, timelines, and biographies for figures like John Dee and Marsilio Ficino, served through a Python-to-SQLite pipeline.

### 4. Hypnerotomachia Poliphili Marginalia
A repository documenting the readership and marginalia of the 1499 Aldine edition. Based on James Russell's PhD thesis, it tracks 109 annotated folios, 11 annotator hands, 60 scholars, and implements a deep provenance tracking model (HIGH/MEDIUM/LOW confidence).

### 5. HermeticDB (EmeraldTablet)
A deterministically-grounded Next.js knowledge portal tracking Hermetic, Alchemical, and Neoplatonic textual transmission. It uses a multi-pass autonomous pipeline to extract and synthesize 7,003 atomic claims into Wikipedia-style scholarly articles with exact source provenance.

### 6. Bach Studies
A scholarly research database utilizing the standardized "DH Framework" (SQLite → Python → Static HTML). It maintains strict data invariants, ensuring changes flow in a single direction and AI-generated content is locked to DRAFT status until human review.

### 7. SocialsDB
A unified personal data mining hub serving as an expansion of Megabase. It manages nearly 4 million messages across 11 sources without invoking LLMs during ingestion, relying entirely on deterministic Python scripts and SQLite FTS5 triggers.

### 8. MarxistPortal
A curated educational website companion to Capital RAG. It explores the Marxist intellectual tradition through a static site compiler, modeling contemporary issues across four theoretical lenses: Classical Marxism, Value-Form Theory, Geographical Materialism, and Structuralist Marxism.

### 9. Shakespeare Sonnets
A DH site analyzing Shakespeare's 154 Sonnets across four pillars: Analyses, Directing, Contexts, and Essays. It uses a rigid "Deckard Boundary" that strictly separates deterministic Python formatting tasks from LLM-assisted literary interpretations, holding the 1609 Quarto text as an immutable seed.

### 10. QueryPat (Philip K. Dick Knowledge Portal)
A React/Vite-based scholarly portal about Philip K. Dick. It synthesizes 1,107 Exegesis segments, 646 biography events, and 237 scholarly documents. Governed by a deep ontological framework (`PKDontology.md`), it surfaces rather than flattens contradictions and classifies evidence across five distinct interpretive lanes.
