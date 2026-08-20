# Artifacts

Use existing files first. Create new artifacts only when they help the current
work or the selected studio dimension requires them.

## Preferred Paths

```text
design/gdd/game-concept.md
design/gdd/systems-index.md
design/gdd/<system>.md
design/art/art-bible.md
design/audio/sound-bible.md
design/ux/<screen>.md
design/accessibility-requirements.md

docs/architecture/architecture.md
docs/architecture/adr-NNN-short-title.md
docs/architecture/control-manifest.md
docs/architecture/tr-registry.yaml

production/epics/<epic>/EPIC.md
production/epics/<epic>/<story>.md
production/sprints/sprint-YYYY-MM-DD.md
production/qa/test-plan.md
production/qa/evidence/<feature>.md
production/bugs/<bug-id>.md
production/release/release-checklist.md
```

## Lightweight Concept Template

Use for solo and early indie work.

```markdown
# Game Concept

## Pitch

## Player Fantasy

## Core Loop

## Pillars

## Main Mechanics

## Scope

## Risks

## Next Prototype
```

## System GDD Template

Use when a mechanic needs enough detail for implementation.

```markdown
# <System Name>

## Purpose

## Player Experience

## Rules

## Inputs And Outputs

## Variables And Tuning

## Edge Cases

## Dependencies

## Acceptance Criteria
```

## ADR Template

Use for important technical choices.

```markdown
# ADR-NNN: <Decision Title>

## Status

Accepted | Proposed | Superseded

## Context

## Decision

## Alternatives Considered

## Consequences

## Implementation Rules

## Verification
```

## Story Template

Use when implementation work should be tracked.

```markdown
# <Story Title>

Status: Ready
Owner Lens: <role>
Related Design: <path or none>
Related ADR: <path or none>

## Outcome

## Acceptance Criteria

- [ ] 

## Out Of Scope

## Dependencies

## Test Evidence
```

