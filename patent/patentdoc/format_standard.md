# Patent Document Format & Guidelines
Based on the analysis of `patent/example/` documents.

## 1. Document Structure Standard

The patent documentation should follow this structured approach to ensure comprehensive coverage and technical depth.

### 1.1 Title
*   Clear, technical, and descriptive name of the invention.
*   Format: `一种[应用场景]的[核心技术]方法、装置、设备及存储介质`

### 1.2 Section I: Original Technical Pain Points (Background Technology)
*   **Objective:** Clearly articulate the limitations of current solutions.
*   **Format:**
    *   **Pain Point N:** Title of the problem.
    *   **Description:** Detailed explanation of the bottleneck (e.g., "Coupling between art and logic", "Performance bottlenecks").
    *   **Consequence:** What is the negative impact? (e.g., "Linear increase in memory overhead", "Workflow disconnection").

### 1.3 Section II: Core Invention Overview
*   **Objective:** High-level summary of the proposed solution.
*   **Content:**
    *   Core concept name (e.g., "Deferred Entity Instantiation").
    *   Brief explanation of the core logic.
    *   Key subsystems or modules involved.

### 1.4 Section III: Detailed Implementation - Part 1 (Production/Tools)
*   *If applicable, describe the offline/production pipeline.*
*   **Workflows:** How users (e.g., artists/designers) interact with tools.
*   **Data Structures:**
    *   JSON schemas.
    *   Binary file formats (headers, fields, types).
    *   Unique ID generation logic.
*   **Data Flow:** Diagrammatic description of data movement (Editor -> Exporter -> Runtime).

### 1.5 Section IV: Detailed Implementation - Part 2 (Runtime/Logic)
*   **System Architecture:** List of modules and their responsibilities.
*   **Core Definitions:** Enums, States, Entity Types (e.g., "Type 1: Entity" vs "Type 2: MapUnit").
*   **Algorithms & Logic:**
    *   Streaming/Loading mechanisms.
    *   Spatial Query algorithms.
    *   **Core Conversion/Interaction Flow:** Step-by-step breakdown (Phase 1 to Phase N).
    *   Sequence Diagrams (described in text).
*   **Protocols:** Network packet structures (ProtoBuf definitions).
*   **Configuration:** Resource tables and properties.

### 1.6 Section V: Beneficial Effects (Improvements)
*   **Objective:** Highlight the advantages over the "Pain Points".
*   **Format:** Numbered list.
*   **Content:**
    *   Performance metrics (e.g., "Reduced memory by 99%").
    *   Workflow improvements (e.g., "Decoupling").
    *   Scalability (e.g., "Orders of magnitude increase").

### 1.7 Section VI: Differentiation Analysis (Optional but Recommended)
*   **Objective:** Pre-emptively distinguish from known existing patents/techniques.
*   **Format:** Comparison table or structured text.
*   **Dimensions:** Scope, Level of operation (e.g., Rendering vs Logic), Data flow.

---

## 2. Key Formatting & Content Requirements

*   **Technical Precision:** Use actual variable names, struct definitions, and protocol fields. Do not just describe vaguely.
*   **Code Snippets:** Include pseudo-code, C# structs, or ProtoBuf definitions where they clarify the data structure.
*   **Step-by-Step Flows:** Use "Phase 1", "Phase 2" structure for complex logic.
*   **Quantitative Claims:** Where possible, use comparative metrics (e.g., "hundreds vs tens of thousands").

## 3. Example Reference
*   **Source:** `patent/example/一种MMORPG游戏中大规模可交互地图资源的延迟实体化方法...docx`
*   **Style:** Technical Disclosure / Internal Patent Draft.
