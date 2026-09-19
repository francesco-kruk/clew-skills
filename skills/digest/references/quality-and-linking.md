# Quality, linking, and portability reference

## Default and optional structures

This reference is self-contained for portable Markdown. No other skill, vault,
app, graph, or course package is needed. Apply coverage, fidelity, reporting, and
preservation gates to every output mode. Apply integration-specific gates only
when that output is explicitly requested; see
[optional integrations](optional-integrations.md). For an explicit legacy Clew
export, installed `course-content` owns the structure; "index" in the gates below
means its canonical hub. Portable output need not conform to that legacy package contract to be read
by student Clew; default reading accepts the copied Markdown bundle as-is.

Digest is the editable conversion/recovery route. The separate optional
`content-ingest` skill retains the image-first workflow. Do not apply digest's
editable-prose requirements to erase that route or call an image-first result a
verified editable transcription. If the requested image-first skill is not
installed, report that limitation instead of silently changing routes.

## Portable bundle structure

```text
Book-Markdown\
  index.md
  01-first-section.md
  02-second-section.md
  answers.md
  assets\
    book-figure-01.png
  sources\
    book-original.pdf
  reports\
    conversion-manifest.json
    verification.json
```

Names and counts are illustrative, not a fixed schema. Include `answers.md` only
for a separate source answer key; keep in-chapter answers in their chapter.
Include the original PDF only when authorized for reproduction/distribution.
For a short paper, the complete transcription may live in `index.md`; for a long
document use actual chapters/major sections, with subsection notes only when useful.
Do not create empty asset folders, concept graphs, Canvas files, or course metadata.

Preserve source section identifiers in headings even when filenames are sanitized.
Prefer simple lowercase, hyphenated filenames and deterministic names. Use
Windows-safe filenames without reserved device names, trailing periods/spaces,
control characters, or `<>:"/\|?*` within a filename. Avoid `#`, `%`, `^`, `[` and
`]` in names to reduce link ambiguity. Apply the naming policy before creating links.
Check names case-insensitively, including collisions with existing destination
notes when authorized access to the destination is available.

## Portable Markdown links and source references

- Link notes using explicit relative `.md` paths: `[First section](01-first-section.md)`.
  Paths resolve from the containing note, not a vault root or the current working
  directory. A nested note links back with `[Index](../index.md)`. Do not use
  wikilinks, basename search, absolute paths, drive letters, or `file:` URLs.
