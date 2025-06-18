

Storybook 是一个强大的 UI 组件开发工具，它能帮助你独立地构建、展示和测试 UI 组件。用它来展示 AI UI pattern 是一个绝佳的选择，因为它能清晰地隔离每个模式，方便团队理解、复用和迭代。

下面我将为你设计 3 个常见的 **AI UI Pattern**，并说明如何在 Storybook 中展示它们的核心思路和代码结构。



### **AI UI Pattern 1: 智能搜索/命令输入 (Intelligent Search/Command Input)**

这个模式常见于 AI 助手、代码编辑器或任何需要用户通过自然语言获取信息或执行操作的场景。

核心思想：

当用户输入时，AI 实时提供预测、建议或可执行的命令，帮助用户更快地找到答案或完成任务。

**Storybook 展示思路：**

- **Default State:** 默认的输入框，等待用户输入。
- **Typing State:** 用户输入中，展示 AI 实时提供的建议列表（例如，`"你是不是想问..."`，`"建议执行命令..."`）。
- **Loading State:** AI 正在生成建议时的加载动画。
- **Error State:** AI 建议服务出错时的提示。

**代码骨架 (React 示例，Storybook Component Story Format):**



```JavaScript
// components/IntelligentSearchInput.jsx
import React, { useState, useEffect } from 'react';
import './IntelligentSearchInput.css'; // 假设有样式文件

const IntelligentSearchInput = ({ placeholder, onSearch, suggestions = [], isLoading = false, error = null }) => {
  const [query, setQuery] = useState('');

  const handleChange = (e) => {
    setQuery(e.target.value);
    // 实际应用中，这里会触发对AI服务的调用
    if (onSearch) {
      onSearch(e.target.value);
    }
  };

  return (
    <div className="intelligent-search-container">
      <input
        type="text"
        placeholder={placeholder}
        value={query}
        onChange={handleChange}
        className={`intelligent-search-input ${isLoading ? 'loading' : ''} ${error ? 'error' : ''}`}
      />
      {isLoading && <div className="loading-indicator">思考中...</div>}
      {error && <div className="error-message">{error}</div>}

      {suggestions.length > 0 && query.length > 0 && !isLoading && !error && (
        <ul className="suggestions-list">
          {suggestions.map((s, index) => (
            <li key={index} onClick={() => setQuery(s.text)}>
              {s.text} {s.type && <span className="suggestion-type">({s.type})</span>}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default IntelligentSearchInput;

// stories/IntelligentSearchInput.stories.jsx
import React from 'react';
import IntelligentSearchInput from '../components/IntelligentSearchInput';

export default {
  title: 'AI UI Patterns/Intelligent Search Input',
  component: IntelligentSearchInput,
  argTypes: {
    placeholder: { control: 'text' },
    onSearch: { action: 'searched' },
    suggestions: { control: 'object' },
    isLoading: { control: 'boolean' },
    error: { control: 'text' },
  },
};

const Template = (args) => <IntelligentSearchInput {...args} />;

export const Default = Template.bind({});
Default.args = {
  placeholder: '输入你的问题或命令...',
};

export const WithSuggestions = Template.bind({});
WithSuggestions.args = {
  placeholder: '输入你的问题或命令...',
  suggestions: [
    { text: '如何开始使用？', type: 'FAQ' },
    { text: '生成一份周报', type: 'Command' },
    { text: '查询最新数据', type: 'Data' },
  ],
};

export const LoadingState = Template.bind({});
LoadingState.args = {
  placeholder: '输入你的问题或命令...',
  isLoading: true,
};

export const ErrorState = Template.bind({});
ErrorState.args = {
  placeholder: '输入你的问题或命令...',
  error: 'AI 服务暂时不可用，请稍后再试。',
};

// 你还需要为 IntelligentSearchInput.css 添加一些基本样式来展示效果
```

---

### **AI UI Pattern 2: AI 生成内容区域 (AI Generated Content Area)**

这个模式用于展示 AI 生成的文本、代码、图像或其他内容，通常伴随着一些交互选项。

核心思想：

清晰地展示 AI 的生成结果，并提供复制、编辑、点赞/踩、刷新或调整生成参数等交互功能。

**Storybook 展示思路：**

- **Text Generation:** 展示一段 AI 生成的文本，包含复制、编辑、评价按钮。
- **Code Generation:** 展示一段 AI 生成的代码，带有代码高亮和复制按钮。
- **Image Generation:** 展示一张 AI 生成的图片，带有下载、刷新或分享按钮。
- **Loading State:** 内容生成中的加载动画。
- **Empty State:** 尚未生成内容时的提示。

