# 项目会话总控（Session Master）

## 1. 架构目标
- 目标：用“一个总控 session + 多个需求级 session”管理社交设计文档的状态、提交记录与跨会话继承
- 适用范围：docs/ 与 publish/ 下所有社交设计需求文档

## 2. Session 分层结构
- 总控文件：session/session.md（本文件）
- 需求文件目录：session/requirements/
- 命名规范：session/requirements/<doc_slug>.md
- 新需求动作：创建需求文档时，同步创建对应需求 session，并在本文件登记

## 3. 文档状态总览（与 index 同步）
- 同步基线：scripts/update_hub.py 的 DOCUMENTS 为唯一清单来源；当前 14 条
- 同步结果：index.html 当前 14 个文档卡片，要求与本节逐条一致
- 统一状态口径：
  - 已发布：index 可访问且发布页可打开
  - 维护中：本轮有持续迭代或最近有修复提交

| Doc ID | 文档标题 | 入口链接 | Tag | 状态 | 需求 Session |
|---|---|---|---|---|---|
| sevenday_social_progression | 🗺️ 七日社交渐进与地图玩法 CP | publish/sevenday_social_progression.html | Published | 已发布 / 维护中 | session/requirements/sevenday_social_progression.md |
| matchmaking_rules_analysis | ⚔️ 副本匹配规则详细方案 | docs/matchmaking_rules_analysis.html | Core | 已发布 | 待创建 |
| scheme2_detailed_design | 🏗️ 合线详细方案 | publish/scheme2_detailed_design.html | Tech | 已发布 | 待创建 |
| beagle_social_analysis_report | 📊 社交分析报告总览 | publish/Beagle_Social_Analysis_Report.html | Analysis | 已发布 | 待创建 |
| social_framework_report | 📊 社交框架整体汇报 | docs/social_framework_report.html | Report | 已发布 | 待创建 |
| concept_economic_symbiosis_squad | 🤝 7日版本社交生态框架 | docs/concept_economic_symbiosis_squad.html | Hot | 已发布 | 待创建 |
| gve_alliance_boss_design_v2 | 🐲 GVE 联盟 Boss 设计 v2.0 | docs/GVE_Alliance_Boss_Design_v2.html | v2.0 | 已发布 | 待创建 |
| login_flow_design | 🔐 登录流程设计 | publish/login_flow_design.html | Flow | 已发布 | 待创建 |
| town_relocation_design | 🏕️ 城镇布局与迁城系统设计 | publish/town_relocation_design.html | New | 已发布 | 待创建 |
| pvp_tile_detailed_design | ⚔️ PVP 地块玩法详细设计 | publish/pvp_tile_detailed_design.html | New | 已发布 | 待创建 |
| beagle_map_gameplay_design | 🗺️ 大地图pvp地块战斗玩法cp | publish/beagle_map_gameplay_design.html | Core | 已发布 | 待创建 |
| branching_design_spec | 🌿 合线方案CP | publish/branching_design_spec.html | Meta | 已发布 | 待创建 |
| light_social_design | 🎈 轻度社交设计 | publish/light_social_design.html | Casual | 已发布 | 待创建 |
| design_alliance | 🛡️ 联盟系统设计 | publish/design_alliance.html | System | 已发布 | 待创建 |

## 4. 提交记录总账
- 2026-03-30 | b809cba | docs: publish - finalize sevenday social progression release sync | 发布七日文档并同步索引
- 2026-04-01 | fe53497 | fix: publish - restore hub index entries and generator mapping | 修复 Hub 文档入口缩减与生成映射
- 2026-04-01 | 31d5cd2 | fix: publish - add missing sevenday svg assets for remote rendering | 补齐远端缺失 SVG 资源
- 2026-04-01 | 3b81c22 | docs: publish - update cp2/cp3 scope and cp2 timeline curve | 更新 CP2/CP3 Scope，重绘 CP2 时间轴，精简冗余文本
- 2026-04-01 | [已推送] | docs(sevenday): update CP1/CP2/CP3 scope, timeline SVG, and sync HTML/MD | 根据反馈重构七日社交方案、精简时间轴并更新图示
- 2026-04-01 | [已推送] | chore: clean up temp files and sensitive scripts from root directory | 删除根目录下临时生成的调试脚本、PAT 记录及冗余的垃圾文件

## 5. 运行规则（会话继承）
- 新对话启动时，先读取本文件的“文档状态总览 + 提交记录总账”
- 锁定目标文档后，必须继续读取对应需求 session，继承其状态、变更历史与待办
- 若发生流程级变更，记录在本文件；若发生文档内容变更，记录在需求 session
- **CRITICAL: 新对话必须优先阅读 `.trae/rules` 或 `rules/rules.md` 中的全局规则，确保遵循最新开发规范与门禁。**

## 6. 流程级变更记录
- 2026-03-30：初始化 rules/rules.md，正式生效“回复前缀与执行原则”
- 2026-03-30：创建 session/session.md，建立会话管理框架
- 2026-03-31：固化“新会话首轮执行 rules 与 mistakes 双检索”
- 2026-04-01：固化“新需求即建 index/update_hub 入口”“提交前展示拟提交清单并二次确认”
- 2026-04-01：会话架构重整为“总控 + 需求级 session”分层管理
- 2026-04-01：总控会话升级为“index 全量预览模式”，要求与 scripts/update_hub.py 和 index.html 保持同源同步
- 2026-04-01：rules 补充“index 创建维护统一规则”与“草稿到正式发布流程门禁”，并固化规则分层策略（rules 摘要化 + spec 细则化）
- 2026-04-01：rules 新增“执行优先级 Top 5”，将门禁、设计确认、三同步、提交二次确认、会话继承前置为最高优先级
- 2026-04-01：新增 spec/feedback-revision-spec.md，并在 rules 接入关键词“针对反馈进行一些修改”作为既有文档反馈修改流程入口
- 2026-04-01：更新 HTML 生成过滤规范，在 `scripts/md_to_spec_html.py` 及 `rules/rules.md` 中规定生成对外展示页时需移除内部管理章节（如第 8、9、10 章节）。

## 7. 注意事项
- 设计相关变更需事先书面确认；文档/脚手架类工作可直接执行，但必须记录
- Markdown 文档变动需保持与 HTML 单文件页面一致
- 需求级 session 不可缺失提交记录与状态字段

## 8. 版本
- v2.1 总控索引同步版（总控预览与 index 对齐）
- v2.2 新增“反馈修改流程”规则入口与 spec 链接
