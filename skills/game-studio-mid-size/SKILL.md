---
name: game-studio-mid-size
description: Run a structured mid-size game studio workflow with department leads, story readiness checks, architecture review, QA planning, and risk tracking.
metadata:
  short-description: Structured mid-size game studio workflow
---

# Game Studio Mid-Size

Use the mid-size dimension of the Codex Game Studio model when a game has
multiple systems, several contributors, engine-specific complexity, or a real
production schedule.

## First Move

Inspect the project stage and identify the handoff that matters most: design to
architecture, architecture to stories, stories to implementation, implementation
to QA, or QA to release. Name the active department lenses so the user can see
why the process is heavier than solo mode.

Role lenses:

- producer;
- creative director;
- technical director;
- game design lead;
- programming lead;
- art, audio, narrative, UX, QA, and release leads as relevant;
- engine specialist;
- accessibility and localization when player-facing UI or text exists.

Operating style:

- maintain project stage and milestone context;
- align design and architecture before broad implementation;
- use story readiness and story-done checks;
- record risks, dependencies, owners, and acceptance criteria;
- propose two to four subagent or worktree tracks when the environment supports
  delegation and the work can be split cleanly;
- run department reviews at important handoffs;
- turn review findings into clear actions, owners, and next checks.

Common outputs:

- project-stage summary;
- system GDD or architecture review;
- ADR and control-manifest updates;
- story readiness checks;
- sprint plans, risk notes, QA plans, and release readiness reports.

Useful paths:

```text
design/gdd/
design/ux/
docs/architecture/
production/risks.md
production/epics/
production/sprints/
production/qa/
production/release/
src/
tests/
```

When the full `game-studio` skill is installed beside this preset, read its
references for detailed role routing, artifacts, workflows, and quality gates.
