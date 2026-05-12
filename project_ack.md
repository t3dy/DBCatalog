# Project: Almagest Construction Kit (ACK)

## Overview
**Type**: RAG System / Procedural Ideation Toolkit
**Path**: Distributed (Components integrated into `digby-game` and Prompt Archaeology pipelines)

The Almagest Construction Kit (ACK) is a highly localized Retrieval-Augmented Generation (RAG) system designed to act as an automated ideation partner for the creator. It functions similarly to NotebookLM but is strictly governed by the local ontologies and the Deckard Boundary of the DH Framework.

## Architectural Notes
* **Components**: Features specialized agents such as the *Narrative Sculptor* and *Market Sculptor*.
* **Document Ingestion**: Automates the uploading and chunking of complex PDFs (e.g., scholarly texts, historical biographies like Kenelm Digby's) to act as grounding contexts for LLM generation.
* **Significance**: The ACK bridges the gap between passive reading (Knowledge Portals) and active generation (Procedural Engines) by turning static primary sources into actionable game design documents and application architectures.

## Integration with the Memory System
This represents the "brain" that feeds the `megabase`. By loading a historical text into the ACK, the user can generate thousands of tokens of ideation, which are then saved, parsed, and eventually retrieved by the `wiki_extractor.py`.
