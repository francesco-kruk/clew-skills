# Explicit optional integrations

Read this reference only for a requested integration. Installing digest does not
install any integration below. Locate available skills by their installed names,
not by repository-relative sibling paths. Load only guidance needed for the
selected output. A missing prerequisite blocks that mode: name it and explain
what the user must separately install, without installing it or substituting a
different deliverable. Portable conversion does not need these skills.

## Clew course export

This is the preserved **legacy hub/package export**, not a requirement for using
ordinary portable bundles in the student Clew workflow.
On an explicit request to export a legacy Clew course, load installed `course-content`,
its `references/structure.md`, and (for distribution) its
`references/package-contract.md`. These remain authoritative; do not freeze a
copy of the contract in digest. Follow its writer prerequisites, including
`obsidian-markdown` for course notes. A Clew export selects that contract's
Obsidian note syntax, but does not select Canvas or live app operations.

- Use one canonical `courses\<course>\hub.md` and exactly one complete file per
  actual source chapter in `chapters\`, with finer sections as headings. Never
  substitute section shards plus an index, or emit a competing portable index.
- Ground hub/chapter metadata, domains, sources, chapter order, and concept
  locations in the supplied material and author decisions. Ask for missing
  metadata; do not invent canonical concept IDs or learner state.
- Apply the contract's course-qualified hub backlinks, source links, supporting
  note roles, and exact destination prefix. Concept notes/maps remain optional.
- Keep digest's bounded page verification, full transcription, figure recovery,
  manifest, and limitations. Structural validation alone is not fidelity evidence.
- For distribution, assemble the package inventory, hashes, attribution, rights
  evidence, and reports and run the installed `scripts/validate_course.py` with
  an explicit `--package` path. Install its own `requirements.txt` in an isolated
  environment only when using that validator. Use `--mode draft` for local
  pending-rights drafts; publication still requires the contract's rights gate.
- Package the `courses\<course>\` tree under the declared vault root. Do not
  recommend opening the inner course folder as a vault when links assume that
  prefix. Hand off the actual hub, destination, reports, and source limitations.
  Subsequent reading uses `course-content`, not PDF re-extraction.

Separately installing `course-content` currently brings its existing
`obsidian-markdown`, `json-canvas`, and `obsidian-cli` dependencies. This is
unchanged and is not part of digest's standalone installation. Their availability
does not authorize creating Canvas files, accessing a vault, or running an app.

## Obsidian-specific Markdown

Only when Obsidian-specific output is requested (or required by the explicitly
selected Clew contract), load installed `obsidian-markdown` before authoring its
syntax. For a non-Clew bundle, retain the source-based section organization; no
course contract, concept graph, or course metadata is required.

- Use unique-basename wikilinks with readable aliases, such as
  `[[Book - First section|first section]]`, when moving a non-course bundle among
  subfolders. Resolve every basename unambiguously; otherwise use the exact
  authorized vault-relative path.
- Heading targets match actual heading text. Use explicit `^block-id` targets
  only when needed. Embed assets with `![[Book - Figure 01.png]]`, with physical
  source-page captions; `[[Book - Original.pdf#page=7|PDF page 7]]` uses physical
  page numbers, not printed labels.
- Keep math out of wikilink targets/aliases. Tags do not replace meaningful links.
  Concept notes or maps, if requested, need source links and explained
  relationships, not arbitrary link quotas or duplicated chapter bodies.
- Check wikilinks, embeds, aliases, heading/block targets, ambiguity, and index
  reachability. No running Obsidian application or plugin is needed to write or
  validate files. Do not claim live rendering was tested unless it was.

## JSON Canvas

Create a `.canvas` file only on explicit request and after loading installed
`json-canvas`. Canvas alone does not require rewriting portable Markdown as
wikilinks; load `obsidian-markdown` only if that syntax is also selected.

Obsidian Canvas file-node paths are **vault-root-relative**, never relative to
the Canvas file. Serialized paths use `/`, even on Windows. Establish one strategy:

1. Standalone root: paths are relative to the bundle root. For Obsidian use, open
   that folder as a vault or copy its contents directly into a vault root.
2. Known vault subfolder: prefix every file-node path with that exact subfolder;
   Clew paths retain `courses/<course>/...`. Validate against that destination.
3. Unknown destination: ask for it or explicitly agree on a fixed standalone-root
   layout. Do not silently omit a requested Canvas or promise arbitrary placement.

Use a manageable overview with meaningful groups and labeled relationships.
Validate JSON `nodes`/`edges`, unique IDs, finite geometry and positive dimensions,
edge endpoints, file targets, and actual heading/block subpaths using the declared
root. Test broken-edge and wrong-prefix failures. Inspect layout in the chosen
viewer if available; otherwise report live rendering as untested. A valid Canvas
is neither proof of transcription fidelity nor a substitute for note navigation.
