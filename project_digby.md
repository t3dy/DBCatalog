# Project: Digby Game & Almagest Showcase

## Overview
**Type**: Procedural Engine (The Laboratory)
**Path**: `C:\Dev\digby-game`

The Digby Game is a highly interactive Digital Humanities engine focused on the life, esoteric theories, and philosophical world of Sir Kenelm Digby. It moves beyond static reading environments by building an LLM-driven "Dungeon Master" layer on top of a rigidly defined historical ontology.

## Architectural Notes
* **Tech Stack**: TypeScript, React, Local JSON Ontologies.
* **The Deckard Boundary**: This project is the primary testbed for enforcing the boundary between generative text and immutable game state. The LLM is restricted to generating narrative and describing rooms based on Digby's actual texts (e.g., *The Powder of Sympathy*), while a deterministic TypeScript engine manages the `reagents`, `commodities`, and `locations`.
* **The "Laboratory" Model**: This project realizes the DH mandate to let users *play* with historical concepts. It bridges the gap between the Academic Researcher and the Occult Practitioner by allowing active experimentation with alchemical rulesets.

## Integration with the Memory System
* **Data Provenance**: The JSON ontologies driving this game (`reagents.json`, `scenes.json`) must be consistently cross-verified against the academic texts housed in `RenMagDB`.
* **Audience**: Perfectly serves the Gamer and the Practitioner, bringing high-cultural 17th-century science into an accessible, interactive format.
