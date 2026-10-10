# 初始化与项目入口

只在用户要求初始化或明确安装维护入口时执行写入。接手项目发现上下文缺失但未要求建档时，读取现有材料并提出缺项，不自动安装规则。更新单文档和只读审计不触发初始化。

1. 找现有 README、AGENTS/AGENT/CLAUDE、CONTEXT、任务入口、CHANGELOG、环境模板和 docs，沿用实际路径。
2. 看项目清单、入口、配置和相关测试确认事实；不猜命令和历史。
3. 依据 [文档职责](doc-contracts.md) 选档，有内容才建文件，不建空目录或占位文档。用 [模板目录](../assets/templates/) 中的相关结构，填充事实并裁掉无内容章节、未创建目标和生成说明。
4. 优先在现有 AGENTS.md、AGENT.md 或 CLAUDE.md 中增补缺失执行约定，保留原命名与内容；仅在这些入口均不存在或用户明确指定新入口时，用 [AGENTS 模板](../assets/templates/AGENTS.template.md) 创建 AGENTS.md。已有多个入口时沿用实际主入口，其他入口引用已有维护约定，不重复安装；维护小节只留一个。
5. 不复制 Skill 维护规则到项目。已有 doc-maintenance 若有项目特例可保留；若纯粹重复，在明确整理范围内将重复规则改为入口，不擅自删除用户原文。
6. 为已创建文件生成真实可点击导航。多个主题文档时增加 docs/README；文件少时可由根 README 承担索引，参考 [导航规则](links.md)。
7. 核对链接、定义和安全可验证命令，报告新建/沿用、待确认、实际验证。完成后重新执行应无重复维护章节或事件条目。

## 规模建议

以下目录树是结构示例，标明按需的项不要求全量创建。生成项目导航时使用带真实链接的列表。

### 小型

```text
project/
├── README.md
├── AGENTS.md
├── TODO.md                  # 或已有任务入口
├── CONTEXT.md               # 按已有职责和实际需求保留
├── CHANGELOG.md             # 有用户可见变化时
├── .env.example             # 有环境变量时
└── docs/                    # 有独立主题内容才创建
    ├── README.md            # 多个主题文档时创建索引
    ├── architecture.md      # 简短说明可并入根 README
    └── testing.md           # 有测试或验收步骤时
```

### 中型

```text
project/
├── README.md
├── AGENTS.md
├── CONTEXT.md
├── TODO.md
├── CHANGELOG.md
├── .env.example
└── docs/
    ├── README.md
    ├── prd.md
    ├── architecture.md
    ├── data-model.md        # 有持久化或复杂模型时
    ├── api.md               # 有接口时；优先现有机器契约
    ├── testing.md
    ├── setup.md
    ├── glossary.md          # 术语确有独立价值时
    ├── adr/                # 确认重要决策时
    └── notes/              # 有实际交接或已知问题时
        ├── progress.md
        └── known-issues.md
```

### 长期维护或多人协作

```text
project/
├── README.md
├── AGENTS.md
├── CONTEXT.md
├── TODO.md
├── CHANGELOG.md
├── .env.example
├── CONTRIBUTING.md          # 有协作要求时
├── LICENSE                  # 仅在权利人指定许可证后
└── docs/
    ├── README.md
    ├── prd.md
    ├── architecture.md
    ├── data-model.md
    ├── api.md
    ├── testing.md
    ├── setup.md
    ├── glossary.md
    ├── deployment.md        # 有部署流程时
    ├── security.md          # 有权限/敏感数据约束时
    ├── operations.md        # 有运维要求时
    ├── adr/
    └── notes/
        ├── progress.md
        └── known-issues.md
```

CONTEXT 可能是现有会话总览，也可能是业务上下文，先读再沿用。根 CONTEXT 若承载业务规则，就不再建立同职责的 docs/context；若总览之外需要独立业务文档，可按实际需要创建并链接。新建会话入口主要链接目标、现状与任务来源，避免复制完整技术栈、进度与待办。

## 完成条件

已存在文档入口可达；AGENTS 维护小节至多一份；没有复制完整维护规则；未知事实待确认；用户原有内容保留；规范冲突已提出；初始化重复执行不会产生新增重复条目。
