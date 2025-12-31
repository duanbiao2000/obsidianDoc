---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
---
### **📘 AI 精英学院™ Slides Extended 开发规范 v1.1**

#### **v1.1 版本更新日志 (Changelog):**

1.  **【修复】内容宽度问题**: 在全局样式中引入了 `.reveal .slides > section` 选择器，将幻灯片内容的最大宽度从默认的 `960px` 提升至 `1200px`，并增加了内边距，为多列布局提供了更充足的空间。
2.  **【修复】主题颜色不一致**: 在“设计美学标准”中，将对背景色的规定从“建议”提升为“**必须**”，并明确了全局背景色应在 `reveal.initialize` 中设定，或通过 `data-background-color` 属性在每页幻灯片中保持一致，以杜绝颜色不统一的问题。
3.  **【修复】卡片底部对齐**: 在多列布局的 CSS 样式中，将 `display: flex` 升级为 `display: grid`，并为卡片容器 `.col` 增加了 `display: flex; flex-direction: column;`。这利用了现代 CSS 的强大能力，确保了无论内容多少，同一行的卡片都能保持等高且底部对齐。
4.  **【修复】文字两端对齐**: 在全局样式中，明确为 `.reveal .slides` 设定了 `text-align: left;`，并为需要居中的元素（如主标题）单独设置 `text-align: center;`。这从根本上避免了浏览器在 flex/grid 布局中可能产生的、不美观的 `text-align: justify;` 效果。
5.  **【优化】规范结构**: 将“扩展组件库”中的 CSS 样式直接整合进了“标准模板结构”的 `<style>` 块中，使其更具即用性，并增加了对三栏布局的支持。

---

### **AI精英学院™课程页面开发规范slides格式版本 v1.1**

# 📘 AI 精英学院™ Slides Extended 开发规范 v1.1

## 🧭 总览

本规范旨在为使用 Obsidian `Slides Extended` 插件创建课程内容提供一套统一、专业的设计与技术标准，确保所有幻灯片产出都符合 AI 精英学院™ 的品牌形象与教学质量要求。

| 模块 | 说明 | 作用 |
| :--- | :--- | :--- |
| 1. 总体原则 | 明确幻灯片的核心创作理念 | 设定“合作的游戏规则” |
| 2. 设计系统 | 定义视觉元素（色彩、排版） | 确保品牌风格的统一与美感 |
| 3. 幻灯片布局模式 | 提供针对不同内容的预设风格 | 为内容选择最合适的表达方式 |
| 4. 标准模板结构 | 提供可直接复用的基础代码框架 | 提高开发效率，保证基础质量 |
| 5. 内容与质量标准 | 规定内容创作的准则与检查项 | 确保教学内容的专业与准确 |

---

## 🧱 1. 总体原则

1.  **输出格式**：单一 Markdown (`.md`) 文件，所有自定义样式需完整写入文件顶部的 `<style>` 标签内。
2.  **品牌一致性**：严格遵循本规范中定义的色彩、排版、组件等视觉标准。
3.  **内容导向**：**单一焦点原则**，每张幻灯片应只聚焦于一个核心概念或思想，避免信息过载。
4.  **忠实原文**：所有内容必须可追溯至原始笔记，用设计增强而非替代文字内容。

---

## 🎨 2. 设计系统 (Design System)

### 2.1 核心色彩变量

所有幻灯片的 `<style>` 块都应基于以下色彩变量进行设计。

```css
/* 主色系（Lavender） */
--lavender-50: #E6E6FA; --lavender-100: #DAD0F6; --lavender-500: #967BB6; --lavender-800: #4F3A66;
/* 中性色系（Gray） */
--gray-50: #F9FAFB; --gray-100: #F3F4F6; --gray-600: #4A5568; --gray-800: #1F2937;
```

### 2.2 设计美学标准

-   **背景色**: **必须** 保持所有幻灯片背景色统一。推荐使用 `--gray-50` (近白) 或 `#FFFFFF`。应通过 `data-background-color` 属性在每页幻灯片中明确指定，以避免主题颜色不一致。深色背景仅限用于开篇、结尾或特殊强调的单页。
-   **文字色彩**: 主标题使用 `--gray-800`，正文使用 `--gray-600`，强调色使用 `--lavender-500`。
-   **排版**: **必须** 避免文本两端对齐。全局应设为左对齐，仅对特定标题元素使用居中对齐。

---

## 📐 3. 幻灯片布局模式 (Layout Modes)

根据内容类型，选择最合适的布局模式。

