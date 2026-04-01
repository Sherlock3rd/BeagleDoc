# Beagle 专有名词与术语表（v1）

## 1. 地块与地图结构
- GVE 地块（环状结构）：由两圈构成的圆形地块
  - 内圈：GVE 玩法真实区域（多人协作挑战与进阶资源产出）
  - 环间（内圈与外圈之间）：PVP 区域，用于通过战斗或社交协商来决定进入内圈体验与资源分配
  - 外圈之外：连接到常规 PVE 地块（安全主干道与周边探索）
  - 关键流程参考：七日社交渐进 CP 文档 [sevenday_social_progression.md](file:///d:/charlie/social/docs/map/sevenday_social_progression.md)
- PVP 地块（联盟单位，小中规模）：
  - 定义：以联盟为单位的玩家对战区域；在判定上采用 AllianceID 友军免伤与跨盟红名
  - 分层：L1（常驻低风险）、L2（整点中风险短窗），不承载领土政治，侧重热度与规则演练
  - 关键流程参考：PVP 地块玩法详细设计 [pvp_tile_detailed_design.md](file:///d:/charlie/social/docs/pvp_tile_detailed_design.md)
- GvG 地块（联盟单位，中大规模，独立场景）：
  - 定义：以联盟为单位的更大规模对战场景；独立地块与规则集，强调组织化与场景设计（占点/旗帜/评分/整点）
  - 使用：早期以“预演地块”为主（短窗、荣誉/装饰为主），避免过早绑定数值通道与领土政治
  - 关键流程参考：七日社交渐进 CP 文档 [sevenday_social_progression.md](file:///d:/charlie/social/docs/map/sevenday_social_progression.md)
- PVP 地块分层（L1/L2）：
  - L1（常驻低风险）：倒地快速复活、无核心掉落，用于分流与热身
  - L2（整点中风险短窗）：限时奖励、复活冷却提升，不引入全额掉落，用于制造热点
  - 关键流程参考：PVP 地块玩法详细设计 [pvp_tile_detailed_design.md](file:///d:/charlie/social/docs/pvp_tile_detailed_design.md)
- PVE 地块：安全探索与资源产出区域，玩家自由进出，无对抗压力
  - 关键流程参考：地图玩法路线 [beagle_map_gameplay_design.md](file:///d:/charlie/social/docs/beagle_map_gameplay_design.md)

## 2. 社交类型与判定
- 熟人社交 vs 生人社交：
  - 熟人社交：小队、固定伙伴为核心的协作关系（Day1-2 为主）
  - 生人社交：公共 PVP/GVE 场景下的陌生玩家并存协作或对抗（Day3 起增强）
  - 关键流程参考：七日社交渐进 CP 文档 [sevenday_social_progression.md](file:///d:/charlie/social/docs/map/sevenday_social_progression.md)
- 渗透社交 vs 隔离社交：
  - 渗透社交：随机匹配、临时协作、弱边界的协作形态
  - 隔离社交：以联盟为单位的明确边界（同盟免伤、跨盟红名），在公共 PVP 与 GVE 环间生效
  - 关键流程参考：七日社交渐进 CP 文档 [sevenday_social_progression.md](file:///d:/charlie/social/docs/map/sevenday_social_progression.md)
- 友军判定升级（SquadID → AllianceID）：
  - 当进入公共 PVP/环间 PVP 时，友军判定从小队升级到联盟，避免同盟内战，保留小队为战术执行单元
  - 关键流程参考：仗剑 7 日讨论 [sword_chronicles_7day_discussion.md](file:///d:/charlie/social/docs/sword_chronicles_7day_discussion.md)

## 3. 事件与玩法结构
- 整点广播：在 L2 或 GVE 整点开启前的跨区广播与引导，保障人气集中与组织化
  - 关键流程参考：PVP 地块玩法详细设计 [pvp_tile_detailed_design.md](file:///d:/charlie/social/docs/pvp_tile_detailed_design.md)
- GvG 预演地块（独立）：不与 GVE 环状结构混用，短窗、以荣誉/装饰为主的验证性对抗
  - 关键流程参考：地图玩法路线 [beagle_map_gameplay_design.md](file:///d:/charlie/social/docs/beagle_map_gameplay_design.md)
- 联盟 Boss（Rally Boss）：以联盟为单位的集结战斗目标（RoK 参考“打洛哈”），用于在早期形成“目标→行动”的合作过渡
  - 关键流程参考：七日社交渐进 CP 文档（SLG 过渡要素） [sevenday_social_progression.md](file:///d:/charlie/social/docs/map/sevenday_social_progression.md)
- 联盟集结（Rally）：频道内发起的集合与路径规划，用于组织化参与 L2/GVE/联盟 Boss 等事件
  - 关键流程参考：七日社交渐进 CP 文档（时间线与落位/整点广播） [sevenday_social_progression.md](file:///d:/charlie/social/docs/map/sevenday_social_progression.md)

## 4. 写作规范与引用
- CP 写作规范：每条 CP 必须拆为一章的完整方案，强调“玩家体验与社交渐进”，对标参考就近嵌入章节
  - 规范参考： [CP_WRITING_GUIDE.md](file:///d:/charlie/social/docs/CP_WRITING_GUIDE.md)
- 规则与会话：新增术语需同步维护并在会话中登记，确保跨会话可追溯
  - 规则参考： [rules.md](file:///d:/charlie/social/rules/rules.md)
  - 会话参考： [session.md](file:///d:/charlie/social/session/session.md)

## 5. 术语维护规则
- 新增术语：在本文件补充定义、使用场景与关键流程链接
- 术语变更：同步更新到相关流程文档（CP、地图设计、PVP 设计），并在 session 记录变更
- 对标引用：尽量提供项目内分析链接（analysis_Social/*），无直接对标需标注为风险项
