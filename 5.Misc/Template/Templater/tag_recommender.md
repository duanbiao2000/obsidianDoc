<%*
/**
 * 智能标签推荐模板
 *
 * 功能：根据文件目录、内容特征、关键词自动推荐标签
 * 使用方法：在新建笔记时自动调用，或手动运行
 * 创建时间：2026-01-26
 * 相关：知识库优化线路图 P2-1 - 智能标签推荐系统
 */
-%>

<%*
// 导入推荐规则（从 tag_recommender_rules.md）
// 实际项目中，这些规则应该内联或从配置文件读取
-%>

<%*
// ========================================
// P0: 目录映射规则（Domain 标签）
// ========================================
-%>

<%*
// 获取文件所在目录
const filePath = tp.file.path(true);
const dirPath = filePath.split('/').slice(0, -1).join('/');
const dirSegments = dirPath.split('/');

// 确定主目录类型
let mainDirectory = '';
let subDirectory = '';

if (dirSegments.length >= 1) {
  mainDirectory = dirSegments[0];
  if (dirSegments.length >= 2) {
    subDirectory = dirSegments[1];
  }
}

// 目录到 Domain 标签映射
const domainMapping = {
  '1.Projects': {
    'AI知识IP打造': ['#Domain/AI/KnowledgeIP'],
    '技术能力晋升': ['#Domain/Tech/CareerDev']
  },
  '2.Topics': {
    '00.协议与规范': ['#Domain/Tech/Protocols'],
    '01.技术栈': ['#Domain/Tech/Stack'],
    '02.认知系统': ['#Domain/Cognitive/System'],
    '03.内容创作': ['#Domain/ContentCreation'],
    '04.职业发展': ['#Domain/CareerDev'],
    '05.生活与健康': ['#Domain/LifeAndHealth'],
    '06.语言与移民': ['#Domain/LanguageAndMigration']
  },
  'Atlas': {
    'BASE': ['#Domain/System/Base'],
    'Index': ['#Domain/System/Index'],
    'Docs': ['#Domain/System/Docs']
  }
};

// 跳过不需要 Domain 标签的目录
const noDomainDirectories = ['0.DailyNotes', '3.Resources', '4.Archives', '5.Misc', '6.Calendar'];

// 提取 Domain 标签
let domainTags = [];
if (!noDomainDirectories.includes(mainDirectory)) {
  if (domainMapping[mainDirectory] && domainMapping[mainDirectory][subDirectory]) {
    domainTags = domainMapping[mainDirectory][subDirectory];
  } else if (domainMapping[mainDirectory]) {
    const subDirKeys = Object.keys(domainMapping[mainDirectory]);
    const matchedKey = subDirKeys.find(key => dirPath.includes(key.split('/')[0]));
    if (matchedKey) {
      domainTags = domainMapping[mainDirectory][matchedKey];
    }
  } else if (domainMapping[mainDirectory]) {
    domainTags = Object.values(domainMapping[mainDirectory]).flat();
  }
}
-%>

<%*
// ========================================
// P1: 关键词匹配规则（Topic 标签）
// ========================================
-%>

<%*
// 获取笔记标题和内容
const noteTitle = tp.file.basename;
const noteContent = tp.file.content || '';

