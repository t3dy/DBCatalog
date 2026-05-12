# Project: Dreambase (megabase)

**Location**: `C:\Dev\megabase`
**Type**: Personal Knowledge Archaeology System

## Overview
A comprehensive system that unifies two years of LLM conversations, social media, email, and text messages into a single searchable SQLite database. It surfaces this data through curated scholar profiles, thematic collections, game design showcases, and public domain art galleries. The archive consists of 4,308 conversations and 3.9 million messages across 10 platforms.

## Core Content Themes
- Philip K. Dick (PKD)
- Game Design & Procedural Content Generation
- Digital Humanities
- Alchemy & Western Esotericism
- Kabbalah
- Marxist Economics
- Magic: The Gathering Analytics

## Architecture & Tech Stack
- **Database**: SQLite 3 with FTS5 for full-text search.
- **Web App**: Flask 3.x + Jinja2 (16 templates).
- **Processing**: Pure Python 3.10+ stdlib with minimal dependencies (PyMuPDF for PDF parsing).
- **Sentiment Analysis**: VADER (`vaderSentiment`) for compound sentiment scoring on all messages.
- **Zero API Cost Summarization**: deterministic extraction (first assistant response) or manual human-in-the-loop batch workflow (chunking into GPT window sizes, then structured responses are imported back).

## Key Subsystems
- **Ingestion**: 9 idempotent scripts to parse sources like ChatGPT (JSON), HTML/PDF exports, Claude SQLite, Gmail (streaming mbox), Facebook Messenger, Google Chat, SMS, Twitter, and PKD research chats.
- **Indexing (`index.py`)**: FTS5 indexing, VADER sentiment scoring, Keyword tagging (11 categories), Idea detection with maturity classification.
- **Chunk Export (`chunk.py`)**: Turns conversations into GPT-ready chunks of ~60K characters with message boundary preservation for context-heavy manual summarization.

## Related Entities & Concepts
- [[Personal Knowledge Management]]
- [[LLM Conversations as Primary Source]]
- [[Procedural Content Generation]]
- [[Philip K. Dick]]
- [[Game Design]]
- [[Western Esotericism]]
