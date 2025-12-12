---
aliases:
  - 试题生成器
date: 2025-09-01 10:35
tags:
source:
  - https://zread.ai/floatDreamWithSong/QuizAgent
view-count: 1
---
<iframe src="https://claude.site/public/artifacts/59af8000-57da-40a6-8429-bc3a4548d010/embed" title="Claude Artifact" width="100%" height="600" frameborder="0" allow="clipboard-write" allowfullscreen></iframe>


```tsx
import React, { useState } from 'react';
import { Network, Database, FileText, CheckCircle, AlertCircle, ArrowRight, Settings } from 'lucide-react';

const MultiAgentArchitecture = () => {
  const [selectedAgent, setSelectedAgent] = useState(null);
  const [selectedStage, setSelectedStage] = useState(null);

  const agents = [
    {
      id: 'parser',
      name: 'Document Parser Agent',
      role: '文档解析器',
      color: 'bg-blue-500',
      responsibilities: [
        '文档结构分析（章节、标题、段落）',
        '元数据提取（标题层级、引用关系）',
        '文本预处理（去噪、分句、分段）'
      ],
      rules: [
        '规则1: 识别 Markdown/HTML 标题层级（#, ##, <h1>）',
        '规则2: 提取段落边界和语义单元',
        '规则3: 构建文档树状结构（DocumentTree）'
      ],
      output: 'DocumentTree: {sections, paragraphs, metadata}'
    },
    {
      id: 'extractor',
      name: 'Knowledge Extractor Agent',
      role: '知识提取器',
      color: 'bg-green-500',
      responsibilities: [
        '识别知识单元（定义、概念、方法）',
        '提取关键实体和关系',
        '定位知识来源（section + context）'
      ],
      rules: [
        '规则1: 使用 NER 模式识别专业术语和概念',
        '规则2: 基于语义相似度聚合相关知识点',
        '规则3: 为每个知识点生成唯一 KID 和来源引用'
      ],
      output: 'KnowledgeUnits: [{kid, name, content, source, entities}]'
    },
    {
      id: 'organizer',
      name: 'Knowledge Organizer Agent',
      role: '知识组织器',
      color: 'bg-purple-500',
      responsibilities: [
        '构建知识层级关系（模块 → 子模块 → 知识点）',
        '计算知识点依赖关系',
        '评估知识点难度等级'
      ],
      rules: [
        '规则1: 基于共现频率和语义相似度聚类',
        '规则2: 构建有向无环图（DAG）表示依赖',
        '规则3: 根据抽象层次和术语密度评估难度'
      ],
      output: 'KnowledgeGraph: {modules, dependencies, difficultyMap}'
    },
    {
      id: 'generator',
      name: 'Question Generator Agent',
      role: '试题生成器',
      color: 'bg-orange-500',
      responsibilities: [
        '根据知识点生成候选试题',
        '控制题型分布（单选、简答、论述）',
        '生成参考答案和解析'
      ],
      rules: [
        '规则1: 根据难度等级选择题型模板',
        '规则2: 从知识点内容提取关键信息作为题干',
        '规则3: 生成干扰项时保证语义相关性但概念错误'
      ],
      output: 'QuestionCandidates: [{qid, type, stem, options, answer}]'
    },
    {
      id: 'reviewer',
      name: 'Quality Reviewer Agent',
      role: '质量评审器',
      color: 'bg-red-500',
      responsibilities: [
        '检查试题质量（歧义、错误、重复）',
        '验证答案正确性',
        '评估试题区分度'
      ],
      rules: [
        '规则1: 检测题干中的歧义词和不完整表达',
        '规则2: 验证答案与知识点来源一致性',
        '规则3: 计算选项之间的语义距离（避免过于相似）'
      ],
      output: 'ReviewReport: {passedQuestions, issues, suggestions}'
    },
    {
      id: 'coordinator',
      name: 'Workflow Coordinator',
      role: '流程协调器',
      color: 'bg-gray-700',
      responsibilities: [
        '管理 Agent 间的消息传递',
        '控制流程状态机',
        '处理异常和回退逻辑'
      ],
      rules: [
        '规则1: 按依赖关系调度 Agent 执行顺序',
        '规则2: 当某 Agent 失败时触发重试或降级策略',
        '规则3: 维护全局状态和中间结果缓存'
      ],
      output: 'WorkflowState: {currentStage, agentStatus, results}'
    }
  ];

  const stages = [
    {
      id: 'stage1',
      name: 'Stage 1: 文档解析',
      agents: ['parser'],
      input: 'Raw Document (Markdown/PDF/HTML)',
      output: 'DocumentTree',
      rules: [
        '使用正则表达式和 AST 解析文档结构',
        '提取标题层级映射（H1→模块，H2→子模块）',
        '保留原始文本和位置信息用于溯源'
      ]
    },
    {
      id: 'stage2',
      name: 'Stage 2: 知识提取',
      agents: ['extractor'],
      input: 'DocumentTree',
      output: 'KnowledgeUnits[]',
      rules: [
        '对每个段落应用知识模式匹配（定义、公式、方法）',
        '使用 TF-IDF 提取关键术语',
        '记录每个知识点的 section_id 和 paragraph_index'
      ]
    },
    {
      id: 'stage3',
      name: 'Stage 3: 知识组织',
      agents: ['organizer'],
      input: 'KnowledgeUnits[]',
      output: 'KnowledgeGraph',
      rules: [
        '使用层次聚类算法构建模块层级',
        '基于术语共现构建知识点依赖图',
        '计算每个知识点的 PageRank 作为重要性指标'
      ]
    },
    {
      id: 'stage4',
      name: 'Stage 4: 试题生成',
      agents: ['generator', 'reviewer'],
      input: 'KnowledgeGraph + UserRequirements',
      output: 'QualifiedQuestions[]',
      rules: [
        'Generator: 根据难度选择模板，每个知识点生成 2-3 个候选',
        'Reviewer: 批量检查，拒绝率 < 30% 则通过',
        '若拒绝率过高，触发 Generator 重新生成'
      ]
    },
    {
      id: 'stage5',
      name: 'Stage 5: 质量保证',
      agents: ['reviewer', 'coordinator'],
      input: 'QuestionCandidates[]',
      output: 'FinalQuestions[] + QualityReport',
      rules: [
        'Reviewer: 执行语义检查、答案验证、重复检测',
        'Coordinator: 若通过率 < 80%，回退到 Stage 4',
        '最终输出包含置信度分数和改进建议'
      ]
    }
  ];

  return (
    <div className="w-full max-w-7xl mx-auto p-6 bg-gradient-to-br from-gray-50 to-gray-100 rounded-xl">
      <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
        <h1 className="text-3xl font-bold text-gray-800 mb-2 flex items-center gap-3">
          <Network className="w-8 h-8 text-blue-600" />
          QuizzAgent 多 Agent 架构设计
        </h1>
        <p className="text-gray-600">规则驱动 • 分阶段执行 • 结构化协作</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
            <Settings className="w-5 h-5" />
            Agent 定义
          </h2>
          <div className="space-y-3 max-h-96 overflow-y-auto">
            {agents.map(agent => (
              <div
                key={agent.id}
                onClick={() => setSelectedAgent(agent)}
                className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
                  selectedAgent?.id === agent.id
                    ? 'border-blue-500 bg-blue-50'
                    : 'border-gray-200 hover:border-gray-300'
                }`}
              >
                <div className="flex items-center gap-3 mb-2">
                  <div className={`w-3 h-3 rounded-full ${agent.color}`}></div>
                  <span className="font-semibold text-gray-800">{agent.role}</span>
                </div>
                <p className="text-sm text-gray-600">{agent.name}</p>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
            <ArrowRight className="w-5 h-5" />
            执行阶段
          </h2>
          <div className="space-y-3 max-h-96 overflow-y-auto">
            {stages.map((stage, idx) => (
              <div
                key={stage.id}
                onClick={() => setSelectedStage(stage)}
                className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
                  selectedStage?.id === stage.id
                    ? 'border-green-500 bg-green-50'
                    : 'border-gray-200 hover:border-gray-300'
                }`}
              >
                <div className="flex items-center gap-3 mb-2">
                  <span className="font-bold text-lg text-blue-600">{idx + 1}</span>
                  <span className="font-semibold text-gray-800">{stage.name}</span>
                </div>
                <div className="text-sm text-gray-600">
                  <span className="font-medium">参与 Agent:</span> {stage.agents.join(', ')}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {selectedAgent && (
        <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
          <div className="flex items-center gap-3 mb-4">
            <div className={`w-4 h-4 rounded-full ${selectedAgent.color}`}></div>
            <h3 className="text-2xl font-bold text-gray-800">{selectedAgent.name}</h3>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h4 className="font-semibold text-gray-700 mb-2 flex items-center gap-2">
                <CheckCircle className="w-4 h-4" />
                职责范围
              </h4>
              <ul className="space-y-1 text-sm text-gray-600">
                {selectedAgent.responsibilities.map((resp, idx) => (
                  <li key={idx} className="flex items-start gap-2">
                    <span className="text-blue-500 mt-1">•</span>
                    <span>{resp}</span>
                  </li>
                ))}
              </ul>
            </div>
            
            <div>
              <h4 className="font-semibold text-gray-700 mb-2 flex items-center gap-2">
                <AlertCircle className="w-4 h-4" />
                执行规则
              </h4>
              <ul className="space-y-1 text-sm text-gray-600">
                {selectedAgent.rules.map((rule, idx) => (
                  <li key={idx} className="flex items-start gap-2">
                    <span className="text-green-500 mt-1">→</span>
                    <span>{rule}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
          
          <div className="mt-4 p-3 bg-gray-50 rounded border border-gray-200">
            <h4 className="font-semibold text-gray-700 mb-1 flex items-center gap-2">
              <Database className="w-4 h-4" />
              输出数据结构
            </h4>
            <code className="text-sm text-gray-700">{selectedAgent.output}</code>
          </div>
        </div>
      )}

      {selectedStage && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h3 className="text-2xl font-bold text-gray-800 mb-4">{selectedStage.name}</h3>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
            <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
              <h4 className="font-semibold text-blue-800 mb-2">输入</h4>
              <p className="text-sm text-blue-700">{selectedStage.input}</p>
            </div>
            
            <div className="p-4 bg-green-50 rounded-lg border border-green-200">
              <h4 className="font-semibold text-green-800 mb-2">输出</h4>
              <p className="text-sm text-green-700">{selectedStage.output}</p>
            </div>
            
            <div className="p-4 bg-purple-50 rounded-lg border border-purple-200">
              <h4 className="font-semibold text-purple-800 mb-2">参与 Agent</h4>
              <p className="text-sm text-purple-700">{selectedStage.agents.join(', ')}</p>
            </div>
          </div>
          
          <div>
            <h4 className="font-semibold text-gray-700 mb-3 flex items-center gap-2">
              <FileText className="w-4 h-4" />
              阶段执行规则
            </h4>
            <ul className="space-y-2">
              {selectedStage.rules.map((rule, idx) => (
                <li key={idx} className="flex items-start gap-3 p-3 bg-gray-50 rounded border border-gray-200">
                  <span className="font-bold text-blue-600 min-w-[24px]">{idx + 1}</span>
                  <span className="text-sm text-gray-700">{rule}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}

      <div className="mt-6 bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg p-6 border border-blue-200">
        <h3 className="text-lg font-bold text-gray-800 mb-3">🎯 核心设计原则</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
          <div>
            <h4 className="font-semibold text-blue-700 mb-2">规则驱动</h4>
            <p className="text-gray-600">每个 Agent 的行为由显式规则定义，而非依赖 Prompt 暗示</p>
          </div>
          <div>
            <h4 className="font-semibold text-purple-700 mb-2">结构化交互</h4>
            <p className="text-gray-600">Agent 间通过定义明确的数据结构（JSON Schema）通信</p>
          </div>
          <div>
            <h4 className="font-semibold text-green-700 mb-2">可观测性</h4>
            <p className="text-gray-600">每个阶段输出可序列化、可审查、可回溯</p>
          </div>
          <div>
            <h4 className="font-semibold text-orange-700 mb-2">容错机制</h4>
            <p className="text-gray-600">Coordinator 管理重试、降级和异常处理逻辑</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MultiAgentArchitecture;
```

基于您提供的 QuizzAgent 系统研读笔记，我为您提取了核心术语并进行了情景化解读。

---
### 🎯 笔记核心意图
这是一份关于 **QuizzAgent 自动化测验生成系统** 的 **技术架构拆解笔记**，重点阐述了如何通过“分治”策略将非结构化文档转化为高质量试题。

### 🔑 关键术语与情景扩充
| 关键术语 (Key Term) | 情景扩充 (Contextual Expansion) |
| :--- | :--- |
| **分治原则 (Divide & Conquer)** | 系统的底层重构逻辑，即将任务解耦为“知识提炼”与“试题生成”两个独立串行的模块。 |
| **Knowledge Planner** | 系统的第一阶段模块，扮演“智能文档解析师”，负责提取层级分明且带来源标注的结构化知识。 |
| **Question Builder** | 系统的第二阶段模块，作为“试题设计专家”，依据上游提取的知识点动态构建符合规范的试题。 |
| **Prompt (提示词)** | 驱动各模块的核心指令（如定义 Role 为架构师/专家），通过设定约束确保 AI 输出的精确性。 |

### 💡 极速理解摘要
该笔记揭示了 **QuizzAgent** 系统基于 **分治原则** 的核心工作流：首先利用 **Knowledge Planner** 配合特定的 **Prompt** 将原始文档清洗为结构化的知识清单；随后将这些标准化数据输入 **Question Builder**，再次通过动态构建的 **Prompt** 生成定制化试题，从而实现从“文档解析”到“测验生成”的全自动化闭环。

---

### 动态prompt

“动态构建的 Prompt” 在 **QuizzAgent** 系统中，指的是 **Question Builder 模块根据 Knowledge Planner 输出的结构化知识清单内容，实时生成与之匹配、语义一致、难度/题型适配的提示词（Prompt）**，而非使用固定模板。

---

### 一、什么是“动态构建”？

它包含以下关键特征：

1. **内容感知（Content-aware）**  
    Prompt 不是写死的，而是根据输入的知识点自动调整。例如：
    
    - 若知识点是“牛顿第一定律”，Prompt 会围绕“惯性”“力与运动状态”等关键词构造；
    - 若知识点是“Python 的 lambda 表达式”，Prompt 会聚焦于匿名函数、语法格式、应用场景等。
2. **题型/难度可配置（Configurable）**  
    根据用户需求（如“生成单选题”或“生成简答题”），系统会注入不同的指令到 Prompt 中：
    
    ```plaintext
    你是一个教育专家，请基于以下知识点生成一道【单选题】，包含4个选项，其中仅一个正确。
    知识点：{extracted_knowledge}
    ```
    
3. **上下文嵌入（Context Injection）**  
    将结构化知识（如定义、示例、应用场景、常见误区）作为上下文注入 Prompt，引导模型生成更精准、有区分度的题目。
    
4. **避免模板僵化（Avoiding Rote Templates）**  
    固定 Prompt 容易导致题目雷同、缺乏变化；动态构建可引入多样性控制（如温度参数、few-shot 示例轮换），提升试题质量。
    

---

### 二、现实实例说明

#### 📌 场景：从一份《机器学习基础》讲义自动生成测验

**步骤1：Knowledge Planner 输出结构化知识**

```json
{
  "concept": "过拟合（Overfitting）",
  "definition": "模型在训练集上表现很好，但在测试集上泛化能力差的现象。",
  "causes": ["模型过于复杂", "训练数据太少", "噪声过多"],
  "solutions": ["正则化", "增加数据", "早停法", "简化模型"],
  "example": "用高阶多项式拟合少量带噪声的数据点，曲线剧烈震荡。"
}
```

**步骤2：Question Builder 动态构建 Prompt**

> 用户请求：生成一道**多选题**，考察对“过拟合解决方案”的理解。

系统自动生成如下 Prompt：

```plaintext
你是一位机器学习课程助教。请根据以下知识点生成一道高质量的多选题（至少两个正确选项）：
- 考察重点：过拟合的解决方案
- 知识背景：
    过拟合指模型在训练集上表现优异但测试集上泛化差。
    常见原因包括模型复杂度过高、数据量不足等。
    有效解决方案包括：正则化（如L1/L2）、增加训练数据、使用早停法（early stopping）、简化模型结构。
    注意：交叉验证主要用于评估模型性能，不是直接的过拟合解决方案。

请输出格式：
题目：……
A. ……
B. ……
C. ……
D. ……
正确答案：……

确保干扰项具有迷惑性但明显错误。
```

**结果（LLM 输出）：**

```
题目：以下哪些方法可以有效缓解机器学习中的过拟合问题？
A. 增加训练数据量
B. 使用L2正则化
C. 采用更高阶的特征多项式
D. 在验证集性能不再提升时提前停止训练
正确答案：A、B、D
```

✅ 干扰项 C（更高阶多项式）正是过拟合的**诱因**，具有教学意义。

---

### 三、为什么“动态”很重要？

|方式|固定 Prompt|动态构建 Prompt|
|---|---|---|
|适应性|差（所有知识点用同一套话术）|强（贴合具体概念）|
|题目质量|易重复、泛化弱|多样、精准、有区分度|
|教学价值|低|高（可针对误区设计干扰项）|
|扩展性|难以支持多题型/多学科|可通过规则+元数据灵活扩展|

---

### 总结

> **“动态构建的 Prompt” = 基于结构化知识内容 + 用户需求（题型/难度） + 教学策略（如干扰项设计），实时合成高度定制化的 LLM 指令。**

这正是 QuizzAgent 实现“从文档到高质量测验”自动化闭环的关键技术环节，体现了 **分治思想** 中“将复杂任务（出题）分解为可编程子模块（规划 + 动态提示生成）”的工程智慧。