---
view-count: 4
---
# React 19 范式重构：从手动优化到自动 Action

### 1. 核心定义
*   **传统模式**：命令式。手动管理 `isLoading`、`error` 状态，手动用 `useCallback` 包裹函数。
*   **React 19 模式**：声明式。使用 **Actions** 处理数据突变，**编译器 (React Compiler)** 自动处理记忆化（Memoization）。

---

### 2. 实例对比

#### **传统方式 (React < 19)**
*状态碎片化，心智负担重。*

```jsx
function ProfileForm({ user }) {
  const [name, setName] = useState(user.name);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // 必须手动 useCallback 优化性能，管理依赖项
  const handleSubmit = useCallback(async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await updateApi({ name });
      alert("成功");
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  }, [name]); // 依赖项漏写会导致 Bug

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={e => setName(e.target.value)} />
      <button disabled={loading}>{loading ? "保存中..." : "保存"}</button>
      {error && <p>{error.message}</p>}
    </form>
  );
}
```

#### **React 19 方式 (Actions + Compiler)**
*自动状态管理，逻辑高度内聚。*

```jsx
// 1. 纯逻辑 Action 函数（可抽离到独立文件）
async function updateProfileAction(prevState, formData) {
  const name = formData.get("name");
  try {
    await updateApi({ name });
    return { success: true, error: null };
  } catch (err) {
    return { success: false, error: err };
  }
}

// 2. 组件层：无需手动优化性能，无需 useState 追踪加载中
function ProfileForm({ user }) {
  // useActionState 自动提供 [状态, 触发器, 是否提交中]
  const [state, formAction, isPending] = useActionState(updateProfileAction, { error: null });

  return (
    <form action={formAction}>
      <input name="name" defaultValue={user.name} />
      
      {/* 提交状态通过 isPending 自动获取 */}
      <button disabled={isPending}>
        {isPending ? "保存中..." : "保存"}
      </button>

      {state.error && <p>{state.error.message}</p>}
    </form>
  );
}
```

---

### 3. 为何不再需要 `useCallback` / `useMemo`？

在 React 19 编译器环境下：
1.  **自动记忆化**：编译器会自动分析 `updateProfileAction` 或组件内的内联函数。如果输入的属性（props）和状态（state）没有改变，它会自动保持函数引用的稳定性，不再需要手动包裹 `useCallback`。
2.  **细粒度更新**：编译器会生成类似“记忆化区块”的代码。它知道哪些 UI 部分依赖于哪些变量，只有当变量真正改变时，相关的组件才会重渲染。
3.  **结果**：开发者只需编写“纯粹”的 JavaScript 逻辑，复杂的性能调优由编译器在构建阶段自动完成。

---

### 4. 收益总结
*   **代码量**：减少约 40%，移除大量冗余的 `useState` 和 `try-catch` 模板代码。
*   **健壮性**：原生支持并发更新，表单提交不会阻塞 UI，且自动处理竞态条件。
*   **DX（开发者体验）**：不再需要管理复杂的依赖数组（Dependency Arrays），彻底告别 `useMemo` 带来的心智隐患。