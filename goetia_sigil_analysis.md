---
title: Goetia Sigil Analysis
type: project-ontology
project: GoetiaRevEng
path: C:\Dev\GoetiaRevEng\
tags: [goetia, sigils, computer-vision, reverse-engineering, kabbalah, kamea, gematria, DH]
---

# Goetia Sigil Analysis — Ontology & Project Record

Computational reverse-engineering of the 72 demonic seals from the *Goetia of Dr. Rudd* (British Library Harley MS 6483 / Sloane MS 3825). The project treats the sigils as structured visual data and asks whether their construction can be explained by a formal process — specifically, whether they are traces on planetary magic squares (kamea) or assembled from a letter-grid grammar.

Repository: `C:\Dev\GoetiaRevEng\`
Dashboard: <https://t3dy.github.io/goetia-sigil-analysis/>

---

## Data Entities

### Sigil
The core unit of analysis. One record per spirit.

| Field | Type | Description |
|---|---|---|
| `id` | int 1-72 | Canonical Goetia ordering |
| `name` | string | Spirit name (e.g., "Bael", "Gusion") |
| `rank` | enum | King, Duke, Prince, Marquis, Earl, President, Knight |
| `planet` | string | Planetary attribution (Agrippa) — inferred from rank |
| `legions` | int | Number of legions commanded |
| `gematria` | int | Hebrew gematria of name (Agrippa transliteration) |
| `kamea_square` | enum | Hypothesised magic square: saturn_3x3, jupiter_4x4, mars_5x5, sun_6x6, venus_7x7, mercury_8x8, moon_9x9 |
| `sigil_file` | string | Filename of extracted PNG image |
| `bbox` | [x,y,w,h] | Bounding box in source image |

**Rank → Planet mapping (Agrippa):**
- King → Sun (6x6)
- Duke → Venus (7x7)
- Prince → Mercury (8x8)
- Marquis → Moon (9x9)
- Earl → Mars (5x5)
- President → Saturn (3x3)
- Knight → Saturn (3x3)

### AnalysisFeature
Per-sigil computed metrics. Multiple feature sets exist at different pipeline stages.

| Field | Source Script | Description |
|---|---|---|
| `ink_ratio` | 05 | Fraction of bounding box containing ink |
| `aspect_ratio` | 01 | Width/height ratio |
| `compactness` | 05 | Ink pixels / ink bounding box area |
| `fractal_dimension` | 05 | Box-counting FD (range 1.0-2.0; sigils: 1.16-1.55) |
| `horizontal_symmetry` | 05 | Pearson r vs horizontal mirror |
| `vertical_symmetry` | 05 | Pearson r vs vertical mirror |
| `radial_profile` | 05 | Ink density in 8 concentric annular bins |
| `quadrant_density` | 05 | Ink per quadrant [NW, NE, SW, SE] |
| `connected_components` | 02 | Disconnected pieces in skeleton |
| `skeleton_length_px` | 02 | Total skeleton pixel count |
| `junctions` | 02/03 | Branch points (>2 skeleton neighbours) |
| `endpoints` | 02/03 | Terminal tips (1 skeleton neighbour) |
| `holes` | 02 | Enclosed regions (contour hierarchy) |
| `euler_number` | 02 | Components minus holes |
| `junction_endpoint_ratio` | 02 | Branching density metric |
| `n_lines` | 04 | Hough line count |
| `n_circles` | 04 | Hough circle count |
| `dominant_angle` | 04 | Dominant line orientation (degrees) |
| `angle_histogram` | 04 | 12-bin histogram 0-180° |
| `fourier_descriptors` | 12 | 160-dim rotation/scale/translation-invariant fingerprint |

### Cluster
8 structural families identified by Ward hierarchical clustering on the 38-dim feature matrix.

| Cluster | Name | n | Signature |
|---|---|---|---|
| 1 | Sparse Minimalists | 9 | Low FD (avg 1.16), few junctions, open designs |
| 2 | Spread Networks | 22 | Moderate complexity, 75° preference, "antler" forms |
| 3 | Circuit Loops | 6 | Highest FD (1.55), most holes (avg 10.8), grid-like |
| 4 | Diagonal Stars | 2 | 45°/120° diagonals, high horizontal symmetry |
| 5 | Mixed-Angle Composites | 14 | 150°/15° angles, organic/curvilinear |
| 6 | Wide Horizontals | 3 | Aspect ratio >1.8, strong 0° emphasis |
| 7 | Unified Verticals | 15 | Few components (avg 12), 90° spine, totem-pole form |
| 8 | Outlier (Zepar) | 1 | 3:1 aspect ratio, peripheral ink density |

### PrecedentImage
Cross-corpus comparanda from other manuscript traditions.

| Field | Description |
|---|---|
| `source` | Manuscript / tradition (e.g., "Sefer Raziel", "Clavicula Solomonis") |
| `image_path` | File path |
| `cosine_dist` | Fourier descriptor distance to matched Goetia sigil |
| `matched_sigil_id` | Best matching Goetia spirit |

Cross-corpus data: `cross_corpus_features.json`, `cross_corpus_distances.json`

### GridScore
Output of the grid-construction analysis pipeline (scripts 27-31).

| Field | Source | Description |
|---|---|---|
| `gridness_score` | 27 | Regularity of vertex positions on a grid |
| `best_waypoint_fit` | 28 | Best alignment of skeleton waypoints to kamea cells |
| `best_angle_coverage` | 29 | Fraction of lines at grid-consistent angles |
| `hausdorff_dist` | 30 | Hausdorff distance: theoretical kamea path vs actual skeleton |
| `nn_dist` | 30 | Mean nearest-neighbour distance, same comparison |
| `best_orientation` | 30 | Best isometry index (0-7) for theoretical path alignment |
| `composite_score` | 31 | Weighted combination (see formula below) |
| `classification` | 31 | "likely grid-constructed" / "possible" / "unclear" |

**Composite score formula:**

```
composite = 0.20 * norm(gridness)
          + 0.30 * norm(best_waypoint_fit)
          + 0.30 * norm(best_angle_coverage)
          + 0.20 * (1 - norm(hausdorff_dist))
