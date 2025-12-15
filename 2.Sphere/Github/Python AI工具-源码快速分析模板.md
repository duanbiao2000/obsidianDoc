---
view-count: 5
---

### 依赖关系 (谁依赖谁)

```
User Input
    ↓
[Parser/Handler]
    ↓
[Core Logic]
    ↓
[LLM Module] ──→ [Cache]
    ↓
[Formatter]
    ↓
Output
```

---


## 5️⃣ 快速参考

### 常用命令

```bash
# 查找所有类定义
grep -rn "^class " --include="*.py"

# 查找所有函数入口
grep -rn "^def " --include="*.py" | head -20

# 查找导入关系
grep -rn "^from\|^import" --include="*.py" | sort | uniq

# 查找关键概念
grep -rn "llm\|model\|context\|cache" --include="*.py"

# 追踪函数调用
grep -rn "function_name(" --include="*.py"
```

### 推荐阅读顺序

1. README.md 与 documentation
2. setup.py 或 pyproject.toml (依赖和包结构)
3. main 或 **init**.py (初始化逻辑)
4. core 模块中最小的文件 (从简单到复杂)
5. 测试文件 (看如何使用)
6. 类和函数定义 (完整理解)