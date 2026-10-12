# 文档职责

示例文件名不等于强制布局。生成项目文档时将已存在文件名改成真实相对 Markdown 链接；不存在的推荐文件标待创建。

## 目录职责与分层

新项目文档较多、覆盖多个职责时，在 `docs/` 下按下面的主题归类；一两篇短文可以平铺。文件数量之外，也看内容是否有不同读者、更新时机或业务边界。文件夹名沿用项目惯例，`setup`、`testing` 等文件名不限定文档必须位于 docs 根目录。

同一职责内再按业务或组件拆分，例如 `domain/orders/` 放订单状态和权限规则，`interfaces/payments/` 放支付接口及错误语义。只有存在实际内容才建子目录，保持层级精简；跨主题文档按主要职责归属，由其他主题索引链接，同一事实只有一份主文档。

已有对应主题目录时，新文档直接归入该目录。普通更新沿用现有文件路径；用户要求整理或迁移时才移动旧文档，保留原文及用户内容，并同步 [文件链接与导航](links.md)。根 README、CONTEXT、TODO、CHANGELOG 等入口和主文档保留各自职责；根 CONTEXT 已承载领域规则时由 domain 索引链接它。

根 `docs/README.md` 负责跨主题导航；主题下有多篇文档或子主题时建立自己的 `README.md`，只写主题范围、每篇文档用途和链接。只有一篇短文时根索引直接链接正文。嵌套索引均需从根入口到达；目录链接和相对路径依据 [导航规则](links.md) 处理。

## 主文档职责

| 文件（示例） | 职责 | 更新 |
| --- | --- | --- |
| README | 定位、最短启动流程、目录与导航 | 当前事实原地改 |
| AGENTS | 项目特有约束、短收尾约定、Skill 入口 | 只在初始化或明确授权安装/改规则时改 |
| CONTEXT.md | 沿用现有领域上下文或会话入口职责 | 规则与事实原地改；总览链接详细主文档 |
| TODO/现有任务系统 | 当前任务、验收、下一步、待决 | 状态更新，不编造已完成 |
| CHANGELOG | 用户可见版本变化 | 历史保留，未发布去重 |
| .env.example | 变量、用途、假值、必填与加载说明 | 随配置变更，无真实秘密 |
| docs/README.md | 全部文档主题索引和目录导航 | 链接随文件增删移动更新 |
| docs/{主题}/README.md | 一个职责主题或子主题的范围、文件用途与索引 | 主题文件增删移动时更新 |
| docs/product/prd.md | 用户、目标、范围、非目标、验收 | 已确认需求原地改 |
| docs/product/acceptance.md | 需要独立维护时的详细验收条件 | 作为验收主文档，PRD 保留摘要和链接；无需独立时仍写在 PRD 中 |
| docs/domain/context.md | 业务规则、权限、状态语义 | 与已有 CONTEXT 同职责则引用已有主文档 |
| docs/architecture/architecture.md | 当前模块边界、依赖与数据流 | 原地改，决策原因链接 ADR |
| docs/architecture/data-model.md | 实体、关系、字段语义与约束 | 链接真实 schema，不复制整套机器定义 |
| docs/interfaces/api.md 或现有契约 | 认证、错误、接口使用语义 | 与现有机器契约保持一致 |
| docs/delivery/testing.md | 测试命令、策略与验收方式 | 区分实跑和未运行 |
| docs/delivery/release.md | 发布步骤与交付检查 | 验证与发布状态据实记录；版本历史仍由 CHANGELOG 承载 |
| docs/operations/setup.md | 开发环境完整准备流程 | 与 README/变量模板同步 |
| docs/domain/glossary.md | 当前术语与命名 | 更新定义，标明废弃名称 |
| docs/adr/ 或已有决策目录 | 为什么选择某方案及取舍 | 见 [ADR 规则](adr.md) |
| docs/notes/progress.md | 接续工作需要的成果、证据与下一步 | 同任务去重，不复制待办全表 |
| docs/notes/known-issues.md | 现象、条件、影响、绕过、解决状态 | 更新原条目，保留历史 |
| docs/operations/ 下的 deployment.md、security.md、operations.md | 实际运行、权限、安全、备份与故障规则 | 有实际需求才创建 |
| CONTRIBUTING | 人类协作、评审、提交约定 | 已授权规则原地改 |
| LICENSE | 权利人指定的授权条款 | 未指定则保持未指定 |

现状、规范和历史可以同文件共存，但必须明确：代码是当前实现证据，明确规范是约束；实现偏离约束不能通过静默改文档合理化。总览中同一信息只保留必要摘要和来源链接。

核对实现只读受影响范围；全面审计依用户范围展开。纯死链审计直接使用 [链接规范](links.md)。

有常用模板的主题见 [模板目录](../assets/templates/)；总索引采用 [docs/README 模板](../assets/templates/docs-index.template.md)，主题索引采用 [主题 README 模板](../assets/templates/topic-index.template.md)，新决策采用 [ADR 模板](../assets/templates/adr.template.md)。模板仅提供结构，实际路径由初始化适配。
