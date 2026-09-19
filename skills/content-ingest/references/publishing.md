# Extraction-to-legacy-package publishing handoff

The extractor writes **staging artifacts**, not a complete course. Do not point
learners at the extraction directory as if it were already canonical.
This checklist applies only to explicitly requested legacy hub/package
publication. The teacher's default reviewed portable bundle uses standalone
`digest`; ordinary student reading does not require this package contract,
a catalog, or a validator run. Current Clew has no course importer.

1. Obtain authorization for the destination vault root, selected course root,
   asset placement, and any edits or overwrites. Load `course-content` and its
   legacy structure and package references. If unavailable, stop at extraction.
2. Reconcile heuristic splits with real source chapters and preserve provenance
   and physical-page references. Retain image-only and unverified-fidelity
   labels. Report skipped front matter, unresolved grouping, missing text, or
   unsupported material; do not invent chapters, answers, concepts, or metadata.
3. Assemble the canonical `courses/<course>/hub.md` and one complete Markdown
   file per actual chapter in `courses/<course>/chapters/`, following
   `course-content`.
   Use the hub's ordered inventory, explicit chapter backlinks, real heading
   anchors, and grounded required metadata. Do not publish section shards plus
   an index instead of a complete chapter.
4. Move/copy assets only as authorized, recompute links from their final notes,
   and confirm every target. Retain authorized source attachments and citations;
   do not upload original PDFs merely to make links work.
5. Assemble `course-package.json` with the package contract's inventory, hashes,
   attribution, rights evidence, and reports. Run the installed
   **course-content validator** with `--package` pointing to that package
   directory, not the vault root. Its package contract owns the schema and CLI:

   ```powershell
   python "<installed course-content>\scripts\validate_course.py" --package "<package directory>" --mode draft
   python "<installed course-content>\scripts\validate_course.py" --package "<package directory>"
   ```

   Draft mode permits pending rights only for local drafts; the default publish
   mode requires confirmed rights. Install the validator's requirements only
   when needed. `--catalog` is optional for an explicitly authored catalog,
   not evidence that the teacher repository provides one.
   Capture the command, exit code, and findings. An unavailable validator,
   structural failure, or unresolved chapter grouping blocks a validated-course
   handoff; report staging-only output instead.
6. Separately report source-fidelity review and any live-rendering checks
   actually performed. A structural validator cannot establish transcription
   accuracy, image legibility, complete source coverage, or Obsidian rendering.

Handoff summary: source scope; extraction Markdown/asset roots; success and
failure counts; canonical hub and chapter paths (only if assembled); validator
command/result (only if run); fidelity limitations; remaining user decisions.
Do not create learner models, progress records, or personalized plans as part
of ingestion or publication.
