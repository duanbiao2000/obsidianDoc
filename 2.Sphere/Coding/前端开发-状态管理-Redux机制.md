---
aliases:
  - React-Redux
source: 
author: 
date: 
update: 
categories: 
important: false
tags:
  - Domain/Productivity/Tools
---
Redux 是一个可预测的状态管理工具，用于集中管理应用的状态。其核心思想是通过单向数据流更新状态：
1.  **状态 (State)**：应用的单一真实数据源。
2.  **动作 (Action)**：描述“发生了什么”的普通对象。
3.  **Reducer**：纯函数，根据当前状态和动作计算并返回新状态。
4.  **Store**：保存状态、接收动作、执行 Reducer 并通知订阅者。

**流程**：组件发出 Action -> Store 收到 Action -> Reducer 更新 State -> Store 通知订阅者 -> 组件更新。

**React-Redux** 提供连接 React 组件和 Redux Store 的工具（如 `useSelector`, `useDispatch`）。**Redux Toolkit** 简化了 Redux 开发（如 `configureStore`, `createSlice`）。
