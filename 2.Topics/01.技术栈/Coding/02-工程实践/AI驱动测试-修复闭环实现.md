---
view-count: 4
tags:
  - AI-driven-testing
  - code-optimization
  - AI
  - AI-content-creation-process
  - Domain/AI
  - Domain/AI/Agent
  - Domain/Technology/DevOps
  - Type/Reference
---
# AI驱动测试-修复闭环实现 (Brutally Minimal)

## 核心架构

```
AI生成代码 → 自动测试 → 捕获失败 → AI修复 → 重复直到通过
```

**关键**: AI编程助手 + 自动化测试 + CI/CD + 脚本化反馈

---

## 工具选择

| 工具             | 自动修复支持 | 备注                       |
| -------------- | ------ | ------------------------ |
| Cursor         | ✅ 强推荐 | 本地模型+编辑操作+可扩展           |
| Windsurf       | ❓      | 新兴工具，需查文档              |
| GitHub Copilot | ❌      | 无官方API                   |
| OpenAI API     | ✅ 通用  | 需自建提示词+解析逻辑            |

**推荐**: Cursor + 本地脚本

---

## 实现步骤

### 1. 标准化测试

```bash
# Python
pytest

# JS/TS
npm test 或 vitest

# Go
go test ./...

# Rust
cargo test
```

**建议**: 输出机器可读格式(JUnit XML/JSON)

---

### 2. 修复循环脚本

**核心逻辑**
```python
import subprocess
import sys
from pathlib import Path

MAX_RETRIES = 3

def run_tests():
    result = subprocess.run(
        ["pytest", "--tb=short"],
        capture_output=True,
        text=True
    )
    return result.returncode == 0, result.stdout + result.stderr

def request_ai_fix(error_log: str):
    prompt = f"""
你是资深开发者。以下是测试失败日志，请直接修改源代码使其通过。
只输出需要修改的文件路径和完整新内容，格式：

--- FILE: path/to/file.py ---
[完整新内容]
--- END ---

错误日志：
{error_log}
"""
    # 调用OpenAI
    from openai import OpenAI
    client = OpenAI(api_key="your-api-key")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def apply_ai_patch(ai_response: str):
    """解析AI返回并写入文件"""
    lines = ai_response.splitlines()
    current_file = None
    buffer = []
    
    for line in lines:
        if line.startswith("--- FILE: "):
            if current_file and buffer:
                Path(current_file).write_text("\n".join(buffer))
            current_file = line[10:-4].strip()
            buffer = []
        elif line == "--- END ---":
            if current_file and buffer:
                Path(current_file).write_text("\n".join(buffer))
            current_file = None
            buffer = []
        elif current_file:
            buffer.append(line)

def main():
    for attempt in range(1, MAX_RETRIES + 1):
        print(f"\n🔄 第{attempt}次测试...")
        passed, output = run_tests()
        
        if passed:
            print("✅ 测试通过!")
            sys.exit(0)
        
        print("❌ 测试失败，请求AI修复...")
        ai_response = request_ai_fix(output)
        
        try:
            apply_ai_patch(ai_response)
            print("💾 代码已更新")
        except Exception as e:
            print(f"⚠️ 应用补丁失败: {e}")
            break
    
    print("🛑 达到最大重试次数")
    sys.exit(1)

if __name__ == "__main__":
    main()
```

---

### 3. 集成方式

**本地开发**
```bash
python ai-fix-loop.py
```

**Git Hook (提交前)**
```bash
# .git/hooks/pre-commit
#!/bin/sh
python ai-fix-loop.py || exit 1
```

**CI/CD (GitHub Actions)**
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

---

## 安全限制

**防护措施**
- 最大重试次数(防无限循环)
- 限制修改文件范围
- Git快照备份(`git stash`/`git commit`)
- 沙箱环境运行(CI中)

**备份示例**
```python
def safe_main():
    # 备份
    subprocess.run(["git", "stash", "-u"])
    
    try:
        main()
    finally:
        # 可选: 恢复
        # subprocess.run(["git", "stash", "pop"])
        pass
```

---

## 提示词优化

**基础版**
```
你是资深开发者。修改代码使测试通过。
输出格式: --- FILE: path --- [内容] --- END ---
错误日志: {log}
```

**增强版**
```
你是资深开发者。根据测试失败日志修复代码。

要求:
1. 只修改必要文件
2. 保持代码风格一致
3. 添加必要注释说明修复原因
4. 不要破坏现有功能

输出格式:
--- FILE: path/to/file.py ---
[完整修复后代码]
--- END ---

测试失败日志:
{error_log}

项目上下文:
{project_context}
```

---

## 工作流变体

**Cursor专用(假设有CLI)**
```python
def request_ai_fix(error_log: str):
    # 调用Cursor CLI
    result = subprocess.run(
        ["cursor-cli", "fix", "--error", error_log],
        capture_output=True,
        text=True
    )
    return result.stdout
```
