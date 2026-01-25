---
tags:
  - Domain/知识管理
  - Status/Done
  - Type/教程
created: 2026-01-25
update: 2026-01-25
rating: 5
view-count: 0
related:
  - [[Atlas/BASE/快速入门指南.md]]
  - [[5.Misc/Template/]]
---

## 🔗 相关链接

**上级索引**:
- [[Atlas/BASE/_Index_of_BASE.md|BASE]]
- [[Atlas/BASE/插件使用指南/|插件使用指南]]

---

# 🧩 Templater 插件使用指南

> **Templater 是 Obsidian 最强大的模板插件**，它让你可以使用动态模板和脚本，自动化笔记创建流程。

---

## 🎯 什么是 Templater？

Templater 是一个模板系统，它超越了简单的静态模板，支持：
- 📝 **动态变量**：插入日期、时间、文件名等
- 🔧 **JavaScript 脚本**：执行复杂的逻辑
- 🔄 **用户输入**：在插入模板时提示输入
- 📂 **文件操作**：创建、打开、移动文件

---

## 📦 安装和配置

### 安装步骤

1. 打开 Obsidian 设置
2. 进入 **"社区插件"**
3. 搜索 **"Templater"**
4. 点击安装并启用

### 基本配置

在 Templater 设置中：

1. **Template folder location**: 设置为 `5.Misc/Template/`
2. **Trigger Templater on new file creation**: ✅ 启用
3. **Enable Daily Notes**: ✅ 启用（如果需要日记功能）
4. **Enable System Commands**: ⚠️ 谨慎启用（安全风险）

---

## 🚀 核心语法

### 1️⃣ **动态变量**

Templater 提供了许多内置变量：

```md
<% tp.date.now("YYYY-MM-DD") %>        <!-- 当前日期 -->
<% tp.file.title %>                    <!-- 文件标题 -->
<% tp.file.path %>                    <!-- 文件路径 -->
<% tp.system.clipboard() %>           <!-- 剪贴板内容 -->
```

**示例**：

```md
# <% tp.file.title %>

创建日期: <% tp.date.now("YYYY-MM-DD HH:mm") %>
标签: #Type/Note
```

### 2️⃣ **用户输入**

在插入模板时提示用户输入：

```md
---
title: <% tp.file.title %>
author: <% tp.system.prompt("请输入作者姓名") %>
category: <% tp.system.suggester(["技术", "生活", "工作"], ["选择类别"]) %>
---
```

### 3️⃣ **条件判断**

使用 JavaScript 进行条件判断：

```md
<%*
if (tp.file.title.includes("紧急")) {
  tR += "🔥 这是紧急任务！\n";
} else {
  tR += "✅ 普通任务\n";
}
%>
```

### 4️⃣ **循环**

使用 JavaScript 循环：

```md
<%*
for (let i = 1; i <= 5; i++) {
  tR += `- 任务 ${i}\n`;
}
%>
```

---

## 💡 实用模板示例

### 📝 **Zettelkasten 笔记模板**

```md
---
tags:
  - Type/Note
  - Domain/<% tp.system.suggester(["AI", "编程", "心理学"], ["选择领域"]) %>
created: <% tp.date.now("YYYY-MM-DD") %>
update: <% tp.date.now("YYYY-MM-DD") %>
rating:
---

# <% tp.file.title %>

## 🎯 目标 (Purpose)
<% tp.system.clipboard() %>

## 💡 核心概念 (Core Concept)


## 📖 详细说明 (Details)


## 🔗 连接的笔记 (Related Notes)


## 🤔 反思 (Reflection)


## 📚 参考文献 (References)

```

### ✅ **项目管理模板**

```md
---
tags:
  - Type/Project
  - Domain/<% tp.system.suggester(["技术", "内容", "学习"], ["项目类型"]) %>
status: Active
created: <% tp.date.now("YYYY-MM-DD") %>
deadline: <% tp.system.prompt("截止日期 (YYYY-MM-DD)") %>
---

# <% tp.file.title %>

## 📊 项目概述

**开始日期**: <% tp.date.now("YYYY-MM-DD") %>
**截止日期**: <% tp.system.prompt("截止日期 (YYYY-MM-DD)") %>
**优先级**: <% tp.system.suggester(["🔴 高", "🟡 中", "🟢 低"], ["选择优先级"]) %>

## 🎯 项目目标

<% tp.system.clipboard() %>

## 📋 任务清单

```tasks
- [ ] 任务1
- [ ] 任务2
- [ ] 任务3
```

## 📈 进度跟踪

| 阶段 | 状态 | 完成日期 |
|------|------|----------|
| 阶段1 | ⏳ | - |
| 阶段2 | ⏳ | - |
| 阶段3 | ⏳ | - |

## 📝 项目日志

### <% tp.date.now("YYYY-MM-DD") %>
-

## 🏁 完成标准



## 🔗 相关资源

```

