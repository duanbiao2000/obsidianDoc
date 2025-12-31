在 Python（及其他编程语言）中，**docstring** 和 **注释（comment）** 都用于解释代码，但它们的目标读者、使用场景和最佳实践有明确分工。以下是清晰对比与推荐做法：

---

## 一、核心区别

|特性|Docstring（文档字符串）|注释（Comment）|
|---|---|---|
|**目标读者**|**代码使用者**（调用者、API 用户）|**代码维护者**（开发者自己或同事）|
|**可见性**|运行时可通过 `help()`、`__doc__` 访问|仅源码可见，运行时被忽略|
|**位置**|模块、类、函数/方法的**第一行**（紧跟定义）|任意位置（行内、上方、下方）|
|**格式**|通常遵循规范（如 Google、NumPy、reStructuredText）|自由格式|
|**工具支持**|自动生成文档（Sphinx, MkDocs）、IDE 提示|无特殊工具链支持|

---

## 二、各自分工详解

### ✅ Docstring：回答 “**它是什么？怎么用？**”

用于描述 **公共接口的行为**，包括：

- 函数/方法的用途
- 参数含义与类型
- 返回值
- 异常（Raises）
- 使用示例（可选）

```python
def calculate_tax(income: float, rate: float = 0.2) -> float:
    """计算应缴税款。
    
    Args:
        income: 税前收入，必须为非负数。
        rate: 税率，默认为 20%。
        
    Returns:
        应缴税款金额。
        
    Raises:
        ValueError: 如果 income < 0。
        
    Example:
        >>> calculate_tax(1000)
        200.0
    """
    if income < 0:
        raise ValueError("Income cannot be negative")
    return income * rate
```

> 📌 **关键**：假设读者**不看源码**，仅靠 docstring 就能正确使用该函数。

---

### ✅ 注释：回答 “**为什么这么写？**”

用于解释 **实现细节中的非显而易见逻辑**，例如：

- 复杂算法的思路
- 临时 workaround（如兼容旧版本）
- 性能优化原因
- TODO/FIXME 提醒

```python
# 使用双指针避免 O(n²) 时间复杂度
left, right = 0, len(arr) - 1

# FIXME: 临时绕过第三方 API 的 bug（2025-12 前需移除）
if vendor_api_version < "2.1":
    data = legacy_parse(response)
```

> ❌ **不要用注释重复代码字面意思**：
> 
> ```python
> # 将 x 加 1
> x += 1  # ← 冗余！
> ```

---

## 三、最佳实践（Python 社区共识）

### 📚 Docstring 最佳实践

1. **所有 public 接口必须有 docstring**  
    （模块、类、public 函数/方法）
2. **遵循一种风格并保持一致**  
    推荐 [Google Style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) 或 [NumPy Style](https://numpydoc.readthedocs.io/)
3. **包含类型提示（Type Hints） + docstring 语义说明**  
    类型提示说明“是什么类型”，docstring 说明“代表什么含义”
4. **提供简单示例（尤其工具函数）**
5. **私有方法（_开头）可省略或简化**

### 💬 注释最佳实践

1. **少而精**：只解释“为什么”，不解释“做什么”
2. **保持更新**：过时的注释比没有更危险
3. **用 TODO/FIXME 标记待办事项**（部分 IDE 可高亮）
    
    ```python
    # TODO: 改用异步 HTTP 客户端提升性能
    response = requests.get(url)
    ```
    
4. **避免情绪化或指责性语言**  
    （如 “这里写得很烂，但没时间改”）

---

## 四、常见误区

|误区|正确做法|
|---|---|
|用注释代替 docstring|公共接口必须用 docstring|
|docstring 写实现细节|docstring 只描述行为，不暴露内部逻辑|
|注释解释显而易见的代码|删除冗余注释，让代码自解释|
|不写任何文档|至少为 public 接口写最小化 docstring|

---

## 五、总结口诀

> **Docstring 告诉别人“怎么用”，  
> 注释告诉同事“为什么这么干”。**

- 用户调用你的函数？→ 看 **docstring**
- 同事接手你的代码？→ 看 **注释 + 清晰的代码**

遵循这一分工，你的代码将更专业、可维护、易协作。