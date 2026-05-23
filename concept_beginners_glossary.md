# Beginner's Glossary: Plain English for Every Term in This Wiki

*Written for a beginning CS student. Every definition includes a real example from one of the projects in this catalog. No prior knowledge assumed.*

---

## Part 1: Core CS Building Blocks

### Database
A database is a structured filing system for information that a computer can search extremely fast. Think of it as a giant spreadsheet where every row is one thing (one book, one monster, one witchcraft trial) and every column is a piece of information about that thing (title, date, author, outcome). Unlike a real spreadsheet, a database can store millions of rows and find the one you want in milliseconds.

### SQLite
The specific type of database used in nearly every project here. Unlike databases that run on a separate server (like PostgreSQL or MySQL), SQLite is just a single file on your hard drive — for example, `megabase.db` or `emerald_tablet.db`. This makes it perfect for a solo developer: no server to manage, no network connection required, and you can copy the whole database by just copying the file. The trade-off is that it is not designed for thousands of simultaneous users.

### SQL
The language you use to talk to a database. SQL stands for *Structured Query Language*. You write sentences like `SELECT * FROM scholars WHERE tradition = 'Hermetic'` to get back a list of all Hermetic scholars. Every project here uses SQL (via Python scripts) to read from and write to the SQLite database.

### Python
The programming language that does the "plumbing" in every project here. Python scripts handle all the hard work that happens before the website exists: reading PDF files, extracting names and dates from raw text, writing data into the SQLite database, and generating the HTML files. Python is chosen here because it is readable, has excellent libraries for text processing, and is effectively the standard language for data work.

### Script / Pipeline Script
A "script" is just a Python file you run to do one specific job — for example, `build_site.py` reads everything out of the SQLite database and produces the finished HTML website. A "pipeline" is a sequence of scripts that run in order, each one transforming the data one step further. The standard pipeline in this catalog is: *raw PDFs → Python reads them → SQLite database → Python generates HTML → finished website*.

### Static HTML
A website made of plain HTML files that sit on a server and never change unless you deliberately re-build them. When a visitor loads a static page, the server just sends them the file — no computation happens on the server. This is why all the projects here can be hosted for free on GitHub Pages. The alternative (a *dynamic* website) runs code on the server for every visitor (like Flask in the Megabase), which is more powerful but more complex and expensive to host.

### GitHub Pages
A free web hosting service provided by GitHub. If you push a folder of HTML files to a GitHub repository and turn on GitHub Pages, the files are immediately available as a live website. This is why projects like HermeticDB and RenMagDB are publicly accessible at no cost.

### JSON
*JavaScript Object Notation* — a simple text format for storing structured data. It looks like this: `{"name": "Paracelsus", "era": "Renaissance", "tradition": "Alchemy"}`. In the Digby Game, all the game state lives in JSON files like `reagents.json` and `scenes.json` because JavaScript (which runs in the browser) can read JSON files directly without a database.

### Schema
The blueprint that defines what a database looks like — which tables exist, what columns each table has, and what type of data goes in each column. For example, the WitchcraftStudiesDB schema says the `trials` table has a `date`, a `region`, a `verdict`, and a `confidence` field. The schema is the law: if you try to put text in a column that expects a number, the database refuses.

### Frontend vs. Backend
**Frontend** is everything the user sees in their browser: the page layout, the buttons, the colors, the text. **Backend** is everything that runs on a server before the page is sent: database queries, Python computations, authentication. In the static HTML projects here, there is barely any backend — Python runs locally on your computer to build the files, and then GitHub Pages just serves those finished files with no server-side computation.

---

## Part 2: How Data Moves (The Pipeline)

### Ingestion
"Ingesting" data means reading it from some raw source (a PDF, a website, a text file) and loading it into the database in a structured way. When it says "ingested 70+ academic volumes" for HermeticDB, it means a Python script read those PDFs using PyMuPDF, extracted the relevant information, and inserted it as rows into SQLite.

### Deterministic
Code is "deterministic" when it always produces the exact same output from the same input. If you run the script twice on the same data, you get identical results. This is extremely important in this catalog because it means you can *trust* the data — it was not randomly generated, it cannot change behind your back, and if something is wrong you can trace it back to a specific line of code. The opposite of deterministic is a process that involves randomness or an LLM, which might produce different output every time.

### Idempotent
An idempotent script can be run any number of times without breaking anything or creating duplicates. If the ingestion script for SocialsDB is idempotent, you can run it today and again tomorrow and it will only add genuinely new messages — it will not re-add everything that was already there. This is a basic hygiene requirement for any data pipeline.