// 关键词到 Topic 标签映射
const keywordTopicMap = {
  '技术-前端': ['#Topic/Frontend'],
  '前端': ['#Topic/Frontend'],
  'React': ['#Topic/Frontend'],
  'Vue': ['#Topic/Frontend'],
  'Angular': ['#Topic/Frontend'],
  'TypeScript': ['#Topic/Frontend'],
  'CSS': ['#Topic/Frontend'],
  'HTML': ['#Topic/Frontend'],
  'UI': ['#Topic/Frontend'],
  'UX': ['#Topic/Frontend'],
  '组件': ['#Topic/Frontend'],
  '界面': ['#Topic/Frontend'],
  
  '技术-后端': ['#Topic/Backend'],
  '后端': ['#Topic/Backend'],
  'Node.js': ['#Topic/Backend'],
  'Express': ['#Topic/Backend'],
  'Python': ['#Topic/Backend'],
  'Java': ['#Topic/Backend'],
  'Spring': ['#Topic/Backend'],
  'Go': ['#Topic/Backend'],
  'API': ['#Topic/Backend'],
  '数据库': ['#Topic/Backend'],
  '服务': ['#Topic/Backend'],
  
  '技术-DevOps': ['#Topic/DevOps'],
  'DevOps': ['#Topic/DevOps'],
  'Docker': ['#Topic/DevOps'],
  'CI/CD': ['#Topic/DevOps'],
  'Git': ['#Topic/DevOps'],
  '部署': ['#Topic/DevOps'],
  '自动化': ['#Topic/DevOps'],
  'AWS': ['#Topic/DevOps'],
  '云': ['#Topic/DevOps'],
  '运维': ['#Topic/DevOps'],
  
  '技术-AI': ['#Topic/AI/ML'],
  'AI': ['#Topic/AI/ML'],
  'GPT': ['#Topic/AI/ML'],
  'LLM': ['#Topic/AI/ML'],
  '大模型': ['#Topic/AI/ML'],
  '机器学习': ['#Topic/AI/ML'],
  '提示词': ['#Topic/AI/ML'],
  'Prompt': ['#Topic/AI/ML'],
  '提示词工程': ['#Topic/AI/ML'],
  '深度学习': ['#Topic/AI/ML'],
  '神经网络': ['#Topic/AI/ML'],
  '模型': ['#Topic/AI/ML'],
  
  '产品-设计': ['#Topic/ProductDesign'],
  '设计': ['#Topic/ProductDesign'],
  'UI': ['#Topic/ProductDesign'],
  'UX': ['#Topic/ProductDesign'],
  '用户体验': ['#Topic/ProductDesign'],
  '产品': ['#Topic/ProductDesign'],
  '用户': ['#Topic/ProductDesign'],
  '体验': ['#Topic/ProductDesign'],
  '交互': ['#Topic/ProductDesign'],
  'Figma': ['#Topic/ProductDesign'],
  '界面': ['#Topic/ProductDesign'],
  
  '写作-学术': ['#Topic/AcademicWriting'],
  '论文': ['#Topic/AcademicWriting'],
  '学术': ['#Topic/AcademicWriting'],
  '研究': ['#Topic/AcademicWriting'],
  '文献': ['#Topic/AcademicWriting'],
  '引用': ['#Topic/AcademicWriting'],
  '数据': ['#Topic/AcademicWriting'],
  '实验': ['#Topic/AcademicWriting'],
  '发表': ['#Topic/AcademicWriting'],
  
  '写作-创意': ['#Topic/CreativeWriting'],
  '故事': ['#Topic/CreativeWriting'],
  '小说': ['#Topic/CreativeWriting'],
  '创意': ['#Topic/CreativeWriting'],
  '文案': ['#Topic/CreativeWriting'],
  '剧本': ['#Topic/CreativeWriting'],
  '写作': ['#Topic/CreativeWriting'],
  '创作': ['#Topic/CreativeWriting'],
  
  '职业-规划': ['#Topic/CareerPlanning'],
  '职业': ['#Topic/CareerPlanning'],
  '规划': ['#Topic/CareerPlanning'],
  '目标': ['#Topic/CareerPlanning'],
  '成长': ['#Topic/CareerPlanning'],
  '发展': ['#Topic/CareerPlanning'],
  '转型': ['#Topic/CareerPlanning'],
  '跳槽': ['#Topic/CareerPlanning'],
  '求职': ['#Topic/CareerPlanning'],
  
  '学习-方法': ['#Topic/LearningMethod'],
  '学习': ['#Topic/LearningMethod'],
  '记忆': ['#Topic/LearningMethod'],
  '笔记': ['#Topic/LearningMethod'],
  '知识': ['#Topic/LearningMethod'],
  '复习': ['#Topic/LearningMethod'],
  '理解': ['#Topic/LearningMethod'],
  '掌握': ['#Topic/LearningMethod'],
  '方法': ['#Topic/LearningMethod'],
  
  '效率-系统': ['#Topic/ProductivitySystem'],
  '效率': ['#Topic/ProductivitySystem'],
  '系统': ['#Topic/ProductivitySystem'],
  '时间': ['#Topic/ProductivitySystem'],
  '管理': ['#Topic/ProductivitySystem'],
  '工具': ['#Topic/ProductivitySystem'],
  '自动化': ['#Topic/ProductivitySystem'],
  '工作流': ['#Topic/ProductivitySystem']
};

