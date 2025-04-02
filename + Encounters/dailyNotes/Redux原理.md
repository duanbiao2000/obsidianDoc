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
  - Effective/Tools
---


**核心概念与简化：**

1.  **Redux核心思想：**
    *   **本质：** Redux 是一个状态管理工具，集中管理应用状态，并以可预测的方式更新状态。
    *   **核心流程：**
        1.  组件通过 `dispatch` 发起 `action`。
        2.  `reducer` 接收 `action` 和当前 `state`，计算新的 `state`。
        3.  `store` 保存 `state`，并通知订阅者（通常是 React 组件）。
        4.  组件从 `store` 获取更新后的 `state` 并重新渲染。
2.  **React-Redux：**
    *   **作用：** 连接 React 组件和 Redux `store`。
    *   **核心 API：**
        *   `Provider`：将 `store` 传递给整个应用。
        *   `connect`：高阶组件，连接 React 组件和 `store`。
            *   `mapStateToProps`：将 `state` 映射到组件的 `props`。
            *   `mapDispatchToProps`：将 `dispatch` 映射到组件的 `props`。
        *   `useSelector`：React Hook，用于在函数组件中订阅 `state`。
        *   `useDispatch`：React Hook，用于在函数组件中 `dispatch` action。
3.  **Redux Toolkit：**
    *   **作用：** 简化 Redux 开发流程，提供最佳实践。
    *   **核心 API：**
        *   `configureStore`：简化 `store` 的配置。
        *   `createSlice`：简化 `reducer`、`action` 和初始 `state` 的创建。
        *   `createAsyncThunk`：简化异步 `action` 的处理。

**第一性原理分析：**

*   **状态管理：** Redux 的核心在于集中化状态管理，解决组件间状态共享和传递的问题。
*   **单向数据流：** Redux 强制单向数据流，使得状态变化可预测和可追踪。
*   **纯函数：** Reducer 必须是纯函数，保证相同的输入始终得到相同的输出，易于测试和调试。
*   **解耦：** React-Redux 将 React 组件和 Redux `store` 解耦，提高组件的可复用性和可测试性。


---

**核心概念提炼（第一性原理）:**

1.  **状态 (State):** 应用程序的数据。
2.  **动作 (Action):** 描述发生了什么事情的普通 JavaScript 对象。
3.  **Reducer:** 接收先前的状态和一个动作，然后返回新状态的纯函数。
4.  **Slice (Redux Toolkit):** 包含 reducer 逻辑和 action 创建器的代码集合。

**Redux 工作流程 (费曼学习法):**

1.  **事件发生:** 用户与界面交互或应用程序接收到数据。
2.  **Action 被 dispatch:**  一个描述事件的 action 被发送到 Redux store。
3.  **Reducer 更新状态:** Redux store 调用 reducer 函数，传递当前状态和 action。Reducer 根据 action 的类型返回一个新的状态。
4.  **组件更新:** Redux store 通知所有订阅的组件，状态已经发生变化。组件重新渲染，显示新的状态。

**简化和组织:**

*   **Reducers:**
    *   核心职责是 *根据* `action` *更新 state*。
    *   必须是纯函数，不能修改原 `state`，而是返回一个 *新的* `state`。
*   **Actions:**
    *   本质是描述“发生了什么”的 *事件*。
    *   包含 `type` 字段 (必须)，用于标识动作类型。
    *   可以包含 `payload` 字段 (可选)，用于传递数据。
*   **PayloadAction:**
    *   是 `@reduxjs/toolkit` 中的类型，用于 *更清晰地定义带 payload 的 action*。
*   **Slice (Redux Toolkit):**
    *   *整合* 了 reducer 逻辑和 action 创建器。
    *   使用 `createSlice` 可以 *简化* Redux 代码。
    *   `createSlice` 自动生成 action creators，避免手动编写。