**代码骨架 (React 示例):**


```JavaScript
// components/AIGeneratedContent.jsx
import React from 'react';
import './AIGeneratedContent.css'; // 假设有样式文件

const AIGeneratedContent = ({ type, content, onCopy, onEdit, onLike, onDislike, onRefresh, isLoading = false, isEmpty = false }) => {
  if (isLoading) {
    return <div className="ai-content-container loading">AI 正在生成中，请稍候...</div>;
  }

  if (isEmpty) {
    return <div className="ai-content-container empty">点击按钮开始生成内容</div>;
  }

  const renderContent = () => {
    switch (type) {
      case 'text':
        return <p className="generated-text">{content}</p>;
      case 'code':
        return <pre className="generated-code"><code>{content}</code></pre>;
      case 'image':
        return <img src={content} alt="AI Generated" className="generated-image" />;
      default:
        return <p>未知内容类型</p>;
    }
  };

  return (
    <div className="ai-content-container">
      {renderContent()}
      <div className="ai-content-actions">
        {onCopy && <button onClick={onCopy}>复制</button>}
        {onEdit && <button onClick={onEdit}>编辑</button>}
        {onLike && <button onClick={onLike}>👍</button>}
        {onDislike && <button onClick={onDislike}>👎</button>}
        {onRefresh && <button onClick={onRefresh}>刷新</button>}
      </div>
    </div>
  );
};

export default AIGeneratedContent;

// stories/AIGeneratedContent.stories.jsx
import React from 'react';
import AIGeneratedContent from '../components/AIGeneratedContent';

export default {
  title: 'AI UI Patterns/AI Generated Content',
  component: AIGeneratedContent,
  argTypes: {
    type: { control: { type: 'select', options: ['text', 'code', 'image'] } },
    content: { control: 'text' },
    onCopy: { action: 'copied' },
    onEdit: { action: 'edited' },
    onLike: { action: 'liked' },
    onDislike: { action: 'disliked' },
    onRefresh: { action: 'refreshed' },
    isLoading: { control: 'boolean' },
    isEmpty: { control: 'boolean' },
  },
};

const Template = (args) => <AIGeneratedContent {...args} />;

export const TextContent = Template.bind({});
TextContent.args = {
  type: 'text',
  content: 'AI 生成的这段文字是关于如何有效学习编程的建议，它涵盖了从基础概念到实践项目的重要性，并强调了持续学习和解决问题的能力。',
};

export const CodeContent = Template.bind({});
CodeContent.args = {
  type: 'code',
  content: `function factorial(n) {\n  if (n === 0) return 1;\n  return n * factorial(n - 1);\n}`,
};

export const ImageContent = Template.bind({});
ImageContent.args = {
  type: 'image',
  content: 'https://via.placeholder.com/400x300/CCCCCC/FFFFFF?text=AI+Generated+Image', // 替换为实际图片URL
};

export const ContentLoading = Template.bind({});
ContentLoading.args = {
  isLoading: true,
};

export const EmptyContent = Template.bind({});
EmptyContent.args = {
  isEmpty: true,
};
```

---

### **AI UI Pattern 3: AI 辅助决策/推荐 (AI Assisted Decision/Recommendation)**

这个模式旨在展示 AI 如何处理复杂信息并为用户提供数据驱动的建议或决策支持。

核心思想：

AI 分析数据、权衡利弊，并以清晰、可解释的方式呈现推荐结果，通常伴随对推荐理由的解释。

**Storybook 展示思路：**

- **Simple Recommendation:** 基于简单规则的推荐（如“为您推荐最优惠的方案”）。
- **Comparative Recommendation:** 展示多个选项，并对比 AI 评估的关键指标（例如，产品对比、路线规划）。
- **Justification Included:** 推荐结果附带 AI 给出理由或依据。
- **Confidence Level:** 显示 AI 对其推荐的置信度。
- **Interactive Refinement:** 用户可以调整参数，AI 实时更新推荐。

**代码骨架 (React 示例):**

JavaScript

