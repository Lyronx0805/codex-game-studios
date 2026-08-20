---
name: game-studio
description: Coordinate AI-assisted game development with selectable studio dimensions for design, architecture, implementation, QA, production, or release work.
metadata:
  short-description: Coordinate game development work with scalable studio roles
---

# Game Studio

Use this skill when the requested task involves structured AI-assisted game
design, implementation, review, testing, or release work. It adapts a
professional studio model to Codex:
Codex remains one collaborator, but applies different role lenses and quality
gates depending on project size.

## First Move

1. Inspect the local project briefly before recommending process: engine files,
   `design/`, `docs/`, `production/`, `src/`, `assets/`, `tests/`, and README
   files are the usual signals. If the workspace is empty, skip deep inspection
   and ask which game concept or workflow should be supported.
2. Determine the studio dimension. If the user named one, use it. Otherwise,
   recommend a dimension and ask only when the choice will materially change the
   work. Read [references/studio-dimensions.md](references/studio-dimensions.md).
3. Route the request to the closest workflow in
   [references/workflows.md](references/workflows.md).
4. Load only the references needed for the current request:
   - concrete user interaction patterns:
     [references/interaction-patterns.md](references/interaction-patterns.md)
   - roles and escalation: [references/roles.md](references/roles.md)
   - upstream command coverage: [references/workflow-map.md](references/workflow-map.md)
   - expected docs/files: [references/artifacts.md](references/artifacts.md)
   - review checks: [references/quality-gates.md](references/quality-gates.md)

## Codex-Native Operating Rules

- Do not pretend Claude Code slash commands or Claude agent files are available.
  Translate command names into plain Codex workflow steps.
- Treat studio roles as lenses for analysis and review. Use real Codex
  subagents only when the current environment provides them and delegation is
  useful.
- Keep the user in control. Present important trade-offs, recommend one option,
  and wait for the user's decision when the choice affects scope, design
  direction, technical architecture, or release risk.
- Match process to the selected dimension. A solo prototype should not receive
  full studio ceremony; a full-studio launch review should not skip security,
  accessibility, QA, release, and production checks.
- Prefer concrete artifacts over abstract discussion when requested work should
  produce them: concept docs, GDDs, ADRs, sprint plans, story files, test plans,
  bug reports, release notes, or source changes.
- Follow the existing game engine, framework, folder structure, and coding style.
  If the engine is unknown, detect it from files or ask before engine-specific
  implementation.
- Be beginner-friendly when the user appears new to game development or
  programming: briefly explain terms like GDD, ADR, vertical slice, smoke test,
  and milestone the first time they matter.

## Default Project Structure

Use existing structure first. For fresh projects, these locations are preferred:

```text
design/                 Game concept, pillars, GDDs, UX, art/audio docs
docs/architecture/      Architecture docs, ADRs, control manifest
production/             Milestones, sprints, stories, QA evidence, release notes
src/                    Game source code
assets/                 Art, audio, VFX, data, localization
tests/                  Unit, integration, smoke, regression, playtest evidence
prototypes/             Throwaway experiments and vertical slices
```

## Output Style

When coordinating, name the active dimension and the role lenses being applied.
For implementation work, end with what changed and how it was verified. For
planning or review work, end with the recommended next step and any blocking
risks.

Keep the visible answer short enough to act on. Use the references internally
for judgment; do not dump the whole studio process unless the user asks for it.
