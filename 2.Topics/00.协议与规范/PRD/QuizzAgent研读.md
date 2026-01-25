---
aliases:
- 试题生成器
date: 2025-09-01 10:35
rating: 2.5
source:
- https://zread.ai/floatDreamWithSong/QuizAgent
tags:
- quiz-automation
- knowledge-unit-extraction
- agent-architecture
- algorithm
- Domain/AI
- Domain/AI/Agent
- Type/Reference
view-count: 5
---
# [[QuizAgent_Architecture]] - 自动化测验生成协议

---

## 1. Agent 协作矩阵 `agent-matrix`

| 角色 | 核心职责 (Action) | 输出物 |
| :--- | :--- | :--- |
| **Parser** | 文档结构分析 + 元数据提取 | `DocumentTree` |
| **Extractor** | 识别知识单元 + 建立 KID | `KnowledgeUnits[]` |
| **Organizer** | 构建 DAG 依赖 + 难度评估 | `KnowledgeGraph` |
| **Generator** | 模板驱动出题 + 干扰项设计 | `QuestionCandidates[]` |
| **Reviewer** | 歧义检测 + 来源一致性验证 | `ReviewReport` |
| **Coordinator** | 状态机控制 + 异常回退逻辑 | `WorkflowState` |

---

## 2. 五阶段执行流 `execution-pipeline`

### S1: 文档解析 (Parsing)
- **操作**: 使用 AST/正则解析 Markdown/PDF。
- **规则**: 映射 H1/H2 为模块层级，保留原始位置用于溯源。

### S2: 知识提取 (Extraction)
- **操作**: 段落模式匹配（定义/公式/方法）+ TF-IDF 提词。
- **规则**: 为每个知识点生成 KID，强制记录 `section_id`。

### S3: 知识组织 (Organizing)
- **操作**: 层次聚类构建层级，术语共现构建依赖图。
- **规则**: 计算 `PageRank` 作为权重，根据术语密度定级难度。

### S4: 试题生成 (Generation)
- **操作**: 动态合成 Prompt (内容 + 难度 + 题型模板)。
- **规则**: 干扰项必须语义相关但逻辑错误。

### S5: 质量保证 (QA)
- **操作**: 语义检查 + 答案验证 + 重复度过滤。
- **规则**: 通过率 < 80% 触发 `Coordinator` 强制回退至 S4 重新生成。

---

## 3. 动态提示词协议 `dynamic-prompt`

- **公式**: `Prompt = 结构化内容 + 用户约束 (难度/题型) + 教学策略 (干扰项逻辑)`
- **价值矩阵**:
    - **固定 Prompt**: 泛化弱、易重复、教学价值低。
    - **动态 Prompt**: 贴合概念、精准、高区分度、支持元数据扩展。

---

## 4. 核心设计原则 `core-principles`

- **规则驱动**: 显式规则定义行为，拒绝模糊暗示。
- **结构化交互**: Agent 间强制 JSON Schema 通信。
- **可观测性**: 阶段性输出必须可序列化、可回溯。
- **容错机制**: Coordinator 集中管理重试、降级与回滚。

---

## 5. 执行检查清单 (Checklist)

- [ ] **溯源**: 每道题是否关联了原始 `section_id`？
- [ ] **拓扑**: 知识点依赖是否形成了合法的 DAG？
- [ ] **区分度**: 选项间的语义距离是否经过计算（避免过近）？
- [ ] **闭环**: 拒绝率过高时是否能自动触发重新生成？

---

**最后更新: 2026-01-01**