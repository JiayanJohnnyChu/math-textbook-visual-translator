# Mathematical Textbook Visual Translator

A Codex skill for translating complete mathematical textbooks and lecture notes from visually rendered PDF pages into faithful Chinese LaTeX projects.

The workflow is designed for long-form mathematical material where formulas, proofs, figures, footnotes, errata, and back matter must be preserved without summarization or silent rewriting.

## Core guarantees

- Transcribes directly from 200 dpi page images.
- Does not use the PDF text layer, OCR, or extracted text unless the user explicitly permits it.
- Assigns coherent whole chapters to chapter-scale subagents.
- Uses a TeX-only self-QA pass by the translator and one independent page-by-page visual QA pass by another subagent.
- Preserves proof structure, hypotheses, quantifiers, notation, numbering, and references.
- Keeps source errors in the body and records proposed corrections in identified translator's notes.
- Reuses extracted or cropped source figures instead of redrawing complex figures in TikZ.
- Builds a unified LaTeX environment for the specific book and tests it on representative material before freezing shared interfaces.
- Excludes later aesthetic redesign, cover work, and typography experiments.

## Installation

Clone the repository into your personal Codex skills directory:

```powershell
git clone https://github.com/JiayanJohnnyChu/math-textbook-visual-translator.git `
  "$env:USERPROFILE\.codex\skills\math-textbook-visual-translator"
```

Or download the repository and copy its root folder to:

```text
~/.codex/skills/math-textbook-visual-translator/
```

The folder must contain `SKILL.md` at its root.

## Usage

Invoke the skill explicitly:

```text
Use $math-textbook-visual-translator to translate this mathematical textbook PDF into a faithful Chinese LaTeX project.
```

The skill is also eligible for automatic discovery when a request clearly asks for complete, visual-only mathematical textbook translation.

## Requirements

- A Codex environment with subagent support.
- Python 3 for the included helper scripts.
- Poppler's `pdftoppm` on `PATH` for `scripts/render_source_pdf.py`.
- A suitable LaTeX distribution selected for the concrete translation project.

The skill deliberately does not prescribe a fixed `main.tex`, preamble, engine, font family, or book design. The integrator establishes and tests a unified environment appropriate to each source book before chapter translation begins.

## Repository contents

- `SKILL.md` — core routing and workflow instructions.
- `references/translation-contract.md` — fidelity, errata, figures, and layout rules.
- `references/chapter-worker.md` — whole-chapter translation subagent contract.
- `references/chapter-reviewer.md` — independent reviewer contract.
- `scripts/render_source_pdf.py` — deterministic 200 dpi page rendering helper.
- `scripts/check_page_coverage.py` — source-page marker coverage checker.
- `agents/openai.yaml` — Codex interface metadata.
