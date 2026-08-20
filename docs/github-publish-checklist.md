# GitHub Publish Checklist

Reference label: `CODEX-ADAPTATION`

## Recommended Repository Settings

Repository name:

```text
codex-game-studios
```

Description:

```text
Codex-created skill package for vibe-coding game developers, adapting the MIT-licensed Claude Code Game Studios workflow into scalable Codex studio dimensions.
```

Topics:

```text
codex
codex-skills
game-development
game-studio
ai-assisted
indie-game-dev
skills
workflow
```

Visibility:

```text
Public
```

License:

```text
MIT
```

## Before First Push

Run:

```bash
python3 tools/validate_skill_pack.py
git status --short --branch
```

Confirm that no local-only files, secrets, build output, or generated cache files
are staged.

## Suggested Initial Commit

```bash
git add -- .github/workflows/validate.yml .gitignore LICENSE NOTICE.md README.md docs skills tools
git commit -m "Initial Codex Game Studios skill pack"
```

## Suggested Remote Setup

Replace `OWNER` with the GitHub account or organization:

```bash
git remote add origin https://github.com/OWNER/codex-game-studios.git
git push -u origin main
```

## Release Notes For v0.1.0

```text
Initial Codex Game Studios release.

- Adds configurable `game-studio` skill.
- Adds solo, indie, mid-size, and full studio dimension presets.
- Adds Codex-native references for roles, workflows, artifacts, and quality gates.
- Adds upstream reference labels and Codex-created publisher notice.
- Adds package validator and GitHub Actions workflow.
```

## Publisher Notice

Reference label: `AI-GENERATED`

This package was created by Codex as an AI-assisted adaptation. It is provided
as-is under the MIT License and should be reviewed before production use.
