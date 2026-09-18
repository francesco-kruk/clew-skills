"""Restore clean consumers from a published immutable Clew skills revision."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

import yaml


PROFILES = {
    "teacher": ["digest", "content-ingest", "course-content"],
    "student": ["digest", "learner-model"],
}
EXPECTED = {
    "teacher": {"digest", "content-ingest", "course-content", "obsidian-markdown", "json-canvas", "obsidian-cli"},
    "student": {"digest", "learner-model", "course-content", "obsidian-markdown", "json-canvas", "obsidian-cli"},
}
UPSTREAM_PINS = {
    "kepano/obsidian-skills": "8ccef29ae8624eccc734e77ced4a6e54baf5d83a",
}
TARGETS = ["copilot", "agent-skills"]


def run(apm: str, folder: Path, *args: str) -> None:
    subprocess.run([apm, *args], cwd=folder, check=True)


def inventory(folder: Path) -> dict[str, str]:
    return {
        str(path.relative_to(folder)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(folder.rglob("*"))
        if path.is_file()
    }


def check_consumer(folder: Path, profile: str, repo: str, sha: str) -> dict[str, str]:
    lock = yaml.safe_load((folder / "apm.lock.yaml").read_text(encoding="utf-8"))
    deps = lock.get("dependencies", [])
    if not deps:
        raise AssertionError("APM generated an empty dependency lock")
    owned = set()
    for dep in deps:
        origin = dep.get("repo_url", "")
        if origin == repo:
            if dep.get("resolved_commit") != sha:
                raise AssertionError(f"Sibling did not inherit immutable SHA: {dep}")
            owned.add(dep.get("virtual_path", "").rsplit("/", 1)[-1])
        elif origin in UPSTREAM_PINS:
            if dep.get("resolved_commit") != UPSTREAM_PINS[origin]:
                raise AssertionError(f"Upstream pin changed: {dep}")
        else:
            raise AssertionError(f"Unexpected dependency origin in {profile}: {origin}")
        if dep.get("is_local") or origin in {"parent", "_parent"}:
            raise AssertionError(f"Unexpanded dependency in lock: {dep}")
    expected_owned = EXPECTED[profile] - {"obsidian-markdown", "json-canvas", "obsidian-cli"}
    if owned != expected_owned:
        raise AssertionError(f"Unexpected Clew dependency closure: {owned} != {expected_owned}")

    skills = folder / ".agents" / "skills"
    discovered = set()
    for skill_file in skills.glob("*/SKILL.md"):
        content = skill_file.read_text(encoding="utf-8")
        if not content.startswith("---"):
            raise AssertionError(f"Missing skill frontmatter: {skill_file}")
        metadata = yaml.safe_load(content.split("---", 2)[1])
        discovered.add(metadata["name"])
    if discovered != EXPECTED[profile]:
        raise AssertionError(f"Deployed skills differ: {discovered} != {EXPECTED[profile]}")
    deployed = {}
    for target in (".agents", ".github"):
        deployed.update({f"{target}/{path}": digest
                         for path, digest in inventory(folder / target).items()})
    if (folder / "AGENTS.md").is_file():
        deployed["AGENTS.md"] = hashlib.sha256((folder / "AGENTS.md").read_bytes()).hexdigest()
    return deployed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default="francesco-kruk/clew-skills")
    parser.add_argument("--sha", required=True, help="Published full 40-character commit SHA")
    parser.add_argument("--apm", default="apm", help="Pinned APM 0.28.0 executable")
    parser.add_argument("--output", default=".apm-smoke")
    parser.add_argument("--profile", choices=[*PROFILES, "all"], default="all")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-fA-F0-9]{40}", args.sha):
        parser.error("--sha must be an immutable full 40-character Git commit")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repo):
        parser.error("--repo must be owner/repository")
    apm = shutil.which(args.apm)
    if apm is None:
        parser.error(f"APM executable not found: {args.apm}")
    apm = str(Path(apm).resolve())
    version = subprocess.check_output([apm, "--version"], text=True)
    if not re.search(r"\bversion 0\.28\.0\b", version):
        parser.error(f"Expected APM 0.28.0, got: {version.strip()}")
    output = Path(args.output).resolve()
    if not output.is_relative_to(Path.cwd().resolve()) or output == Path.cwd().resolve():
        parser.error("--output must be a named child directory of the working directory")
    output.mkdir(parents=True, exist_ok=True)
    profiles = PROFILES if args.profile == "all" else [args.profile]
    for profile in profiles:
        folder = output / f"{profile}-{args.sha.lower()}"
        folder.mkdir(exist_ok=False)
        manifest = {
            "name": f"clew-smoke-{profile}",
            "version": "1.0.0",
            "targets": TARGETS,
            "dependencies": {
                "apm": [f"{args.repo}/skills/{skill}#{args.sha.lower()}" for skill in PROFILES[profile]]
            },
            "includes": [],
        }
        (folder / "apm.yml").write_text(yaml.safe_dump(manifest, sort_keys=False), encoding="utf-8")
        run(apm, folder, "install", "--target", ",".join(TARGETS))
        before = check_consumer(folder, profile, args.repo, args.sha.lower())
        shutil.rmtree(folder / "apm_modules")
        shutil.rmtree(folder / ".agents")
        if (folder / ".github").exists():
            shutil.rmtree(folder / ".github")
        (folder / "AGENTS.md").unlink(missing_ok=True)
        run(apm, folder, "install", "--frozen", "--target", ",".join(TARGETS))
        after = check_consumer(folder, profile, args.repo, args.sha.lower())
        if before != after:
            raise AssertionError(f"Frozen restore changed deployed bytes for {profile}")
        (folder / "smoke-result.json").write_text(
            json.dumps({"profile": profile, "repo": args.repo, "sha": args.sha.lower(),
                        "apm": version.strip(), "targets": TARGETS, "restored_file_count": len(after),
                        "byte_identical_restore": True}, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"PASS {profile}: {len(after)} files restored byte-identically at {args.sha}")


if __name__ == "__main__":
    main()
