---
view-count: 9
---
针对 [[Roadmap]] 中的自动化分析需求，核心具体命令如下：

### 1. 工程完整性扫描 (检查缺失组件)
用于识别项目是否具备生产级基础（测试、文档、CI/CD）：
```bash
ls -R | rg "tests|docs|workflows|docker|Makefile|pyproject\.toml"
```

### 2. 核心链路分析 (识别逻辑重心)
通过代码行数定位逻辑密集的“厚模块”：
```bash
wc -l $(rg --files -t py) | sort -n | tail -10
```

### 3. 技术边界分析 (识别依赖密度)
通过提取导入项识别项目核心技术栈与潜在瓶颈：
```bash
rg -h "^(from|import) " -t py | sort | uniq -c | sort -rn | head -15
```

### 4. 结构化提取 (喂给 AI 的素材)
- **RepoAnalyzer 脚本 |** 运行该 Python 脚本提取核心 API 和类定义，生成功能快照。
- **静态分析 |** 直接将 `ls -R` 的输出与 `requirements.txt` 内容粘贴给 AI。

---

## 黄金法则
**命令提取元数据 $\rightarrow$ AI 对标行业标准 $\rightarrow$ 自动生成 Roadmap。**