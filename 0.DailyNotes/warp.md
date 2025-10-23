# Warp 项目配置

## 项目概述

**obsidianDoc-CS** 是一个 Obsidian 知识库项目，专注于计算机科学学习、面试准备和技术文档的组织与管理。

- **项目类型**: 知识管理系统（Obsidian Vault）
- **主要语言**: Markdown
- **目标受众**: CS 学生、求职者、技术面试准备者

## 项目结构

```
obsidianDoc-CS/
├── 0.DailyNotes/          # 日常笔记和想法
├── 1.Projects/            # 项目相关文档
├── 2.Sphere/              # 知识领域（技能点、概念）
├── 3.Resources/           # 学习资源和参考资料
├── 4.Archives/            # 归档的历史文档
├── 5.Misc/                # 杂项和待整理内容
├── Atlas/                 # 知识图谱和关系映射
├── BASE/                  # 基础知识库
├── Clippings/             # 摘录和引用
├── Extras/                # 额外资源
└── [核心文档]
    ├── AI_Agent_Framework_Interview_Questions.md
    ├── 面试官考察指南-2030核心技能.md
    ├── 系统架构典型场景.md
    ├── Java动态代理.md
    ├── Rust模块系统深度解析.md
    └── 其他专题文档
```

## 核心工作流程

### 1. 内容创建和管理
- 在 `1.Projects` 中组织项目相关的学习内容
- 在 `2.Sphere` 中维护知识点库
- 在 `3.Resources` 中收集学习资源
- 在 `0.DailyNotes` 中记录日常想法和进度

### 2. 知识整理
- 在 `Atlas` 中建立知识关系和思维导图
- 在 `BASE` 中维护基础知识体系
- 使用 Obsidian 的反向链接功能建立内容关联

### 3. 面试准备
- 参考 `面试官考察指南-2030核心技能.md` 了解核心考察点
- 查阅 `系统架构典型场景.md` 学习架构设计
- 研究框架性面试题（如 `AI_Agent_Framework_Interview_Questions.md`）
- 深入学习专题知识（Java、Rust 等）

## 快速命令

### Git 操作
```bash
# 查看项目状态
git status

# 提交更改
git add .
git commit -m "更新内容"

# 推送到远程
git push origin main
```

### 内容搜索
```bash
# 搜索特定关键词
grep -r "关键词" .

# 列出所有 Markdown 文件
Get-ChildItem -Recurse -Filter "*.md"
```

### Obsidian 相关
- 启用核心插件：Graph view、Backlinks、Outgoing links
- 推荐插件：Dataview、Smart Connections、Advanced URI

## 重要文件说明

| 文件 | 用途 |
|------|------|
| `_Index_of_obsidianDoc-CS.md` | 自动生成的文档索引 |
| `面试官考察指南-2030核心技能.md` | 面试核心技能指南 |
| `系统架构典型场景.md` | 系统设计典型场景 |
| `AI_Agent_Framework_Interview_Questions.md` | AI Agent 框架面试题 |
| `Java动态代理.md` | Java 深度专题 |
| `Rust模块系统深度解析.md` | Rust 深度专题 |

## 版本控制

- **VCS**: Git
- **忽略规则**: 参考 `.gitignore`
- **主要忽略项**:
  - `.obsidian/` - Obsidian 配置文件
  - `.vscode/` - VSCode 配置
  - `.idea/` - IntelliJ IDEA 配置
  - `.smart-connections/` - 插件数据
  - `_Index_of_*.md` - 自动生成的索引

## 开发建议

### 📋 内容管理规范

1. **文件命名约定**
   - 使用描述性中文名称，避免特殊字符
   - 避免使用日期作为主要标识符（使用标签替代）

2. **定期整理与清理** (周期：每周)
   - 每周检查 `5.Misc` 中的待整理内容
   - 将已完成的文档从 `0.DailyNotes` 移至相应分类
   - 检查孤立笔记（使用 Obsidian Graph view 识别）
   - 定期归档陈旧内容到 `4.Archives`
   - 删除重复和过时的知识点

3. **内容链接建立**
   - 使用 Obsidian 的 `[[笔记名]]` 语法建立双向链接
   - 每个主要概念应该至少有 2-3 个相关链接
   - 在 `Atlas` 中维护知识点的核心关系图
   - 使用别名链接保持一致性: `[[真实名称|显示名称]]`
   - 避免过度链接（超过 10 个链接的笔记需要重构）

4. **标签体系** (分层标签)
   - **学习阶段**: `#learning/初级`, `#learning/中级`, `#learning/深入`
   - **内容类型**: `#interview/题目`, `#interview/经验`, `#project/实践`, `#concept/基础`
   - **技术栈**: `#tech/java`, `#tech/rust`, `#tech/system-design`
   - **优先级**: `#priority/high`, `#priority/medium`, `#priority/low`
   - **状态**: `#status/draft`, `#status/review`, `#status/complete`
   - 示例标签使用: `#interview/题目 #tech/system-design #priority/high`

