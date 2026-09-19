# Clew skills

Portable learning skills from [Clew](https://github.com/francesco-kruk/clew),
shared as individual [APM](https://github.com/microsoft/apm) packages.

| Skill | Purpose |
| --- | --- |
| [course-content](skills/course-content/SKILL.md) | Read selected portable Markdown; optionally validate legacy course packages. |
| [content-ingest](skills/content-ingest/SKILL.md) | Image-first PDF extraction into local Markdown and assets. |
| [digest](skills/digest/SKILL.md) | Standalone, faithful PDF-to-Markdown conversion; optional Clew/Obsidian export. |
| [learner-model](skills/learner-model/SKILL.md) | Maintain versioned evidence-first Markdown goals, work, errors, preferences and sessions. |

## Install

With **APM 0.28.0**, run this in the workspace where you want to use a skill:

```powershell
apm install francesco-kruk/clew-skills/skills/digest --target copilot,agent-skills
```

**Digest installs only digest.** It has no mandatory skill or MCP dependencies:
`course-content`, `obsidian-markdown`, `json-canvas`, and `obsidian-cli` are not
installed by this command in a clean consumer workspace. Upgrading an existing
workspace is not permission to remove skills already installed there.

Replace `digest` with another skill listed above to select a different package.
Those packages retain their existing dependencies, which APM resolves
automatically. Install `learner-model` separately when learner-record access is
wanted; the other skills do not depend on it.
For a reproducible install, append `#<published-full-commit-sha>` to the package
reference and retain the consumer's generated lockfile.

Keep both targets: a Copilot-only install can skip the skill entrypoints.
Installed skills appear under `.agents/skills/` in the consumer workspace.
This repository has no root aggregate package; install skills by their paths.

## Student workflow

A teacher uses digest in the teacher workspace (`clew-content`) to convert an
authorized PDF and commits the complete portable bundle. The student creates
their own external local vault and manually copies the whole bundle, preserving
notes, images and reports. The student clones Clew, restores its pinned skills,
and configures that vault path once in Clew's ignored `.clew.local.json`
(`version: 1`, `vault: <absolute path>`). Configuration alone creates no learning
records. No course importer, catalog, manifest, hub or running Obsidian is needed.

`course-content` reads the selected bundle/note as-is, using ordinary relative
Markdown links and existing wikilinks. An index/README/hub is useful when present,
never required. It cites exact notes/headings and reports unknown metadata rather
than inventing concepts. A course-only lookup does not open the learner model.
Copied teacher sources stay read-only unless the student explicitly asks to edit
them; personal work stays separate.

`learner-model` 2.x defaults to
[evidence-first-v1](skills/learner-model/references/learner-model-spec.md):
`model/profile.md`, a small routing `model/index.md`, and Markdown notes for
goals, observations, factual errors, confirmed preferences, sessions and changes.
Supplied work and generated personal output live in `artifacts/`. A genuine
goal/attempt creates actual evidence and a session; giving only a path prompts
for a goal. Stable IDs, source links and append-only change history support later
sessions without numerical mastery/confidence scores, inferred preferences or
automatic schedules. No adaptation is a valid state; a current presentation
request is not proof of benefit or a standing preference.

Unknown/old models and reserved-directory collisions require clarification, not
automatic migration. Corrections and confirmed scoped tombstones alter the
effective view without erasing history or hosted context. File tools re-read
changes conservatively, but this is agent guidance, not a transactional backend,
filesystem security mechanism or provider-deletion guarantee. The
[advanced-v1 full model](skills/learner-model/references/advanced-model-spec.md)
and its unresolved numerical/schema policies remain an explicitly selected,
distinct legacy profile, not prerequisites for initial evidence writes.

To test an unpublished checkout, run APM from a separate empty consumer directory
with the absolute path to the edited package (replace the example path):

```powershell
apm install 'C:\Path\To\clew-skills\skills\digest' --target copilot,agent-skills
```

This tests local changes; the GitHub installation command uses the published ref,
not uncommitted files in a checkout.

APM 0.28 cannot resolve `git: parent` from a local-path package. For
`learner-model` (which uses that preserved sibling dependency), push a commit
first and test its immutable GitHub package reference in an empty consumer
workspace, then run `apm install --frozen --target copilot,agent-skills`.
Do not hand-edit generated consumer files or replace dependency pins to bypass
that local-install limitation.

## Standalone PDF conversion

Ask digest to convert an authorized PDF into an external output directory, for
example: "Use digest to convert my authorized worksheet PDF to faithful, editable
Markdown in this output folder." A teacher does not need a Clew course, an
Obsidian vault, a running app, or any other skill.

The default bundle contains an `index.md`, source-organized chapter/section notes,
needed images, and coverage/verification reports. Notes and images use relative
Markdown links, so move the whole bundle together and open `index.md` in a Markdown
editor. Equations remain editable LaTeX; rendered math needs a compatible viewer.
Source-page citations distinguish physical pages from printed labels. Include the
original PDF only when authorized; otherwise retain visible citations and its hash
without broken source links.

Digest preserves complete explanations, examples, exercises, supplied answers,
equations, and figures rather than summarizing them. It verifies pages in bounded
batches and explicitly labels unreadable/image-only regions. This is an
agent-guided workflow, not a bundled deterministic converter or a guarantee that
every scanned equation can become editable text. See its
[quality gates](skills/digest/references/quality-and-linking.md) and
[local runtime setup](skills/digest/references/runtime.md).

### Explicit optional integrations

An installed integration or a document called a "course" does not select a mode.
Ask for the desired export explicitly; digest never silently installs a missing
skill or substitutes another format.

| Requested output | Separately required guidance |
| --- | --- |
| Explicit legacy Clew hub/package export | `course-content` and its preserved structure/distribution contracts, including its Obsidian note-writing prerequisites. |
| Obsidian-specific notes | `obsidian-markdown`; no Clew package or running app required. |
| JSON Canvas overview | `json-canvas`, with an explicit destination root; not created merely because a graph might be useful. |

If a prerequisite is missing, digest explains it and pauses that mode. To choose
legacy Clew export, the user can separately install its package:

```powershell
apm install francesco-kruk/clew-skills/skills/course-content --target copilot,agent-skills
```

That optional package still brings its existing `obsidian-markdown`, `json-canvas`,
and `obsidian-cli` dependencies; it is **not** needed for standalone digest.
Obsidian-only or Canvas-only users can separately install the corresponding
`kepano/obsidian-skills/skills/obsidian-markdown` or
`kepano/obsidian-skills/skills/json-canvas` package with the same targets (the
integration revision used here is recorded in `skills/course-content/apm.yml`).
See [integration behavior](skills/digest/references/optional-integrations.md).
The separate `content-ingest` package remains the unchanged image-first route,
not an automatic digest dependency or fallback.

## Python helpers

APM installs skills, not PDF extraction/rendering/OCR tools. For digest, probe
existing tools, choose a method, then install only missing runtime packages needed
for that method in a task-local environment outside the deliverable. For example,
**only when PyMuPDF is the chosen method and is missing**:

```powershell
python -m venv .venv-digest
.\.venv-digest\Scripts\python.exe -m pip install pymupdf
```

Do not install every PDF backend, OCR engine, or another skill's requirements for
standalone digest. MarkItDown is optional; scans may need local OCR and language
data. See digest's runtime reference for selection, isolation, and failure behavior.

For the separate image-first ingestion engine or course validator, use that
installed skill's requirements in a dedicated environment, only if invoking its
helper. From the consumer workspace, for example:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .agents\skills\content-ingest\requirements.txt
.\.venv\Scripts\python.exe -m pip install -r .agents\skills\course-content\requirements.txt
```

Run only the install commands for skills you have installed and helpers you need.
See each skill's instructions for invocation and limitations. Source packages
live only in `skills/`; edit those rather than generated installations.

## Privacy and licenses

Keep source documents, course outputs and learner records outside this repository.
Local storage does not mean local-only inference: hosted Copilot may process
authorized task-relevant content. Do not bulk-upload vaults or access unrelated
learner records.

[MIT](LICENSE) covers the software and skill documentation, not third-party
documents or learner data. Confirm the rights to process and share each source.
Original authorship is preserved; upstream dependencies retain their own licenses.
See [THIRD_PARTY_NOTICES.txt](THIRD_PARTY_NOTICES.txt).
