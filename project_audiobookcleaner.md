---
name: project_audiobookcleaner
description: Turns scholarly PDFs into clean plain prose and MP3 audiobooks via a clean → translate → narrate CLI pipeline.
type: project
status: ACTIVE
tags: [audio, pdf, ocr, tts, python, pipeline]
---

# Project: AudiobookCleaner

**Location** · `C:\Dev\AudiobookCleaner` — **Type** · Python CLI batch tool — **Stack** · PyMuPDF + Tesseract OCR, langdetect + deep_translator, edge-tts + ffmpeg — **Verified** · `output/` populated across multiple corpora (in active use)

## What it is
A desktop pipeline converting scholarly PDFs into clean reading text and listening-ready MP3 audiobooks.

## Architecture
Three independent root CLI scripts, one per stage: `clean_audiobook.py` (PDF→text, OCR fallback), `translate_to_english.py` (optional non-English→English), `tts_audiobook.py` (text→MP3). `verify_outputs.py` audits the batch. Invokable via the `.claude/skills/audiobook-clean` skill; outputs under `output/`.

## Fragile parts
Hard constraint "never trim the beginning of main text" needs per-book `--start-heading` overrides; some monographs still leak TOC/publisher pages. Latin/Hebrew TTS quality poor (translate first). Tesseract path hardcoded to `C:\Program Files\Tesseract-OCR\tesseract.exe`. No tests/CI; correctness via runtime audit.

## Status & next
Working and in use (Dee, alchemy, Rampling corpora cleaned).

## Related
- [[project_audiobookapp]] — separate Android *player* (consumes audio); no code/data overlap, shares only the "audiobook" theme
- [[project_bookhistory]] — deterministic Epub/PDF ingestion lineage
