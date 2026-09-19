# Contributor tools

This APM aggregator preserves the original Clew pins for skill authoring
(`skill-creator`), ADR writing, web extraction (`defuddle`) and Obsidian Bases.
None is required by the teacher or student runtime packages. Markdown, canvas
and Obsidian CLI tools are runtime dependencies of `course-content` instead.

Install this package explicitly from a published immutable repository SHA, or
consume the repository root aggregate for all runtime and contributor tools.
The local package can also be restored independently with APM 0.28.0 because its
dependencies are all pinned upstream references, not `git: parent`.

The original Clew MIT license applies to this manifest and documentation;
upstream dependencies retain their own licenses. The root
`THIRD_PARTY_NOTICES.txt` preserves the original attribution.
