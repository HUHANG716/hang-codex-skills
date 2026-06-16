# Review Tool Consent

Use this when no diagnostic, simulation, replay, seed, bot, or scenario runner exists and runtime evidence would materially improve the review.

## Consent Rule

Do not create any temporary probe, scenario runner, replay fixture, test, generated data file, or durable project script without explicit user approval.

This applies even if the file would live outside the repo. Reading code, inspecting commands, and running existing tools are fine; creating new tooling is the consent boundary.

## Before Asking

Inspect enough of the project to make the request concrete:

- existing game loop, reducer, state machine, tick/update function, rules engine, or action handlers
- relevant content/tuning data
- available package/runtime commands
- whether randomness needs deterministic seeds or repeated runs
- whether a browser UI still needs separate Playwright observation

## Consent Prompt Template

Use a short prompt like:

```text
I did not find an existing simulation/replay/scenario runner. I can create a [temporary probe / durable script] that calls [existing game logic] and covers [scenario classes].

It would live at [path]. I would [delete it after the review / keep it as project tooling].

Do you want me to create it?
```

Include concrete paths and scenario names whenever possible.

## If The User Approves

- Create the smallest useful harness.
- Call existing rules/state/game-loop code; do not reimplement game rules inside the harness.
- Prefer deterministic seeds or fixed fixtures when randomness exists.
- Output structured route, phase, resource, outcome, failure, and bottleneck data.
- Keep durable tooling consistent with the repo's language, package manager, scripts, and naming style.
- Disclose new files, leftover temporary files, and validation commands in the final report.

## If The User Declines Or Does Not Answer

- Do not create files.
- Continue with static evidence, paper simulation, existing UI/browser observation, and code-path tracing.
- Mark related claims as `Static evidence` or `Inference`.
- Put missing runnable evidence and skipped scenario classes in `Gaps`.

## Durable Tooling Bar

Only propose durable project files when at least one is true:

- the user asked to improve review/debug tooling
- the project will likely need repeated balance checks
- the harness can become a useful regression or scenario test
- the review needs multiple routes, seeds, or before/after tuning comparisons

Otherwise, ask for a temporary probe first.
