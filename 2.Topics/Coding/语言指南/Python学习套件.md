---
view-count: 7
---
# [[2025-12-05-Python学习套件]]：极简版

## 核心公式
**FastAPI + Pydantic = 现代后端标准**
**Pandas + Polars = 数据处理双雄**
**PyTorch + Transformers = AI 工业皇冠**

---

## 1. Web 框架对决

| 框架 | 性能 | 类型安全 | 场景 |
|:--- |:--- |:--- |:--- |
| **FastAPI** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 高性能 API、微服务 |
| **Django** | ⭐⭐ | ⭐⭐ | 大型企业级全栈应用 |
| **Flask** | ⭐⭐⭐ | ⭐ | 小型灵活工具 |

---

## 2. 核心技术栈 (P0 必学)

### I. 后端与数据流
- **接口开发 |** [[FastAPI]] + **Pydantic** (数据验证)。
- **持久化 |** **SQLAlchemy** (ORM) + **redis-py** (缓存)。
- **异步 |** **asyncio** (底层) + **uvicorn** (服务器) + **uvloop** (提速)。

### II. 数据科学与 AI
- **分析 |** **pandas** (标准) + **polars** (高性能/多核)。
- **算法 |** **scikit-learn** (机器学习) + **pytorch** (深度学习)。
- **大模型 |** **transformers** (HuggingFace 事实标准)。

### III. 工程化工具
- **代码质量 |** **ruff** (极速 Linter) + **mypy** (静态类型检查)。
- **包管理 |** **poetry** (现代化依赖管理)。
- **测试 |** **pytest** (自动化测试)。

---

## 3. 专项领域“最优解”

- **面试算法 |** `python-ds` (题型导向) > `thealgorithms` (百科全书)。
- **业务逻辑 |** `transitions` (状态机建模最佳实践)。
- **终端 UI |** **rich** (精美渲染) + **typer** (类型驱动 CLI)。
- **音频处理 |** **librosa** (分析) + **pydub** (极简剪辑)。

---

## 4. 学习路径建议

| 阶段 | 关键动作 | 核心目标 |
|:--- |:--- |:--- |
| **初级** | `requests`, `pandas`, `pytest` | 解决脚本与自动化需求。 |
| **中级** | `FastAPI`, `SQLAlchemy`, `celery` | 构建可扩展的生产级系统。 |
| **高级** | `uvloop`, `pytorch`, `ruff` | 榨干性能，深入 AI 与架构。 |

---

## 黄金法则
**工具选新不选旧 (Ruff > Flake8)，框架选快不选稳 (FastAPI > Flask)，逻辑选简不选繁。**