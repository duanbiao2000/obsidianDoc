<%*
/**
 * 智能标签推荐脚本
 *
 * 功能：根据文件目录、内容特征、关键词自动推荐标签
 * 使用方法：在新建笔记时自动调用，或手动命令触发
 * 创建时间：2026-01-26
 * 相关：知识库优化线路图 P2-1
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
// 获取文件所在目录的父级
const filePath = tp.file.path(true);
const dirPath = filePath.split('/').slice(0, -1).join('/');
const dirSegments = dirPath.split('/');

// 确定主目录类型
let mainDirectory = '';
if (dirSegments.length >= 1) {
  mainDirectory = dirSegments[0];  // 0.DailyNotes, 1.Projects, 2.Topics, etc.
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

// 提取 Domain 标签
const domainTags = [];

// 跳过不需要 Domain 标签的目录
const noDomainDirectories = ['0.DailyNotes', '3.Resources', '4.Archives', '5.Misc', '6.Calendar'];

if (!noDomainDirectories.includes(mainDirectory)) {
  // 检查第二级目录
  if (dirSegments.length >= 2) {
    const subDirectory = dirSegments[1];
    if (domainMapping[mainDirectory] && domainMapping[mainDirectory][subDirectory]) {
      domainTags.push(...domainMapping[mainDirectory][subDirectory]);
    }
  }
}
-%>

<%*
// ========================================
// P1: 关键词匹配规则（Topic 标签）
// ========================================
-%>

<%*
// 获取笔记内容
const noteContent = tp.file.content || '';
const noteTitle = tp.file.basename;

// 关键词到 Topic 标签映射
const keywordTopicMap = {
  '前端': ['#Topic/Frontend'],
  '后端': ['#Topic/Backend'],
  'DevOps': ['#Topic/DevOps'],
  'AI': ['#Topic/AI/ML'],
  'GPT': ['#Topic/AI/ML'],
  'LLM': ['#Topic/AI/ML'],
  '机器学习': ['#Topic/AI/ML'],
  '深度学习': ['#Topic/AI/ML'],
  '神经网络': ['#Topic/AI/ML'],
  '模型': ['#Topic/AI/ML'],
  '提示词': ['#Topic/AI/ML', '#Topic/PromptEngineering'],
  '设计': ['#Topic/ProductDesign'],
  'UI': ['#Topic/ProductDesign'],
  'UX': ['#Topic/ProductDesign'],
  '产品': ['#Topic/ProductDesign'],
  '用户': ['#Topic/ProductDesign'],
  '体验': ['#Topic/ProductDesign'],
  '交互': ['#Topic/ProductDesign'],
  'Figma': ['#Topic/ProductDesign'],
  '论文': ['#Topic/AcademicWriting'],
  '学术': ['#Topic/AcademicWriting'],
  '研究': ['#Topic/AcademicWriting'],
  '文献': ['#Topic/AcademicWriting'],
  '引用': ['#Topic/AcademicWriting'],
  '数据': ['#Topic/AcademicWriting'],
  '实验': ['#Topic/AcademicWriting'],
  '发表': ['#Topic/AcademicWriting'],
  '故事': ['#Topic/CreativeWriting'],
  '小说': ['#Topic/CreativeWriting'],
  '创意': ['#Topic/CreativeWriting'],
  '文案': ['#Topic/CreativeWriting'],
  '剧本': ['#Topic/CreativeWriting'],
  '写作': ['#Topic/CreativeWriting'],
  '创作': ['#Topic/CreativeWriting'],
  '职业': ['#Topic/CareerPlanning'],
  '规划': ['#Topic/CareerPlanning'],
  '目标': ['#Topic/CareerPlanning'],
  '成长': ['#Topic/CareerPlanning'],
  '发展': ['#Topic/CareerPlanning'],
  '转型': ['#Topic/CareerPlanning'],
  '跳槽': ['#Topic/CareerPlanning'],
  '求职': ['#Topic/CareerPlanning'],
  '学习': ['#Topic/LearningMethod'],
  '记忆': ['#Topic/LearningMethod'],
  '笔记': ['#Topic/LearningMethod'],
  '知识': ['#Topic/LearningMethod'],
  '复习': ['#Topic/LearningMethod'],
  '理解': ['#Topic/LearningMethod'],
  '掌握': ['#Topic/LearningMethod'],
  '方法': ['#Topic/LearningMethod'],
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

for (const [keyword, tags] of Object.entries(keywordTopicMap)) {
  if (topicTags.length < topicCountLimit) {
    if (contentLower.includes(keyword) || titleLower.includes(keyword)) {
      topicTags.push(...tags);
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
  '#Type/Journal': [/^\d{4}-\d{2}-/], [/^\d{4}-\d{2}_/],
  '#Type/Structure': ['大纲', '结构', '框架', '架构'],
  '#Type/Checklist': ['清单', '列表', '任务', '待办', 'TODO'],
  '#Type/Code': ['代码', '程序', '实现', 'function', 'class', 'const'],
  '#Type/Concept': ['公式', '定义', '概念', '原理', '定理', '定理'],
  '#Type/Example': ['模板', '示例', '样例', '范例'],
  '#Type/Reference': ['引用', '文献', '参考', '资料', 'source']
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
    break;
  }
}
-%>

<%*
// ========================================
// P3: 状态推断规则（Status 标签）
// ========================================
-%>

<%*
// 状态关键词检测
const statusKeywords = {
  '#Status/TODO': ['TODO', '待办', '未完成', '待处理', '待实现'],
  '#Status/InProgress': ['进行中', '处理', '实施', 'working on'],
  '#Status/Review': ['优化', '改进', '重构', 'review', '审查'],
  '#Status/Done': ['完成', '已完成', 'Done', 'finished', '完成'],
  '#Status/Archive': ['归档', '存档', 'Archive', '归档'],
  '#Status/Obsolete': ['废弃', '过时', 'obsolete', '过时']
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
  ...domainTags,        // P0: 目录映射
  ...topicTags,        // P1: 关键词匹配（最多 3 个）
  ...typeTags,         // P2: 文件类型推断（全部匹配）
  ...statusTags        // P3: 状态推断（最多 1 个）
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
// 输出推荐结果
// ========================================
-%>

<%*
// 输出格式化的标签
tR += `✨ 推荐标签：\n\n`;

if (domainTags.length > 0) {
  tR += `📂 Domain: ${domainTags.join(', ')}\n`;
}

if (topicTags.length > 0) {
  tR += `🏷️  Topic: ${topicTags.join(', ')}\n`;
}

if (typeTags.length > 0) {
  tR += `📄 Type: ${typeTags.join(', ')}\n`;
}

if (statusTags.length > 0) {
  tR += `🚦 Status: ${statusTags.join(', ')}\n`;
}

tR += `\n\`\`\`\n`;
tR += `tags:\n`;
for (const tag of tagsArray) {
  tR += `  - ${tag}\n`;
}
tR += `\`\`\`\n`;
-%>

<%*
// ========================================
// 使用说明
// ========================================
-%>

<%*
tR += `---\n`;
tR += `## 💡 使用说明\n\n`;
tR += `### 自动应用\n`;
tR += `- 在 Templater 设置中配置此模板为默认笔记模板\n`;
tR += `- 新建笔记时会自动运行标签推荐\n\n`;
tR += `### 手动触发\n`;
tR += `- 在现有笔记中运行：添加 \`tp.file.tags = tagsArray\` 到笔记末尾\n`;
tR += `- 或使用命令：\`/tag-recommender\`\n\n`;
tR += `### 推荐优先级\n`;
tR += `1. **P0**: 目录映射 → Domain 标签（自动）\n`;
tR += `2. **P1**: 关键词匹配 → Topic 标签（最多 3 个）\n`;
tR += `3. **P2**: 文件类型推断 → Type 标签（全部匹配）\n`;
tR += `4. **P3**: 状态推断 → Status 标签（最多 1 个）\n\n`;
tR += `### 注意事项\n`;
tR += `- DailyNotes, Resources, Archives 不自动添加 Domain 标签\n`;
tR += `- Topic 标签限制为前 3 个匹配项\n`;
tR += `- Status 标签限制为第 1 个匹配项\n`;
tR += `- Type 标签检测所有匹配项\n\n`;
tR += `---\n`;
tR += `**配置文件**: [tag_recommender_rules.md](./tag_recommender_rules.md)\n`;
tR += `**查看详情**: [仓库标签管理系统](../../Atlas/Index/仓库标签管理系统.md)\n`;
-%>