- Markdown URLs use `/` separators on every platform; Windows filesystem commands
  use `\`. Encode path components when necessary: `[Notes](Chapter%20One.md)`.
  Keep separators and fragments intact; do not encode the entire URL as one name.
- Use actual headings and predictable GitHub-style slugs, such as
  `[Exercise 3](02-second-section.md#exercise-3)`. Prefer unique, simple headings
  over punctuation-heavy or duplicated titles; preserve the original heading text
  when needed and verify the viewer's anchor convention. CommonMark does not define
  heading IDs. Report viewer-specific limitations rather than claiming universal
  anchor support; whole-note links remain portable.
- Use `![Descriptive figure text](assets/book-figure-01.png)` with a nearby source
  caption. Keep labels, axes, legends, and captions in the crop; alt text is not
  a substitute for the source figure. Never replace ordinary prose with images.
- When the PDF is included, cite
  `[PDF page 7](sources/book-original.pdf#page=7)`. Physical page numbers are
  one-based; printed labels belong in caption text separately. Some viewers ignore
  PDF page fragments, so always keep the visible page number.
- If redistribution is not authorized, omit the PDF and its file links. Use
  visible citations such as `Source: Book.pdf, physical PDF page 7 (printed p. 3)`
  plus the manifest's source hash and region mapping. Never emit a broken local
  source link or an absolute path to the author's computer.
- Place citations near sections/items, equations, figures, and fallback crops.
  If a note spans several pages, map its sections/regions rather than attaching
  an unqualified whole-document citation to everything.
- Retain original external citations as external links; do not fetch them merely
  because they are in the PDF. Link supplied answers both ways, retaining exercise
  IDs and subparts. Explain genuine cross-references without inventing relationships.

Optional portable concept notes/maps use these same link rules. Mark any synthesis,
link it to exact source locations, omit empty template sections, and never replace
or duplicate the full transcription with concept summaries.

## Source coverage manifest

Maintain structured fields equivalent to:

- Source filename, SHA-256, total physical pages, and printed-page mapping.
- Each section's stable ID, note path, source pages, and boundary rectangles where
  pages are shared. Do not assume a constant cover-page offset.
- Each page's classification and review state, including deliberately omitted blank
  pages or repeated running headers with a reason.
- Example/exercise/answer identifiers, subpart counts, and destination headings.
- Each figure or fallback's asset path, physical page, crop rectangle, caption,
  and whether it is an original raster, rendered vector crop, or untranscribed region.
- Unresolved fidelity issues and clearly labeled source-error annotations.

Every source page must be accounted for, but coverage is not merely a count of page
images. A page assigned to a note is not proof that its content survived.

## Required acceptance gates

### Fidelity

- Compare every section with its source. Verify no prose, meaningful footnotes,
  tables, examples, exercise subparts, or supplied answers disappeared at boundaries.
- Check formula semantics, not just balanced delimiters: signs, denominators,
  radicals, superscripts, limits, domains, units, and rounding.
- Preserve legible source crops for unresolved math. Caption the limitation.
- Check diagrams for clipped labels, legends, arrows, axes, and missing captions.
- Scan for `(cid:...)`, replacement characters, NULs, mojibake, repeated headers,
  meaningless tables, and unreplaced generation placeholders. Investigate matches;
  do not delete them indiscriminately.
- Check balanced math delimiters outside code and escaped literals. Parser success
  is only structural evidence, not proof of mathematical accuracy.
- Do not silently "fix" a source answer to agree with a derived answer. Preserve the
  original, explicitly annotate a verified discrepancy, and retain its source link.

### Links and navigation

- Parse Markdown inline/reference links and images, ignoring fenced and inline
  code. Resolve decoded local paths relative to each containing note. Reject
  missing files, case mismatches, collisions, and paths escaping the delivered
  bundle. Relative `..` segments are valid only when the resolved target stays
  within it. Classify external citations separately; do not fetch them.
- Check actual target headings against the declared slug convention. Do not
  accept a fragment merely because its file exists.
- Validate PDF page fragments against the PDF's page count; check every embed exists.
- Ensure every reader-facing note is reachable from the index. Each authored concept
  needs a source chapter link and a meaningful inbound link, with concept-to-concept relationships
  where supported. For course exports, check the hub's ordered chapter inventory,
  required metadata, and chapter backlinks using `course-content`; optional concept
  notes need checking only when authored. No concept graph or minimum link count
  is required for portable conversion.
- Only for selected integrations, check wikilinks/embeds, aliases, block IDs,
  ambiguous basenames, vault-relative paths, and Canvas as specified in the
  optional integration reference. These checks do not require launching Obsidian.
- Exclude machine-readable reports and supporting documentation from orphan-note
  gates unless intentionally included in reader-facing navigation.

### Preservation and packaging

- On revisions, capture an initial inventory/hash baseline. Compare attachment
  hashes and original-source hashes after editing.
- Verify chapter-content preservation beyond byte comparison: links and metadata
  legitimately change bytes. Compare normalized prose and mathematical content,
  exercise identifiers, section coverage, and source-error annotations.
- For a course export, verify the archive/import root preserves the declared
  `courses\<course>\` prefix and that source chapter IDs map to exactly one
  complete chapter file each. Section-batch output is intermediate, not a
  delivered substitute for a chapter. Keep the generic standalone-root advice
  separate from course installation instructions.
- Validate ZIP members use safe relative paths without traversal or absolute paths.
  Compare archive contents and file hashes with the finalized importable folder.
- Test checks using small fixtures with valid links and deliberate failures:
  missing file/image, invalid anchor, orphan note, and path escaping the bundle.
  For optional integrations also test ambiguous basenames, broken Canvas edges,
  and wrong destination prefixes as applicable. A validator that always passes
  proves nothing.
- Save actual outcomes, counts, unresolved regions, and validation limitations.
  Do not claim OCR was verified visually, formulas were checked, or Obsidian was
  launched unless those actions occurred.

### Storage and processing

- Keep output and working files under explicitly authorized external roots, not
  the skill clone. Do not infer or access a learner-model root for PDF conversion.
- Use bounded page/section reads for hosted GitHub Copilot task processing. Local
  storage is not a local-inference promise; no additional processing opt-in is
  required. Never bulk-upload a vault or unrelated learner records.
- Do not add separate cloud OCR/vision uploads, passive telemetry, teacher access,
  or provider retention/training guarantees. Report actual tool capabilities and
  any source regions left untranscribed.

## Efficiency and recovery

Use a small representative extraction probe to select the workflow, then process
bounded sections. Cache page text/geometry and only render changed or uncertain
regions. Recheck affected notes and inbound links after edits; run the complete
navigation/packaging checks once final. Avoid re-extracting the entire PDF after link edits.

A failed extractor is not a failed conversion: try coordinate-aware text extraction,
local OCR, and visual source transcription in that order as appropriate. If all
fail, retain the region as a clearly identified source image. Password protection,
unreadable pages, missing local OCR, or destination conflicts must remain explicit
limitations rather than silent omissions or fabricated text.
