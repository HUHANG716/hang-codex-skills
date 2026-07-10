---
name: officewebsite-cms-bidirectional-sync
description: Use when working in `officewebsite` and a component, CMS form JSON Schema, or CMS configuration must be evaluated, generated, wired, repaired, or synchronized in either direction.
---

# Officewebsite CMS Bidirectional Sync

Use this skill only in `officewebsite`.

## Entry Points

Choose the workflow that matches the user's source of truth.

### Component -> Schema -> Component

Use this path when the user starts from an existing component, a Figma-like UI requirement already落在代码里, or a request such as:
- `帮我看这个组件哪些字段适合给 CMS 配置`
- `根据这个组件生成表单 json`
- `把这个组件改成从 CMS 读配置`
- `改组件后顺手把 schema 也同步掉`

### Schema -> Component

Use this path when the user starts from JSON Schema or a field contract, for example:
- `这是新的 schema，帮我把组件接上`
- `字段改了，反向同步到组件`
- `schema 里新增了颜色/蒙层/跳转配置，组件也要支持`

### Drift Fix / Full Sync

Use this path when component code and schema have already diverged and the user wants both sides aligned in one pass.

### Component Configuration Review

Use this focused path when the request is specifically about deciding which fields should be exposed to editors or drafting a form schema before implementation:

- Group fields into content, selectors, media, links, layout/style tokens, and repeated items.
- Prefer editor-facing concepts such as `backgroundColor`, `textColor`, `buttonTheme`, `overlayOpacity`, `contentAlign`, and `showMask`.
- Avoid one-off font sizes, per-edge spacing, absolute positioning, and decorative micro-controls.
- Use `richtext` when copy needs manual line breaks or mixed emphasis.
- Order schema properties for editor usability: titles, selectors/enums, content, media/files, auxiliary fields, then arrays.
- Always omit `templateType` from the editor form schema.

Start with the schema proposal when the user asks for field evaluation or JSON only. Implement the component wiring only after the contract is accepted, unless the user explicitly requests a full sync.

## Workflow

### 1. Inspect Both Sides Before Editing

- Read the target component, matching PC/mobile variant, shared component if any, related types, and dynamic registration when relevant.
- Read the existing schema if it exists.
- Identify mismatches between hardcoded JSX/styles/defaults and exposed CMS fields.
- Treat the component and schema as one contract. Do not edit only one side unless the user explicitly requests schema-only output.

### 2. Decide What Should Be Exposed

- Expose business-facing content and meaningful section-level display controls.
- Prefer moderate controls such as text, media, links, background, text color, overlay color, overlay opacity, card style, spacing, alignment, and mode selectors.
- Avoid exposing one-off micro typography, arbitrary positioning numbers, or decorative internals unless the user explicitly asks.
- Prefer grouped concepts over raw CSS fragments when possible, but honor explicit user field names once agreed.

### 3. Preserve Backward Compatibility

- Never remove old field support unless the user explicitly asks.
- Keep safe fallbacks so missing CMS data does not crash rendering.
- Support legacy aliases or misspellings when real content may already depend on them.
- If a new schema replaces an old field, accept both during the transition and prefer the new field when both exist.

### 4. Update The Counterpart

If starting from component code:
- Inspect hardcoded content, media, styles, selectors, repeated data, and fallback behavior.
- Draft or revise the schema using `references/json-schema-rules.md`.
- After the schema is settled, refactor the component to consume the agreed fields.

If starting from schema:
- Parse each field, format, required rule, selector contract, and property order.
- Map schema fields into component props, rendering branches, inline styles, fallback values, and shared utilities.
- If the schema implies a missing capability, implement it in the component rather than silently ignoring the field.

### 5. Keep Adjacent Files In Sync

Touch the smallest necessary set of files, which may include:
- The shared/common component
- PC and mobile variants
- `DynamicPage.tsx` registration files
- Shared types
- The component's `.schema.json`

### 6. Verify The Sync

- Re-read the edited component and schema to confirm field names match exactly.
- Confirm every schema field is either consumed by the component or intentionally reserved.
- Confirm required fields are truly required for rendering.
- Run lightweight verification such as `npx tsc --noEmit` when available.

## Output Modes

### Schema-only requests

- Output JSON Schema only.
- Do not include explanatory prose with the JSON.

### Implementation requests

- Edit the component and schema together.
- Mention any backward-compatibility assumptions after the work is done.

## Guardrails

- Use `@/` imports for `src/` modules.
- Follow strict TypeScript and add explicit types when they improve clarity.
- Do not add tests; this repo has no test framework.
- Prefer existing utilities and rendering patterns over inventing new abstractions.
- Keep schema field names stable and editor-friendly.
- Always read `references/json-schema-rules.md` before drafting or revising schema.

## References

- Read [references/json-schema-rules.md](references/json-schema-rules.md) whenever generating or revising component form schema.
