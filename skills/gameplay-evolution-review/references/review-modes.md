# Review Modes

Select the smallest mode that answers the user's request. Combine modes only when the request or evidence demands it.

## Quick Sanity Review

Use when the user asks for a fast read, early prototype feedback, or "does this work?"

- Read project instructions, game loop, and the fastest runnable command.
- Run one intended route and one low-skill or bad route when possible.
- Report only the top 3 issues, the evidence, and the next test to run.
- Do not overbuild a full scenario matrix.

## Full Evolution Review

Use when asked to evaluate progression, long-run experience, balance, pacing, or replayability.

- State the expected arc before seeing fresh results.
- Run at least 4 scenario classes when possible: low-skill baseline, intended route, risky/optimized route, and exploit/stress route.
- Capture phase snapshots: opening, first meaningful decision, first failure/success, midgame, late/endgame, and peak/bottleneck.
- Synthesize findings by player impact and tuning leverage.

## UX And FTUE Review

Use when the request includes comprehension, onboarding, UI feedback, layout, controls, or player confusion.

- Inspect at least one real browser/play flow with Playwright when the project has a browser UI.
- Compare visible state to true engine state.
- Focus on whether the player can answer: what is happening, why did it happen, and what should I do next?
- Treat missing feedback after an action as evidence, not polish.

## Balance And Tuning Review

Use when asked whether numbers, difficulty, rewards, or routes feel fair.

- Identify the explicit tuning levers: constants, tables, formulas, cooldowns, spawn rates, rewards, costs, enemy stats, timers, score thresholds, or content weights.
- Compare intended, cautious, risky, optimized, and exploit routes.
- For stochastic games, use multiple seeds or repeated runs before calling a balance issue.
- For each recommendation, name the expected side effect.

## Exploit Hunt

Use when asked to find breaks, degenerate strategy, dominant builds, farming loops, softlocks, or "can players cheese this?"

- Search for loops that create reward without matching cost, risk, time, attention, or opportunity cost.
- Check stalls, infinite combos, resource conversions, reset loops, save/load abuse, first-player advantage, and UI/engine mismatch.
- Provide reproduction steps and the missing constraint.
- Prefer narrow guardrails over broad nerfs.

## Regression Validation

Use after behavior changes or when asked to verify that a review-only pass did not alter behavior.

- Re-run the same commands, seeds, replays, or snapshots used as evidence.
- Compare before/after on the smallest metrics that express the design intent.
- Separate "stable output" from "good experience"; regression checks do not prove fun.

## Static Or Paper Review

Use when the game cannot run, is only described in docs, or exists as rules/data without executable flows.

- Simulate the rules manually for a short path.
- Audit state transitions, tables, formulas, content, and UI copy.
- Mark all claims that are inference rather than observed runtime behavior.
- Put missing runnable evidence in `Gaps`.
