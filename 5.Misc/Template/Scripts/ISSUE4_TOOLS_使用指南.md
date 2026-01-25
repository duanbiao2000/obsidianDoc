# Issue #4 自动化工具使用指南

**创建时间**: 2026-01-25
**相关**: Issue #4 - 自动化脚本体系优化

---

## 📋 目录

1. [快速开始](#快速开始)
2. [统一 CLI 工具](#统一-cli-工具)
3. [标签管理](#标签管理)
4. [链接分析](#链接分析)
5. [元数据验证](#元数据验证)
6. [核心库 API](#核心库-api)
7. [常见问题](#常见问题)

---

## 快速开始

### 前置要求

- Python 3.7+
- Obsidian vault 已配置
- 已安装 Issue #4 的核心库

### 基本使用

所有工具都在 `5.Misc/Template/Scripts/` 目录下运行：

```bash
cd "D:\迅雷下载\@同步文件\OneDrive\obsidianDoc\5.Misc\Template\Scripts"
```

---

## 统一 CLI 工具

### 查看帮助

```bash
# 查看主帮助
python obsidian-scripts --help

# 查看特定命令的帮助
python obsidian-scripts tags --help
python obsidian-scripts links --help
python obsidian-scripts validate --help
```

### 命令结构

```
obsidian-scripts <命令> <子命令> [选项]

命令:
  tags        标签管理
  links       链接分析
  validate    元数据验证
  workflow    工作流编排
```

---

## 标签管理

### 1. 批量添加 Domain 标签

根据文件路径自动推断并添加 Domain/Type/Status 标签。

```bash
# 预览模式（推荐先运行）
python obsidian-scripts tags add-domain --dry-run

# 实际执行
python obsidian-scripts tags add-domain

# 显示详细信息
python obsidian-scripts tags add-domain --verbose
```

**功能**:
- 根据文件路径自动添加 Domain 标签
- 支持自定义标签映射规则
- 避免标签重复
- 自动创建备份

**示例输出**:
```
======================================================================
Obsidian 知识库自动化工具
Vault: D:\迅雷下载\@同步文件\OneDrive\obsidianDoc
======================================================================

📌 批量添加 Domain 标签

正在处理: 2.Topics/01.技术栈/xxx.md
  添加标签: Domain/Technology

✅ 完成！
  处理: 45 个文件
  跳过: 12 个文件
```

---

### 2. 清理重复标签

移除 YAML frontmatter 中的重复标签。

```bash
# 预览模式
python obsidian-scripts tags cleanup --dry-run

# 实际执行
python obsidian-scripts tags cleanup

# 显示详细信息
python obsidian-scripts tags cleanup --verbose
```

**功能**:
- 检测并移除重复标签
- 保持标签顺序
- 创建备份

**示例输出**:
```
🧹 清理重复标签

发现重复标签: 2.Topics/xxx.md
  tags: [Domain/AI, Domain/AI, Type/Note]
  清理后: [Domain/AI, Type/Note]

✅ 完成！
  处理: 23 个文件
  清理: 15 个重复标签
```

---

### 3. 标签规范化

分阶段执行标签替换（invalid/high/medium/low/all）。

```bash
# 预览所有替换
python obsidian-scripts tags normalize --phase all --dry-run

# 执行所有替换
python obsidian-scripts tags normalize --phase all

# 只替换高频标签
python obsidian-scripts tags normalize --phase high

# 只替换无效标签
python obsidian-scripts tags normalize --phase invalid
```

**阶段说明**:
- `invalid`: 删除无效标签
- `high`: 替换高频错误标签
- `medium`: 替换中频错误标签
- `low`: 替换低频错误标签
- `all`: 执行所有替换

---

## 链接分析

### 1. 查找孤立笔记

识别没有链接或链接数很少的笔记。

```bash
# 查找完全孤立的笔记（0个链接）
python obsidian-scripts links find-orphans --threshold 0

# 查找低连通性笔记（1-2个链接）
python obsidian-scripts links find-orphans --threshold 2

# 生成报告文件
python obsidian-scripts links find-orphans --threshold 0 --output 孤立笔记清单.md

# 显示详细信息
python obsidian-scripts links find-orphans --threshold 0 --verbose
```

**输出文件**:
- `孤立笔记清单_<时间戳>.md` - 按优先级分类的孤立笔记列表
- `低连通性笔记清单_<时间戳>.md` - 只有1-2个链接的笔记

**示例输出**:
```
🔍 查找孤立笔记
阈值: 链接数 <= 0

正在扫描: 926 个文件

✅ 完成！
  找到 169 个孤立笔记（链接数<=0）
  报告: 孤立笔记清单_20260125.md
```

---

### 2. 分析链接连通性

分析笔记的链接连通性，识别高价值笔记。

```bash
# 分析连通性（显示前20个高连通性笔记）
python obsidian-scripts links analyze

# 显示详细信息
python obsidian-scripts links analyze --verbose
```

**示例输出**:
```
📊 分析链接连通性

前 20 个高连通性笔记：
  1. CLAUDE.md: 45 ← → 12
  2. 仓库标签管理系统.md: 38 ← → 8
  3. 项目活跃度看板.md: 25 ← → 15
  ...

✅ 分析完成！
```

---

### 3. 链接密度统计

统计整个知识库的链接密度。

```bash
# 查看链接密度统计
python obsidian-scripts links density

# 显示详细信息
python obsidian-scripts links density --verbose
```

**示例输出**:
```
📈 链接密度统计

  总文件数: 926
  总链接数: 4384
  平均链接数/文件: 4.73
  孤立笔记 (0链接): 169
  低连通性 (1-2链接): 145
  高连通性 (>2链接): 612

✅ 统计完成！
```

---

## 元数据验证

验证笔记的元数据完整性（支持 Issue #3）。

```bash
# 验证 Domain 标签
python obsidian-scripts validate metadata --include-domains

# 验证 Type 标签
python obsidian-scripts validate metadata --include-types

# 验证 Status 标签
python obsidian-scripts validate metadata --include-statuses

# 验证所有元数据
python obsidian-scripts validate metadata --include-domains --include-types --include-statuses

# 自动修复模式（开发中）
python obsidian-scripts validate metadata --fix --dry-run
```

**状态**: ⚠️ 此功能正在开发中...

---

## 核心库 API

如果你需要在 Python 代码中直接使用这些功能：

### 1. TagManager - 标签管理

```python
from obsidian_scripts.core.config import Config
from obsidian_scripts.plugins.tags import TagManager

# 初始化
config = Config()
tag_manager = TagManager(config)

# 添加 Domain 标签
stats = tag_manager.add_domain_tags(
    dry_run=False,
    verbose=True
)
print(f"处理: {stats['processed']} 个文件")

# 清理重复标签
stats = tag_manager.cleanup_duplicates(
    dry_run=False,
    verbose=True
)
print(f"清理: {stats['duplicates_removed']} 个重复标签")

# 标签规范化
stats = tag_manager.normalize_tags(
    phase='all',
    dry_run=False,
    verbose=True
)
print(f"替换: {stats['replaced']} 个标签")
```

---

### 2. LinkAnalyzer - 链接分析

```python
from obsidian_scripts.core.config import Config
from obsidian_scripts.plugins.links import LinkAnalyzer

# 初始化
config = Config()
link_analyzer = LinkAnalyzer(config)

# 查找孤立笔记
orphans = link_analyzer.find_orphan_notes(
    link_threshold=0,
    output_file=None
)
print(f"找到 {len(orphans)} 个孤立笔记")

# 分析连通性
connectivity = link_analyzer.analyze_connectivity()
for title, links in connectivity.items():
    in_count = len(links['in_links'])
    out_count = len(links['out_links'])
    print(f"{title}: {in_count} ← → {out_count}")

# 获取链接密度统计
stats = link_analyzer.get_link_density_stats()
print(f"平均链接数/文件: {stats['avg_links_per_file']}")
```

---

### 3. MetadataValidator - 元数据验证

```python
from obsidian_scripts.utils.validation import MetadataValidator

# 初始化
validator = MetadataValidator()

# 验证所有元数据
issues = validator.validate_all(
    include_domains=True,
    include_types=True,
    include_statuses=True,
    include_dates=True
)

# 按级别统计
from obsidian_scripts.utils.validation import ValidationLevel
error_count = sum(1 for i in issues if i.level == ValidationLevel.ERROR)
warning_count = sum(1 for i in issues if i.level == ValidationLevel.WARNING)

print(f"错误: {error_count}")
print(f"警告: {warning_count}")

# 查看具体问题
for issue in issues[:10]:
    print(f"[{issue.level.value}] {issue.file_path}")
    print(f"  字段: {issue.field}")
    print(f"  问题: {issue.message}")
    if issue.suggestion:
        print(f"  建议: {issue.suggestion}")
```

---

### 4. Config - 配置管理

```python
from obsidian_scripts.core.config import Config

# 使用默认配置
config = Config()
print(f"Vault 根目录: {config.vault_root}")
print(f"包含目录: {config.include_dirs}")

# 使用自定义配置文件
config = Config(config_path="path/to/config.yaml")

# 访问配置项
vault_root = config.vault_root
include_dirs = config.include_dirs
exclude_patterns = config.exclude_patterns
```

---

### 5. FileScanner - 文件扫描

```python
from obsidian_scripts.core.config import Config
from obsidian_scripts.core.file_utils import FileScanner

# 初始化
config = Config()
scanner = FileScanner(config.vault_root, config.include_dirs)

# 扫描所有 Markdown 文件
for filepath in scanner.scan_markdown_files():
    print(f"找到文件: {filepath}")

# 使用排除模式
exclude_patterns = [".agent", ".git"]
for filepath in scanner.scan_markdown_files(exclude_patterns=exclude_patterns):
    print(f"找到文件: {filepath}")
```

---

### 6. FrontmatterParser - YAML 解析

```python
from obsidian_scripts.core.frontmatter import FrontmatterParser

# 解析文件
content = """---
tags: [Domain/AI, Type/Note]
update: 2026-01-25
---

# 笔记内容
"""

fm = FrontmatterParser.parse(content)

# 访问 frontmatter 数据
tags = fm.get_tags()
update = fm.get('update')
title = fm.get('title', '默认标题')

# 修改 frontmatter
fm.set('tags', ['Domain/AI', 'Type/Note', 'Status/Done'])
fm.set('update', '2026-01-26')

# 生成新的内容
new_content = fm.dump()
```

---

## 常见问题

### Q1: 如何在非 Scripts 目录下运行 CLI？

```bash
# 使用完整路径
python D:\迅雷下载\@同步文件\OneDrive\obsidianDoc\5.Misc\Template\Scripts\obsidian-scripts tags add-domain

# 或者添加到 PATH
export PATH="$PATH:D:\迅雷下载\@同步文件\OneDrive\obsidianDoc\5.Misc\Template\Scripts"
obsidian-scripts tags add-domain
```

---

### Q2: 如何修改 vault 路径？

编辑 `config/default.yaml`:

```yaml
vault_root: "D:\\迅雷下载\\@同步文件\\OneDrive\\obsidianDoc"

scan:
  include_dirs:
    - "0.DailyNotes"
    - "1.Projects"
    - "2.Topics"
    # ... 其他目录
```

---

### Q3: --dry-run 模式会修改文件吗？

**不会！** `--dry-run` 只会显示将要执行的操作，不会实际修改任何文件。

**推荐流程**:
1. 先运行 `--dry-run` 预览
2. 检查输出，确认操作范围
3. 移除 `--dry-run` 实际执行

---

### Q4: 备份文件存在哪里？

备份文件默认存储在 `.backup_enhance/` 目录：

```
Scripts/
├── .backup_enhance/
│   ├── 20260125_143022_tags/
│   └── 20260125_150845_links/
```

备份会自动清理（默认保留30天）。

---

### Q5: 如何运行测试？

```bash
cd "D:\迅雷下载\@同步文件\OneDrive\obsidianDoc\5.Misc\Template\Scripts"

# 运行所有测试
python -m pytest

# 运行特定测试
python -m pytest tests/test_core.py

# 查看测试覆盖率
python -m pytest --cov=obsidian_scripts --cov-report=html
```

---

### Q6: 遇到 YAML 解析错误怎么办？

某些笔记的 YAML frontmatter 格式可能不规范。脚本会跳过这些文件并显示警告。

**解决方法**:
1. 检查警告信息中提到的文件
2. 修正 YAML 格式
3. 重新运行脚本

**常见 YAML 错误**:
```yaml
# ❌ 错误：混合使用数组和多行
tags: ["Tag1", "Tag2"]
  - Tag3

# ✅ 正确：使用数组格式
tags: ["Tag1", "Tag2", "Tag3"]

# ✅ 正确：使用多行格式
tags:
  - Tag1
  - Tag2
  - Tag3
```

---

## 相关文档

- [Issue #4 实施计划](../../Atlas/Docs/plans/2026-01-25-issue4-automation-scripts-optimization.md)
- [仓库标签管理系统](../../Atlas/Index/仓库标签管理系统.md)
- [README.md](README.md)

---

**最后更新**: 2026-01-25
**维护者**: Claude Code
