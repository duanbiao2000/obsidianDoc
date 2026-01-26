当然可以！下面我将对你提供的 `agent.md`（来自 oh-my-opencode 项目中的 agents 目录）进行详细分析和讲解。

---

## 一、整体结构与目的

这份文档描述了一个由 10 个 AI agent 组成的“多模型协作系统”，每个 agent 都有明确的角色、模型偏好、工具权限和分工。整体设计思想是模拟一个高效的“AI 团队”，通过分工协作来完成复杂的任务，同时通过工具限制和角色分离提升安全性和质量。

---

## 二、目录结构解析

```
agents/
 ├── atlas.ts                # 主协调者
 ├── sisyphus.ts             # 主执行者（核心推动力）
 ├── sisyphus-junior.ts      # 子任务执行者（按类别动态生成）
 ├── oracle.ts               # 策略性顾问
 ├── librarian.ts            # 研究员/文档检索专家
 ├── explore.ts              # 快速上下文搜索者
 ├── multimodal-looker.ts    # 多模态媒体分析者
 ├── prometheus-prompt.ts    # 规划者/面试/顾问模式
 ├── metis.ts                # 预规划分析者
 ├── momus.ts                # 计划审核者（严苛检查）
 ├── dynamic-agent-prompt-builder.ts # 动态提示词生成器
 ├── types.ts                # 通用类型定义
 ├── utils.ts                # 工具函数和帮助方法
 └── index.ts                # 导出所有内置 agent
```

每个文件/agent 负责不同环节的任务，整体呈现出“分治合作”和“分权治理”的组织结构。

---

## 三、各个 agent 的职责与分配

| Agent            | 主要职责                                    | 用的模型                   | 热度(Temp) | 特殊限制                |
|------------------|--------------------------------------------|---------------------------|------------|------------------------|
| **atlas**        | 主协调者（todo 列表管理，全局调度）         | claude-opus-4-5           | 0.1        |                        |
| **sisyphus**     | 主推动者（核心任务执行，SF Bay Area 工程师角色） | claude-opus-4-5           | 0.1        |                        |
| **sisyphus-junior** | 子任务执行者（按类别动态生成）             | claude-sonnet-4-5         | 0.1        | 不能直接 task/delegate_task |
| **oracle**       | 策略性顾问（复杂问题分析、调试）            | gpt-5.2                   | 0.1        | 不能写、编辑、任务分派 |
| **librarian**    | 文档和代码检索专家（GitHub、Context7）       | big-pickle                | 0.1        | 不能写、编辑、任务分派、不能调用其他 agent |
| **explore**      | 快速上下文搜索（Grok Code 风格）            | gpt-5-nano                | 0.1        | 同 librarian           |
| **multimodal-looker** | 多模态媒体分析（图片/文档等）          | gemini-3-flash           | 0.1        | 只读，不能写            |
| **prometheus**   | 规划者（面试、咨询、长期规划）             | claude-opus-4-5           | 0.1        | 只做规划，不写代码     |
| **metis**        | 预规划分析（检测空白/风险）                | claude-sonnet-4-5         | 0.3        |                        |
| **momus**        | 计划审核者（严格批评和纠错）                | claude-sonnet-4-5         | 0.1        |                        |

- **Temp**：是模型采样温度，0.1 通常是低温（更确定性），0.3 更具探索性。
- **工具限制**：比如 oracle 不能写东西，librarian 不能执行任务，multimodal-looker 只读，prometheus 只做规划不写代码，sisyphus-junior 不能直接 task/delegate_task，防止权限滥用和污染。

---

## 四、扩展新 agent 的流程

1. 新建 `src/agents/my-agent.ts`，实现 agent 工厂和元数据。
2. 在 `src/agents/utils.ts` 的 `agentSources` 注册。
3. 更新 `src/config/schema.ts` 里的 `AgentNameSchema`，让系统能识别新 agent。
4. 在 `src/index.ts` 初始化注册进全局。

---

## 五、工具限制与安全设计

- 通过 `createAgentToolRestrictions` 或 `createAgentToolAllowlist` 实现白名单/黑名单式工具控制。
- 例如 oracle 不可写、不可分派任务，librarian 也不能写、不能调用其他 agent，防止意外操作。
- multimodal-looker 只读，保证不会修改媒体内容。
- prometheus 只做规划，不写代码，避免自动执行风险。
- “不相信报告”原则：即使 agent 报告“完成”，也要有上层验证，防止自动化欺骗。

---

## 六、设计模式与最佳实践

- **分工协作**：每个 agent 有明确职责，实现模块化。
- **动态生成子任务**：sisyphus-junior 可按类别动态生成，支持灵活扩展。
- **动态提示词构建**：有专门的 agent 用于生成高质量的提示词。
- **工具隔离**：通过权限分离和工具限制，提升系统安全和可控。
- **多模型兼容**：不同任务选用最合适的大模型。
- **防御式工程**：强调“不相信任何 agent 的自我报告”，强制多重验证。

---

## 七、agent 之间的协作流程举例

假设要完成一个复杂开发任务：

1. **atlas**（协调者）收集 todo 列表。
2. **sisyphus**（主推进者）解析任务，决定调度方向。
3. **metis** 做预分析，检测潜在风险/空白。
4. **prometheus** 做长期规划，拆解为若干子任务。
5. **momus** 严格审核计划，指出逻辑漏洞。
6. **librarian** 搜索相关文档和代码库。
7. **explore** 快速在上下文中搜索关键信息。
8. **multimodal-looker** 分析涉及图片/文档等多媒体资料。
9. **sisyphus-junior** 负责具体的子任务执行（如生成代码、测试、格式化等）。
10. **oracle** 可以被调用做复杂调试或咨询。
11. 每一步结果都有上层 agent（如 atlas/sisyphus）做验证和接力。

---

## 八、总结与设计精髓

这套 agent 设计的核心理念是“分权、分工、分模型、分验证”，借鉴了企业组织管理的分工原则，但用 AI agent 实现自动化协作。通过明确角色、限制权限、强化验证、支持动态扩展，实现高效、可控、可维护的复杂任务自动化流程。

---

### 如果你有具体某一部分想深入了解，比如 agent 之间的通信机制、prompt 构建方式、工具限制实现细节等，可以继续追问！