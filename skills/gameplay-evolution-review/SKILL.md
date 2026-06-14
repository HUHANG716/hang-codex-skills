---
name: gameplay-evolution-review
description: Use when asked to simulate, evolve, playtest, balance, or evaluate a game/prototype's progression, economy, pacing, player personas, failure routes, exploits, or long-run gameplay experience.
---

# Gameplay Evolution Review

## Overview

Review games by evolving the actual system first, then judging the experience through multiple player and operator roles. Evidence beats vibes: run the game, scripts, or headless simulation before making design claims whenever the repo provides a way to do so.

## Workflow

1. Read the local instructions and project map first: `AGENTS.md`, `README`, package scripts, core game/state/data files, and recent dirty diff. Treat dirty worktree changes as user-owned: inspect them, but do not revert, normalize, or edit unrelated changes unless explicitly asked.
2. State the expected arc before looking at fresh results: early pressure, viable choices, midgame unlocks, failure routes, success routes, and what "healthy" should feel like.
3. Run real evolution. Prefer existing commands such as `npm run diagnose`, `npm run simulate`, replay tools, automated playtests, or purpose-built scenario runners. If no tool exists, inspect the game loop and create only a throwaway local probe when necessary; keep probes in `/tmp` or another clearly temporary path, do not update baselines from probes, and delete or disclose any leftovers.
4. Cover scenario classes, not just one happy path:
   - no-action baseline
   - obvious bad route
   - conservative/safe route
   - balanced route
   - min-max or exploit route
   - stress route for late-game load, failures, or scarce resources
   If any class is skipped, name the missing route and reason in `Gaps`.
5. Record phase snapshots, not only the final state. Capture early, mid, late, peak values, and the exact bottleneck or gate blocking progression.
6. **REQUIRED SUB-SKILL:** Use `playwright` and inspect at least one real browser/play flow when the review scope includes player comprehension, UI feedback, layout, or interaction flow. If the browser flow cannot run, record that in `Gaps`; do not replace browser observation with code inference.
7. Run regression checks after behavior changes or when validating that a review-only pass did not alter behavior. Use commands such as `npm run snapshot:check`, tests, or build checks for this lane.
8. Review through role lenses, then synthesize into prioritized findings. For high-impact balance or design claims, map the claim to at least one reference lens below and keep observed behavior separate from inferred player psychology.

## Role Lenses

Use the roles that fit the game; do not force all of them if the task is small.

| Lens | Ask |
| --- | --- |
| First-time player | Do I understand what to do, why it worked, and why I failed? |
| Optimizer | Is there one dominant route, exploit, or obvious solved strategy? |
| Casual player | Can I recover from imperfect decisions without reading source code? |
| Systems designer | Are economy, risk, pacing, gates, and feedback loops coherent? |
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
- Economy: revenue, costs, margins, and cash flow avoid runaway triviality unless intended.
- Risk and failure: bad routes fail for understandable reasons; failure state matches the product model.
- Trade-offs: safe, cheap, fast, risky, and scalable routes each have real costs.
- Feedback: UI metrics and HUD signals explain what changed, why it changed, and what to try next.
- Pacing: early game has tension, midgame has new problems, late game has scale pressure.
- Exploitability: one-button loops, dominant pricing, infinite money, or risk-free strategies are called out.
- Instrumentation: diagnostics measure phase snapshots, peaks, gates, and bottlenecks.
- Regression safety: behavior-changing observations are tied to tests, snapshots, or reproducible commands.

## Output Shape

Keep the report concise and evidence-led:

1. Expected arc: a short hypothesis before results.
2. Commands run: include exact commands and whether they passed.
3. Scenario table: route, final day/state, customers/progression, money, risk/quality, notable bottleneck.
4. Expected vs observed: note surprising bottlenecks, dominant strategies, missing pressure, or failed hypotheses.
5. Role review: short bullets by relevant lenses.
6. Findings: prioritize by player impact. For each high-priority finding, include `Evidence`, `Lens`, `Code path`, `Lever`, and `Expected side effect`; UI/UX findings need browser observation, screenshot, or UI panel evidence when available.
7. Recommendations: 2-4 tuning paths with trade-offs, not a giant backlog.
8. Gaps: state what was not verified, missing scenario classes and reasons, browser playtesting gaps, or temporary probes that could not be cleaned up.

## RelayOps Defaults

For RelayOps-style business simulators, always check:

- Prefer `npm run diagnose` when available for phase snapshots, gate gaps, peaks, and scenario comparison; if absent, use `npm run simulate` or another existing scenario runner and state the gap.
- `npm run simulate` for regression-sensitive scenario output; `npm run snapshot:check` after behavior changes or when verifying no behavior drift.
- `src/game/`, `src/state/`, and relevant `src/ui/` panels before attributing behavior.
- Whether the UI-visible gates match the engine gates.
- Whether risk is a readout or a fail condition, and whether cash flow is the true game-over state.
- Whether server/concurrency/bandwidth pressure is actually visible to the player, not merely present in code.

## Common Mistakes

- Do not review only from intuition; run or inspect the actual system.
- Do not treat the final state as the whole journey; phase snapshots matter.
- Do not judge balance from only the balanced route; compare bad, safe, exploit, and no-action routes.
- Do not invent hidden mechanics; trace code paths for gates, failures, and metrics.
- Do not report a finding without a source: cite a script, command output, function, data constant, state field, or UI panel when the repo makes that possible.
- Do not suggest tuning without naming the lever and expected side effect.
- Do not edit the game during review unless the user asks for fixes.
- Do not treat regression checks as gameplay evaluation; they prove stability, not fun or balance.
- Do not quote a framework name as proof; use it to structure evidence from the actual game.
