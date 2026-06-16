---
name: gameplay-evolution-review
description: Use when asked to simulate, evolve, playtest, balance, or evaluate a game/prototype's progression, economy, pacing, player personas, failure routes, exploits, or long-run gameplay experience.
---

# Gameplay Evolution Review

## Overview

Review games by evolving the actual system first, then judging the experience through the roles, goals, and metrics that fit that game. Evidence beats vibes: run the game, scripts, replays, bots, or headless simulation before making design claims whenever the project provides a way to do so.

This skill applies to many game shapes: prototypes, board/card games, RPGs, roguelikes, strategy games, sims, idle/incremental games, puzzle games, action loops, narrative systems, multiplayer economies, and gamified products. Adapt the scenario set and measurements to the actual design instead of forcing a business-simulator template.

Use references selectively:

- `references/review-modes.md` when choosing review scope or depth.
- `references/genre-profiles.md` when adapting scenarios and metrics to a game type.
- `references/severity-rubric.md` when prioritizing findings.
- `references/evidence-templates.md` when shaping scenario tables, phase snapshots, before/after tuning, UI truth checks, exploit reproduction, or multi-seed comparisons.
- `references/studio-workflow-notes.md` for larger reviews that benefit from lightweight studio-style passes.

Optional helper: `scripts/make_review_plan.py` can generate a first-pass checklist from a short brief. Use it as planning scaffolding only; it does not replace reading the project, running the game, or collecting evidence.

## Workflow

1. Read the local instructions and project map first: `AGENTS.md`, `README`, package scripts, core game/state/rules/data files, test fixtures, scenario definitions, save/replay formats, content tables, and recent dirty diff. Treat dirty worktree changes as user-owned: inspect them, but do not revert, normalize, or edit unrelated changes unless explicitly asked.
2. Choose the review mode and genre profile. Use `references/review-modes.md` and `references/genre-profiles.md` for non-trivial reviews, hybrid games, unclear scope, or when the user asks for balance, UX, exploit, regression, or long-run evaluation.
3. Identify the game type and evaluation target before judging it:
   - primary loop and session length
   - win/loss or success/failure conditions
   - player verbs and constraints
   - key resources, timers, scores, units, cards, levels, encounters, narrative flags, or social states
   - intended audience and skill curve when stated
4. State the expected arc before looking at fresh results: early learning, first pressure, viable choices, midgame changes, failure routes, success routes, late-game/end-state pressure, and what "healthy" should feel like for this genre.
5. Run real evolution. Prefer existing commands such as `npm run diagnose`, `npm run simulate`, `npm test`, replay tools, solver scripts, bot matches, automated playtests, telemetry fixtures, or purpose-built scenario runners. If no tool exists, inspect the game loop and create only a throwaway local probe when necessary; keep probes in `/tmp` or another clearly temporary path, do not update baselines from probes, and delete or disclose any leftovers.
6. Cover scenario classes, not just one happy path. Choose the relevant routes and rename them to match the game:
   - no-action, random, or minimum-skill baseline
   - obvious bad route or misunderstood-player route
   - cautious/safe route
   - intended balanced route
   - aggressive/risky route
   - optimizer, solver, speedrun, or min-max route
   - exploit, degenerate loop, stall, farming, or infinite-combo route
   - stress route for late-game load, scarce resources, high difficulty, content exhaustion, multiplayer pressure, or many turns/ticks
   If any class is skipped, name the missing route and reason in `Gaps`.
7. Record phase snapshots, not only the final state. Capture opening, first decision, first failure/success, midgame, late/endgame, peak values, and the exact bottleneck, gate, exploit, or comprehension break blocking progression.
8. **REQUIRED SUB-SKILL:** Use `playwright` and inspect at least one real browser/play flow when the review scope includes player comprehension, UI feedback, layout, onboarding, or interaction flow. If the browser flow cannot run, record that in `Gaps`; do not replace browser observation with code inference.
9. Run regression checks after behavior changes or when validating that a review-only pass did not alter behavior. Use commands such as tests, snapshot checks, build checks, replay validation, deterministic seed checks, or golden-output comparisons for this lane.
10. Review through role lenses, then synthesize into prioritized findings. For high-impact balance or design claims, map the claim to at least one reference lens below and keep observed behavior separate from inferred player psychology. Use `references/severity-rubric.md` for high-priority or multi-issue reports.

## Role Lenses

Use the roles that fit the game; do not force all of them if the task is small.

