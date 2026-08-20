---
name: game-studio-indie
description: Run a balanced indie game studio workflow for small-team planning, design docs, implementation stories, QA, and release prep.
metadata:
  short-description: Balanced indie game studio workflow
---

# Game Studio Indie

Use the indie dimension of the Codex Game Studio model. This is the default
size for most small games because it gives structure without heavy ceremony.

## First Move

Inspect the project stage from existing files, then choose the nearest useful
workflow: concept, system design, architecture, implementation, QA, or release.
If the user asks for a feature, turn it into a small design/implementation path
instead of starting with heavy documentation.

Role lenses:

- producer: scope, milestone, next action;
- creative/design: pillars, mechanics, UX, player fantasy;
- technical: architecture, engine conventions, performance;
- implementation: gameplay, UI, tools, data;
- content/audio/art: asset needs, feedback, tone;
- QA: tests, bugs, acceptance criteria.

Operating style:

- create lightweight but useful artifacts;
- use ADRs for important technical choices;
- break multi-file work into epics or stories;
- run focused design, architecture, code, and QA gates;
- use role lenses by default, with one optional review or QA subagent when the
  environment supports it and the task is risky enough;
- end with the next production step;
- keep explanations concise and define terms like GDD or ADR when needed.

Common outputs:

- concept docs and system GDDs;
- small ADRs for important technical choices;
- epics or stories for multi-file work;
- source changes and focused tests;
- QA notes, bug reports, release checklists, or patch notes.

Useful paths:

```text
design/gdd/
design/art/
design/ux/
docs/architecture/
production/epics/
production/sprints/
production/qa/
src/
tests/
```

When the full `game-studio` skill is installed beside this preset, read its
references for templates, role details, and quality gates.
