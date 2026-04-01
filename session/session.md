# 项目会话（Session）

## 1. 当前阶段
- 阶段名称：规则框架初始化 v1.0 → 七日版本地图与社交渐进（CP 已发布，进入迭代维护）
- 目标：在遵循规则的前提下，维护“七日版本社交渐进中地图玩法渐进讨论”发布版，按反馈持续迭代并保持 HTML 与索引同步

## 2. 当前状态
- 已创建：
  - rules/rules.md（角色确认、回复前缀、执行原则、错误与更新流程、文档维护规范要点）
- 正在进行：
  - 新需求：七日版本社交渐进中地图玩法渐进讨论（docs/map/sevenday_social_progression.md，已按 CP 规范重写，并拆分 CP-A/B/C 三套完整方案）
- 待维护：
  - mistakes/（记录模板与归纳方式）
  - 双重索引：根目录 PUBLISHED_DOCS.md（计划）与 index.html（计划）

## 3. 下一步规划
- 建立 mistakes/ 目录与 README（记录模板、归纳/标签规范、防呆清单）
- 建立根目录 PUBLISHED_DOCS.md（双重索引之一），收录当前已发布/确认文档
- 设计 index.html 的单文件入口（Hub），后续将发布文档统一纳入（遵循漫画手绘风格）
- 执行前流程引入：检索 mistakes/ 同类问题与防呆清单
- CP 文档流程：待策划确认后，收到“生成文档”关键词再生成 HTML 并维护索引

## 4. 变更记录
- 2026-03-30：初始化 rules/rules.md，正式生效“回复前缀与执行原则”；纳入 brain 文档维护规范要点
- 2026-03-30：创建 session/session.md，建立阶段与规划框架
- 2026-03-30：按 rules 流程新增 docs/map/sevenday_social_progression.md；在“生成文档”关键词未发出前，撤回 publish/sevenday_social_progression.html 与相关索引；在 mistakes/README.md 登记本次偏差并更新防呆清单
- 2026-03-30：重写 CP 文档并加入 CEO 的“SLG 转化验证”目标；将第三章与后续章节重构为 CP-A/CP-B/CP-C 三套完整方案；在 CP_WRITING_GUIDE.md 增补“常见错误与防呆”
- 2026-03-30：新增 docs/beagle_glossary.md（术语表），收录 GVE 环状地块、PVP L1/L2、熟人/生人、渗透/隔离、友军判定升级、整点广播等术语，并为关键流程文档提供单点链接
- 2026-03-30：更新 spec/rules-bootstrap-spec.md 与 rules/rules.md，将术语表纳入标准交付物；同步七日 CP 文档以环状结构修正三条路径的时间线与体验叙述
 - 2026-03-30：“生成文档”执行：生成 publish/sevenday_social_progression.html（图文并茂，含环状 GVE 与三条时间轴 SVG 示意）；更新 index.html 卡片入口与 PUBLISHED_DOCS.md 索引
- 2026-03-31：针对“新会话未按 rule 执行”问题完成流程纠偏：执行 rules 与 mistakes 双检索、在 mistakes/README.md 增加会话启动类错题记录，并将“新会话首轮规则检查”固化为防呆项
- 2026-04-01：七日 CP 文档节奏同步：CP-B 调整为 Day3 L1/L2、Day4 外圆 GvG、Day5 内圆 GVE；CP-C 调整为 Day6 内外圆同步开放，Day3-5 禁入并迷雾遮挡；对应同步 publish/sevenday_social_progression.html、docs/map/sevenday_social_progression.md、cp-b/c 时间轴图
- 2026-04-01：CP-A 纠偏同步：协作峰值锚定 Day4，Day5-7 改为“外圆 GvG 与内圆 GVE 多轮轮转”；移除“GvG 强化窗口/强化验证窗”等歧义术语，并同步 HTML、Markdown 与 cp-a 时间轴图
- 2026-04-01：术语统一同步：CP-B“熟人→生人”描述由“强化跨队协同”改为“形成跨队协同”，并在发布页与源文档保持一致
- 2026-04-01：收到“可以发布文档”指令后完成发布确认：同步更新 docs/map/sevenday_social_progression.md 与 publish/sevenday_social_progression.html 的发布状态描述，并更新 index.html 与 PUBLISHED_DOCS.md 索引信息
- 2026-04-01：发布流程修正：补齐 scripts/update_hub.py 的 DOCUMENTS 配置，纳入 sevenday_social_progression.html，避免后续自动生成 index.html 时丢失该文档入口
- 2026-04-01：Hub 回归修复：定位到 scripts/update_hub.py 仅保留 7 条配置导致重生成 index 时文档卡片缩减；已恢复并扩展为 14 条（含登录流程），并新增 docs/* 与 publish/* 混合链接支持，重新生成 index.html

## 5. 注意事项
- 设计相关变更需事先书面确认；文档/脚手架类工作可直接执行，但必须在本文件记录
- Markdown 文档变动需保持与 HTML 单文件页面一致（修改即同步）

## 6. 版本
- v1.0 初始化