| Lens | Ask |
| --- | --- |
| First-time player | Do I understand what to do, why it worked, and why I failed? |
| Optimizer | Is there one dominant route, exploit, or obvious solved strategy? |
| Casual player | Can I recover from imperfect decisions without reading source code? |
| Systems designer | Are economy, risk, pacing, gates, and feedback loops coherent? |
| Content designer | Are levels, encounters, cards, units, events, quests, or prompts varied and readable? |
| Competitive player | Are matchups, fairness, counterplay, and skill expression credible? |
| Accessibility reviewer | Can players with different input, reading, timing, or sensory needs understand and act? |
| Live-ops operator | Which metrics would I monitor, and what tuning lever would I pull? |
| Domain expert | Does the game model the real-world subject in a believable way? |
| UI/telemetry reviewer | Does the screen explain the engine's actual state and next action? |
| Technical reviewer | Are scripts, tests, snapshots, and code boundaries trustworthy? |

## Reference Lenses

Use these as compact evaluation rulers; do not let them replace real playtesting or simulation.

| Lens | Use It For | Question |
| --- | --- | --- |
| MDA | Link mechanics to emergent dynamics and intended feeling. | Produce: rule -> observed dynamic -> player-facing effect. |
| GameFlow | Check clear goals, feedback, challenge/skill balance, control, concentration, immersion, and social fit when relevant. | Produce: goal/feedback/challenge note tied to a scenario phase. |
| PLAY/HEP/GAP | Review playability, learnability, approachability, recovery, and first-session friction. | Produce: first-session action, failure, recovery, and learning note. |
| Telemetry discipline | Ground conclusions in behavior plus context before interpreting motivation. | Produce: scenario, phase, metric, condition, and observed behavior. |
| UX heuristics | Check visibility, consistency, real-world match, control, and error recovery. | Produce: visible UI state -> true engine state -> next-action clarity. |
| Difficulty curve | Check whether challenge rises through new decisions, tighter constraints, or deeper mastery. | Produce: phase -> challenge source -> player tool/counterplay -> result. |
| Dominant strategy analysis | Detect solved play, degenerate loops, farming, stalling, or risk-free rewards. | Produce: strategy -> why it dominates -> cost/risk missing -> tuning lever. |

## Game UI/UX Checkpoints

When UI/player comprehension is in scope, inspect the real screen and cover the relevant checkpoints:

- Player question: can the player answer "what is happening, why, and what should I do next?" within the current phase?
- HUD/information hierarchy: primary pressure, resources, goals, warnings, and next actions are visible without making every metric equally loud.
- Feedback timing: after a decision, the UI shows what changed, why it changed, and whether the result was good, risky, blocked, or recoverable.
- FTUE/approachability: in the first minute or first phase, the player can form a goal, act once, see feedback, fail safely, and learn a next move.
- Control clarity: available actions, disabled actions, costs, risks, prerequisites, and undo/recovery paths are discoverable before commitment.
- Readability/accessibility: text, contrast, spacing, color dependence, icon meaning, dense panels, and small-screen layout support repeated play.
- Engine truth: visible gates, warnings, progress, timers, and failure states match the underlying game state and code path.

## Review Dimensions

Check these dimensions against evidence:

- Core loop clarity: the player makes meaningful, repeated decisions.
- Progression: unlocks are paced, visible, and backed by believable evidence.
- Goal structure: objectives, subgoals, win/loss states, and optional mastery goals are legible.
- Difficulty curve: challenge increases through mechanics, constraints, opponents, speed, information, scarcity, or execution demands that the player can learn.
- Resource model: currencies, health, time, energy, cards, actions, cooldowns, inventory, units, information, score, or social capital avoid runaway triviality unless intended.
- Risk and failure: bad routes fail for understandable reasons; failure states match the game model and offer appropriate recovery or restart paths.
- Trade-offs: safe, cheap, fast, powerful, risky, expressive, and scalable routes each have real costs.
- Feedback: UI metrics and HUD signals explain what changed, why it changed, and what to try next.
- Pacing: early game teaches, midgame varies, late game pressures or resolves without becoming pure repetition.
- Content variety: encounters, levels, cards, events, units, choices, story beats, or puzzles avoid stale repetition unless that repetition is the intended mastery loop.
- Agency and fairness: outcomes feel traceable to player choices, skill, luck, hidden information, or authored constraints in the intended proportions.
- Exploitability: one-button loops, dominant builds, infinite resources, farming stalls, softlocks, solved openings, or risk-free strategies are called out.
- Instrumentation: diagnostics measure phase snapshots, peaks, gates, and bottlenecks.
- Regression safety: behavior-changing observations are tied to tests, snapshots, or reproducible commands.

