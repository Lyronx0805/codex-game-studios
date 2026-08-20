# Role Lenses

Use roles as thinking lenses. Announce only the roles that help explain the
recommendation.

## Role Lens Or Real Agent

A role lens is a viewpoint used by the current Codex agent. It is the default
because it is fast, portable, and works without special tooling.

A real agent is a separate Codex task or subagent, optionally using an isolated
worktree when the current environment supports it. Use real agents only when a
task is large enough to benefit from independent work or review. Keep one
coordinating agent responsible for merging conclusions and verifying the final
result.

For detailed delegation rules, use `multi-agent-mode.md`.

## Leadership

| Role | Owns | Use When |
| --- | --- | --- |
| Creative Director | pillars, tone, player fantasy, identity | major creative direction, feature cuts, cross-discipline conflicts |
| Technical Director | architecture, engine fit, performance strategy | major technical choices, refactors, multiplayer, persistence, build risk |
| Producer | schedule, scope, milestones, dependencies | planning, triage, sprint work, risk management |

## Department Leads

| Role | Owns | Use When |
| --- | --- | --- |
| Game Designer | mechanics, loops, balance, progression | GDDs, formulas, tuning, system interactions |
| Lead Programmer | code architecture, interfaces, review | implementation plans, code quality, test strategy |
| Art Director | visual identity, asset standards | art bible, asset reviews, UI visual cohesion |
| Audio Director | music, SFX direction, mix priorities | audio bible, event lists, feedback clarity |
| Narrative Director | story, setting, characters, lore | quests, dialogue, world rules, tone conflicts |
| QA Lead | test strategy, bug triage, quality evidence | test plans, release readiness, regression |
| Release Manager | builds, versioning, changelogs, rollback | launches, patches, hotfixes |
| Localization Lead | strings, locale testing, translation flow | UI text, multi-language support |

## Specialists

| Role | Owns |
| --- | --- |
| Gameplay Programmer | moment-to-moment mechanics and systems |
| Engine Programmer | low-level engine systems, performance-sensitive foundations |
| AI Programmer | NPC behavior, pathfinding, decision systems |
| Network Programmer | replication, authority, matchmaking, online safety |
| Tools Programmer | editor tools, pipelines, debug utilities |
| UI Programmer | screens, widgets, data binding, input handling |
| Systems Designer | formulas, loops, rules, economies |
| Level Designer | spaces, pacing, encounter flow |
| Economy Designer | resources, rewards, stores, progression |
| UX Designer | flows, readability, controls, accessibility interaction |
| Technical Artist | shaders, VFX, asset pipeline, optimization |
| Sound Designer | audio events, SFX lists, mix notes |
| Writer | dialogue, item text, lore entries |
| World Builder | setting rules, factions, geography, history |
| QA Tester | test cases, repro steps, edge cases |
| Performance Analyst | profiling, budgets, optimization recommendations |
| DevOps Engineer | CI, builds, deployment automation |
| Analytics Engineer | telemetry events, dashboards, experiment design |
| Security Engineer | anti-cheat, exploit prevention, secrets, save/network security |
| Accessibility Specialist | remapping, contrast, captions, text scale, assistive options |
| Live-Ops Designer | events, seasons, retention, economy updates |
| Community Manager | player-facing communication and feedback synthesis |

## Engine Specialists

Apply the matching specialist lens when the engine is known:

- Godot: scene/node structure, signals, GDScript/C# patterns, resources.
- Unity: MonoBehaviour vs DOTS, prefabs, Addressables, URP/HDRP, UI Toolkit.
- Unreal: Actor/Component design, Blueprint/C++ boundary, GAS, replication,
  UMG/CommonUI.

## Conflict Handling

When roles disagree, surface the real trade-off:

1. state the decision;
2. list two or three options;
3. explain impact on fun, scope, tech risk, schedule, and quality;
4. recommend one option;
5. let the user decide before changing direction.
