# Idea: Static Site Generator for LLM Logs (The Protocol)

**Review Status**: VERIFIED
**Source**: Megabase Extract (2026-05-11)
**Extraction Lane**: dh_app_spec

## The Core Concept
A pipeline designed to export, parse, and format thousands of ChatGPT conversations into a structured static website (Jekyll/Hugo). This is the literal architectural precursor to our current DBCatalog and Prompt Archaeology methodologies. 

## Key Features
1. **Automated Markdown Export**: A script that intercepts the massive JSON data dumps from ChatGPT and parses them into individual `.md` files.
2. **Thematic Tagging**: Automatically applying frontmatter to conversations based on categories (e.g., tutorials, brainstorming, code generation) to allow for distant reading.

## Methodological Note (Q-Log)
This early app specification reveals the initial desire to escape the "walled garden" of the LLM interface. It proves that the drive to treat prompt history as a primary source (*Prompt Archaeology Value #4*) was present long before the formal `megabase` existed.
