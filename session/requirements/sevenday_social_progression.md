# 需求会话：七日社交渐进与地图玩法 CP

## 1. 基本信息
- Doc ID：sevenday_social_progression
- 需求名称：七日社交渐进与地图玩法 CP
- 源文档：docs/map/sevenday_social_progression.md
- 发布文档：publish/sevenday_social_progression.html
- Hub 入口：index.html（publish/sevenday_social_progression.html）
- 生成配置：scripts/update_hub.py（DOCUMENTS）
- 当前状态：已发布，迭代维护中
- 当前阶段：维护阶段（修正与一致性保障）
- 最后更新：2026-04-01（反馈迭代）

## 2. 目标与验收口径
- 目标：确保 CP1/CP2/CP3（按 Scope 分层）方案与发布页一致，并完成“耐受度验证方案 + 指标映射”对齐
- 验收口径：
  - docs 与 publish 内容一致
  - index.html 与 scripts/update_hub.py 入口一致
  - 发布页引用资源均在远端可访问
  - 提交记录可追溯

## 3. 当前状态快照
- 内容状态：已完成主要文档撰写与发布时间轴修正
- 发布状态：已发布
- 索引状态：已纳入 index.html，update_hub 支持 docs/publish 混合链接
- 资源状态：docs/assets/sevenday/ 四张 SVG 已推送远端
- 风险状态：中，当前主要风险为发布页 JS 动态插图锚点在不同渲染结构下可能失效，需优先做可视回归

