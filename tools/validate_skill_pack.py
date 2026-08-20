#!/usr/bin/env python3
"""Validate the Codex Game Studios skill pack without third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = [
    "game-studio",
    "game-studio-solo",
    "game-studio-indie",
    "game-studio-mid-size",
    "game-studio-full",
]
ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def top_level_keys(text: str) -> list[str]:
    keys: list[str] = []
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#") or line.startswith(" "):
            continue
        if ":" not in line:
            continue
        key, _value = line.split(":", 1)
        keys.append(key.strip())
    return keys


def validate_unique_keys(keys: list[str], path: Path) -> None:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for key in keys:
        if key in seen:
            duplicates.add(key)
        seen.add(key)
    if duplicates:
        fail(f"{path}: duplicate top-level keys: {', '.join(sorted(duplicates))}")


def parse_simple_frontmatter(text: str, path: Path) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        fail(f"{path}: missing or invalid YAML frontmatter")

    frontmatter_text = match.group(1)
    validate_unique_keys(top_level_keys(frontmatter_text), path)

    result: dict[str, str] = {}
    for line in frontmatter_text.splitlines():
        if not line.strip() or line.startswith("  "):
            continue
        if ":" not in line:
            fail(f"{path}: unsupported frontmatter line: {line}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def validate_skill(name: str) -> None:
    skill_dir = ROOT / "skills" / name
    skill_md = skill_dir / "SKILL.md"
    metadata = skill_dir / "agents" / "openai.yaml"

    if not skill_md.exists():
        fail(f"{name}: missing SKILL.md")
    if not metadata.exists():
        fail(f"{name}: missing agents/openai.yaml")

    text = skill_md.read_text(encoding="utf-8")
    frontmatter = parse_simple_frontmatter(text, skill_md)
    extra = set(frontmatter) - ALLOWED_FRONTMATTER
    if extra:
        fail(f"{name}: unexpected frontmatter keys: {', '.join(sorted(extra))}")

    declared = frontmatter.get("name", "")
    if declared != name:
        fail(f"{name}: frontmatter name is {declared!r}")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", declared):
        fail(f"{name}: invalid skill name")
    if not frontmatter.get("description"):
        fail(f"{name}: missing description")
    if "[TODO:" in text:
        fail(f"{name}: unfinished TODO placeholder")

    metadata_text = metadata.read_text(encoding="utf-8")
    validate_unique_keys(top_level_keys(metadata_text), metadata)
    for required in ("display_name:", "short_description:", "default_prompt:"):
        if required not in metadata_text:
            fail(f"{name}: metadata missing {required}")


def validate_references() -> None:
    main = ROOT / "skills" / "game-studio"
    skill_text = (main / "SKILL.md").read_text(encoding="utf-8")
    linked = re.findall(r"\(references/([^)]+)\)", skill_text)
    for rel in linked:
        if not (main / "references" / rel).exists():
            fail(f"game-studio references missing file: {rel}")

    required_refs = {
        "interaction-patterns.md",
        "studio-dimensions.md",
        "roles.md",
        "workflows.md",
        "workflow-map.md",
        "artifacts.md",
        "quality-gates.md",
    }
    actual_refs = {p.name for p in (main / "references").glob("*.md")}
    missing = required_refs - actual_refs
    if missing:
        fail(f"missing required references: {', '.join(sorted(missing))}")


def validate_docs() -> None:
    required = [
        "README.md",
        "LICENSE",
        "NOTICE.md",
        "docs/specification.md",
        "docs/usage.md",
        "docs/functional-review.md",
        "docs/publisher-notice.md",
        "docs/reference-labels.md",
        "docs/validation-report.md",
        "docs/github-publish-checklist.md",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            fail(f"missing {rel}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in ("Created by Codex", "UPSTREAM-CCGS", "CODEX-ADAPTATION", "AI-GENERATED"):
        if phrase not in readme:
            fail(f"README missing required phrase: {phrase}")


def validate_no_local_junk() -> None:
    for path in ROOT.rglob(".DS_Store"):
        if ".git" not in path.parts:
            fail(f"local Finder metadata should not be published: {path.relative_to(ROOT)}")


def main() -> None:
    for skill in SKILLS:
        validate_skill(skill)
    validate_references()
    validate_docs()
    validate_no_local_junk()
    print("Skill pack validation passed.")


if __name__ == "__main__":
    main()
