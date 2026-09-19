# Clew skills

Portable learning skills from [Clew](https://github.com/francesco-kruk/clew),
shared as individual [APM](https://github.com/microsoft/apm) packages.

| Skill | Purpose |
| --- | --- |
| [course-content](skills/course-content/SKILL.md) | Read and navigate courses; validate course packages. |
| [content-ingest](skills/content-ingest/SKILL.md) | Image-first PDF extraction into local Markdown and assets. |
| [digest](skills/digest/SKILL.md) | Faithful editable document reconstruction and course export. |
| [learner-model](skills/learner-model/SKILL.md) | Maintain learner-controlled evidence, goals and adaptations. |

## Install

With **APM 0.28.0**, run this in the workspace where you want to use a skill:

```powershell
apm install francesco-kruk/clew-skills/skills/digest --target copilot,agent-skills
```

Replace `digest` with any skill listed above. APM resolves sibling and upstream
skill dependencies automatically. Install `learner-model` separately when
learner-record access is wanted; the other skills do not depend on it.
For a reproducible install, append `#<published-full-commit-sha>` to the package
reference and retain the consumer's generated lockfile.

Keep both targets: a Copilot-only install can skip the skill entrypoints.
Installed skills appear under `.agents/skills/` in the consumer workspace.
This repository has no root aggregate package; install skills by their paths.

## Python helpers

APM installs skills, not Python dependencies. If you use PDF ingestion or the
course validator, install the corresponding runtime requirements in a dedicated
environment. From the consumer workspace, for example:

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