### Provenance
In scholarship, "provenance" means knowing the full history of where something came from. In this catalog, every piece of data has provenance fields: `source_method` (was this extracted deterministically, or did an LLM help?), `review_status` (has a human checked it?), and `confidence` (HIGH/MEDIUM/LOW). A claim in HermeticDB without provenance is meaningless; a claim with a verbatim citation back to a specific page of a specific book is trustworthy.

### One-Directional Data Flow
In every project here, data flows in only one direction: *Source Material → SQLite Database → HTML Website*. You never edit the HTML directly, and you never edit the database by hand. If you need to change something, you change the source and re-run the pipeline. This rule prevents the catalog from getting into a state where the database says one thing and the website shows something different.

### Source of Truth
The "source of truth" is the single place where the canonical, authoritative version of the data lives. In these projects, that is always the SQLite database. The HTML website is just a view of the database — a presentation layer. If the website and the database disagree, the database is right, and you re-generate the website.

---

## Part 3: The Frontend Tech Stack

### React
A JavaScript library made by Facebook for building interactive web user interfaces. Instead of writing HTML by hand, you write components (reusable building blocks) in JavaScript that React assembles into a page. QueryPat and the Digby Game use React because they need complex interactivity — fuzzy search, dynamic filtering, game state — that would be painful to build in plain HTML and JavaScript.

### TypeScript
A version of JavaScript that adds "types" — rules that say "this variable must be a number" or "this function must return a string." TypeScript catches whole categories of bugs before you even run the code. The Digby Game uses TypeScript because it has a complex game state with many interacting pieces, and TypeScript keeps that complexity manageable.

### Next.js / Static Site Generation (SSG)
Next.js is a framework built on top of React that, among other things, can "statically generate" every page of a website at build time — meaning it runs the JavaScript code once on your computer, produces finished HTML files, and those files are what gets hosted. HermeticDB uses Next.js 15 with SSG because it has thousands of pages but still wants the fast load times and free hosting of a static site.

### D3.js
A JavaScript library for drawing data visualizations in the browser — bar charts, network graphs, timelines, anything you can imagine. D3 works by turning data (an array of figures and dates) directly into SVG shapes on screen. AlchemyTimelineMap uses D3 to draw the force-directed timeline where figure nodes float in space and transmission arcs connect them. Unlike a chart library that gives you pre-made chart types, D3 gives you the raw building blocks, so anything is possible.

### SVG (Scalable Vector Graphics)
SVG is an image format defined by coordinates and shapes (circles, lines, rectangles) rather than by pixels. Because it is mathematical rather than pixelated, an SVG image is perfectly sharp at any zoom level. D3.js draws everything as SVG, which is why you can zoom into an AlchemyTimelineMap transmission arc and the lines remain crisp.

### Leaflet.js + GeoJSON
**Leaflet.js** is a JavaScript library for embedding interactive maps in a webpage. **GeoJSON** is the JSON format for geographic data — it describes regions, points, and paths using longitude/latitude coordinates. WitchcraftStudiesDB uses Leaflet to show a map of European witchcraft prosecution clusters, where the GeoJSON file defines the shapes of each region.

### Web Audio API
A browser-built-in system for generating and manipulating sound with JavaScript — no plugins required. The `architecture_new_directions.md` document recommends using it in AtalantaClaudiens to let users isolate and play the individual voices of Michael Maier's three-part fugues directly in the browser.

---

## Part 4: AI and LLM Terms

### LLM (Large Language Model)
The type of AI behind Claude and ChatGPT. An LLM is trained on enormous amounts of text and learns to predict what word comes next in a sentence — which turns out to be enough to answer questions, write code, summarize documents, and do most language tasks. In this catalog, LLMs handle the "Judgment Zone" work: writing scholarly analysis, identifying rhetorical devices, generating dictionary definitions. They do not handle anything that requires guaranteed accuracy, because...

### Hallucination
When an LLM confidently states something that is completely made up. LLMs do not know what they know vs. what they are guessing — they just produce the most plausible-sounding next word. This is why every project here tags LLM-generated content as DRAFT until a human verifies it, and why the Deckard Boundary exists.

### RAG (Retrieval-Augmented Generation)
A technique where, before asking the LLM to write something, you first retrieve the relevant actual facts from your database and include them in the prompt. Instead of asking the LLM "who was Jabir ibn Hayyan?" (and risking hallucination), you fetch his database entry and say "here is what we know — now write a scholarly summary of this." The Almagest Construction Kit (ACK) is the project most explicitly built around RAG.