```JavaScript
// components/AIDecisionRecommendation.jsx
import React from 'react';
import './AIDecisionRecommendation.css'; // 假设有样式文件

const AIDecisionRecommendation = ({
  recommendation,
  confidence = null,
  justification = null,
  options = [],
  onSelectOption,
  isLoading = false,
}) => {
  if (isLoading) {
    return <div className="ai-recommendation-container loading">AI 正在分析并生成推荐...</div>;
  }

  return (
    <div className="ai-recommendation-container">
      {recommendation && (
        <div className="main-recommendation">
          <h3>AI 推荐：{recommendation.title}</h3>
          <p>{recommendation.description}</p>
          {confidence !== null && (
            <p className="confidence-score">置信度：{Math.round(confidence * 100)}%</p>
          )}
        </div>
      )}

      {justification && (
        <div className="recommendation-justification">
          <h4>推荐理由：</h4>
          <p>{justification}</p>
        </div>
      )}

      {options.length > 0 && (
        <div className="alternative-options">
          <h4>其他选项：</h4>
          <ul>
            {options.map((option, index) => (
              <li key={index} onClick={() => onSelectOption && onSelectOption(option)}>
                <strong>{option.title}</strong>: {option.description}
                {option.pros && <span className="pros"> (优点: {option.pros})</span>}
                {option.cons && <span className="cons"> (缺点: {option.cons})</span>}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default AIDecisionRecommendation;

// stories/AIDecisionRecommendation.stories.jsx
import React from 'react';
import AIDecisionRecommendation from '../components/AIDecisionRecommendation';

export default {
  title: 'AI UI Patterns/AI Decision Recommendation',
  component: AIDecisionRecommendation,
  argTypes: {
    recommendation: { control: 'object' },
    confidence: { control: { type: 'range', min: 0, max: 1, step: 0.01 } },
    justification: { control: 'text' },
    options: { control: 'object' },
    onSelectOption: { action: 'optionSelected' },
    isLoading: { control: 'boolean' },
  },
};

const Template = (args) => <AIDecisionRecommendation {...args} />;

export const SimpleRecommendation = Template.bind({});
SimpleRecommendation.args = {
  recommendation: {
    title: '推荐方案 A',
    description: '此方案能够最大化您的投入回报，并有效控制风险。',
  },
  confidence: 0.92,
  justification: '基于对过去一年市场趋势的深度分析，该方案与您当前的用户画像匹配度最高，预计转化率可达 15%。',
};

export const ComparativeOptions = Template.bind({});
ComparativeOptions.args = {
  recommendation: {
    title: '方案 B (更激进的增长)',
    description: '此方案有望带来更高的用户增长，但风险也相对较高。',
  },
  options: [
    {
      title: '方案 A (稳健增长)',
      description: '适合长期投资，风险较低。',
      pros: '市场成熟，投入回报稳定',
      cons: '增长速度较慢',
    },
    {
      title: '方案 C (创新尝试)',
      description: '探索全新市场，潜力大，但波动性强。',
      pros: '可能获得爆发式增长',
      cons: '市场不确定性高',
    },
  ],
  confidence: 0.75,
  justification: '综合考虑您的风险偏好和期望收益，我们为您对比了以上三种主要策略。方案 B 在现有市场中表现出最高的增长潜力，但您需要做好应对高波动的准备。',
};

export const LoadingRecommendation = Template.bind({});
LoadingRecommendation.args = {
  isLoading: true,
};
```

---

### **如何运行这些示例 (假设你已安装 Node.js 和 npm/yarn)**

1. **初始化一个新的 React 项目 (如果你还没有)：**
```Bash
    npx create-react-app my-ai-ui-patterns --template @storybook/cra-ts # 或者其他你喜欢的模板
    cd my-ai-ui-patterns
    ```
    
2. **安装 Storybook：**
  
    ```Bash
    npx storybook@latest init
    ```
    
3. **创建文件：**
    - 在 `src/components` 目录下创建 `IntelligentSearchInput.jsx`, `AIGeneratedContent.jsx`, `AIDecisionRecommendation.jsx` (以及相应的 `.css` 文件)。
    - 在 `src/stories` 目录下创建 `IntelligentSearchInput.stories.jsx`, `AIGeneratedContent.stories.jsx`, `AIDecisionRecommendation.stories.jsx`。
4. **运行 Storybook：**

    ```
    npm run storybook
    ```

这将会在你的浏览器中打开 Storybook UI，你就可以看到这些 AI UI pattern 的不同状态和交互方式了。通过 Storybook，你可以独立地开发和测试这些模式，确保它们在集成到完整应用前就能提供最佳的用户体验。