### 📅 **每日日记模板**

```md
---
date: <% tp.date.now("YYYY-MM-DD") %>
week: <% tp.date.now("ww") %>
---

# 📅 <% tp.date.now("YYYY年MM月DD日 dddd") %>

## 💭 今日反思

**主要成就**:


**遇到的问题**:


**明天计划**:


## 📚 今日学习


## 💡 今日灵感



---
**备注**:
```

---

## 🔧 高级用法

### 📂 **动态创建文件**

在模板中创建新文件：

```md
<%*
const fileName = await tp.system.prompt("输入子笔记名称");
if (fileName) {
  await tp.file.create_new(tp.file.folder() + "/" + fileName + ".md", "内容");
}
%>
```

### 🔍 **查询 Dataview 数据**

在模板中嵌入 Dataview 查询：

```md
```dataview
TABLE file.link, rating
FROM "<% tp.file.folder %>"
WHERE rating
SORT rating DESC
LIMIT 5
```
```

### 📊 **读取 YAML 元数据**

读取当前文件的元数据：

```md
<%*
const rating = tp.file.frontmatter.rating;
if (rating && rating >= 4) {
  tR += "⭐ 这是一篇优秀笔记！";
}
%>
```

---

## 🎨 常用命令

### 📋 **模板快捷命令**

```
<% tp.file.create_new("路径/文件名.md", "内容") %>
<% tp.file.append("内容") %>
<% tp.file.cursor(行, 列) %>
<% tp.system.clipboard() %>
<% tp.system.prompt("提示文字") %>
```

### 📅 **日期格式化**

```
<% tp.date.now("YYYY-MM-DD") %>        <!-- 2026-01-25 -->
<% tp.date.now("yyyy-MM-dd HH:mm") %>  <!-- 2026-01-25 14:30 -->
<% tp.date.now("dddd") %>               <!-- 星期几 -->
<% tp.date.weekday("zh-CN") %>          <!-- 星期几 -->
```

---

## 🐛 常见问题

### Q1: 模板不生效？

**解决方法**：
1. 检查模板文件是否在 `5.Misc/Template/` 目录下
2. 确认 Templater 插件已启用
3. 检查模板语法是否正确

### Q2: 如何在模板中使用换行？

**方法**：
```md
<%*
tR += "第一行\n";
tR += "第二行\n";
%>
```

或者：
```md
<%*
tR = `第一行
第二行
第三行`;
%>
```

### Q3: 如何调试模板？

**方法**：
1. 使用 `console.log()` 在开发者控制台查看
2. 先测试简单模板，逐步增加复杂度
3. 检查变量是否存在：`<%= tp.file.title %>`

---

## 💡 最佳实践

### ✅ **好的做法**

1. **模块化模板**：创建可复用的小模板
2. **添加注释**：在模板中添加使用说明
3. **使用建议**：使用 `suggester` 提供选项
4. **错误处理**：检查用户输入是否有效

### ❌ **避免的做法**

1. ❌ 过于复杂的模板（难以维护）
2. ❌ 硬编码路径（不便于迁移）
3. ❌ 没有注释的复杂逻辑
4. ❌ 过度使用动态功能

---

## 📚 更多资源

### 🔗 **官方文档**

- Templater GitHub: [https://github.com/SilentVoid13/Templater](https://github.com/SilentVoid13/Templater)
- 内部函数参考: [https://silentvoid13.github.io/Templater/internal-functions/](https://silentvoid13.github.io/Templater/internal-functions/)

### 📂 **本库模板**

- [[5.Misc/Template/Zettelkasten模板.md]]
- [[5.Misc/Template/项目管理模板.md]]
- [[5.Misc/Template/研究笔记模板.md]]

---

## 🚀 下一步

1. **尝试模板**：使用现有模板创建新笔记
2. **自定义模板**：根据需求修改模板
3. **学习脚本**：掌握 Templater 的 JavaScript 功能
4. **分享模板**：与团队分享你的模板

---

**更新日志**:
- **2026-01-25**: 创建 Templater 使用指南

**预计学习时间**: 40-60 分钟
**难度等级**: ⭐⭐⭐☆☆ (中级)
**适合人群**: 已熟悉 Obsidian 基础操作的用户