### FTS5 (Full-Text Search)
SQLite has a built-in search engine called FTS5 that can search through millions of text records nearly instantly. It works like a search bar that searches the full content of every message or document, not just the metadata. The Megabase uses FTS5 to scan 4 million personal messages for specific keywords as the first stage of the Prompt Archaeology pipeline.

### Vector Embeddings / Semantic Search
A technique for finding text that is *conceptually similar* even when the exact words differ. An "embedding" turns a piece of text into a list of numbers (a vector) that represents its meaning. Two texts about similar topics will have vectors that are mathematically close together. The wiki currently uses FTS5 (keyword matching), but `architecture_new_directions.md` recommends adding vector search via **SQLite-vec** so you can find all Megabase messages about a concept even when you don't know exactly what words were used.

### spaCy + NER (Named Entity Recognition)
**spaCy** is a Python library for natural language processing. **NER** is one of its capabilities: automatically scanning text and identifying which words are names of people, places, organizations, and dates. RenMagDB uses spaCy NER during ingestion to automatically extract the names of Renaissance figures from scanned PDFs without manually reading every page.

### PyMuPDF
A Python library for reading PDF files programmatically — extracting text, images, and page structure. Almost every project here uses PyMuPDF as the first step of ingestion: load the academic PDF, extract the raw text, then pass that text through further processing.

### TF-IDF (Term Frequency-Inverse Document Frequency)
A mathematical formula for finding which words are *distinctive* to a specific document versus words that appear everywhere. The word "the" appears in every document (low TF-IDF score); the word "Nigredo" might appear mostly in alchemical texts (high TF-IDF score). RenMagDB uses TF-IDF to automatically cluster documents by topic.

### VADER Sentiment Analysis
A tool that reads a piece of text and scores it as positive, negative, or neutral. The Megabase uses VADER to track the emotional tone of LLM conversations over time — whether the conversations tend to be exploratory and optimistic or frustrated and stuck.

---

## Part 5: This Wiki's Special Vocabulary

### The Deckard Boundary
The central architectural rule of this entire catalog: there is a strict line between what Python must handle (anything deterministic, structural, or factual) and what the LLM is allowed to handle (literary analysis, scholarly synthesis, rhetorical identification). Python handles math, database writes, text structure, and data validation. The LLM handles interpretation, style, and judgment. Crossing the boundary in either direction causes problems: Python cannot judge the literary quality of a sonnet, and an LLM cannot be trusted to add a row to a database without inventing data.

The name comes from the movie *Blade Runner* — Deckard is the detective who runs "Voigt-Kampff" tests to determine whether something is human or replicant. Here, the Deckard Boundary tests every task: is this deterministic (Python) or does it require judgment (LLM)?

### Prompt Archaeology
The practice of treating your own archive of LLM conversations as a primary source — mining it for ideas, decisions, and insights that were generated in those conversations but never preserved anywhere permanent. The Megabase (4 million messages) is the raw material; the Prompt Archaeology pipeline uses FTS5 to sift through it and extract useful nuggets into the `vault/` directory for future use.

### The Vault (`vault/`)
A folder inside this repository where "mined" ideas from Prompt Archaeology are stored as Markdown files. Think of it as a quarry — the Megabase is the mountain, the Prompt Archaeology scripts are the mining tools, and the vault/ is where the extracted ore is kept before it is refined into a proper wiki document.

### Karpathy Pattern
Andrej Karpathy (an AI researcher) popularized the idea of using plain Markdown text files as persistent memory for an AI agent — rather than a vector database or a complex memory system, just write everything down in well-organized text files and include the relevant ones in the LLM's context. This entire wiki is built on that idea. The CLAUDE.md file tells the LLM what it knows and how to behave; the project files are its long-term memory.

### Agent Operating System
A way of thinking about the wiki: it is not just documentation, it is the operating system that makes the LLM work correctly. Just as an operating system manages a computer's resources and enforces rules about what programs can do, the wiki manages the LLM's knowledge and enforces rules about how it writes (Scholar Profiles), what it can modify (Deckard Boundary), and how it tracks its own work (the log.md).

