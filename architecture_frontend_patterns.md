---
title: "Architecture: Frontend Patterns & UI/UX Framework"
type: "concept"
tags: ["frontend", "design", "ui/ux", "relational_browsing"]
---

# Architecture: Frontend Patterns & UI/UX Framework

To ensure the DH Portals (The Cathedral) and Procedural Engines (The Dungeon Master) do not degrade into generic, visually flat webpages, the frontend framework must adhere to a strict set of design and structural patterns. The user experience must be immediately arresting—utilizing vibrant dark modes, sleek glassmorphism, and dynamic micro-animations—while maintaining absolute scholarly rigor.

This document outlines the required templates, style guides, and relational browsing rules for displaying complex academic data.

---

## 1. Core Aesthetic Principles (The "Wow" Factor)
The framework demands a highly polished, premium design language. A simple MVP interface is unacceptable for the final portals.

*   **Color Palettes:** Avoid default primary colors. Use deeply curated HSL gradients, dark slate backgrounds (e.g., `#0f172a`), and vivid accents (emerald, neon pink, or cyan) to highlight interactive elements.
*   **Typography:** Default browser fonts are prohibited. Use modern, highly readable sans-serif pairings like **Outfit** (for striking, bold headings) and **Inter** or **Roboto** (for dense scholarly body text).
*   **Micro-animations:** All interactive elements (cards, links, buttons) must feature subtle transitions (e.g., `transform: translateY(-2px)`, `box-shadow` expansion) to make the reading environment feel alive and responsive.
*   **Glassmorphism:** Use translucent backgrounds (`backdrop-filter: blur()`) with subtle borders to overlay context menus or modal cards over the core text.

---

## 2. Scholarly Data Cards (Templates)

The framework must provide pre-built, standardized templates for different ontological entities. These cards are the primary vehicle for delivering the database to the reader.

### A. The Biographical Card (Persons)
Instead of a generic Wikipedia-style biography, the Biographical Card must be structured to map intellectual lineage and conflict.
*   **Header:** Name, Lifespan, and a highly specific "Role/Epithet" (e.g., "Hermetic Philosopher" rather than "Writer").
*   **The "Lineage" Block:** Visual tags showing who this person influenced, and who influenced them.
*   **The "Scholarly Dispute" Section:** A dedicated block that explicitly names two or more scholars who disagree on this person's legacy. *Never synthesize the disagreement into a flat middle ground.*
*   **Citational Tethers:** Every claim in the biography must have a hovering `[1]` that links directly to the specific primary or secondary text in the database.

### B. The Dictionary/Concept Card
For tracking esoteric terminology, philosophical concepts, or alchemical reagents.
*   **Etymology & Origin:** A clean breakdown of the term's root.
*   **Definitions by Era:** A timeline view. How did the definition of "Ether" change from Aristotle to Newton?
*   **Relational Web:** A visual or tag-based list of texts in the database where this concept is centrally featured.

### C. The Scholarly Text Summary Card
Used for books, manuscripts, or essays.
*   **The "Diplomatic" vs. "Normalized" Toggle:** If displaying primary text, always provide a toggle between the raw, original transcription (Diplomatic) and a modernized, readable version (Normalized).
*   **The Argument:** A concise, undergraduate-level summary of the text's primary thesis.
*   **Marginalia/Annotations Pane:** A side-gutter where database annotations are pinned directly to specific paragraphs.

---

## 3. Relational Browsing (The User Experience)

The primary failure of legacy wikis is the "dead-end page" or the "lost tab" syndrome. The frontend framework must solve this through spatial navigation.

*   **No Dead Ends:** Every entity (person, text, concept) must link out to at least three other entities in the database.
*   **Side-Panel Previews (The "Peeking" UX):** When a user clicks a citation or a related concept, do *not* navigate away from the current page. Instead, slide open a side-panel (or an elegant glassmorphic modal) displaying the target Card. This allows the user to explore tangents without losing their place in the primary text.
*   **Visual Network Maps:** For complex portals (like QueryPat), integrate a canvas or SVG-based network graph where nodes represent entities and edges represent relationships (e.g., "Critiqued By," "Influenced").

---

## 4. Framework Integration Next Steps

To automate this within the `C:\Dev\framework` scaffolding CLI:
1.  **Component Library:** Build React/Vanilla HTML templates for the `BiographyCard`, `ConceptCard`, and `TextSummaryCard`.
2.  **CSS Reset & Variables:** Inject a master `index.css` into every new project that defines the dark-mode variables, typography imports, and animation utilities by default.
3.  **Link Routing:** Implement the side-panel logic at the framework level, ensuring that any `<a href="entity:...">` tag automatically triggers the preview pane rather than a hard page reload.

---

## Glossary for Undergraduates
*   **Relational Browsing:** Designing a website so that you never hit a "dead end." Every page acts as a crossroads pointing you to related ideas, much like falling down a Wikipedia rabbit hole, but structured specifically for academic research.
*   **Glassmorphism:** A modern web design trend that makes elements look like frosted glass. It allows the background to blur through the element, creating a sense of depth and hierarchy without feeling heavy or cluttered.
*   **Citational Tethers:** Our rule that a claim in the database cannot just float freely; it must be visually "tied" (tethered) to the specific book or document it came from, allowing the reader to instantly verify the source.
