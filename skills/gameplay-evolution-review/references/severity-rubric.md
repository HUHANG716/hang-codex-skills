# Severity Rubric

Prioritize findings by player impact, reproducibility, and tuning leverage. Use the lowest severity that still reflects the actual harm.

## P0: Blocks Core Play

Use for issues that prevent the core loop from functioning.

- Crash, softlock, unwinnable required path, impossible tutorial, broken save/load, or required UI action unavailable.
- Engine state and UI state diverge so badly that the player cannot make a valid decision.
- Economy/rules allow immediate infinite progression that invalidates the game.

## P1: Breaks Intended Experience

Use for issues that most target players will feel or that invalidate progression/balance.

- One dominant strategy removes meaningful choice.
- First-time player cannot understand goal, feedback, or failure cause.
- Difficulty spike, resource wall, or randomness blocks normal progression.
- Major exploit, farming loop, or stall route gives large rewards without intended cost.
- Competitive fairness, matchmaking, or counterplay is substantially compromised.

## P2: Degrades Repeated Play

Use for issues that are noticeable but do not collapse the core experience.

- Weak route diversity, stale midgame, slow feedback, unclear secondary metrics, minor content repetition.
- Tuning lever exists and likely fixes the issue without redesign.
- UI communicates the state, but hierarchy or timing makes repeated play tiring.

## P3: Polish Or Observability

Use for issues that improve clarity, measurement, or feel but are not urgent.

- Better labels, telemetry, snapshot coverage, scenario naming, formatting, or minor balance smoothing.
- Helpful but non-blocking accessibility or readability refinements.

## Finding Template

For high-priority findings, include:

- `Severity`
- `Evidence`
- `Lens`
- `Code path`
- `Player impact`
- `Lever`
- `Expected side effect`
- `Validation`
