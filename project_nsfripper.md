# Project: NSFRIPPER & NES Music Lab

## Overview
**Type**: Archive / Technical Reverse-Engineering
**Path**: `C:\Dev\NSFRIPPER`, `C:\Dev\NESMusicLab`

The NSFRIPPER ecosystem is dedicated to the strict, provenance-aware reverse-engineering of classic NES audio engines (specifically Konami's custom sound drivers for games like *Super C* and *Castlevania*). It also powers the automated pipeline that maps Bach MIDI compositions onto these extracted 8-bit instrument palettes.

## Architectural Notes
* **Tech Stack**: Python, 6502 Assembly Disassembly, REAPER Project Integration (.RPP).
* **The Anti-Hallucination Mandate**: When reverse-engineering Bank 12 of a Japanese NES ROM, there is zero tolerance for LLM hallucination. This project forces the LLM into a restricted Oracle interface, demanding line-by-line evidence and preventing "knowledge drift" when mapping hardware registers.
* **The Output**: Generates perfect, high-fidelity WAV files by bypassing speculative parsing and relying purely on trace-backed 6502 control logic.

## Integration with the Memory System
* **Methodology**: This project serves as the technical extreme of the Deckard Boundary. If an LLM cannot be trusted to guess the state of an APU register, it similarly cannot be trusted to guess the state of a game's inventory or the nuance of an academic debate.
* **Audience**: Serves the technical gamer, the musician, and the historian of early digital architecture.
