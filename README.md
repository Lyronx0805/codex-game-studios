# Codex Game Studios

Codex Game Studios is a Codex skill package for vibe-coding game developers
seeking studio-style structure for AI-assisted game design, implementation,
testing, and release planning.

**Created by Codex:** This skill pack was generated and organized by Codex as
an AI-assisted adaptation. It is provided as-is under the MIT License. The
publisher distributes the package but does not warrant game outcomes, legal
fitness, upstream compatibility, or dispute-free use.

This project adapts the studio-hierarchy and quality-gate idea from
[Claude Code Game Studios](https://github.com/donchitos/claude-code-game-studios)
for Codex skills. Instead of Claude slash commands, Claude subagent files, and
Claude hooks, this pack uses Codex-native skill instructions, progressive
references, selectable studio dimensions, role lenses, and optional multi-agent
execution when the Codex environment supports it.

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

| Dimension | Role Lenses | Execution Model | Review Weight | Artifact Weight |
| --- | ---: | --- | --- | --- |
| Solo | 3 | Single-agent role lenses | Lightweight | Minimal checklists and notes |
| Indie | 6 | Role lenses, optional reviewer | Balanced | Design docs, ADRs, sprint/story notes |
| Mid-size | 12 | Optional multi-agent tracks | Structured | Department reviews and quality gates |
| Full | 25+ | Multi-agent recommended when available | Thorough | Full studio pipeline, director sign-offs, release gates |

## Hybrid Mechanism

The skill uses two execution layers.

**Role-lens layer:** Codex remains a single active collaborator and examines
the game through selected studio viewpoints. For example, the same response can
apply designer, programmer, producer, QA, release, accessibility, or security
lenses depending on the selected dimension and task risk. This is the default
because it works in any Codex skill environment.

**Multi-agent layer:** When the Codex environment provides subagents, parallel
tasks, or isolated worktrees, larger work can be split into separate tracks.
The coordinating Codex agent proposes the split, confirms it when the split was
not already requested, assigns clear objectives and file boundaries, then
synthesizes the results before presenting a final recommendation or change.

The execution model scales with the studio dimension:

- `solo`: one Codex agent using role lenses;
- `indie`: one Codex agent by default, with an optional reviewer or QA subagent
  for risky work;
- `mid-size`: optional design, technical, implementation, QA, or release task
  tracks;
- `full`: multi-agent coordination recommended for launch, multiplayer,
  security, live-ops, or broad specialist reviews when supported.

Detailed delegation rules are defined in
[skills/game-studio/references/multi-agent-mode.md](skills/game-studio/references/multi-agent-mode.md).

## Why This Skill Is Useful

Many AI-assisted game-development workflows provide either minimal structure or
excessive process. A single general chat can miss design, QA, scope, or release
risks, while a full studio process can add unnecessary overhead to a prototype.

Codex Game Studios solves that by making studio size selectable:

- solo mode supports rapid work on prototypes, school projects, and game jams;
- indie mode adds structure for small-team production;
- mid-size mode introduces department-style handoffs and optional multi-agent
  tracks for complex games;
- full mode adds director gates, specialist checks, release planning, security,
  accessibility, localization, live-ops review, and multi-agent coordination
  when the stakes are higher.

The operational advantage is control over workflow scale. A project can receive
the appropriate amount of planning, documentation, implementation guidance, and
QA without being forced into one fixed process. Small tasks stay with one Codex
agent applying role lenses; larger tasks can split into separate Codex tasks or
subagents, optionally using isolated worktrees when that capability is
available.

## Specification

The full specification is in [docs/specification.md](docs/specification.md).

Short version:

- `skills/game-studio/` is the primary configurable skill.
- `skills/game-studio-*/` are preset entry points for specific studio sizes.
- `skills/game-studio/references/` contains the detailed playbook loaded only
  when needed.
- `skills/game-studio/references/multi-agent-mode.md` defines when to stay with
  role lenses and when to propose real subagent or worktree delegation.
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
- multi-agent execution becomes optional and environment-dependent rather than
  required for basic use;
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
