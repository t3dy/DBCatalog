# Project: MarxistPortal

**Location**: `C:\Dev\MarxistPortal`
**Type**: Curated Educational Website

## Overview
A companion website to the Capital RAG project providing a curated, guided tour of the Marxist intellectual tradition. It features a dictionary of terms, chronological biographical profiles (Who's Who), and an analysis section that examines 21st-century issues through four distinct Marxist theoretical lenses.

## Theoretical Lenses
The portal explicitly models interpretation across four distinct traditions:
1. **Classical Marxism** (Marx, Engels, Lenin, Luxemburg)
2. **Value-Form Theory** (Heinrich, Rubin)
3. **Geographical Materialism** (Harvey)
4. **Structuralist Marxism** (Althusser)

## Architecture
- **Stack**: Node.js build step → JSON data → Vanilla HTML/JS with Tailwind CSS.
- **Data Model**: Content lives as Markdown files with YAML frontmatter in `content/` (thinkers, texts, terms, analyses), which is compiled into `data/` at build time.

## Related Entities & Concepts
- [[Marxism]]
- [[Capital RAG]]
- [[Value-Form Theory]]
