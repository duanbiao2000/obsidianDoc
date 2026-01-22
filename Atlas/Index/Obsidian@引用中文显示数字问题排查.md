---
uid: 2026-01-22-obsidian-mention-chinese-issue
tags:
  - Domain/技术栈
  - Status/Review
  - Type/Troubleshooting
created: 2026-01-22
updated: 2026-01-22
rating: 8
view-count: 0
related: [[CLAUDE.md]]
---

# Obsidian @ 引用中文显示数字问题排查

> 问题描述：在 Obsidian 中使用 `@` 符号引用文件或标签时，中文名称显示为数字 ID

## 问题现象

使用 `@` 引用时：
- **预期显示**: `UX本质` 或 `数据结构与算法`
- **实际显示**: `62a5f8d522e391c9` 或类似的十六进制数字

## 问题根源

### 1. Obsidian 内部 ID 机制

Obsidian 为每个文件、标签页和界面元素生成**内部十六进制 ID**：

```json
// .obsidian/workspace.json
{
  "id": "62a5f8d522e391c9",      // 内部 ID
  "type": "split",
  "children": [
    {
      "id": "f882884bfecca64f",  // 子元素 ID
      "state": {
        "file": "2.Topics/01.技术栈/数据结构与算法.md"
      }
    }
  ]
}
```

### 2. 插件干扰

可能影响 @ 引用的插件：

#### Obsidian Copilot
- **作用**: 为每个文件生成 MD5 哈希索引用于 AI 检索
- **影响**: @ 引用时可能返回向量索引 ID 而不是文件名
- **证据**: `.obsidian/copilot-index-*.json` 文件包含哈希映射

#### Smart Connections
- **作用**: 创建笔记的语义连接和向量搜索
- **影响**: 可能使用内部 ID 进行引用

## 解决方案

### 方案 1: 禁用 Copilot 的 @ 引用集成

1. 打开 Obsidian 设置 → **Copilot 插件**
2. 查找 "Mention" 或 "引用" 相关设置
3. 禁用 Copilot 对 `@` 符号的拦截

### 方案 2: 使用英文别名 + Title 字段

为中文文件添加英文别名，让 @ 引用有可用的 ASCII 标识：

```yaml
---
title: UX本质
aliases:
  - UX Essence
  - UX Design
file-name: ux-essence  # 可选：建议英文文件名
---
```

### 方案 3: 使用原生 Obsidian 引用语法

不要使用 `@`，改用：
- `[[Wiki Link]]` - 双方括号引用
- `![[Embed]]` - 嵌入式引用
- `[[文件名|显示文本]]` - 自定义显示文本

### 方案 4: 调整插件优先级

在 `.obsidian/community-plugins.json` 中调整插件加载顺序：
1. 将 `smart-connections` 和 `copilot` 移到列表末尾
2. 让核心 Obsidian 功能优先处理 `@` 符号

## 临时排查步骤

### 步骤 1: 禁用所有插件

```bash
# 安全起见，先备份插件列表
cp .obsidian/community-plugins.json .obsidian/community-plugins.json.backup
```

然后在 Obsidian 中：
1. 设置 → **社区插件** → **全部禁用**
2. 重启 Obsidian
3. 测试 `@` 引用是否正常

### 步骤 2: 逐个启用插件

按以下顺序测试：
1. 只启用 **copilot** → 测试 `@`
2. 只启用 **smart-connections** → 测试 `@`
3. 同时启用两者 → 测试 `@`

### 步骤 3: 检查 Copilot 设置

查看 `.obsidian/plugins/copilot/data.json`：

```bash
cat .obsidian/plugins/copilot/data.json | grep -A5 -B5 "mention\|reference"
```

## 最佳实践建议

### 长期方案：文件命名规范

对于关键的、经常被引用的文件，建议：

```
├── ux-essence.md              # 英文文件名
│   ├── title: UX本质          # YAML title 保持中文
│   └── aliases: UX Essence    # 英文别名
│
├── data-structures.md         # 英文文件名
│   ├── title: 数据结构与算法  # YAML title
│   └── aliases: DS, Algo      # 英文别名
```

### 保留中文的场景

对于不常被引用的文件，可以保留中文文件名：
- 日记笔记
- 临时笔记
- 归档内容

## 相关文件

- `.obsidian/workspace.json` - 存储 Obsidian 界面状态和内部 ID
- `.obsidian/copilot-index-*.json` - Copilot 向量索引（40MB+）
- `.obsidian/plugins/smart-connections/data.json` - Smart Connections 配置
- `.obsidian/community-plugins.json` - 已安装插件列表

## 下一步行动

- [ ] 测试禁用插件后 @ 引用是否正常
- [ ] 检查 Copilot 插件的详细设置
- [ ] 为高频引用的文件添加英文别名
- [ ] 考虑制定文件命名规范

---

**创建时间**: 2026-01-22
**问题状态**: 待验证
**优先级**: 中等（影响用户体验）
