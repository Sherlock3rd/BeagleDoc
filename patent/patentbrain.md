# Patent Application Tracking: Scheme 2 Detailed Design

## 1. Project Overview
**Objective:** Create a patent application based on `scheme2_detailed_design.html`.
**Current Draft:** `patent/patentdoc/draft_v1.md` / `patent/patentdoc/patent_application_v2.doc`
**Target Format:** Word Document (`.docx`)
**Reference Style:** `patent/example/` directory

## 2. Work Plan
- [x] Analyze initial draft (`patent/orgin.md`)
- [x] Receive and process feedback from patent attorneys/reviewers
- [x] Refine content based on feedback (iterative process)
- [x] Format final output as `.docx` (Using HTML-based .doc for better encoding support)

## 3. Current Status
- **Date:** 2026-02-27
- **Phase:** Draft V2 Completed
- **Notes:**
    - Initial draft exists in `patent/orgin.md`.
    - Feedback received regarding A/B flow split and scenario prioritization.
    - **New Draft Generated:** `patent/patentdoc/draft_v1.md`.
    - **Word Document Generated:** `patent/patentdoc/patent_application_v2.doc` (HTML format with UTF-8, solves encoding issues).

## 4. Technical Lessons Learned
### Document Generation Issues & Solutions
- **Issue:** Generating `.doc` files using simple RTF text replacement caused "Rich Text display errors" (乱码) when handling Chinese characters and mixed formatting.
- **Root Cause:** Incomplete RTF header definitions and encoding handling in simple Python scripts without heavy dependencies (like `win32com`).
- **Solution:** Use **HTML-based DOC generation**.
    - Create a standard HTML file with `<meta http-equiv="Content-Type" content="text/html; charset=utf-8">`.
    - Use CSS for styling (fonts like SimSun/Times New Roman).
    - Save with `.doc` extension.
    - Word opens these files seamlessly and renders formatting/encoding correctly.
- **Guideline:** For future document generation tasks involving Chinese content in this environment, **always prefer HTML-to-DOC conversion** over RTF manipulation.

## 5. Feedback Log
*(This section will be updated as feedback is received)*

| Date | Source | Feedback Summary | Action Taken |
|------|--------|------------------|--------------|
| 2026-02-27 | User | 1. Split flows into A (Interaction) and B (Underlying). <br> 2. Prioritize scenarios (Main/Sub/Special). | Created `patent/patentdoc/draft_v1.md` implementing the A/B structure and scenario-based detailed description. |
| 2026-02-27 | User | Update path name to patent\patentdoc | Updated references to `patent/patentdoc/` in tracking file. |
| 2026-02-27 | User | Fix rich text display errors (encoding issues) | Switched from RTF generation to HTML-based DOC generation with explicit UTF-8 charset. |

## 6. File Structure
- `patent/orgin.md`: Original content source.
- `patent/patentdoc/draft_v1.md`: **Latest Content Draft** (Markdown).
- `patent/patentdoc/patent_application_v2.doc`: **Latest Document File** (HTML-based, open with Word).
- `patent/example/`: Reference examples.
- `patent/patentbrain.md`: This tracking file.
