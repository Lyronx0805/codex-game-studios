# Codex Game Studios

Codex Game Studios is a Codex skill package for vibe-coding game developers
seeking studio-style structure for AI-assisted game design, implementation,
testing, and release planning.

**Created by Codex:** This skill pack was generated and organized by Codex as
an AI-assisted adaptation. It is provided as-is under the MIT License. The
publisher distributes the package but does not warrant game outcomes, legal
fitness, upstream compatibility, or dispute-free use.

This project adapts the studio-hierarchy idea from
[Claude Code Game Studios](https://github.com/donchitos/claude-code-game-studios)
for Codex skills. Instead of Claude slash commands, Claude subagent files, and
Claude hooks, this pack uses Codex-native skill instructions, progressive
references, and selectable studio dimensions.

## Reference Labels

| Label | Meaning |
| --- | --- |
| `UPSTREAM-CCGS` | The MIT-licensed source inspiration: `donchitos/claude-code-game-studios` |
| `CODEX-ADAPTATION` | New Codex skill structure, wording, references, validation, and dimension presets |
| `AI-GENERATED` | Content created or revised by Codex and requiring normal human review before production use |

## What's Included

| Skill | Studio Dimension | Best For |
| --- | --- | --- |
| `game-studio` | Configurable | Codex can select or confirm the appropriate studio size |
| `game-studio-solo` | Solo | One developer, prototypes, school projects, game jams |
| `game-studio-indie` | Indie | Small projects that need design, code, QA, and production structure |
| `game-studio-mid-size` | Mid-size | Multi-system games with enough complexity to need department leads |
| `game-studio-full` | Full | Large games needing director gates, specialists, release planning, and deeper documentation |

## Studio Dimensions

The main improvement over a one-size studio is selectable process depth.

| Dimension | Role Lenses | Review Weight | Artifact Weight |
| --- | ---: | --- | --- |
| Solo | 3 | Lightweight | Minimal checklists and notes |
| Indie | 6 | Balanced | Design docs, ADRs, sprint/story notes |
| Mid-size | 12 | Structured | Department reviews and quality gates |
| Full | 25+ | Thorough | Full studio pipeline, director sign-offs, release gates |

## Why This Skill Is Useful

Many AI-assisted game-development workflows provide either minimal structure or
excessive process. A single general chat can miss design, QA, scope, or release
risks, while a full studio process can add unnecessary overhead to a prototype.

Codex Game Studios solves that by making studio size selectable:

- solo mode supports rapid work on prototypes, school projects, and game jams;
- indie mode adds structure for small-team production;
- mid-size mode introduces department-style handoffs for complex games;
- full mode adds director gates, specialist checks, release planning, security,
  accessibility, localization, and live-ops review when the stakes are higher.

The operational advantage is control over workflow scale. A project can receive
the appropriate amount of planning, documentation, implementation guidance, and
QA without being forced into one fixed process.

## Specification

The full specification is in [docs/specification.md](docs/specification.md).

Short version:

- `skills/game-studio/` is the primary configurable skill.
- `skills/game-studio-*/` are preset entry points for specific studio sizes.
- `skills/game-studio/references/` contains the detailed playbook loaded only
  when needed.
- `tools/validate_skill_pack.py` checks skill names, frontmatter, references,
  UI metadata, and README links without third-party Python packages.

Validation notes are in [docs/validation-report.md](docs/validation-report.md).
Functional review notes are in [docs/functional-review.md](docs/functional-review.md).
GitHub publishing steps are in
[docs/github-publish-checklist.md](docs/github-publish-checklist.md).

## Installation

Copy one or more folders from `skills/` into the Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/game-studio ~/.codex/skills/
cp -R skills/game-studio-indie ~/.codex/skills/
```

Restart Codex or reload skills after copying.

For detailed installation and examples, see [docs/usage.md](docs/usage.md).

## Basic Invocation

Start with:

```text
Use $game-studio to plan this game project.
```

Or choose a preset:

```text
Use $game-studio-solo to prototype a 2D platformer movement system.
Use $game-studio-full to review launch readiness for a multiplayer game.
```

## Codex Adaptation Notes

The upstream project has 49 Claude agents, 73 Claude skills, hooks, path rules,
and a slash-command workflow. Codex skills do not use the exact same mechanism,
so this version keeps the intent and professional studio structure while
changing the implementation:

- studio roles become "role lenses" Codex can apply during planning, reviews,
  implementation, and QA;
- slash commands become named workflow modes inside the skill references;
- Claude hooks become manual quality gates and checklists;
- review intensity scales with the selected studio dimension.

## Attribution

This project is revised and adapted from
`donchitos/claude-code-game-studios`, which is MIT licensed. The original
copyright notice is preserved in `LICENSE`.

## Publisher Notice

This repository is an AI-assisted Codex adaptation, not an official upstream
release. Review the skill text before using it for commercial production,
publishing decisions, legal/compliance work, or safety-sensitive game systems.
See [docs/publisher-notice.md](docs/publisher-notice.md).
