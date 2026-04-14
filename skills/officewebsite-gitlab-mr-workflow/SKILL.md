---
name: officewebsite-gitlab-mr-workflow
description: Split staged `officewebsite` changes into semantic commits, generate a one-theme merge request summary against remote `dev`, and create or update the merge request on the self-hosted GitLab with `glab`. Use when the user asks to拆分 staged 变更、分别提交、生成 PR/MR 信息、推送分支、提 PR/MR，or to run the full officewebsite Git workflow end to end.
---

# Officewebsite GitLab MR Workflow

Use this skill for the `officewebsite` repo only. Treat `origin/dev` as the default comparison base and target branch unless the user explicitly says otherwise.

## Defaults

- GitLab host: `10.99.10.5:8088`
- Repo: `yyrjb-git/frontend/officewebsite`
- Target branch: `dev`
- CLI: `glab`
- Compare base for summaries: `origin/dev..HEAD`
- Default assignee: `huhang`（胡航）
- Default reviewer: `zhuzhipeng`
- Keep output concise and Chinese unless the user requests another language.

## Workflow

### 1. Preflight

- Run from repo root and confirm `git remote -v`, current branch, and `git status --short`.
- Run `git fetch origin dev` before evaluating commits or MR content.
- Check `glab auth status`.
- If `glab` is missing, install it first. On this Windows machine prefer `choco install glab -y`.
- If not authenticated, log in to `10.99.10.5:8088` before continuing. Prefer existing local auth.
- If the user provides a token, use `glab auth login --hostname 10.99.10.5:8088 --token` and pass the token over stdin instead of writing it to disk.

### 2. Split staged changes into semantic commits

- Start from `git diff --cached --stat` and `git diff --cached`.
- Split by independent rollback unit, not by file count.
- Keep related behavior, supporting types, and required wiring in the same commit.
- Separate business changes from infra, refactor, or style-only changes when they can be independently reverted.
- If staged changes are mixed, unstage and restage per commit with `git restore --staged .`, `git add <path>`, or `git add -p`.
- Create and push commits one by one only after the staged set for that commit is clean.

#### Commit message rules

- Format: `[模块名-变更类型] 具体描述`
- Keep one line only.
- Describe outcome or behavior, not implementation details.
- Avoid field names, function names, color values, frame counts, or “from A to B”.
- Keep each message abstract enough to survive future refactors.

#### Module mapping

- `src/components/*/layout/` or navigation: `Layout`
- Form components: `Form`
- `dynamic/`, `common/`, or `lazy/`: `Display`
- Home, preview, or `404`: `Page`
- `category/`: `Category`
- `product/`: `Product`
- `src/lib/`, `src/utils/`, config, or shared tooling: `Infra`

#### Type selection priority

- New end-user capability: `功能新增`
- Behavior change to an existing capability: `功能修改`
- Bug fix or abnormal behavior correction: `问题修改`
- Behavior or structure improvement: `功能优化`
- Runtime or loading efficiency improvement: `性能优化`
- Visual-only change: `样式调整`
- Pure code organization without behavior change: `代码重构`
- Config-only change: `配置调整`

### 3. Generate MR information

- Compare the current branch with `origin/dev`.
- Use one main theme for the title. Prefer the single most important business change instead of listing every detail.
- Use this structure:

```markdown
# <单一主题标题>

## 变更内容

### <变更类型>
- ...

## 影响范围
- PC端：...
- 移动端：...
- 公共：...
```

- Group bullets by semantic type such as `功能新增`, `功能优化`, `问题修改`, `代码重构`, or `样式调整`.
- Describe capability, behavior, structure, or UI effect.
- Do not mention implementation details, filenames in the body, or raw git mechanics unless the user asks.
- Summarize impact scope with component or module names, not every touched file.
- When there is no meaningful impact on one side, omit that line instead of writing filler.

#### Title rules

- Keep the title centered on one theme.
- Prefer the user-facing outcome over infra work.
- If both infra and business changes exist, let the title follow the main business change and place infra work inside `代码重构` or `影响范围`.

### 4. Create or update the MR

- Push the branch before creating the MR: `git push -u origin <branch>` if upstream is missing, otherwise `git push`.
- Check for an existing open MR for the source branch before creating a new one: `glab mr list --source-branch <branch>`.
- If an open MR already exists, update or verify it instead of creating a duplicate unless the user explicitly asks to open another.
- By default, set assignee to `huhang` and reviewer to `zhuzhipeng` when creating or updating the MR, unless the user explicitly requests different people.
- Create the MR against `dev` with the generated title and body.
- After creation or update, verify assignee and reviewer with `glab mr view <id>` when practical.
- After creation, return the MR URL and the exact source and target branch pair.

## Recommended command order

```bash
git fetch origin dev
git status --short
git diff --cached --stat
git diff --cached
git restore --staged .        # only when staged changes must be re-split
git add <paths-or-patches>
git commit -m "[模块名-变更类型] 描述"
git push -u origin <branch>   # first push only
git push                      # later commits
glab auth status
glab mr list --source-branch <branch>
glab mr create --source-branch <branch> --target-branch dev --assignee huhang --reviewer zhuzhipeng --title "<title>" --description-file <temp-file>
glab mr update <id-or-branch> --assignee huhang --reviewer zhuzhipeng
```

## Response style

- When the user asks only for commit messages, output only commit messages, one per line, with no numbering or explanation.
- When the user asks only for PR information, output only the title, body, and impact range content and do not create the MR.
- When the user asks to push commits one by one, actually create the commit sequence and push after each commit.
- When the user asks to create the MR or PR, create it if auth is ready; otherwise install or authenticate `glab` first.
- Mention blockers briefly and concretely: missing token, no staged changes, existing MR already open, or branch divergence that needs a user choice.

## Officewebsite-specific guardrails

- Respect the repo `AGENTS.md` instructions and commit convention.
- Do not add tests or unrelated fixes unless the user asks.
- Use `npx tsc --noEmit --pretty false` as an optional verification step when the change touched TypeScript behavior and the user wants a check.
- Keep the workflow focused on this repo; do not reuse the same defaults for other projects.
