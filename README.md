# Clew skills

Portable learning skills extracted from [Clew](https://github.com/francesco-kruk/clew).
This repository contains skills and their bundled contracts, not a learner vault
or the Clew application. Original Clew authorship and MIT terms are preserved.
Upstream skill pins and license notices are preserved; attribution paths describe
this repository's installed dependencies rather than the original application.

## Pick an entrypoint

| Skill | Use |
| --- | --- |
| [course-content](skills/course-content/SKILL.md) | **Stable reading entrypoint:** locate a course hub, follow chapter navigation, read bounded grounded excerpts. |
| [content-ingest](skills/content-ingest/SKILL.md) | Teacher image-first PDF ingestion into an external course package. |
| [digest](skills/digest/SKILL.md) | Faithful editable reconstruction, course export, or standalone document bundles. |
| [learner-model](skills/learner-model/SKILL.md) | Maintain evidence, uncertainty, goals, adaptations and learner-controlled records. |

Each folder is a self-contained hybrid APM package with its own `SKILL.md`,
resources, manifest and license. Package code does not depend on a Clew checkout.
APM resolves declared sibling skills; copying only `SKILL.md` is not installation.

## Install

Use **APM 0.28.0**, not the earlier 0.26 CLI. Install it in an isolated environment;
do not replace a global installation. From this checkout, in PowerShell:

```powershell
python -m venv .venv-apm-0.28.0
.\.venv-apm-0.28.0\Scripts\python.exe -m pip install -r requirements-dev.txt -r skills\content-ingest\requirements.txt -r skills\course-content\requirements.txt
$apm = (Resolve-Path .\.venv-apm-0.28.0\Scripts\apm.exe).Path
& $apm --version
```

In a separate consumer directory, set `$sha` to a **published full commit SHA**
of this repository (not a branch name or the literal placeholder):

```powershell
$sha = '5ed0f288a6c5c0c0f891939385ddf38fa5b32504'
# Teacher: course tools only; no learner model or contributor tooling.
& $apm install "francesco-kruk/clew-skills/skills/digest#$sha" "francesco-kruk/clew-skills/skills/content-ingest#$sha" "francesco-kruk/clew-skills/skills/course-content#$sha" --target copilot,agent-skills
# Student: run in a different consumer directory.
& $apm install "francesco-kruk/clew-skills/skills/digest#$sha" "francesco-kruk/clew-skills/skills/learner-model#$sha" --target copilot,agent-skills
```

Use **both** targets: the source packages declare `agent-skills`, so a
Copilot-only install can exit successfully while skipping their entrypoints.
Check that the expected first-party `.agents/skills/*/SKILL.md` files exist;
successful dependency resolution alone does not prove skill deployment.

Load `course-content` for ordinary reading; do not run ingestion to answer a
chapter question. Resolve the authorized external course/vault/model root
explicitly. Never store course PDFs, private learner records or output vaults
in this skill repository. Python ingestion helpers have package-specific
`requirements.txt` files; APM installs skills, not Python dependencies.

## Dependency boundaries

```text
digest -----------+--> course-content --> obsidian-markdown, json-canvas, obsidian-cli
content-ingest ---+
learner-model ----+
digest -------------------------------> obsidian-markdown, json-canvas
development --------------------------> skill-creator, defuddle, obsidian-bases, ADR
root aggregate -----------------------> all four skills + development
```

Digest, course-content and content-ingest do not depend on learner-model.
Learner-model is installed separately for explicitly authorized student use.
Contributor tools live in `packages/development`, outside individual runtime
dependency closures. Use the root aggregate only when all contributor tools are
wanted.

APM 0.28.0 [`git: parent`](https://github.com/microsoft/apm/blob/v0.28.0/docs/src/content/docs/reference/manifest-schema.md#412-object-form)
inherits the remote repository and resolved revision. Its `path` is
**repository-root-relative**, for example `skills/course-content`, not `../course-content`.
The root aggregate pins the four runtime packages and development package to the published source
revision above. APM 0.28.0 rejects `git: parent` under a local parent, so local
`path: ./skills/...` references cannot replace these remote pins. Development
uses the same immutable source revision as all runtime packages. From this checkout,
run `& $apm install --frozen --target copilot,agent-skills` to restore the maintainer
environment. After changing skill sources, publish a new source revision, update
all five root pins together, run `apm install`, and rerun clean consumer tests.
Never handwrite a lockfile or replace sibling inheritance with floating refs.

## Development and verification

Run the repository's synthetic checks before publishing. The CI workflow pins
APM, exercises synthetic tests, then restores fresh teacher/student consumers
from a published commit and repeats with `--frozen`. The smoke script rejects
branch refs, checks exact sibling/upstream revisions and runtime closures, and
compares deployed file hashes after deleting `apm_modules` and `.agents`.

```powershell
.\.venv-apm-0.28.0\Scripts\python.exe -m unittest discover -s skills\course-content\tests -q
.\.venv-apm-0.28.0\Scripts\python.exe -m unittest discover -s skills\content-ingest\tests -q
.\.venv-apm-0.28.0\Scripts\python.exe scripts\apm_smoke_consumers.py --sha $sha --apm $apm
```

Results remain in ignored `.apm-smoke`; existing consumer directories are never
overwritten. Delete only your own previous smoke directory or choose a new
`--output` before repeating the same SHA.
`apm_modules` and virtual environments are ignored. APM-generated `.agents`
outputs and actual `apm.lock.yaml` files are versioned when generated for the
maintainer environment; regenerate them with the pinned tool, never edit them.
At source revision `5ed0f288a6c5c0c0f891939385ddf38fa5b32504`, clean teacher and
student installations and frozen restores passed with APM 0.28.0, reproducing
39 and 30 deployed files byte-for-byte respectively. Each closure inherited
the same immutable source SHA; the teacher closure excluded learner-model.
Synthetic tests validate contracts and packaging,
not real PDFs, OCR quality, teaching effectiveness or live learner data.

On Windows, deeply nested checkouts can exceed the native path-length limit
under the current OS/process settings. A 310-character PNG destination failed
with both PyMuPDF 1.28.2 and plain Python `write_bytes`, while a short-path
control succeeded; this is not a PyMuPDF-only bug. Use a short checkout for
tests and short, explicit authorized output/assets paths for ingestion. CI
runs the same tests on Windows from a short `s` checkout with a project-local
scratch root for `TEMP`/`TMP`; it does not skip long-path-sensitive tests.
Two ingestion fixture tests failed in a deeply nested consumer clone despite
passing in the shorter source checkout. Preserve that limitation in reports
rather than modifying generated tests or the pinned source.

## Privacy and rights

Vault storage stays local and portable; it is **not a local-only inference
guarantee**. During ordinary authorized use, hosted GitHub Copilot may process
relevant bounded pages, excerpts and learner records without a separate opt-in.
Do not bulk-upload a vault, inspect unrelated records, add passive telemetry,
or grant teacher/institutional access. No provider retention, training or
deletion promises are made. Separate cloud OCR services are not an implicit
fallback.

[MIT](LICENSE) covers the original **software and skill documentation**, not
third-party PDFs, textbooks, course exports or learner data. Confirm the rights
to ingest, reproduce and share each source; derived content retains applicable
source restrictions. Upstream skills retain their own licenses; see
[THIRD_PARTY_NOTICES.txt](THIRD_PARTY_NOTICES.txt) and installed license files.
