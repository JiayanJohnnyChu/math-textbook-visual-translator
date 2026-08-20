# Whole-Chapter Translation Subagent Contract

Give this contract to a chapter subagent together with the chapter number, physical source-page range, target file, and frozen glossary.

## Ownership

You own one complete chapter or one clearly defined front- or back-matter unit. You are not alone in the codebase: do not revert other agents' edits, and adapt to shared interfaces already committed to the workspace.

Modify only:

- the assigned chapter `.tex` file;
- the chapter's translation QA record;
- the chapter-specific figure directory only when the task explicitly assigns it to you.

Do not modify `main.tex`, the shared preamble, global glossary, central `ERRATA.md`, other chapters, shared scripts, or build configuration. Record requests for shared macros, terminology decisions, or cross-chapter labels in the chapter QA.

## Work requirements

1. Read the project's `TRANSLATION-CONTRACT.md` and `GLOSSARY.md` in full.
2. Open the assigned 200 dpi page images in physical-page order. Do not use the PDF text layer, OCR, `pdftotext`, or extracted text.
3. Write the chapter guide when required and identify it explicitly as translator-added.
4. Translate all prose, formulas, theorem-like objects, proofs, lists, author footnotes, captions, and references without summarizing, compressing, or rewriting proofs.
5. Insert one clear `% SOURCE_PDF_PAGE: n` tracking marker for every physical page and record blank pages in QA.
6. Preserve source errors in the body. Add a stable-ID `\SourceErratum` and record its source page and evidence in QA.
7. Call existing extracted figures. If an asset is missing, record the expected file, source page, and figure number; do not redraw it in TikZ.
8. Run feasible isolated static checks or a chapter build. Do not run a full-book build concurrently from the shared project root. Use targeted compiled smoke tests for new macros, complex mathematics, figures, footnotes, or other constructs whose rendering is not obvious from TeX.

## TeX-only QA deliverable

After completing the draft, inspect the resulting TeX from beginning to end without reopening every source-page image solely for QA. This is a structural and implementation review, not a second visual transcription pass. Do not create a page-by-page visual QA table for the translator, and do not perform an exhaustive visual sweep of the provisional compiled chapter. The authoritative output-page review occurs only after content freeze and the final full build.

Record:

- source-page marker coverage, including missing, duplicate, out-of-range, and intentionally blank pages;
- chapter, section, numbered-equation, theorem-like object, proof, author-footnote, and figure inventories derived from the TeX;
- unbalanced environments or delimiters, duplicate or unresolved labels, broken references, missing figure paths, malformed macros, and duplicate erratum IDs;
- every erratum candidate, new terminology request, shared-macro request, and cross-chapter label not yet available;
- static-check, isolated-build, compilation-warning, missing-glyph, and material-overflow status.

Report completion only after every assigned source page has been viewed during transcription, all content has been committed to the chapter, and the TeX-only QA pass is complete. A different reviewer owns the exhaustive source-to-TeX comparison; final-output reviewers later own the exhaustive final TeX-to-PDF comparison.
