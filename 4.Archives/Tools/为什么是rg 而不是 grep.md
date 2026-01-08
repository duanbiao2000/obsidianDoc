---
view-count: 3
update: 2026-01-08 13:38
related:
  - "[[Github高效搜索语法]]"
  - "[[专业大学生实用操作指南]]"
  - "[[产品经理都有哪些常用方法论]]"
  - "[[Python AI工具-源码快速分析模板]]"
---

## 为什么是rg 而不是 grep

`rg` 是 **ripgrep** 的缩写，是一款比 `grep` 更快、功能更强大的命令行搜索工具，尤其适合在代码库中快速查找关键词、正则表达式等内容。它默认忽略 `.gitignore` 中的文件，且对代码文件有更好的支持（如自动识别编码、跳过二进制文件）。

以下是 `rg` 的核心用法示例，结合代码搜索场景说明：

### 1. 基础搜索：查找关键词

```bash
# 在当前目录及子目录中，搜索所有文件里的 "user_id"
rg "user_id"

# 搜索时不区分大小写（-i 即 --ignore-case）
rg -i "User_Id"

# 只搜索特定类型的文件（-t 指定文件类型，如 js、ts、md）
rg -t js "fetchData"  # 只在 JavaScript 文件中搜 "fetchData"
rg -t tsx "useState"  # 只在 TypeScript JSX 文件中搜 "useState"
```

支持的文件类型可通过 `rg --type-list` 查看（如 py、java、json 等）。

### 2. 搜索并显示上下文

```bash
# 显示匹配行的前后各 3 行内容（-C 即 --context）
rg -C 3 "error_log"

# 只显示匹配行的前 2 行（-B 即 --before-context）
rg -B 2 "unhandled rejection"

# 只显示匹配行的后 5 行（-A 即 --after-context）
rg -A 5 "successfully connected"
```

### 3. 正则表达式搜索（默认支持）

```bash
# 搜索所有以 "func" 开头、后面跟括号的内容（如函数定义）
rg "func \w+\(\)"

# 搜索邮箱格式（简单正则示例）
rg "\b[\w\.-]+@[\w\.-]+\.\w+\b"

# 关闭正则表达式，按纯文本搜索（-F 即 --fixed-strings）
rg -F "a.b.c"  # 此时 "." 不会被当作正则通配符
```

### 4. 排除/包含特定文件/目录

```bash
# 排除 node_modules 目录和 dist 目录（-g 即 --glob，支持通配符）
rg "api_key" -g "!node_modules" -g "!dist"

# 只搜索 src 目录下的文件
rg "config" -g "src/**/*"

# 排除 .json 文件
rg "password" -g "!*.json"
```

### 5. 其他实用选项

```bash
# 只显示匹配的文件名，不显示具体内容（-l 即 --files-with-matches）
rg -l "deprecated"  # 列出所有包含 "deprecated" 的文件路径

# 统计匹配次数（-c 即 --count）
rg -c "console.log"  # 显示每个文件中 "console.log" 出现的次数

# 以 JSON 格式输出结果（方便程序处理，-oJ 即 --json）
rg -oJ "user_login"

# 搜索时显示行号（默认已显示，-n 可显式开启）
rg -n "database_url"
```
