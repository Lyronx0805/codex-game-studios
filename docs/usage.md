# Usage

Reference label: `CODEX-ADAPTATION`

## Install

Copy one or more skill folders into the Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/game-studio ~/.codex/skills/
cp -R skills/game-studio-solo ~/.codex/skills/
cp -R skills/game-studio-indie ~/.codex/skills/
cp -R skills/game-studio-mid-size ~/.codex/skills/
cp -R skills/game-studio-full ~/.codex/skills/
```

Restart Codex or reload skills after copying.

## Choose A Dimension

Use `game-studio` when Codex should choose or recommend a dimension:

```text
Use $game-studio to plan a game project.
```

Use a preset when the studio size is already known:

```text
Use $game-studio-solo to prototype the player jump.
Use $game-studio-indie to plan a crafting system.
Use $game-studio-mid-size to organize production for a multi-system demo.
Use $game-studio-full to run a launch readiness review.
```

The dimension is the main feature. It controls how much process the skill
applies:

- select `solo` for speed;
- select `indie` for useful structure without excessive ceremony;
- select `mid-size` for games with several systems or contributors;
- select `full` when launch, multiplayer, live operations, security, or release
  risk needs deeper review.

## Choose An Execution Model

The skill uses role lenses by default. One Codex agent can examine the game as a
designer, programmer, producer, QA lead, release manager, or specialist without
starting extra tasks.

Multi-agent execution is optional. When the Codex environment supports
subagents, parallel tasks, or worktrees, larger dimensions can split work into
separate tracks:

- `solo`: keep one Codex agent unless an independent review is explicitly
  requested;
- `indie`: add one reviewer or QA subagent when risk justifies it;
- `mid-size`: split design, technical, implementation, QA, or release tracks
  when work can be separated cleanly;
- `full`: recommend multi-agent coordination for launch, multiplayer, security,
  live-ops, or broad specialist reviews.

Example requests:

```text
Use $game-studio-mid-size with multi-agent mode if supported to plan and review this combat system.
Use $game-studio-full to run a launch readiness review with separate QA and release tracks if available.
Use $game-studio-solo without subagents to prototype the inventory interaction quickly.
```

## Example Requests

Concept:

```text
Use $game-studio-indie to turn a cozy exploration idea into a concept doc.
```

Architecture:

```text
Use $game-studio-mid-size to create ADRs for save/load and inventory.
```

Implementation:

```text
Use $game-studio-solo to implement a dash mechanic in this Godot project.
```

QA:

```text
Use $game-studio-full to review multiplayer release risks and make a QA plan.
```

Existing project:

```text
Use $game-studio to inspect this repo and report the current game-development stage.
```

## Recommended Project Folders

The skill works with existing structure first. For new projects, these folders
are recommended:

```text
design/
docs/architecture/
production/
src/
assets/
tests/
prototypes/
```

## Expected Behavior

The skill usually:

1. inspect the project briefly;
2. choose or confirm a studio dimension;
3. choose role-lens or optional multi-agent execution;
4. apply the relevant role lenses or task tracks;
5. create, edit, review, or implement the requested artifact;
6. summarize what changed and what should happen next.

## Human Review

Reference label: `AI-GENERATED`

This skill pack was created by Codex. Generated plans, documents, code changes,
and release advice should be reviewed before reliance.
