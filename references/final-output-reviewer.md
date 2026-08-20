# Final TeX-to-PDF Visual Reviewer Contract

Run this review only after source-to-TeX content review is complete, shared interfaces are frozen, the full project builds successfully, bibliography and index tools have finished, and the candidate PDF hash has been recorded. Assign coherent chapters or continuous final-output ranges so that every physical output page has exactly one owner.

## Review inputs

Use only:

- the frozen final TeX project;
- the final compiled Chinese PDF rendered page by page at the project's QA resolution;
- the final build log, PDF hash, and page-range assignment.

Do not reopen the source PDF during this stage. Source fidelity was certified by the independent source-to-TeX review. Figure crop fidelity was certified separately during source-to-asset QA.

## Review focus

Compare every physical final-output page with the corresponding TeX structure and check:

- whether all TeX prose, displayed mathematics, theorem-like objects, proofs, lists, author footnotes, translator errata, captions, and bibliography or index material appear;
- signs, arrows, accents, subscripts, superscripts, delimiters, alignment, piecewise cases, and other mathematics whose compiled form may differ from its intended TeX;
- literal control-sequence text, malformed macro expansion, missing glyphs, replacement boxes, mojibake, or incorrect fonts;
- clipping, overlap, material overflow, abnormal spacing, unreadable scaling, bad page breaks, and orphaned headings or index parents;
- figure presence, scale, placement, and legibility in the book, without re-auditing the extraction crop against the source PDF;
- page headers, page numbers, chapter openings, part and appendix transitions, blank pages, table of contents, bookmarks, cross-references, bibliography, symbol list, and index page locations.

This is a rendering and assembly review, not a new translation review. Do not rewrite prose or reopen settled source-content decisions merely for style.

## Corrections and invalidation

- Record the exact output page, corresponding TeX file or construct, problem, and correction.
- After a local correction, rebuild and recheck the affected output page and adjacent pages. Expand the range when floats, footnotes, counters, references, or pagination move.
- A change to global fonts, geometry, theorem styles, shared macros, bibliography style, or index style invalidates all output pages materially affected by that change. Rerender and reinspect the appropriate range; use a complete rerun when the impact cannot be bounded reliably.
- Bind the completed record to the reviewed PDF's SHA-256. Any later PDF with a different hash is not covered unless the record explicitly documents the changed and rechecked ranges.

## QA record

Record every physical final-output page, allowing consecutive clean pages to be represented as compact ranges when the project still has deterministic coverage accounting. List every issue and recheck explicitly. Completion requires zero unassigned pages, zero unresolved rendering defects, and a PDF hash matching the reviewed artifact.
