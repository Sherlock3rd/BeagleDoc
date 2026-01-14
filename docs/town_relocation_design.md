# 🏘️ 城镇布局与迁城系统设计 (Town Layout & Relocation)

## 1. 城镇详细空间布局 (Detailed Spatial Layout)

城镇从中心向外依次分为三层同心结构，通过骨干路网串联。

### 1.1 核心层：建筑区 (Building Zone)
*   **位置**: 城镇正中心。
*   **形态**: **不规则圆形布局** (Irregular Circle)。虽然整体是圆的，但建筑边缘和广场边界会有自然的起伏和错落。
*   **功能**: 视觉地标与 NPC 交互中心（市政厅、交易所、工坊）。
*   **路网关系**: 被一条闭合的 **"内环路 (Inner Ring Road)"** 包围。所有从城门延伸进来的主干道均汇聚于此。
*   **交互**: 玩家车辆停在内环路边或广场空地，下车与 NPC 交互。

### 1.2 中间层：迁城区 (Relocation Zone)
*   **位置**: 位于"内环路"与"外城边界"之间的环形/矩形区域。
*   **构成**: 由多个 **不规则圆形街区 (Organic Round Blocks)** 组成。
    *   **街区形态**: 整体布局贴近正圆，但内部边缘做些许不规则变化，打破死板的网格感。
    *   **车位形态**: 车位不再是单纯的停车线，而是 **"营地基座 (Camp Base)"**。
        *   **正圆基础**: 每个基座以正圆为基础形状。
        *   **自然变化**: 在正圆范围内，根据地形或植被做些许不规则的边缘裁切或突起，显得更自然。
*   **车位与路的关系 (Slot-Road Logic)**:
    *   **临街直达**: 每个车位必须至少有一边紧邻道路（无论是主干道还是支路）。
    *   **无死角**: 确保车辆可以直接从道路倒车入库，**严禁**设计需要穿过 A 车位才能到达 B 车位的布局。
    *   **朝向**: 车位开口默认朝向最近的道路。

### 1.3 外围层：边界与城墙 (Boundary & Walls)
*   **当前版本 (v1.0)**:
    *   表现为非实体的视觉边界（如低矮栅栏、界碑）或自然地形边界。
    *   设有 2-4 个 **"出入口 (Gates)"** 连接野外大地图道路。
*   **未来扩展 (Future)**:
    *   在边界线上直接升起实体 **城墙 (City Walls)**。
    *   **预留空间**: 在迁城区最外圈与边界线之间，必须预留一条 **"外环路 (Outer Ring Road)"** 或 **"城墙基座带"** (约 2-3 个车位宽度)。这既是为了战时兵力调动，也是为了防止未来加城墙时挤压现有车位。

### 1.4 道路分级 (Road Hierarchy)
1.  **十字/米字主干道**: 连接城门与中心广场，最宽，将迁城区切割为不同扇区。
2.  **内环路**: 环绕中心建筑区，是交通枢纽。
3.  **毛细支路**: 分隔停车街区，确保每个车位都有路可走。

---

## 2. 核心讨论：迁城体验与车位机制 (Core Discussion)

针对“从A点迁移到B点”的核心体验，存在两种截然不同的设计方向。我们需要在此做出选择或融合。

### 🔴 方案 A：预订/契约模式 (Reservation Model) - "置业安家" (后续迭代讨论)
*   **状态**: **Pending (v2.0)** - 暂不开发，留作后续增值服务。
*   **核心体验**: **确定性**与**拥有感**。
*   **交互流程**:
    1.  **远程操作**: 在大地图点击目标城镇 -> 查看剩余空位数。
    2.  **预订/购买**: 支付费用（或消耗迁城令） -> 锁定一个车位（获得“地契”）。
    3.  **悠闲前往**: 玩家驾车前往，系统已为其保留位置，到达即可直接入住。

### 🔵 方案 B：纯野外模式 (Pure Wilderness) - "寻找车位" (后续迭代讨论)
*   **状态**: **Deprecated** - 暂不作为独立方案，已整合进方案 C。
*   **核心体验**: **真实感**与**竞争性**。

### 🟢 方案 C：全域抢占模式 (Global Scramble Model) - 7日版本执行方案
*   **状态**: **Confirmed (v1.0)** - 本次开发目标。
*   **核心理念**: **简化开发，统一规则**。
*   **规则设定**:
    1.  **统一机制**: 无论是城镇内还是野外，**所有车位均需现场抢占 (First-come, First-served)**。
    2.  **城镇优势**: 虽然机制也是抢，但城镇提供**安全区保护**（不可被攻击）和**便捷功能**（NPC/交易所）。
    3.  **野外风险**: 野外车位随处可见，但处于 PVP 区域，存在被攻击风险。
