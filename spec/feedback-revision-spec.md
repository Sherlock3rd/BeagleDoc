# 既有文档反馈修改流程规范（Feedback Revision Spec）

## 1. 目标与适用范围
- 目标：将“基于反馈修改已有文档”的动作标准化，确保 Markdown、HTML、资源、索引与提交记录一致
- 适用范围：已存在于 docs/ 与 publish/ 的设计文档迭代（包括文本、图示、图片资源）
- 启动关键词：针对反馈进行一些修改

## 2. 触发与输入
- 触发条件：用户明确表示基于反馈修改已有文档，或直接给出启动关键词
- 必要输入：
  - 目标文档标识（Doc ID 或 docs 路径）
  - 完整反馈清单（逐条、可执行、可验收）
  - 修改边界（只改文案 / 文案+图示 / 文案+图示+结构）

## 3. 标准流程（固定顺序）
1) 确认要改的文档  
   - 锁定 docs 源文档、publish 发布文档、需求级 session 文档
2) 收集完整反馈意见  
   - 将反馈按“必须改 / 建议改 / 可选改”分组，避免遗漏
3) 二次确认修改幅度与内容  
   - 形成可执行清单：改动点、影响段落、是否涉及设计变更
4) 修改现有 Markdown 文档  
   - 仅在既有 md 上迭代，不另起平行草稿
5) 触发 HTML 同步  
   - 前置条件：用户已明确确认“MD 内容可进入发布同步”
   - 关键词“反馈生成文档”或“生成文档”：基于最新 md 同步更新 html
6) 修改本地 HTML 文件  
   - 完成版式、图示、资源引用、段落结构对齐
7) 根据反馈继续调优  
   - 对文本与图片执行增删改，直到与反馈清单逐条对齐
8) 确认无误后执行 Git 更新  
   - 按 spec/git-update-spec.md 完成拟提交清单、范围确认、commit/push

## 4. 强制门禁（Gates）
- Gate A：未确认目标文档，不得开始改动
- Gate B：未形成完整反馈清单，不得进入 md 编辑
- Gate C：md 未完成，不得进行 html 同步
- Gate C1：未获得“MD 已确认可同步 HTML”的明确确认，不得生成或修改 html
- Gate D：html 与 md 不一致，不得进入提交
- Gate E：未完成提交范围二次确认，不得 push

## 5. 一致性与记录要求
- 一致性：docs 与 publish 内容必须同轮同步，不允许单边更新
- 资源：新增图片/SVG 必须确认路径可访问且已被 Git 跟踪
- 会话记录：
  - 文档内容变更写入 session/requirements/<doc_slug>.md
  - 流程规则变更写入 session/session.md
- 索引：若文档入口、标题、路径发生变化，需同步 scripts/update_hub.py、index.html、PUBLISHED_DOCS.md

## 6. 七日 CP 文档示例映射
- Doc ID：sevenday_social_progression
- 源文档：docs/map/sevenday_social_progression.md
- 发布文档：publish/sevenday_social_progression.html
- 需求会话：session/requirements/sevenday_social_progression.md

## 7. 与 rules 的链接关系
- rules/rules.md 中以“关键词：针对反馈进行一些修改”作为本流程入口
- rules 只保留入口与门禁，执行细则以本 spec 为准

## 版本
- v1.0：初始化“既有文档反馈修改”标准闭环
- v1.1：新增门禁“MD 需先确认后才可同步 HTML”
