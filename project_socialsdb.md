# Project: SocialsDB

**Location**: `C:\Dev\SocialsDB`
**Type**: Personal Data Mining Hub

## Overview
A unified personal data mining hub that integrates conversations from Megabase, Claude Data, GPT Archive, and SMS archives into a single queryable system. 

## Architecture
- **Hub-and-Spoke Model**: Uses the existing Megabase schema (`C:\Dev\megabase\megabase.db`) as the central hub.
- **Satellites**: Various data sources (Claude Data, GPT Archive, SMS) feed into the hub via deterministic Python ingestors.
- **Constraints**: No LLM calls happen in the pipeline; all processing is deterministic Python and SQLite.
- **FTS5 Integration**: Uses SQLite FTS5 with custom triggers to automatically update search indexes (messages_fts and segments_fts) on insertions/updates/deletions.

## Scale
As of recent audits, it handles 5,271 conversations and nearly 4 million messages across 11 different source types (ChatGPT, Claude, Facebook, SMS, Google Chat, etc.).

## Related Entities & Concepts
- [[Dreambase (megabase)]]
- [[LLM Conversations as Primary Source]]
- [[Personal Knowledge Management]]