### DRAFT / MEDIUM / HIGH (Confidence Levels)
Every piece of data in these projects carries a `review_status` and a `confidence` level. **DRAFT** means an LLM generated it and no human has checked it yet. **MEDIUM** means it is probably right but came from a secondary source or inference. **HIGH** means it was verified directly against a primary source by a human. LLM content always starts at DRAFT/MEDIUM and cannot promote itself.

### Scholar Profile Standard
A template (`template_scholar.md`) that defines exactly what information every entry about a scholar must contain: their central claim, their methodological framework, their scholarly lineage (who trained them, who they argue against), documented disputes with other scholars, and at least one verbatim quotable passage. This template exists because LLMs naturally write vague, conflict-free summaries. The template forces specificity.

### The Triple Audience
Every project in this catalog is evaluated against three distinct audiences, each with different needs:
- **The Academic Researcher**: wants exact citations, strict provenance, and methodological transparency.
- **The Gamer**: wants interactive feedback, agency, and mechanics that make the data *playable*.
- **The Occult Practitioner**: wants usable grimoire structures, correspondence tables, and aesthetic reverence.

The goal of every project is to serve all three simultaneously. A portal that only serves academics is too austere; one that only serves gamers loses its scholarly credibility.

### The Engine + Portal (Library + Laboratory)
The ideal end state for every DH project: two frontends built from the same SQLite database.
- **The Library (Portal)**: Clean, academically rigorous reading environment — dictionary, timeline, bibliography. For the researcher.
- **The Laboratory (Engine)**: Interactive, gamified playground with an LLM layer that lets you manipulate the historical concepts. For the gamer and practitioner.

The Digby Game is the most developed Laboratory in the catalog. HermeticDB is the most developed Library. The goal is projects that are both.

---

## Part 6: Digital Humanities Terms

### Digital Humanities (DH)
An academic field that applies computational tools to humanistic questions — history, literature, philosophy, art history. Instead of reading one book carefully (traditional humanities), DH might analyze patterns across ten thousand books at once. Instead of describing a manuscript by hand, DH might map its marginalia with coordinate data and connect it to similar manuscripts worldwide. Every project in this catalog is a DH project.

### Corpus
A collection of texts treated as a unified body of material for scholarly analysis. RenMagDB's corpus is its 337 scholarly documents on Renaissance magic. The Shakespeare project's corpus is the 154 sonnets of the 1609 Quarto. A corpus has clearly defined boundaries: you know exactly what is in it and what is not.

### Ontology (in CS/DH)
In philosophy, an ontology is a theory of what exists. In computer science and DH, an ontology is a structured map of the concepts in a domain and the relationships between them — like a blueprint for a database, but at a higher level of abstraction. QueryPat's ontology (`PKDontology.md`) defines what kinds of things exist in Philip K. Dick studies (novels, scholars, theological concepts, biographical events) and how they can be related to each other. A good ontology makes the database reflect reality rather than just convenience.

### Distant Reading
Analyzing patterns across a very large number of texts at once using computational methods, rather than reading individual texts closely. An example: tracking how often the word "mercury" appears in alchemical texts by decade across the full RenMagDB corpus. You cannot do this by reading; you write a SQL query. The term was coined by Franco Moretti in opposition to...

### Close Reading
The traditional literary practice of reading a single text slowly and carefully, paying attention to word choice, structure, ambiguity, and historical context. The Shakespeare Sonnets project's analysis and directing notes are close reading. Close and distant reading are both in use here — the database enables the distant reading, while the LLM-generated annotations do the close reading.

