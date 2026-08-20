# Specification

Reference label: `CODEX-ADAPTATION`

Codex Game Studios is a Codex skill package for structuring AI-assisted game
development work around scalable studio dimensions.

## Package Goals

- Give Codex a reusable game-studio operating model.
- Preserve the useful studio-hierarchy idea from `UPSTREAM-CCGS`.
- Avoid Claude-only assumptions such as slash commands, Claude hooks, and
  Claude agent configuration.
- Let users select a studio dimension so small projects stay light and larger
  projects get stronger review coverage.

## Core Advantage

The central advantage is selectable studio size. Users are not locked into one
workflow. A beginner can ask for a solo prototype workflow with minimal process,
while a larger or higher-risk project can ask for mid-size or full-studio review
with more roles, stronger gates, and more complete production evidence.

## Skill Inventory

| Skill | Path | Purpose |
| --- | --- | --- |
| `game-studio` | `skills/game-studio/` | Configurable router that chooses or applies a studio dimension |
| `game-studio-solo` | `skills/game-studio-solo/` | Lightweight solo workflow for prototypes and small projects |
| `game-studio-indie` | `skills/game-studio-indie/` | Balanced small-team workflow for normal indie projects |
| `game-studio-mid-size` | `skills/game-studio-mid-size/` | Structured department workflow for complex projects |
| `game-studio-full` | `skills/game-studio-full/` | Thorough review workflow for high-risk or launch-bound games |

## Dimension Behavior

| Dimension | Role Lenses | Review Weight | Expected Behavior |
| --- | ---: | --- | --- |
| Solo | 3 | Light | Prototype rapidly, use short notes, run one compact review |
| Indie | 6 | Balanced | Keep useful docs, ADRs, stories, tests, and QA notes |
| Mid-size | 12 | Structured | Use department reviews, readiness checks, risks, and milestones |
| Full | 25+ | Thorough | Use director gates, specialist reviews, evidence, and release checks |

## Main Skill References

| Reference | Path | Loaded When |
| --- | --- | --- |
| Interaction patterns | `skills/game-studio/references/interaction-patterns.md` | Making responses actionable and beginner-friendly |
| Studio dimensions | `skills/game-studio/references/studio-dimensions.md` | Choosing process size |
| Roles | `skills/game-studio/references/roles.md` | Routing work through role lenses |
| Workflows | `skills/game-studio/references/workflows.md` | Choosing a project workflow |
| Workflow map | `skills/game-studio/references/workflow-map.md` | Translating upstream command coverage |
| Artifacts | `skills/game-studio/references/artifacts.md` | Creating docs, stories, ADRs, QA evidence |
| Quality gates | `skills/game-studio/references/quality-gates.md` | Reviewing design, code, QA, release readiness |

## Required Codex Skill Shape

Each skill folder must contain:

- `SKILL.md` with YAML frontmatter containing `name` and `description`;
- `agents/openai.yaml` with display metadata;
- lowercase hyphen-case skill names;
- no unfinished `[TODO:]` placeholders.

## Non-Goals

- This pack is not a full game engine.
- This pack does not automatically install Claude Code assets.
- This pack does not guarantee correctness, legal fitness, commercial success,
  or release readiness.
- This pack does not replace user review, engine documentation, testing, or
  platform certification.

## Origin And Responsibility

Reference labels:

- `UPSTREAM-CCGS`: upstream MIT-licensed reference project.
- `CODEX-ADAPTATION`: Codex-specific structure and rewritten skill guidance.
- `AI-GENERATED`: content created or revised by Codex.

The skill pack was created by Codex and is provided as-is. Publishers and users
should review the content before relying on it for a specific project.
