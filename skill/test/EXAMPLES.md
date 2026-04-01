# Examples

## Example 1: Executive loop section in HTML report

When the report body is markdown-driven:
1. Keep markdown content simple:
   - heading
   - one-paragraph conclusion
   - placeholder div
2. Render markdown first.
3. Inject the complex visual section afterward with JS.

## Example 2: Two-option comparison

Use comparison mode when the user says:
- "做两个版本我对比一下"
- "一个开放素材版，一个生成版"

Recommended split:
- left: open-licensed collage or card layout
- right: unified generated infographic

## Example 3: When to abandon collage

If any of these happen:
- cards overlap
- art style feels inconsistent
- user asks for "更像正式汇报页"

Then switch to:
- one generated hero infographic
- optional supporting chips or callouts below it

## Example 4: Chinese labels must be exact

Bad pattern:
- generate a full infographic with all Chinese text baked into the image

Better pattern:
1. Generate a no-text cartoon visual base.
2. Put exact labels in HTML:
   - top badge: `前台体验：探索冒险收集 + 实力验证`
   - middle badge: `前台产出：获得比宝、资源、材料与推进资格`
   - bottom labels and legends as normal text blocks
3. Use the image for atmosphere and composition, not for exact wording.

## Example 5: Reused doc image in root HTML

Bad pattern:
- markdown file in `docs/design/` uses `../../tmp/beagle_excel_extract/images/image173.jpeg`
- same path is copied unchanged into a root-level HTML report

Better pattern:
1. Copy the image into `assets/ceo-report/image173.jpeg`
2. In root HTML use `assets/ceo-report/image173.jpeg`
3. In markdown use a path validated from the markdown file's own directory

## Example 6: Evidence screenshot sizing

Use this when adding gameplay UI screenshots inside analysis text:

```css
img[src*="assets/ceo-report/wz_"] {
  width: min(100%, 420px);
  margin: 14px auto 24px;
}
```

This keeps the screenshot readable without letting it overwhelm the page.

## Example 7: Replace box graph with comparison image

When the user says a conceptual graph is "太像框图" or "不够容易理解":
1. Generate one comparison image instead of adding more boxes.
2. Use the image to show the visual contrast:
   - distributed lines
   - converging lines
   - isolated systems
   - overlapping systems
3. Put the exact wording in a short comparison table below the image.

## Example 8: Safe generated-image handoff

Bad pattern:
1. Generate image.
2. Immediately write `![x](assets/foo.png)` into HTML or markdown.
3. Realize later that `assets/foo.png` was never copied into the repo.

Better pattern:
1. Generate image.
2. Copy it into a stable repo path such as `assets/foo.png`.
3. Verify that `assets/foo.png` now exists in the repo.
4. Only then write the reference into HTML or markdown.
5. If the page and markdown live in different directories, validate both relative paths separately.

## Example 9: Improve an existing image without replacing it

User intent:
- "之前这张图不错，直接在图上加强说明"

Bad pattern:
- remove the image
- replace it with a new grid or card-based explanation block

Better pattern:
1. Keep the original image as the main visual.
2. Add a short figure note below it.
3. If exact wording is needed, overlay small HTML labels on top of the image.
4. If the image needs stronger concept emphasis, add repeated markers on the relevant side.

For example:
- on the `Beagle` side, repeat a pet marker on every `比宝`-related line
- on the comparison side, add concise labels like `角色成长` or `装备成长`
- keep the image itself visually primary, with annotations serving as guidance rather than replacement
