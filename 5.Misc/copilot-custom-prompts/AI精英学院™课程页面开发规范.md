---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 1753015956234
---
# AI精英学院™课程页面开发规范


## 一、总体说明
1. **输出格式**：单一HTML文件，样式需完整写入`<style>`标签，不引用外部CSS。
2. **品牌一致性**：严格遵循设计系统的色彩、排版、组件、圆角、阴影、间距规范。
3. **内容导向**：专注教学内容展示，避免营销元素和广告语言。
4. **版权合规**：必须保留页脚版权声明。


## 二、设计系统
### 1. 设计变量
```css
:root {
  /* 主色系（Lavender） */
  --lavender-50: #E6E6FA;
  --lavender-100: #DAD0F6;
  --lavender-500: #967BB6;
  --lavender-800: #4F3A66;
  
  /* 辅助色系（Mint） */
  --mint-50: #E8FFF6;
  --mint-300: #5AD7BD;
  --mint-500: #21C9A5;
  
  /* 中性色系（Gray） */
  --gray-50: #F9FAFB;
  --gray-100: #F3F4F6;
  --gray-600: #4A5568;
  --gray-800: #1F2937;
  
  /* 核心语义化变量 */
  --bg-card: #FFFFFF;
  --primary-color: var(--lavender-500);
  --bg-elevated: var(--lavender-50);
  --text-primary: var(--gray-600);
  --text-heading: var(--gray-800);
  
  /* 几何属性 */
  --radius-sm: 4px;
  --radius-lg: 12px;
  --radius-full: 9999px;
  --space-sm: .5rem;
  --space-lg: 1.25rem;
  --space-3xl: 4rem;
  --shadow-sm: 0 1px 2px rgba(0,0,0,.05);
  --shadow-lg: 0 8px 16px rgba(0,0,0,.08);
}
```


### 2. 设计约束
- **背景色使用**：  
  - 浅色系（50-200层级）用于创造层次感；  
  - 纯白色用于主要内容区域；  
  - 轻度着色（lavender-50、mint-50）用于区域划分；  
  - 深色背景仅限特殊强调区域，需确保文字对比度。  

- **文字色彩**：  
  - 主标题：gray-800/900（确保权威感）；  
  - 正文：gray-600/700（保证可读性）；  
  - 辅助信息：gray-400/500（营造层次）；  
  - 强调文字：lavender-600/mint-600（适度突出）。  

- **装饰元素**：  
  - 图标尺寸：1.5rem-3rem（不喧宾夺主）；  
  - 分割线：gray-200/300（subtle效果）；  
  - 强调边框：lavender-300/mint-300；  
  - 阴影：以shadow-sm/md为主，避免过重。  


### 3. 设计美学标准
- **极简主义原则**：  
  - 留白至上：内容区域间距≥4rem（营造呼吸感）；  
  - 单一焦点：每屏仅突出1个核心概念（避免信息过载）；  
  - 层次清晰：最多3级信息层次。  

- **Apple风格特征**：  
  - 标题与正文字体尺寸对比≥3:1；  
  - 中轴对称、微妙阴影圆角（≤12px）；  
  - 克制色彩（黑灰白+品牌色点缀）。  

- **TIME杂志版式**：  
  - 强烈视觉层次、精确栅格布局；  
  - 优雅引用与分割线、专业排版节奏。  


## 三、布局模式与实现要求
### 1. 布局模式（三选一）
- **模式A（Apple Keynote风格，适合概念介绍）**：  
  - 全屏Hero区：超大标题、副标题、核心理念；  
  - 全屏Content区：概念详解+背景知识、实践案例展示、关键要点总结。  

- **模式B（TIME杂志风格，适合方法论教学）**：  
  - 强势标题栏；  
  - 主要内容区块（理论基础30%+操作步骤40%+案例分析30%）；  
  - 实践指导总结。  

- **模式C（Apple产品页风格，适合复杂概念）**：  
  - 层次化展开：概念总览→详细分解→案例验证→实操指南；  
  - 每个部分独立成屏（内容充实，提供完整学习路径）。  


### 2. 具体实现要求
- 字体尺寸：h1最小4rem（确保视觉冲击力）；  
- 内容平衡：兼顾原文信息完整与视觉简洁；  
- 重要概念：给予充分视觉空间和突出展示；  
- 详细内容：合理分布到多个区块，避免堆积；  
- 完整性：确保原文每个要点恰当呈现；  
- 配色克制：主要用黑灰白，品牌色仅做点缀；  
- 交互简约：悬停效果≤0.3s，变化幅度＜10%；  
- 原文忠实度：所有内容可追溯至原文，不创造新信息。  


## 四、标准模板结构
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow, noarchive, nosnippet">
  <meta name="googlebot" content="noindex, nofollow">
  <title>[具体内容标题] - MAPS AI 系统化训练营</title>
  <!-- Font Awesome 图标库 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <style>
    /* 设计变量定义 */
    /* 基础重置规则 */
    /* 组件库样式 */
    /* 响应式设计规则 */
  </style>
