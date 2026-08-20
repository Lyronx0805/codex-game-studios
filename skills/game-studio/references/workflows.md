# Workflows

Use these workflows as routes, not rigid commands. Pick the smallest workflow
that satisfies the request.

## Start Or Adopt

Use when the user is beginning a game or bringing an existing game into the
studio workflow.

Inspect:

- engine and language indicators;
- existing design docs;
- source and test files;
- prototypes;
- production docs.

Then classify the stage:

- no idea or vague idea: concept;
- concept but no system docs: concept/design;
- GDDs but no architecture: systems design;
- architecture and source: production;
- build/release artifacts: polish or release.

Output a short path with the next one to three steps.

## Concept And Design

Use for brainstorming, concept documents, systems maps, GDDs, art bibles, UX
specs, narrative foundations, and economy design.

Good outputs:

- `design/gdd/game-concept.md`
- `design/gdd/systems-index.md`
- `design/gdd/<system>.md`
- `design/art/art-bible.md`
- `design/audio/sound-bible.md`
- `design/ux/<screen>.md`
- `design/accessibility-requirements.md`

Quality checks:

- pillars are specific and useful for cutting scope;
- mechanics have rules, variables, edge cases, and tuning knobs;
- target player experience is concrete;
- UX and accessibility are considered before implementation.

## Architecture

Use before implementing broad systems or after design changes create technical
risk.

Good outputs:

- `docs/architecture/architecture.md`
- `docs/architecture/adr-NNN-short-title.md`
- `docs/architecture/control-manifest.md`
- `docs/architecture/tr-registry.yaml`

Quality checks:

- engine version and target platforms are known;
- ADRs include decision, consequences, alternatives, and implementation rules;
- cross-system dependencies are clear;
- performance, save/load, input, UI, localization, and testing impacts are
  considered when relevant.

## Production Stories

Use when turning designs into implementable work.

Good outputs:

- `production/epics/<epic>/EPIC.md`
- `production/epics/<epic>/<story>.md`
- `production/sprints/sprint-YYYY-MM-DD.md`
- `production/session-state/active.md`

Story checklist:

- one clear user or system outcome;
- links to the GDD requirement and ADR if available;
- acceptance criteria are testable;
- out-of-scope is explicit;
- dependencies are visible;
- test evidence is named before coding begins.

## Implementation

Use when the user asks to build or change game code.

Steps:

1. Load the relevant story, GDD, ADR, or source context.
2. Identify the role lenses and execution model required by the dimension.
3. For mid-size or full work, consider whether implementation, review, and QA
   should be split into separate subagent or worktree tracks.
4. Implement narrowly, following existing engine and code patterns.
5. Add or update tests when the change is logic-heavy or shared.
6. Run the closest available verification command.
7. Summarize files changed, behavior changed, and verification.

## QA And Review

Use for design review, code review, balance checks, content audits, smoke tests,
regression plans, playtest reports, and release readiness.

Good outputs:

- `production/qa/test-plan.md`
- `production/qa/evidence/<feature>.md`
- `production/bugs/<bug-id>.md`
- `production/release/release-checklist.md`
- `production/release/patch-notes.md`

Review style:

- lead with blockers and high-risk findings;
- separate "must fix" from "should consider";
- tie findings to player impact or shipping risk;
- name missing evidence instead of pretending confidence.
- use an independent review subagent when supported and the selected dimension,
  risk, or user request justifies the extra coordination.

## Release And Live Operations

Use for launch checklists, changelogs, hotfix planning, patch notes, telemetry,
community messaging, and rollback planning.

Quality checks:

- build version and target platforms are clear;
- smoke/regression results exist;
- known issues are categorized;
- rollback or hotfix path exists;
- player-facing notes are honest and readable;
- telemetry and privacy implications are considered.
