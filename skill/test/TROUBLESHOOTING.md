# Visual Troubleshooting

## Common Failure Modes

### 1. Raw HTML shows up as code
Cause:
- multi-line HTML was placed directly inside markdown parsed by `marked`

Fix:
- replace the markdown block with a placeholder node
- after `marked.parse(...)`, inject the visual HTML with JS

## 2. Broken image icon or alt text only
Cause:
- referenced file is not inside the repo
- path is absolute or temporary
- HTML points to a different filename than the actual asset
- the relative path was copied from a markdown file in another directory and no longer matches the final HTML location

Fix:
- copy the final image into `assets/`
- use relative paths like `assets/example.png`
- verify the filename exactly matches
- recalculate the path from the final rendered file, not from the source markdown file
- do not write the final image reference until the repo-local file has been verified to exist

## 3. Cards overlap
Cause:
- absolute positioning was tuned for one image size but reused with mixed assets

Fix:
- switch to grid/flex layout
- reserve absolute positioning for single-style, predictable-size visuals only

## 4. Style mismatch
Cause:
- open-licensed illustrations and generated art use different shape language

Fix:
- use one dominant art source
- or turn the section into a structured card layout where consistency matters less
- if the user wants a polished exec page, prefer a unified generated image

## 5. Generated image is unreadable
Cause:
- prompt over-packed too many labels or too much structure

Fix:
- reduce the number of labels
- ask for larger card shapes and higher hierarchy
- separate dense logic into page text and keep the image conceptual

## 6. Generated Chinese text is wrong
Cause:
- the image model produced malformed or inaccurate Chinese text
- too many labels were baked into the image itself

Fix:
- regenerate a text-free or minimal-text image
- move all important Chinese labels into HTML/CSS
- treat generated image text as decorative only unless manually verified

## Mistake Log

### Case: report visual comparison block rendered as code
What happened:
- a full HTML comparison block was inserted directly into markdown source
- `marked` treated it like code in the final page

Correct pattern:
- markdown keeps only a placeholder slot
- JS replaces the slot with final injected HTML after rendering

### Case: generated image did not render
What happened:
- the page referenced an image path that did not exist in the repo

Correct pattern:
- generated asset must be copied into repo `assets/`
- final HTML should point to the repo-local file
- after copying, verify the repo-local filename before updating the document

### Case: generated image existed in Cursor storage but not in the repo
What happened:
- the image had been generated successfully
- but it only existed in Cursor-managed workspace asset storage
- the final HTML referenced `assets/...` inside the repo, so the browser correctly reported `ERR_FILE_NOT_FOUND`

Correct pattern:
- treat generated output and repo asset as two different states
- always copy from tool output location into repo `assets/...`
- only reference the repo copy in final HTML or markdown
- add an explicit existence check before considering the task done

### Case: image existed but still did not show
What happened:
- the source markdown used a path like `../../tmp/...`
- that path was valid from `docs/design/...`
- but invalid once copied into a root-level HTML report

Correct pattern:
- store reused report images in a stable repo asset directory such as `assets/ceo-report/`
- use one path for root HTML and a separately validated relative path for markdown if needed
- when both markdown and root HTML exist, validate each reference from its own file location

### Case: console showed CDN warnings but image failure had another cause
What happened:
- browser console displayed storage/tracking warnings from external scripts
- the real issue was a broken local image path

Correct pattern:
- do not assume the visible console warning is the root cause
- verify the broken asset URL directly first

### Case: support screenshots were too large
What happened:
- UI screenshots were rendered at near full content width
- they dominated the page and interrupted reading rhythm

Correct pattern:
- treat in-document screenshots as evidence blocks
- limit width to a moderate reading size, usually around `360px-480px`
- keep main hero visuals full-width only when they carry the section's primary meaning

### Case: collage version overlapped badly
What happened:
- absolute-position card layout was used with differently sized SVG assets

Correct pattern:
- mixed assets should use stacked flow or grid card layout
- do not rely on manually tuned coordinates unless all assets share dimensions

### Case: scheme B looked better but text was wrong
What happened:
- the generated infographic had stronger style unity
- but some Chinese wording inside the image was unreliable

Correct pattern:
- keep the generated image as a no-text visual base
- render the final Chinese labels as HTML overlays or adjacent legend cards

### Case: text labels blocked icons and a flow looked disconnected
What happened:
- large overlay labels were placed directly over the main icon cluster
- some intended transitions were only implied by the base art, so `step 2 -> step 3` or `step 5 -> step 1` read as broken

Correct pattern:
- move longer wording into note-style callouts placed in whitespace or near the image perimeter
- keep only short chips near small icons
- add explicit HTML/SVG connector lines when a flow step is not visually obvious enough
- validate that labels improve readability instead of competing with the art

### Case: cross-image arrows made the loop look messy
What happened:
- explicit connector lines were drawn across the main illustration
- the scene already had enough directional language, so the extra lines created visual conflict

Correct pattern:
- first ask whether the environment itself can express the loop through roads, rings, or scene flow
- if yes, let the art carry the circulation and keep overlays to lightweight callouts only
- add short guide lines from labels to nearby targets, not long step-to-step arrows across the whole image
