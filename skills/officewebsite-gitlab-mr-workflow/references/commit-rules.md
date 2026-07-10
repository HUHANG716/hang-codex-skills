# Commit Rules

Use these rules when splitting staged `officewebsite` changes and writing commit messages.

## Split Rules

- Split by independent rollback unit, not by file count.
- Keep related behavior, supporting types, and required wiring in the same commit.
- Separate business changes from infra, refactor, or style-only changes when they can be independently reverted.
- If staged changes are mixed, unstage and restage per commit with `git restore --staged .`, `git add <path>`, or `git add -p`.
- Create each commit only after the staged set for that commit is clean.

## Commit Message Format

```text
[模块名-变更类型] 具体描述
```

- Keep one line only.
- Describe outcome or behavior, not implementation details.
- Avoid field names, function names, color values, frame counts, or "from A to B".
- Keep each message abstract enough to survive future refactors.

## Module Mapping

- `src/components/*/layout/` or navigation: `Layout`
- Form components: `Form`
- `dynamic/`, `common/`, or `lazy/`: `Display`
- Home, preview, or `404`: `Page`
- `category/`: `Category`
- `product/`: `Product`
- `src/lib/`, `src/utils/`, config, or shared tooling: `Infra`

## Type Selection Priority

- New end-user capability: `功能新增`
- Behavior change to an existing capability: `功能修改`
- Bug fix or abnormal behavior correction: `问题修改`
- Behavior or structure improvement: `功能优化`
- Runtime or loading efficiency improvement: `性能优化`
- Visual-only change: `样式调整`
- Pure code organization without behavior change: `代码重构`
- Config-only change: `配置调整`