-   **模式A (Apple / Keynote 风格)**：适用于介绍核心概念、金句。特征是极简，强调视觉冲击力。
-   **模式B (McKinsey / 咨询顾问风格)**：适用于呈现框架、模型、对比分析。特征是逻辑严谨，信息密度高但结构清晰。
-   **模式C (TED Talk 风格)**：适用于讲述故事、案例或演进过程。特征是叙事驱动，常使用 `fragment` 动画控制节奏。

---

## 📝 4. 标准模板结构 (Standard Template v1.1)

所有新的幻灯片文件都应以此模板为基础进行创建。

```markdown
---
title: "[幻灯片标题]"
---

<!--
This slide deck adheres to the AI Elite Academy™ Development Specification v1.1.
Selected Mode: [在此注明选择的模式，如：Mode B (Consulting Style)]
-->

<style>
/* 1. 核心色彩变量 */
:root {
  --lavender-50: #E6E6FA; --lavender-100: #DAD0F6; --lavender-500: #967BB6; --lavender-800: #4F3A66;
  --gray-50: #F9FAFB; --gray-100: #F3F4F6; --gray-600: #4A5568; --gray-800: #1F2937;
}

/* 2. 全局样式 */
.reveal .slides {
  font-family: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
  color: var(--gray-600);
  text-align: left; /* 修复：全局左对齐，避免两端对齐 */
}
.reveal .slides > section {
  max-width: 1200px !important; /* 修复：增加内容区宽度 */
  padding: 0 2em !important;
}
.reveal .main-title, .reveal .subtitle {
  text-align: center; /* 仅对标题元素居中 */
}
.reveal .main-title { font-size: 3em; font-weight: 700; color: var(--gray-800); }
.reveal .subtitle { font-size: 1.2em; font-weight: 400; color: var(--gray-600); font-style: italic; }
.reveal .section-title {
  font-size: 2.2em;
  font-weight: 600;
  color: var(--lavender-500);
  padding-bottom: 0.3em;
  border-bottom: 2px solid var(--lavender-100);
  margin-bottom: 1em;
}

/* 3. 扩展组件样式 */
/* 多列布局 */
.grid-layout {
  display: grid;
  gap: 1.5rem;
  align-items: stretch; /* 修复：确保网格项拉伸以对齐 */
}
.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-layout .col {
  background: #fff;
  padding: 1.5em;
  border-radius: 8px;
  border: 1px solid var(--gray-100);
  display: flex; /* 修复：使用flex确保内部元素对齐 */
  flex-direction: column;
}
.grid-layout .col h3 { font-size: 1.2em; color: var(--gray-800); margin-top: 0; }
.grid-layout .col p:last-child { margin-bottom: 0; }
.grid-layout .col > *:last-child { margin-top: auto; } /* 修复：将最后一个元素推到底部，实现对齐 */

/* 强调信息框 */
.info-box-emphasis {
  background: var(--lavender-50);
  border-left: 4px solid var(--lavender-500);
  padding: 1rem 1.25rem;
  border-radius: 8px;
  margin-top: 1.5rem;
  font-size: 0.9em;
}
.info-box-emphasis strong { color: var(--lavender-800); }
</style>

<!-- .slide: data-background-color="var(--gray-50)" -->

<div class="main-title">幻灯片主标题</div>
<div class="subtitle">副标题或核心思想</div>

Note:
此处为演讲者备注，用于提示演讲要点。

---
<!-- .slide: data-background-color="var(--gray-50)" -->

<div class="section-title">章节标题</div>

<!-- 示例：三栏布局 -->
<div class="grid-layout grid-3">
  <div class="col"><h3>卡片1</h3><p>内容较少。</p></div>
  <div class="col"><h3>卡片2</h3><p>内容非常多，导致这个卡片比其他卡片更高，测试对齐效果。</p><p>第二段内容。</p></div>
  <div class="col"><h3>卡片3</h3><p>中等长度的内容。</p></div>
</div>

```

---

## ✅ 5. 内容与质量标准

-   **内容完整性**：确保原始笔记中的核心概念、逻辑关系和关键洞察都得到呈现。
-   **视觉层次**：使用标题、列表、粗体和组件，清晰地组织信息，引导观众的注意力。
-   **技术检查**：确保 Markdown 语法正确，HTML 结构清晰，CSS 样式无冗余。
-   **最终目标**：产出的幻灯片不仅是信息的载体，其本身就应是一次对原始笔记内容的**结构化重构**和**视觉化升维**。