*   **新增功能：寻找最近车位 (Find Nearest Spot)**:
    *   **触发条件**: 玩家营地收起变为**载具形态**时，快捷栏出现【寻找车位】按钮。
    *   **交互逻辑**:
        1.  点击按钮 -> 系统扫描半径 X 米内最近的**空闲**车位。
        2.  **UI 标记**: 在 HUD 和小地图上高亮显示该目标位置。
        3.  **动态更新**: 玩家移动前往期间，系统持续检测目标状态。
        4.  **被抢占处理**: 若目标车位在途中被他人占据 -> 系统自动重新扫描下一个最近空位并刷新标记，同时弹出轻量提示“目标已被抢占，正在重新规划...”。

### ⚖️ 策划建议 (Architect's Recommendation)

**确认采用：方案 C (全域抢占)**。
在7日版本中，我们优先保证核心循环跑通。所有玩家到了城镇都需要**眼疾手快**找空位。这种“抢车位”的体验本身也具有很强的社交传播性（虽然可能带有负面情绪，但在早期测试中是很好的压力源）。

---

## 3. 基础迁城流程 (Basic Process)

*(以下流程基于“混合模式”草拟，待确认后细化)*

### 3.1 迁入 (Move In)
1.  **抵达**: 玩家驾驶载具穿过城门。
2.  **选址**:
    *   *若有预订*: 导航指引至专属车位。
    *   *若无预订*: 玩家在迁城区自由驾驶，寻找显示“空闲”标记的车位。
3.  **停泊**:
    *   将载具驶入车位框线内。
    *   系统检测位置合格 -> 提示【是否展开营地？】。
4.  **展开**:
    *   确认后，播放**展开动画**（车辆变形/帐篷搭设）。
    *   **生成碰撞体**: 营地展开后，该区域变为阻挡状态，其他车辆不可进入。

### 3.2 迁出 (Move Out)
1.  **收起**: 玩家在营地控制台选择【收起营地/迁出】。
2.  **结算**: 结算当前产生的资源产出或租金消耗。
3.  **撤离**:
    *   播放**收起动画**（变回载具形态）。
    *   车位状态重置为“空闲”。
    *   玩家恢复驾驶状态，可驶离城镇。

---

## 4. 待定事项 (TBD)
*   [ ] **车位规格参数**: $M \times M$ 的具体数值（如 4x4m 还是 6x6m？）。
*   [ ] **溢出处理**: 当城镇完全满员时，新来的玩家如何安置？（野外扎营？临时停车场？）。

---

## 5. 视觉示意图描述 (Visual Diagrams Descriptions)

以下描述用于辅助生成设计示意图或作为美术需求参考。**所有图片比例请保持 16:9。图片中出现的所有文字请使用英文 (All text in images must be in English).**

### 🖼️ 图一：城镇内部空间结构 (Town Internal Structure)
*   **推荐提示词 (Suggested Prompt)**:
    > **Isometric view, 16:9 aspect ratio. A bustling survival settlement town with clear urban planning. Central paved plaza with a large Town Hall building. Paved inner ring road with street lights. Surrounding the center is the Residential Zone with radiating irregular circular plots (Camp Bases), totaling approximately 50 plots. All plots are connected by a network of paved branch roads (no dead ends). The town is lively with infrastructure. High contrast between states: 70% of plots are Occupied (with tents, RVs, fences, warm lights, bustling with life); 30% of plots are Vacant (clearly defined empty flat ground with a prominent wooden sign reading "VACANT"). Heavy truck vehicles moving on paved roads looking for spots. Pedestrians walking.**
*   **详细描述 (Detailed Description)**:
    *   **视角 (Perspective)**: 45度鸟瞰图 (Isometric View).
    *   **核心 (Core)**: 繁忙的生存定居点 (Bustling Survival Settlement)。中心是铺设地面的**广场和市政厅** (Plaza & Town Hall)，有明确的**城市规划感** (Urban Planning)。
    *   **中圈 (Middle Ring)**: 辐射状排列的**居住区 (Residential Zone)**。车位是**不规则圆形的营地基座**。
        *   **数量**: **约 50 个**营地基座 (Total ~50 plots)。
        *   **城镇氛围**: 强调**基础设施** (Infrastructure)，如路灯 (Street Lights)、铺设的道路 (Paved Roads) 和清晰的地块边界。
        *   **路网串联**: 所有营地之间必须有**支路 (Branch Roads)** 相互串联，确保没有孤岛，车辆可以顺畅到达每个基座。
    *   **关键细节 (Key Details)**:
        *   **整体不规则 (Organic Shape)**: 布局依然保持不规则圆形的有机感，但内部设施要现代化/工业化。
        *   **基座统一 (Identical Size)**: 所有营地基座面积大小一致。
        *   **状态强对比 (High Contrast States)**:
            *   **已入驻 (Occupied)**: 建筑实体 + 暖色灯光 + 围栏，**生活气息浓厚**。
            *   **待入驻 (Vacant)**: 约占 **30%**。必须是**边界清晰的平整空地**，插着显眼的 **"VACANT" 木牌**，等待开发。
        *   **动态感 (Dynamics)**: 车辆在**铺装路面**上行驶，行人在设施间穿梭。

