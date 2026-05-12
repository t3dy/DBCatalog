# Architecture: Prompt Archaeology Machines & Idea Sifting

## 1. The Challenge of Megabase
You have a 1.3GB database (`megabase`) containing millions of LLM chat messages and personal logs. Hidden within those chats are flashes of intense creative brilliance: times you brainstormed an occult game mechanic, asked GPT to build a table summarizing Neoplatonic scholarship, or ideated an app combining the Scryfall API with alchemical emblems. 

Currently, these nuggets are buried. `megabase` is an unparalleled storage engine, but without an active extraction layer, the ideas remain inert.

## 2. How the Wiki Solves This (The Curation Layer)
The wiki serves as the **Curation Layer** sitting on top of `megabase`. Instead of leaving ideas as isolated rows in a chat transcript, the wiki allows us to extract, link, and compound them. 

* If you extract a 2024 chat about a Philip K. Dick game mechanic, the wiki explicitly hyperlinks it to `[QueryPat](project_querypat.md)`.
* If you extract a book idea generated from a PDF summary on Renaissance magic, it inherits the rules of `[Scholarly Writing](concept_scholarly_writing.md)`.
* **The Goal**: The wiki transforms raw chat logs into a living "Idea Vault" where concepts from 2022 can collide with code from 2026.

## 3. Building the "Nugget Machines"
To sift through the LLM chats, we need to build automated extraction pipelines that respect the **Deckard Boundary**.

### The Pipeline Design
1. **Deterministic Filter (Python + FTS5)**
   We do not ask the LLM to read 4 million messages. Instead, Python runs strict SQLite FTS5 queries against the `messages_fts` table in `megabase.db` to isolate high-potential conversations.
   - *Game Ideas Query*: `MATCH '"game mechanic" OR "card game" OR "roguelike" OR "prototype"'`
   - *App Ideas Query*: `MATCH '"web app" OR "dashboard" OR "API" OR "interface"'`
   - *Book/Scholarship Query*: `MATCH '"summarize this pdf" OR "table of" OR "chapter outline" OR "monograph"'`

2. **LLM Extraction (The Judgment Zone)**
   Python passes the isolated conversation chunks to the LLM with a strict prompt: 
   *"Act as a prompt archaeologist. Strip away the chat pleasantries. Extract the core game/app/book idea. Identify the primary scholarly sources referenced in the prompt. Output as structured markdown."*

3. **Wiki Ingestion**
   The script does not just insert another row into Megabase. It generates structured Markdown files directly into a new `C:\Dev\wiki\vault\` directory (e.g., `vault/game_alchemy_scryfall.md`), flagging them all as `review_status: DRAFT`.

## 4. Categories of Extraction
Based on your prompt history, the machines should target three specific evidentiary lanes:

### Lane A: Game Ideas
Extracting core loops, rule systems, and thematic skins.
* *Target Signatures*: Discussions about MTG card sets, esoteric combat mechanics, visual novels, and rule-balancing.

### Lane B: Occult & DH App Ideas
Extracting specifications for digital humanities tools and interactive interfaces.
* *Target Signatures*: Requests to wire APIs together, dashboard layouts for exploring texts, or "Karpathy-style" memory architectures.

### Lane C: Book Ideas & Scholarly Synthesis
Extracting the recurring obsessions that appear across years of your PDF uploads.
* *Target Signatures*: Tables you had GPT build summarizing scholarship, outlines for chapters, or deep dives into the intersection of Gnosticism, Marxism, and technology. The machine will group these by theme to reveal the book you've been accidentally writing for years.

## 5. Next Steps for Implementation
To make this real, we can build `C:\Dev\promptarchaeology\scripts\wiki_extractor.py`. This script will connect to `megabase`, run the FTS5 filters, pass the chunks to Claude, and deposit the synthesized nuggets directly into this wiki for your review.
