# Upstream Analysis

This project was created after reviewing `donchitos/claude-code-game-studios`.
The upstream template is organized around a simulated game studio:

- leadership roles protect vision, technical direction, and schedule;
- department leads own design, programming, art, audio, narrative, QA, release,
  and localization;
- specialists handle engine, gameplay, AI, networking, UX, tools, audio,
  security, accessibility, live operations, and community work;
- workflow commands guide a project from concept through launch;
- hooks and path rules add guardrails around commits, pushes, assets, and
  project structure.

## Codex Translation

Codex skills work differently from Claude Code slash commands and agent files,
so this pack keeps the useful studio pattern and changes the mechanics:

- use skills as workflow routers instead of slash commands;
- use references for the large studio playbook;
- use role lenses by default and optional Codex subagents, tasks, or worktrees
  when the environment supports delegation;
- use manual quality gates instead of Claude hooks;
- scale the amount of process through studio dimensions.

## Why Dimensions Matter

A full studio workflow can help a large game, but it can slow down a solo
student or a game-jam prototype. The skill pack therefore ships with presets:

- Solo: fastest path with minimal documents.
- Indie: balanced structure for small projects.
- Mid-size: department-style checks for complex projects.
- Full: maximum coverage for ambitious or production-grade games.
