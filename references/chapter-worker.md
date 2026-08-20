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
8. Run feasible isolated static checks or a chapter build. Do not run a full-book build concurrently from the shared project root.

## QA deliverable

Include at least one row for every physical source page:

| Source physical page | Prose | Mathematics | Theorem/proof | Footnote/figure | Status |
|---:|---|---|---|---|---|

Also record:

- chapter, section, numbered-equation, theorem-like object, proof, author-footnote, and figure inventories;
- every erratum candidate;
- new terminology and shared-macro requests;
- cross-chapter references and labels not yet available;
- static-check, isolated-build, and compiled-output review status.

Report completion only after every assigned source page has actually been viewed and committed to the chapter and QA record.