### 🖼️ 图二：迁城流程六格漫画 (Relocation Process - 6 Panels)
*   **推荐提示词 (Suggested Prompt)**:
    > **Comic strip style, 6 panels, 16:9 aspect ratio. Grid layout: 2 columns by 3 rows. Reading order: Top-Left is 1, Top-Right is 2, Middle-Left is 3, Middle-Right is 4, Bottom-Left is 5, Bottom-Right is 6. Numbered panels.**
    > **Panel 1: Player character returns to their camp base, camp structure folding and packing into a heavy truck.**
    > **Panel 2: Heavy truck driving on a highway road towards a distant town silhouette.**
    > **Panel 3: Truck arrives at a camp spot, but another vehicle is already deploying there. The spot is taken (Occupied).**
    > **Panel 4: Close-up on dashboard UI, finger pressing a button "FIND NEAREST SPOT".**
    > **Panel 5: Truck driving into a new empty spot with a "VACANT" sign.**
    > **Panel 6: Camp fully deployed and unfolded. Player character relaxing inside the camp yard.**
*   **详细描述 (Detailed Description)**:
    *   **形式 (Format)**: 六格漫画 (Comic Strip)，**3行 x 2列布局 (3 Rows x 2 Columns)**。
    *   **阅读顺序 (Reading Order)**:
        *   **第一行**: 左(1) -> 右(2)
        *   **第二行**: 左(3) -> 右(4)
        *   **第三行**: 左(5) -> 右(6)
    *   **Panel 1 (Pack Up)**: 玩家回到营地，营地建筑折叠打包，变形成一辆重型卡车 (Camp packing into truck)。
    *   **Panel 2 (Travel)**: 驾驶卡车在公路上行驶，前往远处的城镇 (Driving to town)。
    *   **Panel 3 (Missed)**: 到达目标车位，但眼看另一辆车刚进去并展开了 (Spot taken by rival)，玩家错失机会。
    *   **Panel 4 (Re-search)**: 车内仪表盘特写，手指点击 **【FIND NEAREST SPOT】** 按钮。
    *   **Panel 5 (Arrival)**: 根据指引来到最近的一个空闲车位 (Arrive at vacant spot)，看到 "VACANT" 牌子。
    *   **Panel 6 (Settled)**: 营地成功展开 (Deployed)，玩家在自己的院子里休闲游玩 (Player relaxing inside)。

### 🖼️ 图三：全局车位关系图 (Global Spots Relationship)
*   **推荐提示词 (Suggested Prompt)**:
    > **High-altitude Satellite Strategic Map View, 16:9 aspect ratio. Wide angle composition. Top-left corner: A small Wilderness Island (occupying approx 10% of the map), chaotic with red triangle markers, NO towns. Connected by a long bridge to a vast Civilized Continent on the right. The Continent features at least TWO distinct Irregular Circular Town Fortresses. Each town is smaller in size than the island. Towns are packed with dense green square markers (Safe Spots). The wilderness between towns has sparse red markers.**
*   **详细描述 (Detailed Description)**:
    *   **视角 (Perspective)**: **极高空卫星视角 (High-Altitude Satellite View)**，视野非常开阔。
    *   **地理比例 (Scale & Ratio)**:
        *   **海岛 (Island)**: 位于左上角，仅占画面的 **约 10%**。
        *   **城镇 (Towns)**: 大陆上至少展示 **2座** 完整的城镇要塞。
        *   **大小对比**: **单个城镇的面积 < 海岛的面积**。
    *   **车位分布对比 (Density Contrast)**:
        *   **海岛上**: 纯粹的野外（红三角），混乱无序。
        *   **大陆上**:
            *   **城镇内**: 绿色的安全营地（方块）高度集中。
            *   **城镇间**: 稀疏的野外营地（红三角）。
