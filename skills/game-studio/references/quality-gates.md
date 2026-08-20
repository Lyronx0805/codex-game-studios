# Quality Gates

Use gates to prevent obvious mistakes without turning every request into a
committee meeting. Scale the number of gates to the selected dimension.

## Design Gate

Ask:

- Does this serve the game pillars?
- Is the player action clear?
- Are rules, variables, and edge cases defined?
- Is the scope small enough for the current milestone?
- Are accessibility and UX concerns visible?

Block only when the design is too vague to implement or conflicts with a core
pillar without user approval.

## Architecture Gate

Ask:

- Is the engine/version known?
- Does the approach match engine conventions?
- Are data flow, ownership, save/load, and lifecycle clear?
- Are performance-sensitive paths identified?
- Are alternatives and consequences recorded for major decisions?

Block when implementation would require guessing a major architecture decision.

## Story Readiness Gate

Ask:

- Is there one clear outcome?
- Are acceptance criteria testable?
- Are dependencies visible?
- Is out-of-scope explicit?
- Is verification defined before coding?

Block when the work cannot be completed without inventing requirements.

## Code Review Gate

Ask:

- Does the change follow local patterns?
- Is game state ownership clear?
- Are numbers data-driven when tuning matters?
- Are frame-time, allocation, or network costs acceptable?
- Are tests or manual evidence appropriate for the risk?

For user-requested reviews, lead with findings ordered by severity.

## QA Gate

Ask:

- Are core happy paths covered?
- Are edge cases and failure cases covered?
- Are regressions likely in adjacent systems?
- Can a human reproduce the validation steps?
- Is playtest evidence needed for feel, UX, or balance?

## Release Gate

Ask:

- Is the build version known?
- Are blocking bugs resolved or explicitly accepted?
- Are release notes accurate?
- Is rollback or hotfix response clear?
- Are telemetry, privacy, accessibility, localization, and support impacts
  considered when relevant?

## Verdicts

Use simple verdicts:

- `PASS`: ready to proceed.
- `PASS WITH RISKS`: proceed if the user accepts named risks.
- `NEEDS WORK`: fix before proceeding.
- `BLOCKED`: missing information or dependency prevents honest progress.