### 🔄 版本管理与备份

5. **Git 提交规范**
   - **提交频率**: 每次完成一个知识点或修复一个问题时提交
   - **提交信息格式**: 
     ```
     类型(范围): 描述
     
     例: feat(interview): 添加系统设计面试题集
         fix(java): 修正动态代理章节错误
         docs(base): 更新基础知识索引
     ```
   - 类型: `feat` (新增), `fix` (修复), `docs` (文档), `refactor` (重构), `chore` (维护)
   - 避免大量文件同时提交，按逻辑分组提交

6. **备份与同步策略**
   - **本地提交**: 每天工作前后各提交一次
   - **远程推送**: 每周至少推送一次，重要内容实时推送
   - **OneDrive 同步**: 保证项目在 OneDrive 中持续同步
   - **冲突处理**: 团队协作时使用分支，避免直接冲突
   - 定期验证: `git log --oneline | head -10` 查看最近提交

### 🎯 知识体系维护

7. **定期知识回顾** (周期：每月)
   - 每月回顾一次 `Atlas` 中的知识关系图
   - 根据 Dataview 统计新增文档数量和修改频率
   - 识别知识盲点并补充相关资料
   - 更新 `面试官考察指南-2030核心技能.md` 的优先级排序

8. **核心文档维护** (周期：每月)
   - 更新 `系统架构典型场景.md` 中的最新案例
   - 补充 `AI_Agent_Framework_Interview_Questions.md` 的新框架问题
   - 完善专题文档（Java、Rust 等）的深度分析
   - 检查所有链接的有效性

### 🛠️ Obsidian 工具优化

9. **插件与功能配置**
   - **核心插件**
     - Graph view: 定期检查知识图谱的连通性
     - Backlinks: 确保被链接次数高的文档保持高质量
     - Outgoing links: 审查每个文档的出站链接质量
   - **推荐插件配置**
     - Dataview: 创建自动分类视图（按标签、创建日期、修改日期）
     - Smart Connections: 发现隐藏的知识关联
     - Calendar: 追踪学习进度
     - Periodic Notes: 自动生成日周月复习计划
     - Advanced URI: 快速导航和自动化工作流

10. **工作流自动化**
    - 为常用文件夹创建模板（template 文件夹）
    - 使用快捷键绑定常用操作
    - 定义日记模板包含学习目标、进度反思
    - 创建每月复习清单模板

### 📊 质量控制与反思

11. **内容质量检查表** (提交前)
    - ✅ 文件名清晰，遵循命名约定
    - ✅ 至少包含 2 个内部链接到相关笔记
    - ✅ 添加了适当的标签（至少 2-3 个）
    - ✅ 内容有明确的开始和结束，逻辑清晰
    - ✅ 没有拼写或语法错误
    - ✅ 代码示例（如有）正确且有注释
    - ✅ 引用了来源或参考资料

12. **定期反思与优化** (周期：每季度)
    - 评估学习效率：查看标记完成的面试题覆盖率
    - 识别薄弱领域：通过标签统计找出低覆盖率的技术栈
    - 优化知识结构：重新组织 `2.Sphere` 中的分类
    - 补充资源缺口：更新 `3.Resources` 中的学习资源
    - 记录改进建议到 `0.DailyNotes` 中的反思笔记

### 🚀 面试准备特别指南

13. **面试冲刺计划**
    - 在 `1.Projects` 中创建 `面试冲刺-[公司/轮次].md`
    - 使用 Dataview 筛选 `#priority/high` 的题目
    - 按 `#tech/*` 标签重点复习的技术栈
    - 定期做模拟面试笔记，记录回答改进点

14. **经验积累**
    - 面试后立即记录经验到 `0.DailyNotes`
    - 整理出被提问的题目到相应的 `#interview/题目` 集
    - 分析高频提问类型，集中补强
    - 建立个人的 "面试高频题库" 文档

### ⚠️ 常见问题与预防

15. **问题预防清单**
    - **链接断裂**: 重命名文件前搜索反向链接
    - **重复内容**: 使用 Dataview 检查相似标题
    - **知识孤立**: 定期查看 Graph view，寻找孤立节点
    - **过期信息**: 为技术类文档标记更新日期
    - **版本冲突**: 只在一个设备上编辑，编辑完全同步后再在其他设备打开

---

### 执行计划示例

**每日**: 10 分钟复习一个 `#priority/high` 的笔记  
**每周**: 整理 `5.Misc`，提交一次 Git  
**每月**: 回顾知识体系，更新核心文档  
**每季度**: 完整反思，优化知识结构

## 联系与支持

此项目为个人学习和面试准备工具，如有改进建议或新增内容需求，在本地编辑后提交。
