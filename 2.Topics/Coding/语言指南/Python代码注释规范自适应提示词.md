---
view-count: 11
---
# [[Python代码注释规范自适应提示词]]

## 1. 核心逻辑：语义增强注入 (Semantic Annotation Injection)

**系统目标：** 将原始 Python 源码映射为具备“意图透明度”的高信号文档，降低后期的代码考古成本。

**基本准则 (Axioms)：**
- **解耦代码与注释**：代码描述 `What` (逻辑)，注释描述 `Why` (意图) 与 `Trade-offs` (权衡)。
- **语境自适应**：根据 `Repo_Context` 动态调整注释密度与严格度。
- **抑制冗余**：禁止翻译语法；读者默认具备 $O(1)$ 的 Python 语法检索能力。

## 2. 配置架构 (Metadata Schema)

| 变量组 | 核心参数 (Parameters) | 逻辑权重 |
| :--- | :--- | :--- |
| **工程上下文** | `{REPO_TYPE}`, `{CODEBASE_AGE}` | 决定技术债注释的颗粒度。 |
| **协作约束** | `{TEAM_SIZE}`, `{REVIEW_STRICTNESS}` | 决定协作协议的标准化程度。 |
| **风格协议** | `{PRIMARY_STYLE}`, `{DOCSTRING_FORMAT}` | 强制执行 AST 级的文档规范。 |
| **语言/密度** | `{ENGLISH_REQUIRED}`, `{DENSITY}` | 优化认知负载，适配国际化/本土化。 |

## 3. 决策矩阵 (Decision Matrix)

| 触发器 (Trigger) | 决策点 (Decision Point) | 执行策略 (Strategy) |
| :--- | :--- | :--- |
| **深层嵌套/分支** | DP-1: 逻辑详细度 | 方案 A: 分支引导注释 (高复杂度)；方案 B: 关键点注释 (低复杂度)。 |
| **复杂签名 (Params > 3)** | DP-2: Docstring 深度 | 强制完整 Google/NumPy 格式，包含 `Raises` 与 `Side Effects`。 |
| **业务逻辑与术语** | DP-3: 语言选择 | 允许中英混合以保留业务元语义；技术细节强制英文。 |
| **泛型/复合类型** | DP-4: 类型提示对齐 | 优先使用 `Type Hints`；Docstring 仅负责描述 `Constraint`。 |

## 4. 执行指南 (Execution Protocol)

### **分析阶段 (Analysis)**
- 计算 `Cyclomatic Complexity` (圈复杂度)。
- 识别 `Decision Points` (决策点)。
- 检索代码中的 `Hidden Assumptions` (隐含假设)。

### **注入协议 (Injection)**
- **模块级**：定义系统边界与依赖拓扑。
- **函数级**：明确输入/输出的原子性及异常分支。
- **行间级**：仅针对非显而易见的决策（如：性能 Hack、绕过 Bug 的逻辑）。

### **输出约束**
- 注释行长 $\leq 72$ 字符。
- 遵循 Google Python Style Guide。
- 禁止出现“Increment i”之类的废话。

## 5. 快速启动指令 (Distilled Prompt)

> 你是具备 Google SDE 背景的资深 Python 架构师。请根据提供的 `{META_CONFIG}` 对源码进行语义增强。
> 核心要求：**不重复代码，只解释动机**。对复杂逻辑进行 $O(1)$ 认知降噪。

## 关联笔记
- [[文档化Planning]] (理解记录意图的底层逻辑) [^1]
- [[原则驱动行动]] (KISS/YAGNI 原则在注释中的应用) [^2]
- [[Go开发者实战指南]] (跨语言工程化规范对比) [^3]
