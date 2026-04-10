# JSON Schema Rules For `officewebsite`

Use this reference whenever generating or revising a CMS form JSON Schema for `officewebsite`.

## Supported Formats

### 1. `select-search`

Use for ID or slug selector fields that are not page-instance selectors.

```json
{
  "format": "select-search",
  "x-select-search-props": {
    "listApi": "/api/pdm/pdmProduct/list",
    "labelField": "productName",
    "valueField": "id",
    "searchField": "productName"
  }
}
```

Rules:
- Use a user-facing `title`, not a storage-facing title.
- Example: `productId` -> `产品`, not `产品ID`.
- Example description: `请搜索并选择产品`.

### 2. `image`

Use for image selector fields.

```json
{
  "type": "object",
  "format": "image"
}
```

Rules:
- Use when the field name contains `img`, `image`, `photo`, or `picture`.
- `type` must be `object`.
- Do not define nested `properties`.

### 3. `video`

Use for video selector fields.

```json
{
  "type": "object",
  "format": "video"
}
```

Rules:
- Use when the field name contains `video`, `movie`, or `clip`.
- `type` must be `object`.
- Do not define nested `properties`.

### 4. `file`

Use for non-image, non-video downloadable file selectors.

```json
{
  "type": "object",
  "format": "file"
}
```

Rules:
- Use when the field name contains `file`, `fileId`, `download`, `document`, `attachment`, or `package`, or when the field semantically selects downloadable assets such as PDF, ZIP, or EXE.
- `type` must be `object`.
- Do not define nested `properties`.
- Description should explain the user is selecting a downloadable file from the material library.

### 5. `frame-sequence`

Use for a sequence of animation or video frames.

```json
{
  "type": "array",
  "format": "frame-sequence"
}
```

Rules:
- Use for names such as `videoFrames`, `animation`, `animationFrames`, `frames`, `frameSequence`, or `videoFrameList`.
- `type` must be `array`.
- Do not define `items.properties` in detail; the form component handles the element structure.
- Description should explain the field stores an ordered frame sequence.

### 6. `richtext`

Use for longer copy or any text likely to need manual line breaks.

```json
{
  "type": "string",
  "format": "richtext"
}
```

### 7. `page-instance`

Use for page selection in navigation, linking, or jump scenarios.

```json
{
  "type": "object",
  "format": "page-instance"
}
```

Rules:
- `type` must be `object`.
- Do not define nested `properties`.
- Use user-facing titles such as `目标页面` or `跳转页面`.
- Example description: `请选择要跳转的页面实例`.

Field-name recognition hints:
- `targetPage`, `targetPageId`, `targetPageInstanceId`
- `jumpPage`, `jumpPageId`, `jumpPageInstanceId`
- `openPage`, `openPageId`, `openPageInstanceId`
- `pageRouter`, `pageRouterId`, `pageRouterInstanceId`
- `router`, `routerId`, `routerInstanceId`
- `pageInstance`, `pageInstanceId`
- `page`, `pageId`
- `linkPage`, `linkPageId`, `linkPageInstanceId`
- `relatedPage`, `relatedPageId`, `relatedPageInstanceId`

Context rules:
- If the field is numeric and the name/context clearly indicates page navigation, prefer `page-instance` before `select-search`.
- If the field sits next to jump/link/url fields, bias toward `page-instance`.

### 8. `enum`

Use for finite mode selectors.

```json
{
  "type": "string",
  "enum": ["value1", "value2"],
  "enumNames": ["选项1", "选项2"]
}
```

Rules:
- Always provide both `enum` and `enumNames`.
- `enum` stores actual values.
- `enumNames` stores Chinese labels shown in the form.

## ID / Slug Recognition Rules

When a field ends with `Id` or `Slug`, inspect both the field name and its context.

### Prefer `page-instance` first

Use `page-instance` when the field name and context clearly refer to a page or route target.

### Otherwise use `select-search`

Common mappings:
- `productId` -> `/api/pdm/pdmProduct/list`, `labelField: "productName"`, `valueField: "id"`, `searchField: "productName"`
- `categoryId` or `productCategoryId` -> `/api/pdm/pdmProductCategory/list`, `labelField: "categoryName"`, `valueField: "id"`, `searchField: "categoryName"`
- `pageTemplateId` -> `/api/pm/pmPageTemplate/list`, `labelField: "name"`, `valueField: "id"`, `searchField: "name"`
- `componentTemplateId` -> `/api/pm/pmComponentTemplate/list`, `labelField: "name"`, `valueField: "id"`, `searchField: "name"`
- `newsSlug` -> `/api/cnt/cntNews/list`, `labelField: "seoTitle"`, `valueField: "slug"`, `searchField: "seoTitle"`
- `caseSlug` -> `/api/cnt/cntCase/list`, `labelField: "seoTitle"`, `valueField: "slug"`, `searchField: "seoTitle"`

Fallback rules:
- Unknown `Id` field -> default `valueField` to `id`.
- Unknown `Slug` field -> default `valueField` to `slug`.
- Infer `listApi`, `labelField`, and `searchField` from the surrounding business context.

## Output Requirements

1. Output valid JSON Schema only when the task is schema-only.
2. Do not include explanatory prose together with final JSON output.
3. Every `type` must be a single scalar type such as `string`, `number`, `integer`, `boolean`, `array`, or `object`.
4. Never use union types such as `["string", "null"]`.
5. Set a proper `type` for every field.
6. Add `items` for arrays.
7. Add `properties` for regular nested objects only, not for custom format objects such as `image`, `video`, `file`, or `page-instance`.
8. Build `required` from what the component truly needs to render correctly.
9. Add meaningful Chinese `title` values.

## Property Ordering Rules

Order properties for editor usability instead of mirroring incoming JSON.

Recommended order:
1. Title and heading fields
2. Selector fields such as `page-instance`, `select-search`, and enums
3. Content fields such as text and richtext
4. Media and file fields such as image, video, and file
5. Other auxiliary fields
6. Array fields

Keep related fields adjacent.

## Example

```json
{
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "title": "标题",
      "maxLength": 200
    },
    "productId": {
      "type": "integer",
      "title": "产品",
      "format": "select-search",
      "x-select-search-props": {
        "listApi": "/api/pdm/pdmProduct/list",
        "labelField": "productName",
        "valueField": "id",
        "searchField": "productName"
      }
    },
    "targetPageId": {
      "type": "object",
      "title": "目标页面",
      "format": "page-instance",
      "description": "请选择要跳转的页面实例"
    },
    "status": {
      "type": "string",
      "title": "状态",
      "enum": ["active", "inactive"],
      "enumNames": ["启用", "禁用"]
    },
    "description": {
      "type": "string",
      "title": "描述",
      "maxLength": 500
    },
    "imageUrl": {
      "type": "object",
      "title": "产品图片",
      "format": "image"
    },
    "downloadFile": {
      "type": "object",
      "title": "下载文件",
      "format": "file",
      "description": "请从素材库选择可下载文件（如PDF、ZIP等）"
    },
    "videoFrames": {
      "type": "array",
      "title": "视频帧序列",
      "format": "frame-sequence",
      "description": "请从素材库选择一组按序排列的图片作为视频帧序列"
    }
  },
  "required": ["title", "productId"]
}
```
