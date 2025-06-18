---

kanban-plugin: board

---

## ROADMAP

- [ ] 精通 LangGraph 节点模型与边逻辑设计（8h | ★★★★★）
- [ ] 完成第一个 Prompt 原型并集成 LangGraph 调用链（6h | ★★★★★）【依赖：掌握节点模型】
- [ ] 学习 Dify 流程控制模型与插件系统（5h | ★★★★☆）
- [ ] 构建自定义 Flow 并接入持久化存储（8h | ★★★★★）【依赖：Dify 插件机制】
- [ ] 掌握异步 Agent Flow 架构与条件跳转（8h | ★★★★☆）【依赖：LangGraph 核心掌握】
- [ ] 撰写验证报告并做 prompt 迭代归档（3h | ★★★★☆）【依赖：原型完成】


## TODO

- [ ] 分析 LangGraph 的 async 节点控制与恢复机制（4h | ★★★★☆）
- [ ] 设计基于 LangGraph 的嵌套 Prompt 流程图（4h | ★★★★★）
- [ ] 学习 Dify 的 API Proxy & 插件开发流程（5h | ★★★★☆）
- [ ] 测试 LangGraph + Dify 联合流程部署（5h | ★★★★☆）【依赖：两者核心掌握】


## DOING

- [ ] 精读 LangGraph 官方文档与案例（4h | ★★★★★）
- [ ] 开发 LangGraph 中条件跳转逻辑（5h | ★★★★★）
- [ ] 搭建异步 Agent Flow 控制组件（4h | ★★★★☆）【依赖：节点模型 + async 理解】
- [ ] 编写原型验证报告结构草稿（2h | ★★★☆☆）


## RESOURCES

- [ ] [[LangGraph Docs]] - 节点、边、异步分支
- [ ] [[Dify 插件系统概览笔记]]（内含快速启动模板）
- [ ] [[Prompt Engineering 模块化模板库]]
- [ ] [[Agent Architecture 思维导图]]
- [ ] [[嵌套 Flow 实验记录]]


## ARCHIVE

- [x] 设计原型 prompt 流程 + 链式思维模板（3h | ★★★★★） ✅ 2025-06-18
- [x] 比较 LangChain、LangGraph 适配架构（已总结）
- [x] 创建 langgraph-dify 联合实验 repo 并初步部署（已 GitHub 推送）
- [x] 快速复现 Dify 项目模板与 vector store 接入脚本（已验证）


## 🧠 使用建议：

- [ ] 可以每周 Sprint 回顾时把 `ROADMAP` 中项目推入 `TODO`；
- [x] `RESOURCES` 中挂实际链接或 `[[内部笔记]]`； ✅ 2025-06-18
- [x] `ARCHIVE` 支持收录版本发布、实验完成的子任务； ✅ 2025-06-18
- [x] 使用 `Templater` 可自动打标签和日期，更易追踪每项工作。 ✅ 2025-06-18




%% kanban:settings
```
{"kanban-plugin":"board","show-checkboxes":true,"show-relative-date":true,"link-date-to-daily-note":false,"date-colors":[{"isToday":false,"distance":1,"unit":"days","direction":"after"}]}
```
%%