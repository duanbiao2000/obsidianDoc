# 仓库快速分析模板

## 0️⃣ 基础信息

- **仓库名称**:
- **主要语言**: Python
- **核心依赖**:
- **项目类型**: AI Code Context Helper

---

## 1️⃣ 全局骨架 (15 min)

### 入口点

```
文件位置: 
函数签名:
调用链示例: input → [step1] → [step2] → output
```

### 核心模块Map

```
模块名          职责                    关键类/函数
─────────────────────────────────────────────────
core/           核心逻辑               
llm/            LLM交互                
utils/          工具函数               
api/            API接口                
```

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

## 2️⃣ 关键概念速查

### 数据流

- **输入格式**:
- **处理流程**:
- **输出格式**:

### 核心算法/逻辑

- **[概念1]**: 文件位置 + 1-2行解释
- **[概念2]**:
- **[概念3]**:

### 扩展点 (如何定制)

- **Plugin系统**:
- **Config**:
- **Hook**:

---

## 3️⃣ 深度索引 (按需查阅)

### 细节深挖清单

- [ ] 请求处理流程完整追踪
- [ ] 错误处理与重试机制
- [ ] 并发/异步处理方式
- [ ] 缓存策略
- [ ] 日志系统
- [ ] 测试覆盖

### 关键文件详细解读

```
[文件路径]
- 行数范围: [start-end]
- 核心内容: 
- 依赖项: 
- 值得注意: 
```

---

## 4️⃣ 高效阅读笔记

### 第一遍发现

- 日期:
- 发现:

### 关键问题与答案

**Q: [你的疑问]** A: [答案 + 源码位置]

### 性能/设计值得学习的点

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