// 搜索笔记内容中的关键词（仅限前 3 个 Topic 标签）
const topicTags = [];
const topicCountLimit = 3;

const contentLower = noteContent.toLowerCase();
const titleLower = noteTitle.toLowerCase();

for (const [keywords, tags] of Object.entries(keywordTopicMap)) {
  if (topicTags.length < topicCountLimit) {
    for (const keyword of keywords) {
      if (contentLower.includes(keyword.toLowerCase()) || titleLower.includes(keyword.toLowerCase())) {
        topicTags.push(...tags);
        break; // 每个分类只匹配一个关键词
      }
    }
  }
}
-%>

<%*
// ========================================
// P2: 文件类型推断规则（Type 标签）
// ========================================
-%>

<%*
// 文件类型特征检测
const typePatterns = {
  '#Type/Index': ['MOC', 'Index', '索引'],
  '#Type/Journal': [/^\d{4}-\d{2}-\d{2}/, /^\d{4}-\d{2}_/],
  '#Type/Structure': ['大纲', '结构', '框架', '架构', '思维导图', '概念图'],
  '#Type/Checklist': ['清单', '列表', '任务', '待办', 'TODO'],
  '#Type/Code': ['代码', '程序', '实现', 'function', 'class', 'const', 'var', 'interface'],
  '#Type/Concept': ['公式', '定义', '概念', '原理', '定理', '模型'],
  '#Type/Example': ['模板', '示例', '样例', '范例', 'demo'],
  '#Type/Reference': ['引用', '文献', '参考', '资料', 'source', '链接']
};

// 检测文件类型
const typeTags = [];

for (const [typeTag, patterns] of Object.entries(typePatterns)) {
  let matched = false;
  for (const pattern of patterns) {
    if (typeof pattern === 'string') {
      if (noteContent.includes(pattern) || noteTitle.includes(pattern)) {
        matched = true;
        break;
      }
    } else if (pattern instanceof RegExp && pattern.test(noteTitle)) {
      matched = true;
      break;
    }
  }
  if (matched) {
    typeTags.push(typeTag);
    break; // 每个分类只匹配一个类型
  }
}
-%>

<%*
// ========================================
// P3: 状态推断规则（Status 标签）
// ========================================
-%>

<%*
// 状态关键词检测（仅限 1 个 Status 标签）
const statusKeywords = {
  '#Status/TODO': ['TODO', '待办', '未完成', '待处理', '待实现'],
  '#Status/InProgress': ['进行中', '处理', '实施', 'working on', 'wip'],
  '#Status/Review': ['优化', '改进', '重构', 'review', '审查', '需要优化'],
  '#Status/Done': ['完成', '已完成', 'Done', 'finished', '解决'],
  '#Status/Archive': ['归档', '存档', 'Archive', '归档到']
};

// 检测状态（仅限 1 个 Status 标签）
const statusTags = [];
const statusCountLimit = 1;

const contentLower = noteContent.toLowerCase();

for (const [statusTag, keywords] of Object.entries(statusKeywords)) {
  if (statusTags.length < statusCountLimit) {
    for (const keyword of keywords) {
      if (contentLower.includes(keyword.toLowerCase())) {
        statusTags.push(statusTag);
        break;
      }
    }
  }
}
-%>

<%*
// ========================================
// 标签去重与合并
// ========================================
-%>

<%*
// 合并所有推荐的标签
const allRecommendedTags = [
  ...domainTags,        // P0: 目录映射（总是应用）
  ...topicTags,         // P1: 关键词匹配（最多 3 个）
  ...typeTags,          // P2: 文件类型推断（全部匹配）
  ...statusTags          // P3: 状态推断（最多 1 个）
];

// 去重并保持顺序
const uniqueTags = [];
const seenTags = new Set();

for (const tag of allRecommendedTags) {
  if (!seenTags.has(tag)) {
    seenTags.add(tag);
    uniqueTags.push(tag);
  }
}

