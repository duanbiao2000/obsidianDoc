---
tags:
  - Effective/Tools
aliases:
  - Bash
  - CLI
---
提取项目依赖,AI对项目使用的三方库进行注解.
`awk '/^require \(/{flag=1; next} /^)/{flag=0} flag {printf "- %s\n", $0}' go.mod | sed -E 's/ [vV][^ ]*//; s/ \/\/.*$//' > docs/dependencies.md`
提取依赖项所在的行 | 取消版本号&注释 > 重定向到 docs/dependencies.md`
- **`print "- " $0`**：在每行依赖项前加上 `-` ，使其符合 Markdown 列表格式。你可以根据需要将 `-` 替换为 `*` 或其他符号。
- 为了确保每行依赖项之间确实有换行符，可以使用 `printf` 而不是 `print`，这样可以显式地添加换行符：