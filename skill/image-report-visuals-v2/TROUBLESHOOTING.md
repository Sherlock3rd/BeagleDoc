# Troubleshooting

## Failure 1: Raw HTML renders as code
Cause:
- multi-line HTML placed directly into markdown parser flow

Fix:
1. Replace block with placeholder node.
2. Inject complex HTML after markdown render.
3. Re-open final page to confirm rendered block is DOM, not code.

## Failure 2: Broken image icon
Cause:
- asset not copied into repo
- wrong filename or relative path
- path copied from another directory context

Fix:
1. Copy image to stable repo path.
2. Verify exact filename.
3. Recalculate relative path from final rendered file.
4. Update reference only after path verification.

## Failure 3: Asset exists but still not visible
Cause:
- image exists in external workspace/cache but not repo path

Fix:
1. Treat generated output and repo asset as separate states.
2. Copy from generation output to repo.
3. Verify repo file exists.
4. Reference repo copy only.

## Failure 4: Card overlap
Cause:
- absolute-position layout reused across mixed-size assets

Fix:
1. Replace with grid/flex layout.
2. Reserve absolute positioning for fixed-size single-style visuals.

## Failure 5: Style mismatch
Cause:
- mixed sources with conflicting visual language

Fix:
1. Use one dominant style source.
2. For polished delivery, switch to unified generated hero image.

## Failure 6: Generated image text is unreadable or wrong
Cause:
- prompt packed too many labels
- generated Chinese wording inaccurate

Fix:
1. Regenerate text-free or minimal-text image.
2. Move critical wording into HTML/CSS labels.
3. Keep image conceptual, keep text precise in DOM.

## Failure 7: Labels block focal content
Cause:
- large overlay badges placed on top of icon cluster

Fix:
1. Shorten labels.
2. Move labels to whitespace/perimeter.
3. Use connector lines from callouts to target area.

## Failure 8: Flow arrows create visual clutter
Cause:
- excessive cross-image arrows layered on already directional art

Fix:
1. Prefer environmental flow when scene already indicates circulation.
2. Keep only lightweight local guide lines.

## Failure 9: Console warnings mislead diagnosis
Cause:
- unrelated external script warnings distract from real issue

Fix:
1. Verify broken asset URL first.
2. Distinguish warning noise from root cause before editing layout.

## Quick Recovery Order
1. Path and filename
2. Repo existence check
3. Render path context check
4. Parser/HTML injection check
5. Layout overlap and readability
6. Label strategy and language accuracy
