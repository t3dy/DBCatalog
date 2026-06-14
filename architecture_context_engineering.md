---
title: "Architecture: Progressive Context Engineering"
type: architecture
description: "A layered strategy for revealing only the minimum necessary portal context to the LLM at each step."
tags: [context-engineering, retrieval, modularity, llm-workflow, architecture]
---

# Architecture: Progressive Context Engineering

This portal should not require the model to load the entire Illuminatus and RAW universe at once. The system must reveal context in layers, starting from stable global rules and moving only as far into the archive as a task requires.

The principle is simple: **card first, page second, source packet last**.

## 1. Context Layers

### Layer 1: Stable System Rules
Load this layer for every task.

- editorial voice
- card/page split
- placeholder protocol
- source discipline
- interpretive caution

### Layer 2: Project Scope
Load only the relevant project area.

- Illuminatus narrative atlas
- RAW biography/bibliography
- esoteric crosswalks
- map interaction rules

### Layer 3: Section Packet
Load only the section type being edited or generated.

- character
- concept
- plot summary
- routine
- location
- RAW book
- RAW media item

### Layer 4: Entity Packet
Load only the specific entity or page being worked on.

Examples:
- one location card
- one RAW title page
- one character page
- one interview record

### Layer 5: Source Packet
Load the smallest possible source set needed to write the entry.

Examples:
- a chapter excerpt
- a bibliography record
- a scan transcript
- a single web page
- a brief note from an archive

## 2. Retrieval Order

When generating or revising content, use this order:

1. Identify the user task.
2. Determine the relevant section type.
3. Pull the minimum entity packet.
4. Pull only the source packet needed to support the entry.
5. Draft the card.
6. Expand to the page only if the task asks for deeper coverage.
7. Add placeholders instead of inventing missing archive data.

## 3. Progressive Reveal Rules

- Do not load full book summaries if the task only needs a card.
- Do not load all RAW media if the task only concerns one interview.
- Do not load all location pages when writing one location note.
- Do not load esoteric background except for the exact terms in view.
- Do not ask the model to synthesize the entire portal before it has a stable card-level map.

## 4. Prompt Packaging

Each generated prompt should be assembled from compact modules:

- `system`: global editorial rules
- `project`: Illuminatus or RAW scope
- `section`: the exact entry type
- `entity`: the one page or card being edited
- `sources`: only the needed references
- `task`: what to produce

This keeps the context readable, auditable, and cheap.

## 5. Best Practices

- Prefer many small prompts over one giant prompt.
- Prefer entity-specific packets over chapter dumps.
- Prefer source snippets over whole documents.
- Prefer stable summary cards over repeated long-form reasoning.
- Prefer cached summaries for known entities and raw source packets only when needed.

## 6. Failure Modes To Avoid

- Monolithic prompts that combine biography, bibliography, map design, and esoteric theory
- Long context windows filled with unrelated pages
- Blind summarization of archive material without source attribution
- Rewriting stable cards when only one page needs expansion
- Inventing bibliographic precision when the source is incomplete

## 7. Editing Workflow

The recommended workflow for this portal is:

1. Build or edit the card.
2. Confirm the card is source-grounded.
3. Expand to the page.
4. Add section-specific subheadings.
5. Add cross-links.
6. Add source notes and placeholders.
7. Only then widen the context to adjacent entities.

This is how the system stays scalable while still feeling richly interconnected.

