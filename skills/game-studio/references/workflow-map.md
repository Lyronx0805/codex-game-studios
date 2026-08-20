# Workflow Map

The upstream Claude project exposes many slash commands. In Codex, use this map
to translate those commands into natural workflow requests. Do not tell the user
to run Claude commands unless they are actually using Claude Code.

## Onboarding And Navigation

| Upstream Intent | Codex Workflow |
| --- | --- |
| start | inspect project state, choose a dimension, recommend next steps |
| help | summarize available workflows for the current stage |
| project-stage-detect | classify the project stage from local artifacts |
| setup-engine | detect or record engine, version, platforms, conventions, budgets |
| adopt | audit an existing project and propose migration into the studio structure |

## Game Design

| Upstream Intent | Codex Workflow |
| --- | --- |
| brainstorm | explore concepts, pillars, player fantasy, core loop |
| map-systems | turn the concept into a systems index and dependency order |
| design-system | write or revise a system GDD |
| quick-design | produce a compact design note for a small feature |
| review-all-gdds | review all GDDs for consistency and gaps |
| propagate-design-change | identify and update docs/code affected by a design change |

## Art, UX, Audio, Narrative

| Upstream Intent | Codex Workflow |
| --- | --- |
| art-bible | define visual identity, asset style, constraints |
| asset-spec | create asset requirements, prompts, dimensions, usage notes |
| asset-audit | review assets for naming, format, coverage, and style fit |
| ux-design | define screen flows, HUD, input, readability, accessibility |
| ux-review | review UX specs against game pillars and accessibility tier |
| localize | plan or implement string externalization and locale QA |
| onboard | create onboarding or tutorial flow |

## Architecture

| Upstream Intent | Codex Workflow |
| --- | --- |
| create-architecture | write architecture overview and system boundaries |
| architecture-decision | write or revise an ADR |
| architecture-review | check coverage, consequences, dependencies, engine risk |
| create-control-manifest | compile accepted decisions into programmer rules |

## Production Planning

| Upstream Intent | Codex Workflow |
| --- | --- |
| create-epics | group implementation work by system or architecture layer |
| create-stories | break epics into testable implementation stories |
| sprint-plan | choose stories, order dependencies, identify risk |
| sprint-status | summarize progress and blockers |
| story-readiness | check a story before coding |
| estimate | estimate effort, confidence, and risk |

## Implementation And Closure

| Upstream Intent | Codex Workflow |
| --- | --- |
| dev-story | implement a story with the relevant design, ADR, and test context |
| code-review | review changed code for bugs and missing tests |
| story-done | verify acceptance criteria and update story status |
| tech-debt | identify and prioritize refactoring or cleanup |

## Reviews, QA, And Analysis

| Upstream Intent | Codex Workflow |
| --- | --- |
| design-review | review a design artifact |
| balance-check | inspect formulas, economies, difficulty, progression |
| content-audit | check narrative, assets, naming, tone, and coverage |
| scope-check | compare ambition to schedule and team capacity |
| perf-profile | profile or reason about performance bottlenecks |
| gate-check | run a phase readiness review |
| consistency-check | find contradictions across docs and systems |
| security-audit | review cheating, data safety, networking, secrets, saves |
| qa-plan | write a test plan |
| smoke-check | run or define rapid confidence checks |
| soak-test | plan longer stability testing |
| regression-suite | define repeatable regression coverage |
| test-setup | scaffold or choose a test framework |
| test-helpers | add fixtures or helpers |
| test-evidence-review | check whether evidence supports the claim |
| test-flakiness | diagnose unstable tests |

## Production And Release

| Upstream Intent | Codex Workflow |
| --- | --- |
| milestone-review | evaluate milestone readiness |
| retrospective | summarize lessons and process improvements |
| bug-report | write a clear repro and impact report |
| bug-triage | rank bugs by severity, risk, and release impact |
| reverse-document | document behavior from existing code or prototype |
| playtest-report | summarize observed playtest findings |
| release-checklist | create release readiness checklist |
| launch-checklist | final launch readiness review |
| changelog | developer-facing change summary |
| patch-notes | player-facing notes |
| hotfix | urgent fix plan and verification |
| day-one-patch | launch-adjacent patch planning |

## Team Orchestration

For team workflows such as combat, UI, audio, level, narrative, live-ops, QA,
polish, or release, choose the matching role lenses from `roles.md`, use the
selected dimension to decide review weight, and read `multi-agent-mode.md` when
real Codex subagents, parallel tasks, or worktrees are available. Coordinate the
work in phases: design, architecture, implementation, integration, validation,
and sign-off.
