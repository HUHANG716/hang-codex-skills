# PR Template

Use this reference when generating PR information for `officewebsite`.

## Title Rules

- Keep the title centered on one theme.
- Prefer the user-facing outcome over infra work.
- Prefer the single most important business change instead of listing every detail.
- If both infra and business changes exist, let the title follow the main business change and place infra work inside `代码重构` or `影响范围`.

## Body Structure

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

## Writing Rules

- Group bullets by semantic type such as `功能新增`, `功能优化`, `问题修改`, `代码重构`, or `样式调整`.
- Describe capability, behavior, structure, or UI effect.
- Do not mention implementation details, filenames, or raw git mechanics unless the user asks.
- Summarize impact scope with component or module names, not every touched file.
- When there is no meaningful impact on one side, omit that line instead of writing filler.

## Delivery Details

- Include the PR URL after creation or update.
- Include the exact source and target branch pair.
- If practical, verify and mention assignee `huhang` and reviewer `zhuzhipeng`.
