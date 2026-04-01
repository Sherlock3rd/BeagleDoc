# Examples

## Example 1: Replace existing inline SVG with generated asset
Scenario:
- existing section uses large inline SVG
- user asks for regenerated visual with cleaner style

Pattern:
1. Keep section heading, table, and figure note structure.
2. Generate new image asset.
3. Copy to `docs/assets/<topic>/...`.
4. Replace `<svg>...</svg>` with `<img class="visual-image" ...>`.
5. Validate references from final HTML file location.

## Example 2: Improve existing image without changing structure
Scenario:
- user says current image is good but needs clearer explanation

Pattern:
1. Keep original image.
2. Add compact figure note.
3. Add small callouts in whitespace.
4. Do not replace with card-grid unless readability still fails.

## Example 3: Markdown-driven report with complex visual block
Scenario:
- markdown parser escapes large raw HTML blocks

Pattern:
1. Keep markdown body concise with placeholder node.
2. Render markdown first.
3. Inject visual HTML block after parsing.
4. Re-check path and class styles in final output page.

## Example 4: Chinese labels must be exact
Scenario:
- generated image text quality is unreliable

Pattern:
1. Generate text-free image base.
2. Put exact Chinese labels in HTML/CSS.
3. Use image for composition and atmosphere only.

## Example 5: Compare two visual directions
Scenario:
- user asks for two versions

Pattern:
- Version A: fast composition with open assets
- Version B: unified generated hero infographic
- Keep the same claim and label set for fair comparison

## Example 6: Reused markdown image fails in root HTML
Scenario:
- image path valid in markdown location but broken in root HTML

Pattern:
1. Move image to stable repo asset path.
2. Recalculate path from root HTML.
3. Validate both markdown and HTML references separately.

## Example 7: Loop flow appears disconnected
Scenario:
- visual has unclear step transitions

Pattern:
1. Add concise connector lines for missing transitions.
2. Keep labels short.
3. If scene already conveys flow, remove excessive cross-image arrows.

## Example 8: Evidence screenshot too dominant
Scenario:
- support screenshots disrupt reading rhythm

Pattern:
1. Cap width around `360px-480px`.
2. Center screenshot with whitespace.
3. Keep hero visuals full width only when they carry primary section meaning.
