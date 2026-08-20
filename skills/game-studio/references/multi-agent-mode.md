# Hybrid Execution

Use role lenses as the baseline execution model. They are portable, fast, and
work in every Codex skill environment. Use real Codex subagents, parallel tasks,
or worktrees only when the current environment exposes those capabilities and
the game-development task benefits from independent work.

## Dimension Defaults

| Dimension | Default Execution | Multi-Agent Guidance |
| --- | --- | --- |
| Solo | Single Codex agent with role lenses | Do not spawn subagents unless the user explicitly asks for an independent review. |
| Indie | Single Codex agent with role lenses | Optionally propose one review or QA subagent for risky features, larger refactors, or release prep. |
| Mid-size | Role lenses with optional delegation | Propose two to four task tracks when design, architecture, implementation, QA, or release work can be split cleanly. |
| Full | Multi-agent recommended when available | Propose a coordinated director, technical, implementation, QA, and release review structure for high-risk work. |

## Use Multi-Agent Execution When

- the environment provides subagent, parallel task, thread, or worktree tools;
- the task has separable tracks with clear ownership;
- independent review would likely catch meaningful design, code, QA, release,
  security, accessibility, localization, or live-ops risks;
- files or branches can be isolated enough to avoid confusing merges;
- the user requested multi-agent execution, or the selected dimension is
  `mid-size` or `full` and the benefit is clear.

## Stay With Role Lenses When

- the task is small, exploratory, or mostly conversational;
- requirements are still ambiguous;
- the environment does not expose safe delegation tools;
- several agents would edit the same files without a clear merge plan;
- the coordination cost would be larger than the likely quality improvement.

## Coordination Contract

Before launching additional agents, state the delegation plan and get
confirmation unless the user has already requested that exact split. Include:

- active dimension;
- proposed agents or task threads;
- each agent's role, objective, inputs, and output format;
- write boundaries and expected touched paths;
- merge or synthesis plan;
- stop condition and verification plan.

The coordinating Codex agent remains responsible for final synthesis. Do not
paste unreviewed agent output directly into the final answer. Reconcile
conflicts, check assumptions, run verification when possible, and report which
parts were verified.

## Suggested Splits

Indie:

- primary agent: implementation or artifact drafting;
- optional reviewer: design/code/QA check after the draft exists.

Mid-size:

- design/production agent: requirements, scope, risks, acceptance criteria;
- technical agent: architecture, engine fit, test strategy;
- implementation agent: focused source changes;
- QA/release agent: tests, repro steps, release risks.

Full:

- director review: creative, technical, and production alignment;
- specialist implementation or analysis: gameplay, engine, network, UI,
  performance, security, accessibility, localization, or live operations;
- QA/release review: evidence, blockers, rollback, hotfix, support, and notes.

## Output Pattern

When multi-agent execution is used, summarize:

1. which agents or task tracks ran;
2. what each track produced;
3. conflicts or trade-offs found;
4. final decision or integrated change;
5. verification performed and remaining risks.
