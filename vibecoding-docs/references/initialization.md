# vibecoding-docs：项目文档初始化

本文是 `vibecoding-docs` 的初始化参考。它规定首次建档时建立什么、何时写入，以及怎样让后续开发持续维护文档。

## 适用范围

当用户要求初始化项目文档、补齐文档体系、接手缺少上下文的项目，或项目第一次进入实质开发时使用。用户已经授权初始化时，直接执行，不把规模评估变成新的确认关卡；无法推断的信息用“待确认”标记，不编造事实。

## 初始化顺序

1. 读取现有 `README*`、`AGENTS.md`/`AGENT.md`、`TODO*`、`CHANGELOG*`、`.env.example` 和 `docs/`，保留已有路径与命名。
2. 从项目清单、配置和目录事实判断技术栈、入口、测试、环境变量与模块规模；不凭空写启动命令。
3. 按下方档位选择文档树。只创建有实际内容的文件，不创建只有标题的空文档。
4. 先读取目标文档再补写。已有文档做局部增补；已授权的整体重组按指令执行，无关的改名、合并、删除或大幅重排保持原样。
5. 从 [维护流程](./maintenance.md) 复制内容到项目的 `docs/doc-maintenance.md`，把触发表的文档路径映射到已有主文档；例如已有根目录 CONTEXT.md 就沿用它。已有等价流程就地补齐，保持唯一入口。
6. 维护文件存在后，再用 [维护小节模板](../assets/AGENTS-doc-maintenance.template.md) 增补根 AGENTS.md，适配项目路径且不覆盖既有内容。缺少 AGENTS.md 时新建精简入口；已有 AGENT.md、CLAUDE.md 等文件保留并必要时引用，不因此搬迁。
7. 按 [链接与导航规则](./maintenance.md#链接与导航) 将真实文件引用、索引、目录导航和触发表改为 Markdown 链接；目录层级用可点击的缩进列表。下方规模树仅是结构示例，不作为生成文档的唯一导航。检查路径、锚点、命令是否真实有效；未创建文件明确标记，把无法安全运行的验证列为“未运行”。
8. 报告新建、沿用、跳过、待确认和验证结果，说明后续写入时机。

## 按规模选择文档树

规模只决定初始范围，不限制之后按事件惰性创建文档。

### 小型：原型、个人项目、单一模块

```text
README.md
AGENTS.md
TODO.md
CHANGELOG.md                 # 有用户可见版本变化时保留
.env.example                 # 有环境变量时保留
docs/
├── context.md               # 有业务规则或术语时保留
├── architecture.md          # 有多个模块时保留，否则并入 README
├── testing.md               # 有测试或验收步骤时保留
└── doc-maintenance.md
```

### 中型：多模块、持续迭代、需要交接

```text
README.md
AGENTS.md
TODO.md
CHANGELOG.md
.env.example
docs/
├── prd.md
├── context.md
├── architecture.md
├── data-model.md            # 存在持久化数据时
├── api.md                   # 对外或跨模块接口存在时
├── testing.md
├── setup.md
├── glossary.md
├── doc-maintenance.md
├── adr/
└── notes/
    ├── progress.md
    └── known-issues.md
```

### 长期：多人协作、生产部署、对外服务

```text
README.md
AGENTS.md
TODO.md
CHANGELOG.md
.env.example
CONTRIBUTING.md              # 有人类贡献流程时
LICENSE                      # 按已确定授权创建，不擅自选协议
docs/
├── prd.md
├── context.md
├── architecture.md
├── data-model.md
├── api.md
├── testing.md
├── setup.md
├── deployment.md          # 有部署流程时
├── glossary.md
├── security.md            # 有认证、权限或敏感数据时
├── operations.md          # 有监控、备份或值班要求时
├── doc-maintenance.md
├── adr/
└── notes/
```

`context.md` 用于业务规则和领域语义；它不是架构决策记录。`CONTRIBUTING.md`、`LICENSE`、`security.md`、`operations.md` 均按实际需要创建，不为凑结构留空文件。

## 初始化完成条件

- 根入口能链接到实际存在的主要文档。
- `AGENTS.md` 已包含每次代码修改后的巡检和冲突上报规则。
- `docs/doc-maintenance.md` 已明确初始化、任务开始、代码批次完成、验证完成、交付前的写入时机。
- 已有用户改动未被覆盖，工作树差异可解释。
- 未把代码违反规范的事实默默改写成新规范；此类冲突进入待裁决报告。

详细职责边界见 [doc-contracts.md](./doc-contracts.md)，持续维护和写入时机见 [maintenance.md](./maintenance.md)。