```

Classification thresholds: >0.7 = likely, 0.4-0.7 = possible, <0.4 = unclear.

---

## Key Relationships

```
Sigil --hasFeature--> AnalysisFeature
Sigil --belongsTo--> Cluster
Sigil --hasGridScore--> GridScore
Sigil --matchedBy--> PrecedentImage (via Fourier / template distances)
GridScore --derivedFrom--> AnalysisFeature
Cluster --characterisedBy--> AnalysisFeature (z-score profiles)
```

---

## Construction Method Hypotheses

### H1: kamea_path
The sigil is a traced path on a planetary magic square, connecting cells whose values encode the spirit's name in gematria. The standard method (attested in Agrippa, *Three Books*, Book II; and in the Rose Cross tradition via Golden Dawn documents) is:

1. Convert spirit name to Hebrew letters via standard letter substitution
2. Assign each letter its gematria value
3. Locate each value on the appropriate kamea grid
4. Connect cells in order with a continuous line
5. Mark start with a circle, end with a crossbar

**Evidence for:** Strong orthogonal/grid bias in line orientations (Hough analysis, Script 04). The Hough angle histogram shows massive 0° and 90° peaks across the corpus.
**Evidence against:** The sigils' high disconnected-component counts (mean 18) are inconsistent with a single continuous kamea trace. A pure kamea path produces one connected stroke.
**Verdict:** Likely applies to a minority subset; Cluster 3 (Circuit Loops) is the strongest candidate group.

### H2: letter_grid
The sigil is constructed by overlaying the spirit's name letters on a grid — each letter occupies a cell and lines connect sequential letters. Variants include the Aiq Bekar (Qabalistic Cipher) letter-square and the Rotas/Sator square.

**Evidence for:** The modular assembly (mean 18 components) is consistent with per-letter strokes being drawn separately.
**Evidence against:** No single letter-grid orientation has been found that aligns well with the actual sigil geometry.
**Verdict:** Plausible for component structure; needs explicit grid-matching test (Script 28 target).

### H3: freehand_scribal
The sigils are scribal inventions with no formal construction rule — accumulated over copying generations, each scribe introducing variation, stylisation, or error.

**Evidence for:** Increasing component count and line count with sequence position (Scripts 14) — consistent with scribal elaboration over time. Near-identical pairs (Vine/Bifrons at adjacent positions) could indicate direct copying.
**Evidence against:** The orthogonal grid bias is too consistent across all 72 to be accidental. The terminal-decoration vocabulary (5 types) is too constrained.
**Verdict:** Partial — accounts for divergence from strict construction rules but cannot explain the geometric regularity.

### H4: corrupted_kamea
A kamea-path original has been degraded through copying: strokes misconnected, omitted, or merged; terminal decorations added or changed; grid offset shifted. The "true" path is present but recoverable only statistically.

**Evidence for:** The Hausdorff distances between theoretical and actual paths (Script 30) cluster rather than scatter randomly — some sigils are much closer to their theoretical path than others.
**Evidence against:** Corruption alone cannot explain the consistent modular structure (18 components implies deliberate multi-part construction, not degraded single traces).
**Verdict:** Likely applies to Cluster 2 (Spread Networks) where paths are partially recoverable.

---

## Data Files

| File | Contents | Producing Script |
|---|---|---|
| `sigil_metadata.json` | id, name, bbox, file, aspect_ratio, grid position | 01 |
| `skeleton_analysis.json` | components, skeleton_length, junctions, endpoints, holes, euler_number | 02 |
| `junction_analysis.json` | per-sigil junction/endpoint locations and terminal type counts | 03 |
| `hough_analysis.json` | n_lines, n_circles, dominant_angle, angle_histogram | 04 |
| `features.json` | full 38-dim feature vector per sigil | 05 |
| `cluster_assignments.json` | cluster ID per sigil | 06 |
| `demon_metadata.json` | rank, legions, appearance, abilities, element | external |
| `graph_analysis.json` | node/edge counts, spectral fingerprints | 10 |
| `learned_grammar.json` | generative model parameters | 11 |
| `fourier_descriptors.json` | 160-dim Fourier fingerprints | 12 |
| `template_matching.json` | shared motif counts and co-occurrence matrix | 13 |
| `historical_ordering.json` | Spearman/Kendall correlations, CUSUM, autocorrelation | 14 |
| `cross_corpus_features.json` | features for comparanda from other traditions | 25 |
| `cross_corpus_distances.json` | pairwise distances between Goetia and comparanda | 25 |
| `stroke_vocabulary.json` | primitive stroke types and frequencies | 26 |
| `gematria_path_scores.json` | hausdorff_dist, nn_dist, theoretical path per sigil | 30 |
| `grid_analysis_summary.json` | composite score, classification (output of full pipeline) | 31 |

---

## Current Analysis Findings Summary

### Geometric Structure (confirmed)
- Dominant angle bias: 0° (28.7%) and 90° (19.8%) — the sigils are built on an orthogonal grid
- Terminal decoration vocabulary: 5 types; simple bare endings dominate (81.2%)
- Centripetal organisation: dense centre, sparse periphery (radial profile)
- Mean 18 disconnected components per sigil (range 3-47) — modular assembly, not single strokes

### Clustering (REVISED by Script 24 — discrete families NOT supported)
- Cluster validation (silhouette, Davies-Bouldin, gap statistic, k=2–15) found all silhouette scores < 0.20
- The original k=8 partition is not supported by the data; the corpus is a **continuum**, not discrete families
- Cluster labels are retained in the UI only as visual neighborhoods, not as established taxonomy
- Earlier observations (Circuit Loops coherence, Zepar outlier) remain valid as descriptions of regions of the continuum

### Textual Independence (confirmed)
- Rank, legions, and Goetia ordering are all statistically independent of sigil complexity
- The sigils do not encode textual metadata visually
- Implication: the sigils derive from a separate visual-constructive tradition, not from illustrative representation

### Historical Ordering (partial)
- n_lines, n_circles, and components all increase with sequence position (p < 0.05)
- But composite complexity shows no overall trend (rho=0.013)
- Scribal variance increases toward the end of the sequence
- No autocorrelation between adjacent sigils — not batch-produced in sequence

### Template Sharing (confirmed)
- 46 unique shared motifs across the corpus
- Amon (#7) shares motifs with 20 other sigils — most "generative" design
- Top co-occurring pair: Amon (#7) & Shax (#44) — 12 shared motifs despite 37-position separation

### Grid Construction Testing (Scripts 27-31, CALIBRATED by Script 32)
- Raw results (31): 1 "likely" (Gusion #11, 0.877), 48 "possible", 23 "unclear"; Venus 7×7 most common best-fit
- **Script 32 null-model calibration** (210 synthetic kamea walks + 210 freehand scribbles, identical instrument chain):
  - Instrument validity: gridness metric separates true kamea walks from freehand at AUC = 0.957 — the instrument works
  - **Venus result falsified**: freehand scribbles score ≥98% angle coverage on Sun/Venus/Mercury/Moon squares; the
    Venus "wins" were artifacts of grid density. Only Saturn 3×3 (AUC 1.0), Jupiter 4×4 (0.99), Mars 5×5 (0.88) coverage discriminates
  - Corpus verdict: real mean gridness (0.509) sits at the **94th percentile of the freehand null** but only the
    **26th percentile of true kamea walks** — more angularly structured than scribbles, less than genuine grid-tracing
  - 32/78 sigils individually exceed the null at p<0.05 (chance expectation: ~4)
  - Caveat: the null models smooth curves; ruled straight-line drawing without a grid would also beat it.
    Exceeding the null is consistent with kamea use but does not demonstrate it
- Honest framing for the site: the grid hypothesis is **neither supported nor refuted**; the corpus shows real angular
  structure intermediate between freehand and grid-traced. Next discriminating test: letter-corruption competing model
- Data files: `calibrated_grid_scores.json`, `calibration_summary.json`, `calibration_distributions.png`, `synthetic_samples.png`

---

## Cross-References

- [Renaissance Magic DB](project_renaissancemagic.md) — related corpus of esoteric visual symbols
- [Emerald Tablet Portal](project_emeraldtablet.md) — overlapping Hermetic textual tradition
- [AtalantaClaudiens](project_claudiens.md) — Maier's emblematic tradition; analogous DH methodology
