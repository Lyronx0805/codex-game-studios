---
name: game-studio-full
description: Run a thorough full-studio game development workflow with director gates, specialists, release readiness, QA evidence, security, accessibility, localization, and live-ops review.
metadata:
  short-description: Full-studio game workflow
---

# Game Studio Full

Use the full dimension of the Codex Game Studio model for ambitious,
production-grade, multiplayer, live, or launch-bound games. This mode prioritizes
coverage and risk reduction over speed.

## First Move

Inspect the project stage, then state the gate being run: concept, systems,
architecture, production, QA, release, or live operations. Name only the role
lenses that matter for the current risk so the response provides thorough
coverage without excessive process detail.

Role lenses:

- creative director, technical director, producer;
- design, programming, art, audio, narrative, QA, release, localization leads;
- gameplay, engine, AI, network, tools, UI, analytics, devops specialists;
- systems, level, economy, UX, accessibility specialists;
- technical art, sound, writing, world-building specialists;
- performance, security, live-ops, and community lenses when relevant.

Operating style:

- run director gates at phase boundaries;
- require evidence for quality and release claims;
- separate blockers from advisory findings;
- recommend multi-agent or worktree execution when supported for high-risk
  launch, multiplayer, security, live-ops, or large cross-discipline reviews;
- create or update release, rollback, telemetry, accessibility, localization,
  player support, and community notes when relevant;
- pause for user decisions on scope, major design direction, architecture, or
  accepted launch risk;
- require evidence for high-confidence claims, and say when evidence is missing.

Common outputs:

- director-gate verdicts;
- specialist review findings;
- architecture, security, performance, accessibility, localization, and QA
  reports;
- release checklists, rollback plans, hotfix plans, patch notes, and live-ops
  risk summaries.

Useful paths:

```text
design/
docs/architecture/
production/epics/
production/sprints/
production/qa/
production/release/
production/live-ops/
production/community/
src/
assets/
tests/
```

When the full `game-studio` skill is installed beside this preset, read its
references for detailed routing, templates, and gates.