## Evidence And Metrics

Use metrics that match the game, and explain why they matter. Common examples:

| Game Shape | Useful Evidence |
| --- | --- |
| Puzzle | solve rate, moves, hints, dead states, branching factor, first-error point, reset count |
| Action | time-to-kill, damage taken, deaths, input windows, cooldown use, enemy pressure, readability failures |
| RPG/roguelike | build path, encounter outcomes, attrition, loot quality, power spikes, death causes, run variance |
| Strategy/4X/tactics | expansion rate, economy/resource curve, unit trades, map control, counterplay, snowball point |
| Card/board | draw variance, hand quality, dominant combos, tempo, stalemate routes, first-player advantage |
| Idle/incremental | time-to-upgrade, prestige/reset value, compounding rate, wait walls, automation unlock pacing |
| Narrative/social | choice visibility, state flags, consequence timing, branch convergence, character/world consistency |
| Multiplayer/live | matchmaking fairness, churn moments, griefing/exploit routes, queue/session length, economy inflation |

If the project has its own telemetry or vocabulary, use that vocabulary in the report.

For broader genre-specific checks, consult `references/genre-profiles.md`.

## Output Shape

Keep the report concise and evidence-led:

1. Expected arc: a short hypothesis before results.
2. Commands run: include exact commands and whether they passed.
3. Scenario table: use columns that fit the game. Default columns are `Route`, `Duration/Phase`, `Progress/Score/Outcome`, `Key Resources`, `Risk/Failure/Quality`, and `Notable Bottleneck`.
4. Expected vs observed: note surprising bottlenecks, dominant strategies, missing pressure, or failed hypotheses.
5. Role review: short bullets by relevant lenses.
6. Findings: prioritize by player impact. For each high-priority finding, include `Evidence`, `Lens`, `Code path`, `Lever`, and `Expected side effect`; UI/UX findings need browser observation, screenshot, or UI panel evidence when available.
7. Recommendations: 2-4 tuning paths with trade-offs, not a giant backlog.
8. Gaps: state what was not verified, missing scenario classes and reasons, browser playtesting gaps, or temporary probes that could not be cleaned up.

Use `references/evidence-templates.md` when a table would clarify route comparison, phase snapshots, tuning before/after, UI truth, exploit reproduction, or multi-seed variance.

## When The Game Cannot Run

If the game cannot run or no executable flow exists:

- Do a static or paper review from rules, code paths, content data, tuning constants, UI screens, and docs.
- Simulate a short path manually when the rules are clear enough.
- Mark claims as `Observed`, `Static evidence`, or `Inference`.
- Put missing runtime, browser, seed, replay, or scenario evidence in `Gaps`.
- Do not present static inference as playtest evidence.

See `references/review-modes.md` for `Static Or Paper Review`.

## Project-Specific Adaptation

Infer local defaults from the repository before reviewing:

- Prefer the repo's named diagnostic, simulation, replay, test, snapshot, seed, or bot-match commands over generic commands.
- Read the code paths that own rules, state transitions, content data, tuning constants, scoring, save/load, UI panels, and telemetry before attributing behavior.
- Translate generic terms into the project's own nouns: resources might be money, mana, health, workers, cards, turns, actions, reputation, morale, clues, territory, or time.
- Check whether UI-visible gates, warnings, timers, scores, progress bars, cooldowns, and failure states match the underlying engine gates.
- For deterministic games, use fixed seeds or known fixtures when possible. For stochastic games, compare multiple seeds/runs before calling something a balance problem.
- For multiplayer or competitive games, separate individual skill expression, matchmaking/fairness, network/session behavior, and economy/live-ops effects.

## Common Mistakes

- Do not review only from intuition; run or inspect the actual system.
- Do not treat the final state as the whole journey; phase snapshots matter.
- Do not judge balance from only the intended route; compare low-skill, cautious, risky, optimized, exploit, and stress routes where relevant.
- Do not invent hidden mechanics; trace code paths for gates, failures, and metrics.
- Do not report a finding without a source: cite a script, command output, function, data constant, state field, or UI panel when the repo makes that possible.
- Do not suggest tuning without naming the lever and expected side effect.
- Do not edit the game during review unless the user asks for fixes.
- Do not treat regression checks as gameplay evaluation; they prove stability, not fun or balance.
- Do not quote a framework name as proof; use it to structure evidence from the actual game.
- Do not force business metrics like customers, revenue, or cash flow onto games that use different goals and resources.
