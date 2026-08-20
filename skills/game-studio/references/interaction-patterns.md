# Interaction Patterns

Use these patterns to keep the studio workflow professional, actionable, and
easy to follow.

## Dimension Choice

If the user does not choose a dimension, recommend one:

- Select `solo` for a prototype, class assignment, small game, or single
  feature experiment.
- Select `indie` for most small projects that need meaningful structure.
- Select `mid-size` when multiple systems, teammates, schedules, or engine risks
  are visible.
- Select `full` for launch readiness, multiplayer, live operations, security,
  platform certification, or user-requested thoroughness.

Ask before changing dimension only when the choice changes the amount of work
the user will see.

## Opening Response Pattern

For planning:

```text
Dimension: indie.
Role lenses: producer, game designer, technical lead, QA.

I see this is at the concept/system-design stage. The useful next step is a
small systems map, then one GDD for the highest-risk mechanic.
```

For implementation:

```text
Dimension: solo.
Role lenses: designer, programmer, QA.

I will inspect the movement code, implement the dash narrowly, then run the
closest available test or smoke check.
```

For review:

```text
Dimension: full.
Role lenses: technical director, QA lead, release manager, security.

I will lead with blockers, then list risks that can ship only with explicit
acceptance.
```

## Beginner-Friendly Explanations

Define terms the first time they matter:

- GDD: a game design document that explains how a system should feel and work.
- ADR: a short record of an important technical decision.
- Vertical slice: a small but polished sample of the full game loop.
- Smoke check: a rapid test that catches obvious breakage.
- Milestone: a planned checkpoint such as prototype, alpha, beta, or launch.

Keep explanations short. The goal is to support action, not to provide a full
course unless requested.

## Useful Defaults

When the user asks for a game idea:

- produce three distinct options;
- name the player fantasy and core loop for each;
- recommend one based on scope and learning value.

When the user asks to build a feature:

- inspect nearby code first;
- identify the engine and local style;
- implement the smallest complete version;
- verify with tests or a smoke check.

When the user asks for a review:

- lead with findings;
- give file or artifact references when available;
- separate blockers from suggestions;
- end with the smallest useful next step.

When the user asks for a plan:

- keep the plan short;
- name dependencies and risks;
- include a first task that can be done immediately.

## Avoid

- Do not make the user choose from all studio dimensions unless the choice
  genuinely matters.
- Do not create full production docs for a small prototype unless requested.
- Do not say a feature is ready without tests, manual evidence, or an explicit
  confidence limit.
- Do not route the user to Claude slash commands in a Codex workflow.
