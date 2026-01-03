---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 1753015956234
view-count: 4
---

# 🛠️ AI精英学院™ 页面开发规范 (v3.2)

**核心原则**：简洁专业 · 教学导向 · 严禁营销。

---

### 📌 总体约束
- **格式**：单一 HTML 文件，样式内嵌至 `<style>`，禁止外部 CSS。
- **品牌**：严格执行 Lavender/Mint 设计系统。
- **内容**：100% 忠实原文逻辑，禁止添加 CTA 按钮或广告语。
- **版权**：必须包含标准页脚（© 2025 AI 精英学院™ & AXTONLIU™）。

---

### 🎨 设计系统 (Design System)

| 类别 | 规范 | 具体数值 |
| :--- | :--- | :--- |
| **主色 (Lavender)** | 核心品牌色 | `--lavender-500: #967BB6;` |
| **辅助 (Mint)** | 强调/成功色 | `--mint-500: #21C9A5;` |
| **中性 (Gray)** | 文字与背景 | `Heading: #1F2937; Text: #4A5568;` |
| **几何属性** | 圆角与阴影 | `Radius: 12px; Shadow: 0 8px 16px rgba(0,0,0,.08);` |
| **排版** | 视觉层次 | `h1: 4rem; Contrast Ratio ≥ 3:1 (Title/Body);` |
| **间距** | 呼吸感 | `Section Gap ≥ 4rem;` |

---

### 🏗️ 布局模式 (Layout Modes)

- **模式 A (Keynote)**：全屏 Hero + 概念详解。适合核心理念。
- **模式 B (TIME)**：强势标题 + 栅格布局 (理论/步骤/案例)。适合方法论。
- **模式 C (Product)**：层次化拆解 (总览→分解→验证→指南)。适合复杂系统。

---

### 📦 核心组件库 (Components)

- **信息框**：
  - `info-box`: Mint 背景，用于基础说明。
  - `info-box-emphasis`: Lavender 背景，用于核心强调。
- **卡片**：
  - `card-minimal`: 1px 描边，极简风格。
  - `card-elevated`: 悬停位移 (`-2px`) + 深度阴影。
- **排版**：
  - `text-gradient`: Lavender 转 Mint 渐变文字。
  - `text-highlight`: Lavender 浅背景高亮。

---

### ⚖️ 质量审计清单 (Audit)

- [ ] **视觉**：背景层级是否清晰？色彩是否克制（黑白灰为主）？
- [ ] **交互**：Transition 是否 ≤ 0.3s？变化幅度是否 < 10%？
- [ ] **内容**：是否包含原文所有要素？是否删除了所有营销诱导？
- [ ] **技术**：CDN 资源是否可靠 (Tailwind/FontAwesome)？是否完美适配移动端？

---

### 🧩 关联规范
- [[品牌视觉识别手册]]：获取更深层的色彩心理学定义。
- [[MAPS教学法规范]]：确保页面结构符合系统化训练营的学习路径。
