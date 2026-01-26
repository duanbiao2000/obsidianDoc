# 智能标签推荐规则库

> 基于文件位置、内容特征、关键词的自动化标签推荐系统
> 创建时间: 2026-01-26
> 相关: 知识库优化线路图 P2-1

---

## 📋 规则体系

### 规则优先级

| 优先级 | 规则类型 | 说明 |
|--------|----------|------|
| **P0** | 目录映射 | 基于文件所在目录自动推荐 Domain 标签 |
| **P1** | 关键词匹配 | 基于笔记内容关键词推荐 Topic 标签 |
| **P2** | 文件类型推断 | 基于文件名和结构推荐 Type 标签 |
| **P3** | 状态推断 | 基于笔记特征推荐 Status 标签 |

---

## 🗂️ P0: 目录映射规则（Domain 标签）

### 规则定义

基于文件所在目录的父级映射到对应的 Domain 标签。

| 目录 | Domain 标签 | 说明 |
|------|------------|------|
| `0.DailyNotes/` | - | 日记通常不添加 Domain 标签 |
| `1.Projects/AI知识IP打造/` | #Domain/AI/KnowledgeIP | AI 知识 IP 项目 |
| `1.Projects/技术能力晋升/` | #Domain/Tech/CareerDev | 技术职业发展 |
| `1.Projects/其他项目/` | - | 按具体项目添加自定义 Domain |
| `2.Topics/00.协议与规范/` | #Domain/Tech/Protocols | 技术协议与规范 |
| `2.Topics/01.技术栈/` | #Domain/Tech/Stack | 技术栈 |
| `2.Topics/02.认知系统/` | #Domain/Cognitive/System | 认知系统 |
| `2.Topics/03.内容创作/` | #Domain/ContentCreation | 内容创作 |
| `2.Topics/04.职业发展/` | #Domain/CareerDev | 职业发展 |
| `2.Topics/05.生活与健康/` | #Domain/LifeAndHealth | 生活与健康 |
| `2.Topics/06.语言与移民/` | #Domain/LanguageAndMigration | 语言与移民 |
| `3.Resources/` | - | 资源通常不添加 Domain 标签 |
| `4.Archives/` | - | 归档通常不添加 Domain 标签 |
| `5.Misc/` | - | 杂项通常不添加 Domain 标签 |
| `6.Calendar/` | - | 日历通常不添加 Domain 标签 |
| `Atlas/` | - | 系统文档，按内容添加 Domain |

**实现逻辑**:
```javascript
// 获取文件所在目录
const filePath = tp.file.path(true);
const dirPath = filePath.split('/').slice(0, -1).join('/');
const dirName = dirPath.split('/').pop();

// 根据目录映射到 Domain
const domainMap = {
  '1.Projects': {
    'AI知识IP打造': '#Domain/AI/KnowledgeIP',
    '技术能力晋升': '#Domain/Tech/CareerDev'
  },
  '2.Topics': {
    '00.协议与规范': '#Domain/Tech/Protocols',
    '01.技术栈': '#Domain/Tech/Stack',
    '02.认知系统': '#Domain/Cognitive/System',
    '03.内容创作': '#Domain/ContentCreation',
    '04.职业发展': '#Domain/CareerDev',
    '05.生活与健康': '#Domain/LifeAndHealth',
    '06.语言与移民': '#Domain/LanguageAndMigration'
  }
};

// 提取 Domain 标签
const domainTag = extractDomainTag(dirPath);
```

---

## 🔍 P1: 关键词匹配规则（Topic 标签）

### 规则定义

基于笔记标题、内容中的关键词推荐 Topic 标签。

| 关键词分类 | 关键词 | Topic 标签 | 说明 |
|------------|--------|-----------|------|
| **技术-前端** | React, Vue, Angular, TypeScript, CSS, HTML, UI, UX, 前端, 组件 | #Topic/Frontend | 前端技术 |
| **技术-后端** | Node.js, Express, Python, Java, Spring, Go, API, 后端, 服务, 数据库 | #Topic/Backend | 后端技术 |
| **技术-DevOps** | Docker, CI/CD, Git, 部署, 自动化, AWS, 云, 运维 | #Topic/DevOps | DevOps |
| **技术-AI** | AI, GPT, LLM, 提示词, 机器学习, 深度学习, 神经网络, 模型 | #Topic/AI/ML | AI 与机器学习 |
| **产品-设计** | 设计, UI, UX, 产品, 用户, 体验, 交互, Figma | #Topic/ProductDesign | 产品设计 |
| **写作-学术** | 论文, 学术, 研究, 文献, 引用, 数据, 实验, 发表 | #Topic/AcademicWriting | 学术写作 |
| **写作-创意** | 故事, 小说, 创意, 文案, 剧本, 写作, 创作 | #Topic/CreativeWriting | 创意写作 |
| **职业-规划** | 职业, 职业, 规划, 目标, 成长, 发展, 转型, 求职 | #Topic/CareerPlanning | 职业规划 |
| **学习-方法** | 学习, 记忆, 笔记, 知识, 复习, 理解, 掌握, 方法 | #Topic/LearningMethod | 学习方法 |
| **效率-系统** | 效率, 系统, 方法, 时间, 管理, 工作流, 自动化, 工具 | #Topic/ProductivitySystem | 效率系统 |