## 4. 需求级变更记录
- 2026-03-30：新增 docs/map/sevenday_social_progression.md，并在“生成文档”关键词未发出前撤回提前发布产物
- 2026-03-30：按 CP 规范重写文档，加入 CEO 的“SLG 转化验证”目标，拆分 CP-A/B/C 三套完整方案
- 2026-03-30：执行“生成文档”，生成 publish/sevenday_social_progression.html 并更新索引
- 2026-04-01：节奏同步修正：CP-B 调整为 Day3 L1/L2、Day4 外圆 GvG、Day5 内圆 GVE；CP-C 调整为 Day6 内外圆同步开放
- 2026-04-01：CP-A 纠偏：协作峰值锚定 Day4；Day5-7 改为外圆 GvG 与内圆 GVE 多轮轮转
- 2026-04-01：术语统一：CP-B“强化跨队协同”改为“形成跨队协同”
- 2026-04-01：发布流程修正：补齐 update_hub 的 sevenday 入口，避免后续重生成丢入口
- 2026-04-01：Hub 回归修复：恢复缺失文档入口并扩展为 14 条，重生成 index.html
- 2026-04-01：远端图片修复：补齐 docs/assets/sevenday 四张 SVG 并推送
- 2026-04-01：按反馈完成 CP 重构：按 Scope 重划 CP1/CP2/CP3；新增“耐受度映射数据指标”；CP1 明确新增城镇争夺 GvG 与联盟进程、去除 GVE 外圈 PVP 属性；CP2 新增联盟攻城与迁城前置强协作；CP3 固化 Day3-L1/L2、Day4-外圆 GvG、Day5-内圆 GVE 分段递进；发布页待 md 复核确认后再同步
- 2026-04-01：对标口径补充：CP 内城镇 PVE/城镇 PVP 统一主要对标《三谋》；仅 CP1 的 GvG 地块扩展争夺玩法参考 RoK/CoD 领土争夺
- 2026-04-01：收到 MD 复核确认后执行 HTML 同步；保持现有图示形式，发布页新增结构图与 CP1/CP2/CP3 渐进体验轴图片块；重画 CP1（cp-a）与 CP2（cp-c）时间轴节点以匹配新方案
- 2026-04-01：HTML 评审修正：去除页面重复标题展示、恢复分段分块样式（section/table wrapper）、移除总览中的两条无效展示项（统一约束/对标口径）、并将 CP1/CP2/CP3 渐进轴图示定位到各自“渐进体验轴（时间轴）”小节下方
- 2026-04-01：定位并修复“渐进轴图缺失”问题：改为按 CP section 定位“渐进体验轴（时间轴）”列表项插图；当前进入新对话前交接状态为“继续进行 HTML 可视回归与版式微调，不改 MD 设计内容”
- 2026-04-01：按“文本分类 + 图文顺序”重排文档格式：CP1/CP2/CP3 统一改为 5 段结构（体验/指标/Scope/时间轴/优缺点）；修正 CP2/CP3 时间轴顺序；发布页插图锚点从“列表项匹配”升级为“标题或后续列表匹配”，避免结构调整后图文错位
- 2026-04-01：图文一致性优化：精简并统一了 `sevenday_social_progression.md` 中 CP1/CP2/CP3 渐进体验轴的列表文案，使其与 SVG 导图描述完全一致；并在 `sevenday_social_progression.html` 的渲染逻辑中过滤掉展示时多余的时间轴文本列表，仅保留插图；同时在总控 session 文档末尾补充“新对话必读 rule”指引。
- 2026-04-01：基于 `matchmaking_rules_analysis.html` 的现代清爽风格，重构了 `sevenday_social_progression.md` 的层级标题（去除“文本分类”字样）和 `publish/sevenday_social_progression.html` 的样式表（采用 Inter 字体体系、扁平化圆角、细边框阴影及响应式表格），大幅提升了页面的阅读体验。
- 2026-04-01：发布页图文展示优化：去除了插图容器的 `max-width: 800px` 限制，使所有的图片宽度能够随文档容器的宽度自动铺满拉伸（满幅展示）；同时修复了 `cp-a-timeline-v2.svg`、`cp-b-timeline-v2.svg`、`cp-c-timeline-v2.svg` 中顶部气泡说明框与曲线可能发生的重叠遮挡问题，上调了气泡坐标。
- 2026-04-01：修正 CP1 的渐进逻辑：Day3 调整为无争夺性的内圆 GVE 合作行动，Day4 为联盟目标形成与组织化，Day5-7 开启城镇争夺 GvG 并维持社交强度高位。同步更新了 `sevenday_social_progression.md` 中的文案，并重绘了 `cp-a-timeline-v2.svg` 的曲线走势与节点文本，使曲线在 Day5 达到主峰后平稳保持至 Day7。
- 2026-04-01：根据用户反馈再次优化文档格式：1) 去除了 `sevenday_social_progression.md` 中错误的“文本分类”标题前缀；2) 将 CP1/CP2/CP3 中的 `新增内容 Scope` 部分用引用块（>）形式进行分块重整，突出“新增玩法模块”、“地图设定调整/体验优化”与“对标参考”，让 Scope 大小一目了然。
- 2026-04-01：根据用户反馈去除了三张渐进轴 SVG（`cp-a-timeline-v2.svg`, `cp-b-timeline-v2.svg`, `cp-c-timeline-v2.svg`）中没有意义的顶部标题文本（如“CP1 最大 Scope”、“CP-B 慢转”、“CP2 中等 Scope”等）以及底部的“节奏特征”文本描述，彻底清理了冗余信息，使图表更加简洁聚焦。
- 2026-04-01：同步修改并清理了 `publish/sevenday_social_progression.html` 中的“文本分类”冗余标题前缀，并将 HTML 中的“新增内容 Scope”部分直接使用 `<blockquote class="highlight-box">` 等原生 HTML 标签进行重新排版。同时，将“在已经生成 HTML 后修改内容时，禁止使用脚本读取 MD 重新生成，必须直接修改 HTML”的新规记入了 `rules/rules.md`，并在 MD 中做了对应同步。
- 2026-04-01：重写了 MD 和 HTML 中的“7. 对比与总结”章节，将其结构化为三个维度：“7.1 方案定位与验证重点”（明确各方案的投入产出比与验证侧重点）、“7.2 核心观测指标共识”（统一商业与留存口径）以及“7.3 地块与解锁规则约束”（重申 GVE 结构与解锁底线），提升了总结的清晰度与深度。
- 2026-04-01：根据用户反馈再次重构了“7. 对比与总结”章节：将“7.1 方案定位与验证重点”重构为直观的 Markdown / HTML 表格横向对比（包含方案、投入定位、新增机制、验证侧重点、GVE 设定五个维度）；并将共识约束等总结性内容收拢在表格下方的“7.2 总结与共识约束”中。
- 2026-04-01：移除了 HTML 文件中不需要对外展示的内部管理章节（第 8、9、10 章节：CP 发散方法总结、后续规划、引用与索引），并更新了 `rules/rules.md` 以及 `scripts/md_to_spec_html.py` 中的生成规范，规定后续 HTML 生成过程必须过滤掉这类纯内部信息。
- 2026-04-01：根据反馈，移除了 `publish/sevenday_social_progression.html` 中 `GVE 环状地块结构图` 下方多余的“保持当前图示形式...”注释文本。
- 2026-04-01：修正了关于 GVE 地块的物理结构定义，明确“内外双圈”的物理结构在所有方案中均存在；在 CP1 和 CP2 中是将双圈合并视为整体以弱化外圈对抗概念，而非物理上不存在双圈。同步更新了 MD 与 HTML 中的地块定义、Scope 设定、时间轴描述以及横向对比总结表。
- 2026-04-01：重构了 CP1 的新增内容 Scope。1) 将“新增玩法模块”精简为“城镇争夺型 GvG、特殊争夺点 GvG 或领土玩法模块”，并将对标参考直接移入该模块下作为列表项；2) 将“地图设定调整”修改为“已有内容修改”，并明确定义 GVE 地块需改为纯 GVE 区域（不再具备 PVP 属性），作为前置的联盟协作玩法存在。
- 2026-04-01：反思并修正了 CP1 时间轴（Day4）的表述。去除了主观臆造且缺乏实际玩法支撑的抽象名词“组织化”（原为“联盟目标形成与组织化”），替换为具体的玩法描述：“合作行动（GVE 继续推进，为后续 GvG 积累资源与阵地）”。同步更新了 MD、HTML 以及 SVG 图片（`cp-a-timeline-v2.svg`）中的对应文本（包含气泡文字与底部描述），并将此次错误记录入 `mistakes/README.md`。
- 2026-04-01：统一优化了 CP2 和 CP3 的新增内容 Scope 格式。将原本独立的“对标参考”分块移除，将其内容作为具体的列表项，直接合并到了各自的“新增玩法模块”分类下方，保持与 CP1 一致的排版结构。
- 2026-04-01：CP2 结构与时间轴修正：重新明确 CP2 的 GVE 地块保留内外圈分割，且外圈具备 GvG 属性并先于内圈开启以验证对抗；将城镇玩法降级为前置协作组织，其对抗峰值低于外圈 GvG。同步调整时间轴为 Day4 城镇占领、Day5 外圈 GvG 开启、Day6 内圈 GVE 开启（峰值：Day6 > Day5 > Day4），并重绘了 cp-c-timeline-v2.svg。
- 2026-04-01：依据用户反馈再次修正 CP2/CP3：调整 CP2 时间轴图片峰值高度（使 Day7 明确回落至低于 Day6 且高于 Day4），重写 CP2/CP3 的“已有内容修改”为“内外圈拆分分批次开启，外圈 GvG 先开启，并且外圈场地需要承载 GvG 属性”，并彻底删除了“流程前置要求”与“体验优化”等冗余内容。
- 2026-04-01：CP3 “已有内容修改”补充：增加“PVP L2 地块要增加联盟对抗的动机，需要修改并调整投放内容”。

## 5. 提交记录
- b809cba | docs: publish - finalize sevenday social progression release sync
- fe53497 | fix: publish - restore hub index entries and generator mapping
- 31d5cd2 | fix: publish - add missing sevenday svg assets for remote rendering
- 3b81c22 | docs: publish - update cp2/cp3 scope and cp2 timeline curve

## 6. 后续维护清单
- 文案改动后，同步更新 docs 与 publish，并更新本文件“需求级变更记录”
- 若新增图示资源，推送前先校验是否已被 Git 跟踪
- 若新增入口或调整排序，同步更新 scripts/update_hub.py 并重生成 index.html
- 提交前按规则执行“拟提交清单 + 全量/部分提交二次确认”
- 新对话接手先验证三张渐进轴图是否在 CP1/CP2/CP3 各自位置正确显示（含强刷缓存后复验）
- 新对话优先做发布页可视回归：标题层级、分段分块、图片注释与表格样式一致性

## 7. 新会话继承指引
- 新对话接手该需求时，先读取 session/session.md 和 rule.md，再读取本文件
- 先确认“当前状态快照”，再继续执行本需求的迭代任务
- 输出结果时，附带本文件最新变更项，保证跨会话连续性
