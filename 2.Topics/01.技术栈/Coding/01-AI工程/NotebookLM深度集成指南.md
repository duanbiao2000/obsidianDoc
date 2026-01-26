# NotebookLM 深度集成指南

> Google NotebookLM AI 知识管理系统的完整使用手册与工作流
> 创建时间: 2026-01-26
> 相关: 知识库优化线路图 P1 - NotebookLM 深度集成

---

## 📋 目录

- [系统概述](#系统概述)
- [核心功能](#核心功能)
- [Obsidian 集成工作流](#obsidian-集成工作流)
- [使用场景](#使用场景)
- [最佳实践](#最佳实践)
- [批量导入脚本](#批量导入脚本)

---

## 系统概述

### 什么是 NotebookLM?

Google NotebookLM 是由 Google 开发的 AI 驱动的知识管理和研究工具,能够:

- **智能问答**: 基于上传的文档进行深度对话
- **多模态输出**: 生成音频、视频、测验、闪卡等多种学习材料
- **深度研究**: 自动搜索网络并整合相关信息
- **知识图谱**: 自动识别概念间的关联

### MCP 集成优势

通过 notebooklm-mcp 工具,我们可以:

- **无缝集成**: 直接在 Obsidian/Claude Code 中使用 NotebookLM
- **自动化流程**: 批量处理笔记和文档
- **智能同步**: 保持 Obsidian 和 NotebookLM 内容同步
- **增强检索**: 利用 AI 能力增强知识发现

---

## 核心功能

### 1. 笔记本管理 (Notebook Management)

#### 创建笔记本
```javascript
// MCP 调用示例
mcp_notebooklm_notebook_create({
  title: "AI 技术学习笔记"
})
```

#### 列出笔记本
```javascript
mcp_notebooklm_notebook_list({
  max_results: 100
})
```

#### 获取笔记本详情
```javascript
mcp_notebooklm_notebook_get({
  notebook_id: "your-notebook-id"
})
```

#### AI 摘要与推荐
```javascript
mcp_notebooklm_notebook_describe({
  notebook_id: "your-notebook-id"
})
// 返回: AI 生成的摘要 + 推荐的探索话题
```

---

### 2. 内容互动与查询 (Interaction)

#### 智能问答
```javascript
mcp_notebooklm_notebook_query({
  notebook_id: "your-notebook-id",
  query: "什么是注意力机制?它与 Transformer 的关系是什么?",
  source_ids: ["source1", "source2"],  // 可选: 指定源文件
  conversation_id: "conversation-id"  // 可选: 继续对话
})
```

#### 配置对话风格
```javascript
mcp_notebooklm_chat_configure({
  notebook_id: "your-notebook-id",
  goal: "learning_guide",  // default | learning_guide | custom
  custom_prompt: "请用通俗的语言解释,并提供具体例子",
  response_length: "longer"  // default | longer | shorter
})
```

---

### 3. 源文件管理 (Source Management)

#### 添加网页/YouTube
```javascript
mcp_notebooklm_notebook_add_url({
  notebook_id: "your-notebook-id",
  url: "https://example.com/article"
})
```

#### 添加 Google Drive 文档
```javascript
mcp_notebooklm_notebook_add_drive({
  notebook_id: "your-notebook-id",
  document_id: "google-drive-doc-id",
  title: "文档标题",
  doc_type: "doc"  // doc | slides | sheets | pdf
})
```

#### 粘贴文本
```javascript
mcp_notebooklm_notebook_add_text({
  notebook_id: "your-notebook-id",
  text: "要添加的文本内容...",
  title: "文本标题"
})
```

#### 同步 Drive 源
```javascript
// 1. 列出需要同步的源
mcp_notebooklm_source_list_drive({
  notebook_id: "your-notebook-id"
})

// 2. 同步更新
mcp_notebooklm_source_sync_drive({
  source_ids: ["source1", "source2"],
  confirm: true
})
```

---

### 4. AI 创作工坊 (Studio Content)

#### 音频概述 (Audio Overview)
```javascript
mcp_notebooklm_audio_overview_create({
  notebook_id: "your-notebook-id",
  source_ids: ["source1", "source2"],
  format: "deep_dive",  // deep_dive | brief | critique | debate
  length: "default",    // short | default | long
  language: "zh-CN",    // BCP 47 语言代码
  focus_prompt: "重点关注实际应用",
  confirm: true
})
```

#### 视频概述 (Video Overview)
```javascript
mcp_notebooklm_video_overview_create({
  notebook_id: "your-notebook-id",
  source_ids: ["source1"],
  format: "explainer",  // explainer | brief
  visual_style: "whiteboard",  // auto_select | classic | whiteboard | kawaii | anime
  language: "zh-CN",
  focus_prompt: "适合初学者的讲解",
  confirm: true
})
```

#### 学习套件

**生成测验**:
```javascript
mcp_notebooklm_quiz_create({
  notebook_id: "your-notebook-id",
  source_ids: ["source1"],
  question_count: 5,
  difficulty: "medium",  // easy | medium | hard
  confirm: true
})
```

**生成闪卡**:
```javascript
mcp_notebooklm_flashcards_create({
  notebook_id: "your-notebook-id",
  source_ids: ["source1"],
  difficulty: "medium",
  confirm: true
})
```

**生成思维导图**:
```javascript
mcp_notebooklm_mind_map_create({
  notebook_id: "your-notebook-id",
  source_ids: ["source1"],
  title: "知识结构图",
  confirm: true
})
```

#### 文档报告
```javascript
mcp_notebooklm_report_create({
  notebook_id: "your-notebook-id",
  source_ids: ["source1"],
  report_format: "Study Guide",  // Briefing Doc | Study Guide | Blog Post
  custom_prompt: "创建一个包含关键概念和实践练习的学习指南",
  language: "zh-CN",
  confirm: true
})
```

#### 幻灯片
```javascript
mcp_notebooklm_slide_deck_create({
  notebook_id: "your-notebook-id",
  source_ids: ["source1"],
  format: "detailed_deck",  // detailed_deck | presenter_slides
  length: "default",
  language: "zh-CN",
  focus_prompt: "包含代码示例和架构图",
  confirm: true
})
```

---

### 5. 深度科研 (Research)

#### 启动深度搜索
```javascript
mcp_notebooklm_research_start({
  query: "量子计算在机器学习中的应用",
  source: "web",      // web | drive
  mode: "deep",       // fast (~30s) | deep (~5min)
  notebook_id: "your-notebook-id",  // 可选: 使用现有笔记本
  title: "量子计算与机器学习研究"
})
// 返回: task_id
```

#### 轮询研究进度
```javascript
mcp_notebooklm_research_status({
  notebook_id: "your-notebook-id",
  task_id: "research-task-id",
  poll_interval: 30,  // 秒
  max_wait: 300,      // 最大等待时间(秒)
  compact: true
})
// 自动等待完成并返回结果
```

#### 导入研究结果
```javascript
mcp_notebooklm_research_import({
  notebook_id: "your-notebook-id",
  task_id: "research-task-id",
  source_indices: [0, 1, 2, 3, 4]  // 导入哪些源,默认全部
})
```

#### 查询研究结果
```javascript
// 研究完成后,可以基于新发现的源进行查询
mcp_notebooklm_notebook_query({
  notebook_id: "your-notebook-id",
  query: "总结量子计算在机器学习中的三个主要应用场景"
})
```

---

## Obsidian 集成工作流

### 工作流 1: 笔记增强

**场景**: 为重要笔记生成多模态学习材料

```bash
# 1. 在 Obsidian 中标记重要笔记
# 添加标签: #Type/Keynote #Status/ReadyForEnhancement

# 2. 使用 Claude Code + MCP 自动处理
# 将笔记添加到 NotebookLM
notebooklm_add_text(obsidian_note_content)

# 3. 生成学习套件
notebooklm_generate_flashcards()
notebooklm_generate_quiz()
notebooklm_generate_mind_map()

# 4. 将生成的内容链接回 Obsidian
![[NotebookLM-输出-笔记名称]]
```

### 工作流 2: 深度研究

**场景**: 为新主题快速建立知识库

```bash
# 1. 在 Obsidian 创建主题笔记
# 例如: "2.Topics/01.技术栈/RAG技术.md"

# 2. 启动 NotebookLM 深度研究
notebooklm_research_deep("RAG技术在企业中的应用", mode="deep")

# 3. 等待研究完成(~5分钟)
# NotebookLM 自动搜索并整理 40+ 相关资源

# 4. 审查并导入最佳资源
notebooklm_research_import(select_best_sources)

# 5. 生成研究报告
notebooklm_generate_report("Study Guide")

# 6. 将报告和关键发现链接回 Obsidian
```

### 工作流 3: 音频学习

**场景**: 将文字笔记转换为音频进行通勤学习

```bash
# 1. 收集相关笔记到 NotebookLM
# 例如: 一周的学习笔记

# 2. 生成音频概述
notebooklm_audio_overview_create(
  format="deep_dive",
  length="long",
  language="zh-CN"
)

# 3. 轮询生成状态
notebooklm_studio_status()

# 4. 下载音频文件
# 保存到: 3.Resources/Audio/主题名称.mp3

# 5. 在 Obsidian 中创建音频笔记
# ![[音频文件]] + 关键摘要
```

---

## 使用场景

### 场景 1: 技术学习

**目标**: 深度学习一个新技术栈

**步骤**:
1. **收集资料**: 将官方文档、博客、教程添加到 NotebookLM
2. **生成学习材料**:
   - 学习指南 (Study Guide)
   - 测验 (Quiz) 检验理解
   - 闪卡 (Flashcards) 记忆关键概念
3. **深度问答**: 针对不懂的点进行多轮对话
4. **音频复习**: 生成音频概述在通勤时复习

**预期收益**:
- 将被动阅读转为主动学习
- 通过测验和闪卡巩固记忆
- 多模态学习提升理解深度

---

### 场景 2: 研究项目

**目标**: 快速了解一个研究领域的前沿

**步骤**:
1. **启动深度研究**: 使用 `research_start` 自动搜索相关论文和资源
2. **AI 摘要**: 生成笔记本摘要并获取推荐话题
3. **定向查询**: 针对具体问题进行深度问答
4. **生成报告**: 创建学习指南或简报文档
5. **可视化**: 生成思维导图梳理知识结构

**预期收益**:
- 节省 80% 文献筛选时间
- AI 自动识别关键概念和关联
- 快速建立领域知识图谱

---

### 场景 3: 内容创作

**目标**: 为视频/博客/演讲准备素材

**步骤**:
1. **收集素材**: 添加相关资料到 NotebookLM
2. **多角度分析**: 通过 critique 和 debate 格式获取不同视角
3. **生成大纲**: 使用 report 创建结构化内容
4. **制作幻灯片**: 基于 report 生成演示文稿
5. **生成脚本**: 使用 audio_overview 作为参考脚本

**预期收益**:
- 快速生成多个版本的内容
- AI 提供不同视角和论点
- 自动适配不同输出格式

---

## 最佳实践

### 1. 笔记组织

**按主题分笔记本**:
- 每个项目/主题一个独立笔记本
- 例如: "LLM原理"、"RAG实战"、"Prompt工程"

**源文件管理**:
- 定期同步 Drive 源保持最新
- 删除过时源避免混淆
- 使用有意义的标题

### 2. 查询技巧

**有效提问**:
- ❌ "告诉我关于 X"
- ✅ "解释 X 的原理,并与 Y 进行比较"

**多轮对话**:
- 使用 `conversation_id` 继续对话
- 逐步深入探索主题

**限制源范围**:
- 使用 `source_ids` 限定查询范围
- 提高回答相关性

### 3. 内容生成

**选择合适的格式**:
- **学习**: Study Guide + Quiz + Flashcards
- **研究**: Briefing Doc + Mind Map
- **创作**: Blog Post + Slide Deck
- **复习**: Audio Overview + Deep Dive

**语言和风格**:
- 使用 `focus_prompt` 定制输出
- 调整 `response_length` 控制详细程度
- 选择合适的 `visual_style`

### 4. 深度研究

**研究策略**:
- **快速探索**: `mode: "fast"` (~30s, ~10 sources)
- **深度调研**: `mode: "deep"` (~5min, ~40 sources)

**源选择**:
- 审查自动发现的源
- 只导入高质量的源
- 使用 `source_indices` 精确控制

---

## 批量导入脚本

### Python 脚本: 批量导入 Obsidian 笔记

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量导入 Obsidian 笔记到 NotebookLM

使用方法:
1. 配置 notebook_id 和 target_dir
2. 运行: python import_to_notebooklm.py
"""

import os
import sys
from pathlib import Path
from typing import List

# 模拟 MCP 调用 (实际使用时替换为真实 MCP)
def notebooklm_add_text(notebook_id: str, text: str, title: str):
    """添加文本到 NotebookLM"""
    print(f"添加到 NotebookLM: {title}")
    print(f"内容长度: {len(text)} 字符")
    # 实际调用: mcp_notebooklm_notebook_add_text(...)
    return True

def find_markdown_files(target_dir: str, limit: int = 10) -> List[Path]:
    """查找要导入的 Markdown 文件"""
    import re

    # 选择标准: 高评分笔记 或 重要标签
    patterns = [
        r"rating:\s*[4-5]\.0",  # 高评分
        r"#Type/Keynote",       # 重要笔记
        r"#Status/Mastered"     # 已掌握内容
    ]

    files = []
    for md_file in Path(target_dir).rglob("*.md"):
        # 检查文件是否符合标准
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if any(re.search(pattern, content) for pattern in patterns):
                files.append(md_file)
                if len(files) >= limit:
                    break

    return files

def extract_note_content(md_file: Path) -> tuple[str, str]:
    """提取笔记内容"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 移除 YAML frontmatter (NotebookLM 不需要)
    lines = content.split('\n')
    if lines[0].strip() == '---':
        try:
            end_idx = lines.index('---', 1)
            content = '\n'.join(lines[end_idx+1:])
        except ValueError:
            pass

    # 提取标题
    title = md_file.stem
    first_line = content.strip().split('\n')[0]
    if first_line.startswith('#'):
        title = first_line.lstrip('#').strip()

    return title, content

def main():
    # 配置
    notebook_id = "your-notebook-id"  # 替换为实际的 notebook_id
    target_dir = "2.Topics/01.技术栈"  # 要导入的目录
    limit = 10  # 最多导入数量

    print(f"开始扫描目录: {target_dir}")
    files = find_markdown_files(target_dir, limit)
    print(f"找到 {len(files)} 个符合条件的文件")

    success_count = 0
    for md_file in files:
        try:
            title, content = extract_note_content(md_file)
            if notebooklm_add_text(notebook_id, content, title):
                success_count += 1
                print(f"✅ 成功: {title}")
        except Exception as e:
            print(f"❌ 失败: {md_file.name} - {e}")

    print(f"\n导入完成: {success_count}/{len(files)} 成功")

if __name__ == "__main__":
    main()
```

---

## NotebookLM 内容归档流程

### 定期归档

**每月执行**:
1. 导出 NotebookLM 生成的学习材料
2. 保存到 Obsidian 对应目录:
   - `3.Resources/NotebookLM/音频/`
   - `3.Resources/NotebookLM/测验/`
   - `3.Resources/NotebookLM/思维导图/`
3. 创建索引笔记链接所有生成内容
4. 更新原始笔记的元数据

### 版本控制

**建议**:
- 保留 NotebookLM notebook ID 在 Obsidian 笔记的元数据中
```yaml
---
notebooklm_id: "abc123"
notebooklm_sources: ["source1", "source2"]
notebooklm_generated: ["quiz", "flashcards", "audio"]
---
```

---

## 故障排除

### 常见问题

**Q: MCP 工具无法连接**
- A: 检查 notebooklm-mcp-auth 认证状态,运行 `notebooklm-mcp-auth`

**Q: 音频/视频生成失败**
- A: 确认 source_ids 有效,源文件不为空,网络连接正常

**Q: 深度研究超时**
- A: 使用 `mode: "fast"` 进行快速探索,或增加 `max_wait` 时间

**Q: 中文输出质量不佳**
- A: 在 `focus_prompt` 中明确要求使用中文,提供示例

---

## 相关资源

### 官方文档
- [NotebookLM 官网](https://notebooklm.google.com/)
- [NotebookLM MCP GitHub](https://github.com/originalsega/notebooklm-mcp)

### 知识库集成
- [3.Resources/信源列表/可供 NotebookLM 使用的信息源网址列表.md](../../3.Resources/信源列表/可供%20NotebookLM%20使用的信息源网址列表.md)
- [0.DailyNotes/2026-01-26-将notebooklm-mcp整合进工具箱.md](../../0.DailyNotes/2026-01-26-将notebooklm-mcp整合进工具箱.md)

### 相关工具
- Obsidian 插件: Smart Connections
- AI 工具: Claude Code, ChatGPT
- 笔记工具: Heptabase, Tana

---

**创建者**: Claude Sonnet 4.5
**最后更新**: 2026-01-26
**下次审查**: 2026-02-26
