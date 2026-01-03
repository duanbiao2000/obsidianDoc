要实现如下 AI 驱动的“测试 → 修复 → 再测试”闭环工作流：

```
Cursor / GitHub Copilot / Windsurf
    ↓ 生成代码
测试套件自动运行
    ↓ 反馈
AI 自动修复 → 直到测试通过
```

你需要将 **AI 编程助手**（如 Cursor、Copilot、Windsurf）与 **自动化测试 + CI/CD + 脚本化反馈机制** 结合。以下是具体实现步骤和配置建议，适用于本地开发或 CI 环境。

---

## 🧩 整体架构概览

1. **AI 生成初始代码**（由开发者触发）
2. **自动运行测试套件**
3. **捕获失败信息**
4. **调用 AI 工具（如 Cursor API / OpenAI API / Windsurf CLI）进行修复**
5. **重复 2–4，直到测试通过或达到最大重试次数**

> 注意：目前 Copilot 没有官方 API 支持自动修复；Cursor 和 Windsurf 更适合此场景（尤其 Cursor 支持本地模型+编辑操作）。

---

## ✅ 步骤详解

### Step 1：准备可自动运行的测试套件

确保你的项目有标准化的测试命令，例如：

```bash
# Python
pytest

# JavaScript/TypeScript
npm test 或 vitest

# Go
go test ./...

# Rust
cargo test
```

建议将测试输出格式设为机器可读（如 JUnit XML、JSON），便于解析失败原因。

---

### Step 2：编写“AI 修复循环”脚本（核心）

创建一个脚本 `ai-fix-loop.py`（以 Python 为例）：

```python
import subprocess
import sys
import time
from pathlib import Path

MAX_RETRIES = 3
PROJECT_ROOT = Path(".").resolve()

def run_tests():
    result = subprocess.run(
        ["pytest", "--tb=short"],  # 替换为你的测试命令
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True
    )
    return result.returncode == 0, result.stdout + result.stderr

def request_ai_fix(error_log: str):
    """
    调用 AI 工具修复代码。
    方式可选：
      - 使用 Cursor 的 CLI（如有）
      - 调用 OpenAI API + 自定义提示词
      - 调用 Windsurf 的修复接口（若支持）
    """
    prompt = f"""
你是一个资深开发者。以下是测试失败日志，请直接修改相关源代码文件使其通过测试。
不要解释，只输出需要修改的文件路径和完整的新内容，格式如下：

--- FILE: path/to/file.py ---
[完整新内容]
--- END ---

错误日志：
{error_log}
"""

	# 示例：调用 OpenAI（需安装 openai 包）
	from openai import OpenAI
	client = OpenAI(api_key="your-api-key")
	response = client.chat.completions.create(
			model="gpt-4o",
			messages=[{"role": "user", "content": prompt}]
	)
	return response.choices[0].message.content

def apply_ai_patch(ai_response: str):
    """解析 AI 返回内容并写入文件"""
    lines = ai_response.splitlines()
    current_file = None
    buffer = []
    in_file = False

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("--- FILE: ") and line.endswith(" ---"):
            if current_file and buffer:
                # 写入上一个文件
                with open(current_file, "w") as f:
                    f.write("\n".join(buffer) + "\n")
            current_file = line[10:-4].strip()
            buffer = []
            in_file = True
        elif line == "--- END ---":
            if current_file and buffer:
                with open(current_file, "w") as f:
                    f.write("\n".join(buffer) + "\n")
            current_file = None
            buffer = []
            in_file = False
        elif in_file:
            buffer.append(line)
        i += 1

def main():
    for attempt in range(1, MAX_RETRIES + 1):
        print(f"\n🔄 尝试第 {attempt} 次运行测试...")
        passed, output = run_tests()
        if passed:
            print("✅ 所有测试通过！")
            sys.exit(0)
        else:
            print("❌ 测试失败，请求 AI 修复...")
            print("错误摘要：\n" + "\n".join(output.splitlines()[-10:]))

            ai_response = request_ai_fix(output)
            print("🔧 AI 建议修复：\n", ai_response)

            try:
                apply_ai_patch(ai_response)
                print("💾 代码已更新，重新测试...")
            except Exception as e:
                print("⚠️ 应用补丁失败:", e)
                break

    print("🛑 达到最大重试次数，未能修复。")
    sys.exit(1)

if __name__ == "__main__":
    main()
```

> 💡 提示：你可以将 `request_ai_fix` 替换为调用 **Cursor 的本地 LLM 接口**（如果它提供 CLI 或 HTTP API），或使用 **Windsurf 的修复功能**（需确认其是否开放）。

---

### Step 3：集成到开发流程

#### 选项 A：本地开发时手动触发

```bash
python ai-fix-loop.py
```

#### 选项 B：集成到 Git Hook（提交前自动修复）

在 `.git/hooks/pre-commit` 中添加：

```bash
#!/bin/sh
python ai-fix-loop.py || exit 1
```

#### 选项 C：CI/CD 中自动运行（如 GitHub Actions）

```yaml
# .github/workflows/ai-fix.yml
name: AI Fix Loop
on: [push]

jobs:
  test-and-fix:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install pytest openai
      - run: python ai-fix-loop.py
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

> ⚠️ 注意：在 CI 中自动修改代码需谨慎，建议仅用于实验或内部项目。

---

### Step 4：选择合适的 AI 工具

|工具|是否支持自动修复|备注|
|---|---|---|
|**Cursor**|✅（强推荐）|支持本地模型、编辑操作、可通过插件扩展；未来可能开放 CLI|
|**Windsurf**|❓|新兴工具，需查看其文档是否支持程序化调用|
|**GitHub Copilot**|❌|无官方 API 用于自动修复代码|
|**OpenAI API**|✅（通用）|需自行构建提示词和解析逻辑|

> 推荐：**Cursor + 本地脚本** 是目前最接近你描述工作流的方案。

---

## 🔒 安全与限制建议

- 设置最大重试次数（防止无限循环）
- 限制 AI 修改的文件范围（避免破坏配置文件等）
- 使用 Git 快照备份（每次修复前 `git stash` 或 `git commit -m "pre-ai-fix"`）
- 在沙箱环境运行（尤其 CI 中）

---

## ✅ 总结

要实现“AI 生成 → 测试 → 自动修复”闭环：

1. **标准化测试命令**
2. **编写修复循环脚本**（调用 AI + 解析输出 + 写回文件）
3. **选择支持程序化调用的 AI 工具**（首选 Cursor 或 OpenAI）
4. **集成到本地/Git/CI 流程**

这套系统本质上是一个 **AI 驱动的自修复开发代理（Self-healing Dev Agent）**，已在部分前沿团队中实验性使用。

如需我为你生成特定语言（如 JS/TS/Python）的完整模板，欢迎指定技术栈！