// 格式化标签为 YAML 数组格式
const tagsArray = uniqueTags;
-%>

<%*
// ========================================
// 用户选择界面（可选）
// ========================================
-%>

<%*
// 显示推荐结果
tR += `\`\`\```
tR += `# 🔮 智能标签推荐\n\n`;
tR += `**笔记**: ${noteTitle}\n\n`;
tR += `**文件路径**: ${filePath}\n\n`;
tR += `---\n\n`;

// 按优先级分组显示
if (domainTags.length > 0) {
  tR += `## 📂 P0: 目录映射 → Domain 标签\n\n`;
  tR += `${domainTags.join('\n  - ')}\n\n`;
}

if (topicTags.length > 0) {
  tR += `## 🏷️ P1: 关键词匹配 → Topic 标签\n\n`;
  tR += `${topicTags.join('\n  - ')}\n\n`;
}

if (typeTags.length > 0) {
  tR += `## 📄 P2: 文件类型 → Type 标签\n\n`;
  tR += `${typeTags.join('\n  - ')}\n\n`;
}

if (statusTags.length > 0) {
  tR += `## 🚦 P3: 状态推断 → Status 标签\n\n`;
  tR += `${statusTags.join('\n  - ')}\n\n`;
}

// 显示最终标签数组
tR += `---\n\n`;
tR += `## 📋 最终推荐的标签\n\n`;
tR += `\`\`\`yaml\n`;
for (const tag of tagsArray) {
  tR += `  - ${tag}\n`;
}
tR += `\`\`\`\n\n`;

tR += `---\n\n`;
tR += `## 📊 推荐统计\n\n`;
tR += `- Domain 标签: ${domainTags.length}\n`;
tR += `- Topic 标签: ${topicTags.length} (限制 3 个)\n`;
tR += `- Type 标签: ${typeTags.length}\n`;
tR += `- Status 标签: ${statusTags.length} (限制 1 个)\n`;
tR += `- 总计: ${tagsArray.length}\n\n`;

tR += `---\n\n`;
tR += `## 🎯 应用方式\n\n`;
tR += `**自动应用**: 直接添加到笔记 YAML\n\n`;
tR += `\`\`\`yaml\n`;
tR += `---\n`;
tR += `tags:\n`;
for (const tag of tagsArray) {
  tR += `  - ${tag}\n`;
}
tR += `\`\`\`\n\n`;
tR += `**手动选择**: 删除不需要的标签\n\n`;
tR += `**编辑优化**: 查看 [tag_recommender_rules.md](./tag_recommender_rules.md) 了解规则\n\n`;
tR += `---\n\n`;
tR += `**配置文件**: [tag_recommender_rules.md](./tag_recommender_rules.md) - 规则库\n`;
tR += `**规则说明**: [tag_recommender.md](./tag_recommender_rules.md) - 完整规则体系\n`;
-%>

<%*
// ========================================
// 输出格式化的标签（用于复制粘贴）
// ========================================
-%>

<%*
tR += `\`\`\`text\n`;
tR += `--- 推荐标签 ---\n`;
tR += `${tagsArray.join('\n')}\n`;
tR += `\`\`\`\n`;
-%>

<%*
// ========================================
// 注意事项
// ========================================
-%>

<%*
tR += `---\n\n`;
tR += `## 💡 使用技巧\n\n`;
tR += `1. **目录映射优先**: Domain 标签基于文件路径，最可靠\n`;
tR += `2. **Topic 限制**: 限制 3 个避免标签爆炸\n`;
tR += `3. **Status 限制**: 限制 1 个避免状态冲突\n`;
tR += `4. **Type 全面**: 所有匹配的类型标签都添加\n`;
tR += `5. **去重机制**: 自动去除重复标签\n\n`;
tR += `6. **手动调整**: 推荐后可根据实际需求修改\n\n`;

tR += `\`\`\`text\n`;
tR += `--- 快速操作 ---\n\n`;
tR += `复制上方 YAML 标签块，粘贴到笔记开头\n`;
tR += `使用 "Ctrl+Shift+V" 格式化 YAML\n`;
tR += `保存笔记，完成自动标签添加\n`;
-%>