**实现逻辑**:
```javascript
// 关键词到 Topic 标签映射
const keywordTopicMap = {
  '前端': '#Topic/Frontend',
  '后端': '#Topic/Backend',
  'DevOps': '#Topic/DevOps',
  'AI': '#Topic/AI/ML',
  '设计': '#Topic/ProductDesign',
  '学术': '#Topic/AcademicWriting',
  '创意': '#Topic/CreativeWriting',
  '职业': '#Topic/CareerPlanning',
  '学习': '#Topic/LearningMethod',
  '效率': '#Topic/ProductivitySystem'
};

// 搜索笔记内容中的关键词
const content = tp.file.content;
const matchedTopics = [];

for (const [keyword, topic] of Object.entries(keywordTopicMap)) {
  if (content.toLowerCase().includes(keyword.toLowerCase())) {
    matchedTopics.push(topic);
  }
}

// 去重并返回
return [...new Set(matchedTopics)];
```

---

## 📄 P2: 文件类型推断规则（Type 标签）

### 规则定义

基于文件名、结构、内容特征推断文件类型。

| 特征 | Type 标签 | 说明 |
|------|-----------|------|
| 文件名包含 `MOC`, `Index`, `TODO` | #Type/Index | 索引或清单 |
| 文件名以日期开头 `YYYY-MM-DD` | #Type/Journal | 日记 |
| 包含大纲、结构、框架关键词 | #Type/Structure | 结构性笔记 |
| 包含清单、列表、任务关键词 | #Type/Checklist | 清单 |
| 包含代码、程序、实现关键词 | #Type/Code | 代码相关 |
| 包含公式、定义、概念关键词 | #Type/Concept | 概念性笔记 |
| 包含模板、示例、样例关键词 | #Type/Example | 示例或模板 |
| 包含引用、文献、资源关键词 | #Type/Reference | 参考资料 |

**实现逻辑**:
```javascript
// 文件类型特征检测
const typePatterns = {
  '#Type/Index': ['MOC', 'Index', '索引'],
  '#Type/Journal': [/^\d{4}-\d{2}-\d{2}/],
  '#Type/Structure': ['大纲', '结构', '框架', '架构'],
  '#Type/Checklist': ['清单', '列表', '任务', '待办'],
  '#Type/Code': ['代码', '程序', '实现', 'function', 'class'],
  '#Type/Concept': ['公式', '定义', '概念', '原理', '定理'],
  '#Type/Example': ['模板', '示例', '样例', '范例'],
  '#Type/Reference': ['引用', '文献', '参考', '资料', 'source']
};

// 检测文件类型
const fileName = tp.file.basename;
let detectedTypes = [];

for (const [typeTag, patterns] of Object.entries(typePatterns)) {
  for (const pattern of patterns) {
    if (typeof pattern === 'string') {
      if (fileName.includes(pattern) || content.includes(pattern)) {
        detectedTypes.push(typeTag);
        break;
      }
    } else if (pattern.test(fileName)) {
      detectedTypes.push(typeTag);
      break;
    }
  }
}

return detectedTypes;
```

---

## 🚦 P3: 状态推断规则（Status 标签）

### 规则定义

基于笔记特征推荐 Status 标签。

| 特征 | Status 标签 | 说明 |
|------|-------------|------|
| 包含 TODO, 待办, 未完成 | #Status/TODO | 待办事项 |
| 包含 进行中, 处理, 实施中 | #Status/InProgress | 进行中 |
| 包含 优化, 改进, 重构 | #Status/Review | 需要审查 |
| 包含 完成, 已完成, Done | #Status/Done | 已完成 |
| 包含 归档, 存档, Archive | #Status/Archive | 已归档 |
| 包含 废弃, 过时, 废弃 | #Status/Obsolete | 已废弃 |

