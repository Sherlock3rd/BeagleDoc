---
name: image-report-visuals-v2
description: Rebuilds and executes a robust image workflow for reports and design docs. Invoke when users ask to generate, replace, refine, or localize document visuals.
---

# Image Report Visuals V2

## Purpose
Provide a systemized, failure-resistant workflow for image-heavy report sections, especially for HTML and markdown-driven design documents.

## Invocation Triggers
Use this skill when the user asks to:
- regenerate existing visuals
- replace SVG/sketch/screenshot with polished visuals
- improve an existing image without changing document structure too much
- create comparison infographics, loop diagrams, or executive visual sections
- localize labels (especially Chinese wording accuracy)

## System Architecture

### Layer 1: Intent Router
Classify request into one of four modes:
1. Replace mode: replace existing visual asset while preserving section structure
2. Refine mode: keep base image and add callouts/labels/notes
3. Rebuild mode: redesign visual block (layout + asset + labels)
4. Compare mode: provide multiple visual options for review

### Layer 2: Asset Strategy
Choose one strategy and document why:
- Generated image first: unified style, presentation quality
- Open asset composition: quick draft and evidence composition
- Hybrid: generated hero + supporting evidence screenshots

### Layer 3: Rendering Strategy
Pick rendering pattern based on document type:
- HTML-first page: directly insert figure block
- Markdown-driven page: parse markdown first, inject complex block afterward
- Mixed path page: verify asset paths from final rendered file location

### Layer 4: Quality Guard
Run mandatory checks:
- asset path validity
- style coherence
- label readability
- flow continuity
- mobile readability

## Default Workflow
1. Identify the visual target and claim it must communicate.
2. Audit current section block before editing.
3. Select mode and strategy.
4. Produce or refine image asset.
5. Copy asset into repo-owned stable path.
6. Confirm file exists at final referenced path.
7. Update HTML/markdown references.
8. Add a short figure note for non-decorative images.
9. Validate rendered result on desktop and mobile width.
10. If failure appears, run troubleshooting playbook before further layout rewrites.

## Mandatory Asset Pipeline
1. Finalize image file.
2. Copy into repo path such as `docs/assets/...` or `assets/...`.
3. Verify file existence in repo.
4. Write final reference only after existence is confirmed.
5. Re-validate relative path from final rendered file location.

An image is not ready until it exists at the exact repo path used by the final page.

## Layout Rules
- Prefer one strong hero image over multiple weak blocks.
- Prefer grid/flex for mixed-size assets; avoid fragile absolute positioning.
- For dense labels, move wording into note-style callouts in whitespace.
- Keep labels away from focal icons/characters.
- For loop visuals, ensure every step connection is explicit.
- If scene flow already communicates circulation, avoid heavy cross-image arrows.

## Language and Label Rules
- Do not rely on generated Chinese text for critical wording.
- Prefer text-free or minimal-text generated image base.
- Put exact Chinese labels in HTML/CSS overlay or adjacent legend blocks.

## Replacement Priority Rules
When user asks to improve existing image:
1. Keep original image as primary visual.
2. Add figure note and compact callouts first.
3. Replace full layout only if readability still fails.

## Rendering Rules
- Use repo-local relative paths.
- Never use temporary absolute local paths in final document.
- Do not assume markdown path works in root HTML; recalculate per file location.
- For markdown parser constraints, use placeholder + JS injection for complex blocks.
- Constrain supporting screenshots to readable evidence width.

## Validation Checklist
- [ ] Image exists in repo at final path
- [ ] Reference path matches actual file
- [ ] No broken image icon
- [ ] Figure note exists for meaningful image
- [ ] Labels are readable and do not block focal area
- [ ] Style is coherent across section
- [ ] Chinese critical wording is not trapped only in pixels
- [ ] Loop/flow connections are visually explicit
- [ ] Mobile layout remains readable

## Failure Recovery
1. Verify path and filename exactness.
2. Verify repo copy actually exists.
3. Verify markdown parser did not escape intended HTML.
4. Replace absolute-position stack with grid/flex if overlap occurs.
5. Regenerate text-free base when generated text is wrong.
6. Move dense labels from center overlays to side callouts.
7. Separate console warning noise from actual asset failure.
8. Re-open rendered page after each fix.

## Additional Files
- Pattern library: [EXAMPLES.md](EXAMPLES.md)
- Diagnostic playbook: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
