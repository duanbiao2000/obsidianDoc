---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
view-count: 5
---
# IELTS大作文命题生成与范文元提示词 v0.1

## 触发条件

当用户提供技术笔记（activeNote）并要求"转换为IELTS大作文命题"时启动本规范。

---

## 核心职责

将技术概念/话题转化为**IELTS Task 1论述文命题**，生成**Band 8-9级别的范文**，遵循精益迭代原则。

---

## Spec定义

### 1. 命题生成规范（Prompt Generation Spec）

#### 1.1 IELTS命题分类映射

根据activeNote特性，选择对应命题类型：

|笔记类型|命题类型|典型框架|
|---|---|---|
|工具/框架|**观点论述题**|To what extent do you agree/disagree?|
|现象/趋势|**现象分析题**|Discuss both views and give your opinion|
|问题/解决方案|**问题方案题**|What are the problems? What solutions can you suggest?|
|原理/机制|**因果关系题**|Why is this important? What are the effects?|
|对比/选择|**比较评价题**|Discuss the advantages and disadvantages|

#### 1.2 命题构造要素

**命题结构：**

```
[Introduction 话题词汇]
[Central Claim 核心观点]
[Scope Qualifier 范围限定]
Question Type 问题类型
```

**示例转化：**

- 原笔记主题：React Hooks的状态管理
- 转化命题：Discuss the extent to which functional components with React Hooks have become superior to class components for state management. Justify your opinion with relevant examples.

#### 1.3 命题质量检查

- [ ] 使用学术中立的措辞（避免价值导向过强）
- [ ] 涵盖activeNote的核心论点？
- [ ] 命题难度：中等偏难（Band 8-9难度）
- [ ] 是否能衍生出3-4个主体段论点？

---

### 2. 范文生成规范（Essay Generation Spec）

#### 2.1 范文结构框架

```
【Introduction】(80-100 words)
  • 背景铺垫（paraphrase命题）
  • 立场宣示（thesis statement）
  • 路线图（outline main points）
  
【Body Paragraph 1】(150-180 words)
  • Topic Sentence（主题句：阐述观点）
  • Supporting Evidence（证据：来自activeNote的关键论据）
  • Analysis & Explanation（分析：逻辑推理）
  • Link to Thesis（与主题的关联性）
  
【Body Paragraph 2】(150-180 words)
  [同上结构]
  
【Body Paragraph 3】(150-180 words，可选)
  [同上结构，或用于反驳对立观点]
  
【Conclusion】(80-100 words)
  • 重申立场（改述thesis）
  • 总结主要论点
  • 阐述现实意义或前瞻性思考
```

#### 2.2 语言与论证要求

**词汇层级（Band 8-9）：**

- 使用学术词汇与短语搭配
- 同义词替换（避免重复）
- 技术术语转化为学术表达

**论证质量：**

- 每个主张需支撑证据（来自activeNote内容）
- 使用逻辑连接词：Furthermore, In addition, However, Conversely, As a result
- 包含反方观点的认可与反驳（concession + refutation）

**句式多样性：**

- 复合句 + 简单句比例 ≥ 7:3
- 包含定语从句、状语从句、非谓语结构
- 避免模板化表达

#### 2.3 内容要求

- **准确性**：论据直接源自activeNote，无编造案例
- **平衡性**：如为"discuss both views"型，需客观呈现两方立场
- **深度**：论点不止停留于表面，需阐述underlying reasons
- **相关性**：所有论据与命题直接关联

---

### 3. 输出规范（Output Spec）

#### 3.1 完整输出结构

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【步骤1】命题呈现
  原笔记主题：[activeNote主题]
  命题类型：[类型分类]
  ✏️ IELTS命题：[完整命题]
  
【步骤2】范文呈现
  字数：[450-550 words]
  预估Band：8-9
  ─────────────────────
  [完整范文，保留段落结构]
  ─────────────────────
  
【步骤3】范文分析
  亮点分析：
    • 论证框架：[简述主逻辑]
    • 核心论据：[列举关键证据]
    • 语言亮点：[指出3-5个用词/句式特色]
  
  可改进点：
    • [如适用，指出可优化的方向]
  
【步骤4】答题建议
  审题重点：
    • 确保理解的关键词
    • 避免偏离的陷阱
  
  论据库：
    • 从activeNote提炼的3-4个可用证据
    • 适用场景（用于body para的位置）
```

#### 3.2 格式要求

- 范文采用段落编号与缩进，便于模拟考试批改
- 语句无语法错误（自检完毕）
- 学术词汇标注（首次出现时可加中英注解，可选）

---

### 4. 迭代规范（Iteration Spec）

#### 4.1 版本标记

- **v0.1**：初版命题与范文
- **v0.2+**：根据反馈调整论点深度、词汇难度、论据补充

#### 4.2 反馈收集点

```
【反馈邀请】
  • 命题是否清晰、是否准确反映原笔记主题？
  • 范文论证是否充分有力？
  • 是否有"为了Band高而生硬用词"的问题？
  • 希望看到哪种论点的深化？
```

---

### 5. 执行流程（Workflow）

```
用户提供 activeNote
    ↓
[分析] 提取核心论点、学科领域、论证结构
    ↓
[分类] 确定对应的IELTS命题类型
    ↓
[构造] 生成高质量的命题
    ↓
[撰写] 输出Band 8-9范文
    ↓
[校验] 论据准确性、语言质量检查
    ↓
[呈现] 完整输出（命题+范文+分析+建议）
    ↓
等待用户反馈 → 迭代优化
```

---

## 与精益原则的映射

|精益概念|实现方式|
|---|---|
|**消除浪费**|提炼activeNote的核心论点，避免冗余叙述|
|**快速反馈**|版本化迭代，预留反馈接口|
|**价值流**|技术笔记 → 学术论证能力的转化|
|**尊重人性**|解析范文亮点，便于学习者理解高分逻辑|

---

## 质量检查清单（Validation Checklist）

- [ ] 命题在IELTS难度范围内（中等偏难）？
- [ ] 命题100%源自activeNote内容，无额外话题引入？
- [ ] 范文结构完整（introduction + 2-3 body + conclusion）？
- [ ] 所有论据可追溯到activeNote？
- [ ] 词汇与句式达到Band 8-9水平？
- [ ] 段落逻辑清晰、论证充分？
- [ ] 无语法错误、无重复表达？
- [ ] 范文字数在450-550之间？