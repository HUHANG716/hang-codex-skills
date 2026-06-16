# Studio Workflow Notes

These notes adapt useful ideas from multi-agent game-development workflows, including Claude Code Game Studios-style setups, without requiring a large agent roster.

## Useful Patterns To Borrow

- Start by selecting a mode, not by running every possible review.
- Use role lenses as temporary review hats rather than permanent agents.
- Keep quality gates explicit: runnable evidence, scenario coverage, UI truth, severity, and validation.
- Turn repeatable review output into small templates.
- Record gaps honestly instead of pretending static inference is playtesting.

## What Not To Borrow By Default

- Do not create a large agent hierarchy for a single skill.
- Do not split every review into many handoffs unless the project is large enough to benefit.
- Do not let production/process ceremony replace running the game.
- Do not treat a template as proof; it is only a way to organize evidence.

## Lightweight Studio Pass

For a larger game review, run these passes in order:

1. Producer pass: choose scope, mode, genre profile, and evidence budget.
2. Systems pass: inspect rules, resources, progression, gates, and tuning levers.
3. Player pass: run or simulate first-time, intended, bad, and optimized routes.
4. UX pass: inspect real screen flow when UI/player comprehension is in scope.
5. QA pass: reproduce major findings, run regression checks, and mark gaps.
6. Designer pass: propose 2-4 tuning paths with trade-offs and side effects.
