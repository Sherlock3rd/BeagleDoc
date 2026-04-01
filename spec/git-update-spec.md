# Git 更新流程规范（Git Update Spec）

## 1. 目标与适用范围
- 目标：固化统一的 Git 更新与发布流程，保障质量、一致性与可追溯性
- 适用范围：本仓库的所有文档与代码更新（含规则、session、spec、publish/doc）

## 2. 先决条件
- 本地已配置 Git 用户信息与远程仓库地址
- 环境：Windows（PowerShell），遵循本项目规则与文档维护规范
- 密钥管理：使用本机环境变量与 GitHub Secrets；严禁将任何密钥写入仓库或日志

## 3. 分支策略
- 主干：master（仅通过受控合并进入）
- 功能分支：feature/<模块>-<简述>
- 修复分支：fix/<模块>-<问题>
- 文档分支：docs/<范围>-<简述>
- 命名示例：feature/social-session-bootstrap、docs/spec-git-update

## 4. 提交信息规范（Commit Message）
- 格式：<type>: <scope> - <summary>
- type：feat / fix / docs / refactor / chore / test
- scope：模块或目录（rules | session | mistakes | spec | publish | docs）
- 示例：docs: spec - add git update spec v1.0

## 5. 更新与发布流程（最小闭环）
1) 创建分支  
   - 从 master 拉取最新，再创建对应分支（feature/fix/docs）
2) 实施修改  
   - 遵循文档维护规范（Hub First + Dual Indexing），涉及发布内容时同步维护 index.html 与 PUBLISHED_DOCS.md
3) 自检与验证  
   - 运行格式/类型检查（如 lint/typecheck），若无配置则执行手动校验（链接可用性、结构完整性、路径正确性）
   - 执行 IDE 诊断（GetDiagnostics）确保无新增错误
4) 提交与推送  
   - 先输出“拟提交文件清单”（含已跟踪修改与未跟踪新增），并二次确认提交范围（全部变更 / 仅本次变更）
   - 仅在确认后执行 git add 与 commit，按规范编写提交信息
   - 推送前复核发布页依赖资源（图片/SVG/CSS/JS）已被 Git 跟踪，再推送到远程同名分支
5) 发起合并请求（PR）  
   - 标题包含 type/scope/summary；描述列出变更点、影响范围、自检项与验证结果
6) 评审与合并  
   - 通过评审后，Squash & Merge 到 master；保留清晰的变更日志
7) 同步会话与规则  
   - 在 session/session.md（总控）登记流程级更新
   - 若本次变更指向具体需求文档，同步更新对应 session/requirements/<doc_slug>.md
   - 若涉及流程/规范变更，同步维护 rules/rules.md

## 6. 质量门槛（Quality Gates）
- 文档一致性：Markdown 改动与 HTML 单文件页面保持一致（修改即同步）
- 结构校验：链接有效、路径正确、引用文件存在
- 索引完整性：新发布需求在开发期即同步 index.html 与 scripts/update_hub.py，不得仅在末尾补录
- 范围确认：提交前必须完成“提交范围二次确认”，避免误提/漏提
- 风格统一：外部文档 HTML 保持漫画手绘风格（Tailwind + Patrick Hand）
- 诊断通过：IDE 诊断无阻塞性错误

## 7. PR 与合并规范
- 标题：<type>(<scope>): <summary>
- 内容：变更列表、理由与影响、验证清单、回滚方案
- 标签：docs / rules / session / spec / publish / breaking-change（如有）
- 合并：优先 Squash，保持 master 历史整洁；必要时使用 Merge Commit 保留分支结构

## 8. 版本与标签（如涉及发布）
- 版本语义化：文档/规范以 vX.Y 维护（如 v1.0 初始化）
- 标签：在 master 上打轻量标签（docs-v1.0、spec-git-update-v1.0）
- 变更日志：在 PR 中记录，必要时维护 CHANGELOG 段落

## 9. 密钥与权限管理（强制规范）
- 禁止：将任何密钥（如 GitHub PAT、OAuth Token）写入仓库、提交历史或 PR 内容
- 本地使用：通过环境变量（如 $Env:GITHUB_TOKEN）临时注入；使用后立即清除
- 远程与自动化：在 GitHub 仓库设置中配置 Secrets（如 ACTIONS 用途）；按最小权限原则分配
- 审计与轮换：定期轮换密钥；若怀疑泄漏，立即撤销并追踪影响范围

## 10. 故障与回滚流程
- 提交前失败：在本地修复，自检通过后再提交
- 合并后发现问题：
  - 紧急修复：创建 fix 分支，修复后走标准 PR
  - 回滚：使用 Revert 恢复到前一健康提交；在 session 登记事件与原因
- 错题记录：在 mistakes/ 记录根因与防呆清单更新

## 11. 常用命令（PowerShell 示例）
- 拉取与分支：  
  - git fetch origin  
  - git checkout -b docs/spec-git-update origin/master
- 提交与推送：  
  - git add .  
  - git commit -m "docs: spec - add git update spec v1.0"  
  - git push -u origin docs/spec-git-update
- 合并（由平台完成）：PR -> Review -> Squash & Merge

## 12. 生效与维护
- 本规范自创建起生效；后续更新以本文件最新版本为准
- 规范调整需在 rules/rules.md 同步，并在 session 中记录变更
- 发布类文档需遵循 Hub First 与 Dual Indexing（index.html 与 PUBLISHED_DOCS.md 的维护）

## 版本
- v1.0 初始化