</head>
<body>
  <main id="content">
    <!-- 内容区域 -->
  </main>
  <!-- 标准页脚 -->
  <footer style="text-align:center;margin-top:var(--space-3xl);padding:var(--space-lg) 0;font-size:.875rem;color:var(--gray-600);">
    <p>© 2025 <a href="https://axtonliu.ai" target="_blank" rel="noopener noreferrer">AI 精英学院™</a> & AXTONLIU™</p>
    <p><small>All rights reserved. 内容仅供付费学员内部学习,未经授权严禁转载。</small></p>
  </footer>
</body>
</html>
```


## 五、扩展组件库
### 1. 信息提示组件
```css
/* 基础信息框 */
.info-box {
  background: var(--mint-50);
  border-left: 4px solid var(--mint-400);
  padding: var(--space-lg);
  border-radius: var(--radius-md);
}

/* 强调信息框 */
.info-box-emphasis {
  background: var(--lavender-100);
  border-left: 4px solid var(--lavender-500);
  padding: var(--space-lg);
  border-radius: var(--radius-md);
}

/* 成功提示 */
.success-box {
  background: var(--mint-100);
  border: 1px solid var(--mint-200);
  padding: var(--space-lg);
  border-radius: var(--radius-md);
}

/* 警告提示 */
.warning-box {
  background: #FEF3C7;
  border: 1px solid #FCD34D;
  padding: var(--space-lg);
  border-radius: var(--radius-md);
}
```

### 2. 卡片组件
```css
/* 简洁卡片 */
.card-minimal {
  background: var(--bg-primary);
  border: 1px solid var(--gray-200);
  border-radius: var(--radius-lg);
  padding: var(--space-xl);
  box-shadow: var(--shadow-sm);
}

/* 浮动卡片 */
.card-elevated {
  background: var(--bg-primary);
  border-radius: var(--radius-lg);
  padding: var(--space-xl);
  box-shadow: var(--shadow-md);
  transition: all 0.3s ease;
}
.card-elevated:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}
```

### 3. 网格布局
```css
.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--space-xl);
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-xl);
}

.grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: var(--space-xl);
}
```

### 4. 排版组件
```css
/* 标题层次 */
.title-hero {
  font-size: clamp(3rem, 8vw, 6rem);
  font-weight: 800;
  color: var(--text-primary);
}

.title-section {
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 700;
  color: var(--text-primary);
}

.title-subsection {
  font-size: 1.875rem;
  font-weight: 600;
  color: var(--text-primary);
}

/* 文字强调 */
.text-gradient {
  background: linear-gradient(135deg, var(--lavender-500), var(--mint-500));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.text-highlight {
  background: var(--lavender-100);
  padding: 0.125rem 0.375rem;
  border-radius: var(--radius-sm);
}
```


## 六、内容创建指导原则
### 1. 应包含内容
- 完整呈现原文内容（不遗漏重要信息，保留深度和广度）；  
- 忠实保持原文逻辑（遵循结构和论述顺序）；  
- 适当视觉层次（用设计突出重点和层次）；  
- 原文所有要素（概念、方法、观点、引用等）。  

### 2. 应避免内容
- 营销语言（推广文案、销售话术、价格信息）；  
- CTA按钮（立即购买、免费试用等行动号召）；  
- 广告元素（促销横幅、限时优惠等）；  
- 原创内容（原文外的案例、细节、观点）。  

### 3. 内容忠实度标准
- 严格基于原文，不增删核心信息；  
- 保持原文完整性和准确性；  
- 用设计增强而非替代文字内容；  
- 所有信息可追溯至原文。  


## 七、技术选择建议
### 推荐CDN资源
- **CSS框架**：Tailwind CSS（https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/）、Bootstrap 5（https://cdnjs.cloudflare.com/ajax/libs/bootstrap/）；  
- **JavaScript库**：Alpine.js（https://cdnjs.cloudflare.com/ajax/libs/alpinejs/）、GSAP（https://cdnjs.cloudflare.com/ajax/libs/gsap/）、AOS（https://cdnjs.cloudflare.com/ajax/libs/aos/）；  
- **图标库**：Font Awesome（https://cdnjs.cloudflare.com/ajax/libs/font-awesome/）、Lucide Icons（https://unpkg.com/lucide@latest/dist/umd/lucide.js）；  
- **字体资源**：Google Fonts（https://fonts.googleapis.com/css2?family=Inter）。  


## 八、质量标准检查
### 1. 设计层面
- 严格遵循设计系统变量；  
- 无禁用色彩和复杂渐变；  
- 颜色对比度符合无障碍标准；  
- 布局节奏自然，避免僵硬排列。  

### 2. 技术层面
- 合理选择外部资源；  
- 外部依赖来自可靠CDN；  
- 代码结构清晰，注释完整；  
- 响应式适配各尺寸设备；  
- 性能优化，快速加载。  

### 3. 内容层面
- 内容专业、准确、有价值；  
- 信息架构清晰易懂；  
- 无营销和广告元素；  
- 符合教学目标和学员需求。  


## 版本信息
- 文档版本：v3.2-lite（优化版）；  
- 最后更新：2025-07-10；  
- 核心理念：简洁专业 · 内容为王 · 教学导向。