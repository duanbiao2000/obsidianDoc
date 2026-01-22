---
tags:
  - AI-Agent-Development
  - Structured-Skill-Repository
  - Skills
  - Superpowers
  - 代码质量
  - 调试
created: 2026-01-22T00:00:00.000Z
type: analysis
---

# Superpowers技能系统分析报告

> 分析日期：2026-01-22
> 位置：`.agent/superpowers/skills/`

---

## 📋 目录索引

- [概述](#概述)
- [技能分类体系](#技能分类体系)
  - [流程管理技能](#1-流程管理-5个)
  - [代码质量技能](#2-代码质量-5个)
  - [工作空间管理](#3-工作空间管理-1个)
  - [技能元技能](#4-技能元技能-2个)
  - [并行处理](#5-并行处理-1个)
- [核心设计原则](#核心设计原则)
- [技能依赖关系](#技能依赖关系)
- [使用场景映射](#使用场景映射)

---

## 概述

Superpowers技能系统是一个为AI代理设计的**结构化技能库**，包含14个技能，覆盖从任务规划、编码执行、质量保证到工作流管理的完整开发生命周期。

### 核心特点

| 特性 | 说明 |
|------|------|
| **标准化结构** | 所有技能采用YAML frontmatter + Markdown格式 |
| **纪律性导向** | 强调TDD、系统性调试、验证优先等工程纪律 |
| **流程可视化** | 大量使用GraphViz流程图展示决策点 |
| **反合理化设计** | 明确禁止常见借口和捷径 |
| **测试驱动** | 技能创建遵循TDD原则（RED-GREEN-REFACTOR） |

---

## 技能分类体系

### 1. 流程管理 (5个)

| 技能名称 | 文件路径 | 核心作用 |
|---------|---------|---------|
| **brainstorming** | `brainstorming/SKILL.md` | 创造性工作前的头脑风暴，将想法转化为设计和规格 |
| **writing-plans** | `writing-plans/SKILL.md` | 为多步任务编写详细实施计划（ bite-sized tasks） |
| **executing-plans** | `executing-plans/SKILL.md` | 在单独会话中批量执行实施计划 |
| **finishing-a-development-branch** | `finishing-a-development-branch/SKILL.md` | 完成开发分支并提供4种集成选项 |
| **subagent-driven-development** | `subagent-driven-development/SKILL.md` | 当前会话中通过子代理执行独立任务（双阶段审查） |

---

### 2. 代码质量 (5个)

| 技能名称 | 文件路径 | 核心作用 |
|---------|---------|---------|
| **test-driven-development** | `test-driven-development/SKILL.md` | TDD流程：红（失败测试）→绿（最小代码）→重构 |
| **systematic-debugging** | `systematic-debugging/SKILL.md` | 系统性调试4阶段：根因→模式→假设→实现 |
| **verification-before-completion** | `verification-before-completion/SKILL.md` | 完成前验证（证据先于断言） |
| **requesting-code-review** | `requesting-code-review/SKILL.md` | 请求代码审查（使用code-reviewer子代理） |
| **receiving-code-review** | `receiving-code-review/SKILL.md` | 接收代码审查反馈（技术评估优先于社会表现） |

---

### 3. 工作空间管理 (1个)

| 技能名称 | 文件路径 | 核心作用 |
|---------|---------|---------|
| **using-git-worktrees** | `using-git-worktrees/SKILL.md` | 创建隔离的git工作树（智能目录选择+安全验证） |

**目录选择优先级：**
1. 现有目录（`.worktrees/` 或 `worktrees/`）
2. CLAUDE.md中的配置
3. 询问用户（本地 `.worktrees/` vs 全局 `~/.config/superpowers/worktrees/`）

---

### 4. 技能元技能 (2个)

| 技能名称 | 文件路径 | 核心作用 |
|---------|---------|---------|
| **using-superpowers** | `using-superpowers/SKILL.md` | 技能查找和使用规则（1%概率=必须调用） |
| **writing-skills** | `writing-skills/SKILL.md` | 创建/编辑新技能（TDD应用于文档） |

**核心规则：**
```
IF 1% chance skill applies → MUST invoke Skill tool
NO exceptions. This is not optional.
```

---

### 5. 并行处理 (1个)

| 技能名称 | 文件路径 | 核心作用 |
|---------|---------|---------|
| **dispatching-parallel-agents** | `dispatching-parallel-agents/SKILL.md` | 面对独立问题时并行调度多个代理 |

**使用条件：**
- 2+ 独立任务
- 无共享状态
- 无顺序依赖

---

## 核心设计原则

### 1. 纪律性设计

| 原则 | 体现技能 | 具体要求 |
|------|---------|---------|
| **测试优先** | TDD | "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST" |
| **根因优先** | 系统性调试 | "NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST" |
| **验证优先** | 完成前验证 | "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE" |
| **技能优先** | using-superpowers | "IF A SKILL APPLIES, YOU DO NOT HAVE A CHOICE" |

### 2. 反合理化机制

所有纪律性技能都包含：

- **"精神与字面"条款** - "Violating the letter is violating the spirit"
- **明确禁止列表** - "No exceptions: [具体借口列表]"
- **红旗警告** - 常见合理化思维的识别清单
- **借口vs现实对照表** - 直接反驳常见借口

### 3. 结构化文档格式

```yaml
---
name: skill-name-with-hyphens
description: Use when [specific triggering conditions]
---
# Skill Name
## Overview
## When to Use (with flowchart)
## Quick Reference
## Implementation
## Common Mistakes
## Real-World Impact
```

---

## 技能依赖关系

### 典型开发流程

```
brainstorming (设计阶段)
    ↓
writing-plans (编写计划)
    ↓
using-git-worktrees (创建工作树)
    ↓
┌─────────────────────────────────────┐
│  执行阶段（二选一）：                │
│  • subagent-driven-development     │
│    (当前会话 + 双阶段审查)           │
│  • executing-plans                 │
│    (单独会话 + 批量执行)             │
└─────────────────────────────────────┘
    ↓
finishing-a-development-branch (完成与集成)
```

### 双阶段审查流程（subagent-driven-development）

```
实现子代理
    ↓ (self-review)
规范审查子代理 (spec-reviewer)
    ↓ (如有问题，修复后重新审查)
代码质量审查子代理 (code-quality-reviewer)
    ↓ (如有问题，修复后重新审查)
任务完成 → 下一个任务
```

---

## 使用场景映射

### 场景1：新功能开发

1. **brainstorming** - 与用户讨论需求和设计
2. **writing-plans** - 编写详细实施计划
3. **using-git-worktrees** - 创建隔离工作区
4. **subagent-driven-development** 或 **executing-plans** - 执行计划
5. **finishing-a-development-branch** - 集成到主分支

**贯穿始终：**
- TDD（每个功能）
- requesting-code-review（每个任务后）
- verification-before-completion（每次声称完成前）

### 场景2：修复Bug

1. **systematic-debugging** - 找到根因（4阶段）
2. **TDD** - 编写失败测试重现bug
3. 实现（红-绿-重构）
4. **verification-before-completion** - 验证修复有效

### 场景3：并发问题

1. **dispatching-parallel-agents** - 识别独立问题域
2. 为每个域启动独立代理
3. 整合所有修复
4. **verification-before-completion** - 全套测试

---

## 技能统计

| 分类 | 数量 | 占比 |
|------|------|------|
| 流程管理 | 5 | 35.7% |
| 代码质量 | 5 | 35.7% |
| 工作空间管理 | 1 | 7.1% |
| 技能元技能 | 2 | 14.3% |
| 并行处理 | 1 | 7.1% |
| **总计** | **14** | **100%** |

---

## 文件大小分析

| 技能 | 行数 | 复杂度 |
|------|------|--------|
| writing-skills | 656 | ★★★★★ |
| systematic-debugging | 297 | ★★★★☆ |
| test-driven-development | 372 | ★★★★☆ |
| subagent-driven-development | 241 | ★★★★☆ |
| receiving-code-review | 214 | ★★★☆☆ |
| using-git-worktrees | 218 | ★★★☆☆ |
| brainstorming | 55 | ★★☆☆☆ |
| writing-plans | 117 | ★★★☆☆ |
| executing-plans | 77 | ★★☆☆☆ |
| finishing-a-development-branch | 201 | ★★★☆☆ |
| dispatching-parallel-agents | 181 | ★★★☆☆ |
| using-superpowers | 88 | ★★☆☆☆ |
| verification-before-completion | 140 | ★★★☆☆ |
| requesting-code-review | 106 | ★★☆☆☆ |

---

## 关键洞察

### 1. 纪律性 > 灵活性

技能系统不惜增加文档长度，也要堵住所有可能的合理化借口。每个纪律性技能都包含：
- "Iron Law"（铁律）
- 违反行为的明确禁止
- 借口 vs 现实对照表

### 2. 测试驱动哲学

不仅代码需要TDD，**技能创建本身也遵循TDD**：
- RED：运行压力场景（无技能时的基线行为）
- GREEN：编写技能解决问题
- REFACTOR：堵住新发现的合理化漏洞

### 3. 双阶段审查机制

`subagent-driven-development`引入了独特的双阶段审查：
1. **规范审查** - 代码是否满足需求？（不多不少）
2. **代码质量审查** - 实现是否良好？（可维护、无缺陷）

这防止了"过度工程"和"偷工减料"两种极端。

### 4. Claude搜索优化（CSO）

技能的`description`字段专门为搜索引擎优化：
- ✅ "Use when [触发条件]"
- ❌ "Use when [流程总结]"（会导致Claude只读描述跳过正文）
- ✅ 包含关键词：错误消息、症状、工具名

---

## 相关链接

- **技能目录**：`.agent/superpowers/skills/`
- **测试示例**：`.agent/superpowers/skills/writing-skills/examples/`
- **GraphViz约定**：`.agent/superpowers/skills/writing-skills/graphviz-conventions.dot`

---

*报告生成时间：2026-01-22*
*技能版本：基于最新SKILL.md文件*
