# Faithful Translation Contract

Read this file before translating any chapter. Keep the project's `TRANSLATION-CONTRACT.md` consistent with the user's requirements; explicit user instructions take precedence.

## Visual source

- Transcribe only from 200 dpi page images rendered from the locked source PDF. Do not use the PDF text layer, OCR, extracted text, or search results as a transcription source.
- Open every physical page directly. Contact sheets may assist navigation but cannot replace page-by-page viewing.
- Place `% SOURCE_PDF_PAGE: <physical page>` near the corresponding content. The marker tracks coverage and must not control Chinese output pagination.
- Record intentional blank pages, part separators, and appendix separators as well.

## Text and proofs

- Translate every title, paragraph, definition, theorem, proposition, lemma, corollary, conjecture, example, remark, proof, list, author footnote, and caption.
- Preserve paragraph order, argumentative order, and proof steps. Do not summarize, compress, paraphrase, modernize, or substitute another proof.
- Adjust word order only as Chinese grammar requires. Do not alter hypotheses, quantifiers, negation, logical strength, object order, or conclusions.
- Preserve formulas, numbering, notation, and cross-references. Record a visual uncertainty instead of guessing.
- Preserve bibliography authors, original titles, journals, and publication data; translate only explanatory prose when applicable.

## Mathematical Chinese

- Use the academic register customary in Chinese mathematical textbooks. Accuracy takes priority over rhetoric.
- Follow the frozen project glossary from first occurrence onward. Do not vary terminology merely for stylistic variety.
- Do not add explanations, historical background, or modern results absent from the source.
- Preserve the strength of proof headings, exceptional cases, and logical connectives such as “clearly” or “it is immediate.”

## Chapter guides

- Add guides only when requested, and mark them explicitly as translator-added.
- Explain the objects studied, main questions, tools, motivation, and relation to adjacent chapters.
- Let length follow the chapter's needs; do not enforce a mechanical word count.
- A guide must not replace the author's introduction or assert results the chapter does not establish or discuss.

## Source errata

- Preserve the source form in the main text; never silently correct it.
- Insert a translator's erratum footnote with a stable ID at the original location and copy it into `ERRATA.md`.
- Call an issue definite only when supported by a direct internal contradiction, uniquely wrong numbering, a missing term, or a uniquely determined correction.
- Use “likely should read” for well-supported but non-unique corrections and “requires verification” when the correction cannot be determined.
- An independent reviewer may reject an unsupported erratum candidate but must record the reason.

Suggested interface:

```tex
\SourceErratum{E-03-004}{
The source reads ... here. In light of the preceding definition and the later
calculation, this likely should read ... . The body retains the source form.
}
```

## Figures and layout

- Prefer extraction of an independent vector Form/XObject, then vector cropping from the page content stream, and use a page screenshot only as a last resort.
- Do not redraw complex figures, commutative diagrams, or schematics in TikZ. Existing English or mathematical labels may remain when the user permits it.
- Render each recovered figure asset and visually compare it once with the figure on its source PDF page. Record crop, line, label, transparency, and completeness status in the figure manifest before content freeze.
- Translate captions and all explanatory prose referring to figures.
- Do not reproduce source line breaks or page breaks, and do not add forced page breaks corresponding to source pages.
- Establish only a clear, stable, compilable baseline layout. Aesthetic redesign is outside this skill.