### ATU Index (Aarne-Thompson-Uther)
A universal reference system for folk tales, the way Dewey Decimal is a universal reference system for books. Every recurring folk tale plot type has a number: ATU 333 is "Little Red Riding Hood," ATU 428 is "The Wolf" (used for Sapkowski's "A Grain of Truth"), ATU 510A is "Cinderella." The WitcherFolkloreDB uses ATU classifications to rigorously place Sapkowski's fairy-tale retellings in the scholarly folklore literature rather than treating them as original inventions.

### IIIF (International Image Interoperability Framework)
A set of standards for sharing high-resolution images of manuscripts, artworks, and old books across different institutional repositories so that any compatible viewer can display them. If the Bodleian Library in Oxford and the BnF in Paris both publish their manuscripts in IIIF format, a scholar can compare a page from an Oxford copy and a Paris copy side by side without leaving their desk. The HPMarginalia project is recommended to adopt IIIF so that the coordinates of marginalia annotations link to the actual institutional scans.

### Linked Open Data (LOD) / Wikidata QIDs
**Linked Open Data** is a practice of publishing data on the internet in a way that uses universal identifiers instead of local names, so that databases from different institutions can link to each other. A **Wikidata QID** is one of those universal identifiers — every person, place, concept, and work has a unique code (e.g., Jabir ibn Hayyan is Q87382). If RenMagDB and HermeticDB both use Jabir ibn Hayyan's QID rather than just typing his name, they are automatically interoperable with each other and with every other LOD-compatible dataset in the world.

### Marginalia
Handwritten notes, marks, and drawings made by readers in the margins of books. The HPMarginalia project exists entirely to study the marginalia in copies of the 1499 *Hypnerotomachia Poliphili* — who wrote in the margins, what they wrote, and what that tells us about who read the book and how.

### Textual Transmission
The history of how a text changed as it was copied, translated, and reinterpreted over centuries. The Emerald Tablet, for example, existed in Greek, was translated into Arabic, was translated from Arabic into Latin, and each step introduced changes — some accidental, some deliberate. HermeticDB maps this transmission history. The DH methodological critique of HermeticDB is that SQLite flattens this into discrete rows, losing the ability to trace how a single mistranslation spawned an entirely new esoteric tradition.

### Diplomatic Transcription
Reproducing a historical text exactly as it appears in the original, preserving idiosyncratic spelling, abbreviations, and punctuation. The opposite is a normalized transcription, which updates spelling and punctuation for modern readability. The Newton Project (mentioned in `concept_prior_art.md`) provides both, with a toggle button. A DH project that silently normalizes without marking the changes is making an invisible editorial decision that affects how scholars can use the data.

---

## Part 7: Advanced Architecture Terms

### Federated Data Layer / `entities.db`
"Federation" means connecting multiple independent databases through a shared reference point instead of merging them into one giant database. The proposed `entities.db` would be a single file containing every canonical person, text, and concept across the entire catalog — one entry for Jabir ibn Hayyan, one for the Emerald Tablet. Every other database (HermeticDB, RenMagDB, AlchemyTimelineMap) would link to entries in `entities.db` by ID rather than spelling out names. When you click on Jabir ibn Hayyan in AlchemyTimelineMap, the app can pull his full profile from HermeticDB because they share the same ID.

### Graph Database (Neo4j)
A type of database designed for storing and querying *relationships* rather than tables. In a standard relational database (SQLite), you store rows and join them together. In a graph database, every piece of data is a *node* and the connections between pieces are first-class *edges* with their own properties. This makes queries like "show me the complete chain of translation from this Greek alchemical term to its Latin theological descendant" much more natural. The `architecture_new_directions.md` recommends considering Neo4j for the transmission arc queries in AlchemyTimelineMap, though it would break the zero-dependency static site architecture.

### Geospatial / GeoJSON
"Geospatial" data is any data that includes geographic coordinates (longitude, latitude). **GeoJSON** is the standard JSON format for encoding geographic shapes — a point, a line, or a polygon region. WitchcraftStudiesDB is the first geospatial project in this catalog, using GeoJSON to define the shapes of European witchcraft prosecution clusters and Leaflet.js to put them on an interactive map.

### DuckDB
A database engine optimized for analytical queries — aggregations, window functions, time-series calculations — rather than the transactional read/write operations that SQLite handles. Think of it as a high-speed calculator you attach to your SQLite data. The `architecture_new_directions.md` recommends DuckDB for running complex queries over the Megabase (like "how did my use of the word 'alchemy' change month by month over five years?") without replacing SQLite as the source of truth.

### Observable Notebooks
A browser-based coding environment similar to Jupyter notebooks, specifically designed for data visualization with D3.js. You write code in the browser, see the output immediately below each code block, and can share the whole notebook as a live URL. The new directions document recommends Observable as a prototyping environment for AlchemyTimelineMap's visualizations before committing to a full static HTML build.

### Svelte / SvelteKit
A frontend JavaScript framework that compiles your code at build time, producing smaller and faster output than React, which does more work in the browser at runtime. SvelteKit (the full-stack version) has excellent static site generation. Mentioned in `architecture_new_directions.md` as a lighter-weight alternative to Next.js for the scholarly portals.

### Materialized View
A database query whose results are pre-computed and stored, so you don't have to recompute them every time. For example, a query that finds every project that references Jabir ibn Hayyan across all six portals could be run once, stored as a JSON file at build time, and served instantly to the browser. The term is borrowed from enterprise databases; here it means "compute the expensive JOIN queries once during the build step, not every time a user loads the page."
