# Studio Dimensions

Choose the smallest studio dimension that provides useful structure.
Upscale only when project complexity, risk, or user preference justifies it.

## Dimension Table

| Dimension | Role Lenses | Execution Default | Best For | Review Weight | Typical Output |
| --- | ---: | --- | --- | --- | --- |
| Solo | 3 | single-agent lenses | first games, class projects, game jams, prototypes | light | short plan, checklist, direct implementation, basic tests |
| Indie | 6 | lenses, optional review subagent | small commercial or portfolio games | balanced | concept docs, system GDDs, ADRs, stories, QA notes |
| Mid-size | 12 | optional multi-agent tracks | multi-system games, team projects, serious production | structured | department reviews, sprint plans, risk register, quality gates |
| Full | 25+ | multi-agent recommended when available | ambitious games, multiplayer/live games, launch reviews | thorough | director sign-offs, specialist reviews, release readiness, evidence |

## Solo Dimension

Use when speed matters more than ceremony.

Core lenses:

- designer: fun, mechanics, player clarity, scope;
- programmer: engine fit, implementation plan, tests;
- QA/release: obvious bugs, smoke test, readiness.

Default behavior:

- ask few questions;
- write lightweight notes instead of full documents unless requested;
- prefer playable prototypes and tight feedback loops;
- use one review pass before calling work complete;
- keep execution single-agent unless the user explicitly requests a separate
  review agent.

## Indie Dimension

Use as the default when the user does not specify a size and the project looks
like a normal solo or small-team game.

Core lenses:

- producer: scope, milestones, next actions;
- creative/design: pillars, mechanics, UX, player fantasy;
- technical: architecture, engine conventions, performance;
- implementation: gameplay, UI, tools, data;
- content/audio/art: assets, style, narrative, feedback;
- QA: tests, bugs, acceptance criteria.

Default behavior:

- create enough docs to keep the project coherent;
- use ADRs for important technical choices;
- break work into stories when implementation spans several files or systems;
- run focused design/code/QA review gates;
- use role lenses by default, and optionally propose one reviewer subagent when
  risk, scope, or release prep makes independent review useful.

## Mid-Size Dimension

Use when the project has multiple subsystems, several contributors, engine
specialists, or a schedule that needs tracking.

Core lenses:

- producer;
- creative director;
- technical director;
- game design lead;
- programming lead;
- art/audio/narrative leads as needed;
- QA lead;
- release manager;
- engine specialist;
- accessibility/localization when player-facing UI or text exists.

Default behavior:

- maintain a visible project stage;
- require design and architecture alignment before broad implementation;
- use story readiness and story-done checks;
- record risks, dependencies, and acceptance criteria;
- propose two to four task tracks when subagent or worktree tools are available
  and the work separates cleanly across design, technical, implementation, QA,
  or release concerns.

## Full Dimension

Use for high-risk projects: online games, live operations, launch reviews,
security-sensitive systems, larger teams, or user-requested thoroughness.

Core lenses include all mid-size roles plus specialists:

- gameplay, engine, AI, network, tools, UI, analytics, devops;
- systems, level, economy, UX, accessibility;
- art direction, technical art, sound, narrative, localization;
- QA testing, performance, security, community, live operations.

Default behavior:

- run director gates at phase boundaries;
- require evidence for quality claims;
- separate advisory findings from blockers;
- create release, rollback, telemetry, accessibility, and support plans when
  relevant;
- recommend multi-agent execution when supported for high-risk launch,
  multiplayer, security, live-ops, or large cross-discipline reviews; fall back
  to role lenses when delegation tools are unavailable.

## Review Modes

Dimensions describe studio size. Review mode describes strictness.

- `solo`: only essential checks.
- `lean`: phase gates and high-risk reviews.
- `full`: all relevant domain reviews.

If the user asks for a full studio but "lean review", keep the role coverage
wide but avoid repeating formal gates.
