---
tags:
  - Domain/知识管理
  - Status/Done
  - Type/Index
created: 2026-01-25
update: 2026-01-25
rating: 5
view-count: 0
---

# 📚 插件使用指南索引

> 这里是 Obsidian 知识库核心插件的使用指南集合。

---

## 🎯 核心插件

### 📊 [Dataview](Dataview使用指南.md) ⭐⭐⭐⭐⭐
**最强大的数据查询插件**
- 📊 查询和展示笔记数据
- 🔍 支持表格、列表、任务列表
- 📈 实时更新，灵活过滤

**使用场景**:
- 质量看板
- 项目统计
- 任务汇总
- 文件索引

---

### 🧩 [Templater](Templater使用指南.md) ⭐⭐⭐⭐⭐
**最强大的模板系统**
- 📝 动态模板和脚本
- 🔧 支持用户输入
- 🚀 自动化工作流

**使用场景**:
- 快速创建笔记
- 日报/周报模板
- 项目管理模板

---

### ✅ [Tasks](Tasks使用指南.md) ⭐⭐⭐⭐☆
**最强大的任务管理插件**
- 📋 智能任务查询
- 🎯 优先级和截止日期
- 🔄 循环任务支持

**使用场景**:
- 每日任务清单
- 项目任务跟踪
- 学习计划管理

---

## 🔧 其他插件

### 🧠 Smart Connections
**AI 驱动的笔记关联发现**
- 使用 AI 发现笔记间的隐藏关联
- 自动推荐相关笔记
- 构建知识图谱

**文档**: 待补充

---

### 📋 Kanban
**看板项目管理**
- 可视化任务看板
- 拖拽管理任务状态
- 适合项目追踪

**文档**: 待补充

---

### 🎨 Excalidraw
**手绘图表和草图**
- 绘制思维导图
- 创建概念图
- 可视化信息

**文档**: 待补充

---

### 📰 Zoottelkeeper
**自动生成索引文件**
- 自动创建目录索引
- 保持索引更新
- 便于文件导航

**文档**: [[Atlas/Index/仓库标签管理系统.md]]

---

## 📚 学习路径

### 🌱 **初级（必学）**

1. ✅ [Dataview](Dataview使用指南.md) - 数据查询
2. ✅ [Templater](Templater使用指南.md) - 模板系统
3. ✅ [Tasks](Tasks使用指南.md) - 任务管理

### 🌿 **中级（推荐）**

4. Smart Connections - AI 关联
5. Kanban - 看板管理
6. Zoottelkeeper - 索引生成

### 🌳 **高级（可选）**

7. Excalidraw - 图表绘制
8. Advanced Topics - 高级主题

---

## 💡 快速参考

### 📊 **Dataview 常用查询**

```dataview
TABLE file.link, tags
FROM "2.Topics"
WHERE rating
SORT rating DESC
LIMIT 10
```

### 🧩 **Templater 快速命令**

```
<% tp.date.now("YYYY-MM-DD") %>
<% tp.file.title %>
<% tp.system.prompt("提示") %>
```

### ✅ **Tasks 快速查询**

```tasks
not done
priority is high
sort by due
```

---

## 🎓 进阶学习

### 📖 **推荐学习顺序**

1. **先学 Dataview**：理解数据查询
2. **再学 Templater**：掌握模板自动化
3. **后学 Tasks**：管理任务和项目
4. **最后学其他插件**：根据需要选择

### 🔗 **外部资源**

- [Obsidian 插件市场](https://obsidian.md/plugins)
- [Dataview 官方文档](https://blacksmithgu.github.io/obsidian-dataview/)
- [Templater GitHub](https://github.com/SilentVoid13/Templater)
- [Tasks GitHub](https://github.com/obsidian-tasks-group/obsidian-tasks)

---

## 🆘 需要帮助？

- 📖 查看 [[Atlas/BASE/快速入门指南.md]]
- ❓ 检查 [[Atlas/BASE/常见问题FAQ.md]]
- 📚 阅读 [[CLAUDE.md]]

---

**更新日志**:
- **2026-01-25**: 创建插件使用指南索引

**预计学习时间**: 每个插件 30-60 分钟
**难度等级**: ⭐⭐⭐☆☆ (中级)
