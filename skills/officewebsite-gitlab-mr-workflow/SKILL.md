---
name: officewebsite-gitlab-mr-workflow
description: Use when working in the `officewebsite` repo and the user asks about staged changes, semantic commits, branch push, PR information, GitLab PR creation, or the officewebsite delivery review flow.
---

# Officewebsite GitLab PR Workflow

Use this skill only for the `officewebsite` repo. Treat `origin/dev` as the default comparison base and target branch unless the user explicitly says otherwise.

## Defaults

- GitLab host: `10.99.10.5:8088`
- Repo: `yyrjb-git/frontend/officewebsite`
- Target branch: `dev`
- CLI: `glab`
- Compare base for summaries: `origin/dev..HEAD`
- Default assignee: `huhang`（胡航）
- Default reviewer: `zhuzhipeng`
- Response language: concise Chinese unless the user requests otherwise

## Resource Map

- Run `scripts/preflight.ps1` for deterministic environment and repository checks.
- Read `references/commit-rules.md` before splitting staged changes or writing commit messages.
- Read `references/mr-template.md` before generating PR title, description, impact scope, or final response text.

## Workflow

### 1. Preflight

From the repo root, run:

```powershell
powershell -ExecutionPolicy Bypass -File "C:/Users/Siyi/.codex/skills/officewebsite-gitlab-mr-workflow/scripts/preflight.ps1"
```

Use the output to confirm:

- current directory is a Git repo
- remote points to `officewebsite`
- current branch is known
- worktree and staged status are visible
- `origin/dev` has been fetched
- `glab` exists and auth status is known
- an existing open PR for the current branch is detected when practical

If `glab` is missing, report that blocker first. Install it only when the user wants to continue creating or updating the PR; on this Windows machine, prefer `choco install glab -y`. If the user provides a token, authenticate with `glab auth login --hostname 10.99.10.5:8088 --token` and pass the token over stdin instead of writing it to disk.

### 2. Split staged changes

Read `references/commit-rules.md`, then inspect:

```bash
git diff --cached --stat
git diff --cached
```

Split by independent rollback unit, not by file count. Keep related behavior, supporting types, and required wiring in the same commit. Separate business changes from infra, refactor, or style-only changes when they can be independently reverted.

If staged changes are mixed, unstage and restage per commit with `git restore --staged .`, `git add <path>`, or `git add -p`. Create each commit only after the staged set for that commit is clean.

### 3. Generate PR information

Read `references/mr-template.md`, compare the current branch with `origin/dev`, and generate the PR title, body, and impact scope from that reference.

### 4. Create or update the PR

Push before creating or updating the PR:

```bash
git push -u origin <branch>   # first push only
git push                      # later pushes
```

Check for an existing open PR for the source branch before creating a new one:

```bash
glab mr list --source-branch <branch>
```

If an open PR already exists, update or verify it instead of creating a duplicate unless the user explicitly asks to open another.

By default, set assignee to `huhang` and reviewer to `zhuzhipeng`. After creation or update, verify assignee and reviewer with `glab mr view <id>` when practical. Return the PR URL and the exact source and target branch pair.

## Response Style

- If the user asks only for commit messages, output only commit messages, one per line, with no numbering or explanation.
- If the user asks only for PR information, output only the title, body, and impact scope; do not create the PR.
- If the user asks to push commits one by one, create the commit sequence and push after each commit.
- If the user asks to create the PR, create it if auth is ready; otherwise install or authenticate `glab` first.
- Mention blockers briefly and concretely: missing token, no staged changes, existing PR already open, or branch divergence that needs a user choice.

## Guardrails

- Respect the repo `AGENTS.md` instructions and commit convention.
- Do not add tests or unrelated fixes unless the user asks.
- Use `npx tsc --noEmit --pretty false` as an optional verification step when the change touched TypeScript behavior and the user wants a check.
- Keep the workflow focused on this repo; do not reuse these defaults for other projects.