**实现逻辑**:
```javascript
// 状态关键词检测
const statusKeywords = {
  '#Status/TODO': ['TODO', '待办', '未完成', '待处理', '待实现'],
  '#Status/InProgress': ['进行中', '处理', '实施中', 'working on'],
  '#Status/Review': ['优化', '改进', '重构', 'review', '审查'],
  '#Status/Done': ['完成', '已完成', 'Done', 'finished', '完成'],
  '#Status/Archive': ['归档', '存档', 'Archive', '归档'],
  '#Status/Obsolete': ['废弃', '过时', '废弃', 'obsolete', '过时']
};

// 检测状态
const content = tp.file.content.toLowerCase();
let detectedStatus = [];

for (const [statusTag, keywords] of Object.entries(statusKeywords)) {
  for (const keyword of keywords) {
    if (content.includes(keyword.toLowerCase())) {
      detectedStatus.push(statusTag);
      break;
    }
  }
}

return detectedStatus;
```

---

## 🎯 推荐策略

### 综合推荐流程

1. **P0: 目录映射** - 总是应用
   - 基于文件所在目录自动添加对应的 Domain 标签
   - 对于 `0.DailyNotes/`, `3.Resources/`, `4.Archives/` 不添加 Domain 标签

2. **P1: 关键词匹配** - 在 P0 之后应用
   - 搜索笔记内容中的关键词
   - 匹配成功则添加对应的 Topic 标签
   - 限制最多添加 3 个 Topic 标签

3. **P2: 文件类型推断** - 在 P1 之后应用
   - 基于文件名和结构特征推断 Type 标签
   - 检测到的类型标签全部添加

4. **P3: 状态推断** - 在 P2 之后应用
   - 搜索笔记内容中的状态关键词
   - 匹配成功则添加对应的 Status 标签
   - 限制只能添加 1 个 Status 标签

### 标签去重

在合并推荐标签时，确保不重复：
```javascript
// 合并所有推荐标签
const allRecommendedTags = [
  ...domainTags,      // P0
  ...topicTags,      // P1 (最多 3 个)
  ...typeTags,       // P2 (全部)
  ...statusTags      // P3 (最多 1 个)
];

// 去重并保持顺序
const uniqueTags = [...new Set(allRecommendedTags)];
```

---

## 📊 质量评分机制

### 评分维度

| 维度 | 评分标准 | 分值 |
|------|----------|------|
| **覆盖率** | Domain 标签覆盖率（非 DailyNotes/Resources/Archives） | 20 |
| **准确性** | Topic 标签与内容的匹配度 | 30 |
| **完整性** | Type 和 Status 标签的覆盖率 | 20 |
| **规范性** | 标签格式符合三层规范 | 15 |
| **一致性** | 同类文件标签使用的一致性 | 15 |

**总分**: 100 分

### 评分标准

| 分数范围 | 等级 | 说明 |
|---------|------|------|
| 90-100 | S (优秀) | 标签推荐准确，覆盖全面 |
| 80-89 | A (良好) | 标签推荐基本准确，覆盖较好 |
| 70-79 | B (合格) | 标签推荐可用，部分遗漏 |
| 60-69 | C (需改进) | 标签推荐不准确，覆盖不足 |
| 0-59 | D (不合格) | 标签推荐失败，需要人工干预 |

---

## 🔧 集成方式

### Templater 自动化

在笔记创建时自动应用标签推荐，详见 `tag_recommender.md`。

### 手动触发

通过命令面板运行：
```bash
/tag-recommender
```

或使用 Dataview 查询需要添加标签的文件：
```dataview
TABLE file.link
FROM ""
WHERE length(tags) < 2
```

---

## 📝 维护指南

### 添加新规则

1. 确定规则类型（P0/P1/P2/P3）
2. 在对应章节添加新的映射或关键词
3. 更新关键词列表
4. 更新评分机制
5. 测试新规则的有效性

### 优化规则

1. 定期分析推荐准确率
2. 根据用户反馈调整关键词列表
3. 优化目录映射表
4. 更新评分权重

---

## 🔗 相关资源

- [仓库标签管理系统](../../Atlas/Index/仓库标签管理系统.md) - 完整标签规范
- [标签推荐实现脚本](../Template/Templater/tag_recommender.md) - 自动化实现
- [质量评估执行日志](../../4.Archives/知识库优化项目/) - 历史评估记录

---

**维护者**: Claude Sonnet 4.5
**最后更新**: 2026-01-26
**下次审查**: 2026-02-09
