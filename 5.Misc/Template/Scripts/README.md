# Obsidian知识库自动化脚本

本目录包含用于维护和优化Obsidian知识库的Python自动化脚本。

## 📂 目录结构

```
Scripts/
├── tags/                    # 标签管理脚本
├── links/                   # 链接分析脚本
├── content/                 # 内容处理脚本(预留)
└── README.md               # 本文件
```

---

## 🏷️ tags/ - 标签管理脚本

### [batch_add_domain_tags.py](tags/batch_add_domain_tags.py)
批量为笔记添加Domain/Type/Status标签

**功能**:
- 根据文件路径自动推断标签
- 支持自定义标签映射规则
- 避免标签重复

**使用方法**:
```bash
python tags/batch_add_domain_tags.py
```

**相关文档**: [batch_add_domain_tags修复说明](../batch_add_domain_tags修复说明.md)

---

### [tag_normalizer.py](tags/tag_normalizer.py)
标签规范化批量替换脚本

**功能**:
- 分阶段执行标签替换(invalid/high/medium/low/all)
- 支持预览模式(--dry-run)
- 自动备份

**使用方法**:
```bash
# 预览模式
python tags/tag_normalizer.py --dry-run

# 执行所有替换
python tags/tag_normalizer.py --phase all

# 只替换高频标签
python tags/tag_normalizer.py --phase high
```

---

### [cleanup_duplicate_tags.py](tags/cleanup_duplicate_tags.py)
清理重复标签脚本

**功能**:
- 移除YAML frontmatter中的重复标签
- 保持标签顺序
- 创建备份

**使用方法**:
```bash
# 预览模式
python tags/cleanup_duplicate_tags.py --dry-run

# 执行清理
python tags/cleanup_duplicate_tags.py

# 显示详细信息
python tags/cleanup_duplicate_tags.py --verbose
```

---

### [replace_tags.py](tags/replace_tags.py)
简化的标签替换脚本

**功能**:
- 快速替换指定标签
- 适用于临时性标签修改

**使用方法**:
```bash
python tags/replace_tags.py <旧标签> <新标签>
```

---

## 🔗 links/ - 链接分析脚本

### [find_orphan_notes.py](links/find_orphan_notes.py)
识别和分析孤立笔记

**功能**:
- 扫描所有Markdown文件
- 统计wiki链接、嵌入、标签
- 生成孤立笔记清单(按优先级分类)
- 生成低连通性笔记清单

**使用方法**:
```bash
python links/find_orphan_notes.py
```

**输出文件**:
- `孤立笔记清单_<时间戳>.md` - 按优先级分类的孤立笔记列表
- `低连通性笔记清单_<时间戳>.md` - 只有1-2个链接的笔记

**相关Issue**: [#2: 孤立笔记链接密度提升计划](https://github.com/duanbiao2000/obsidianDoc/issues/2)

---

### [link_analyzer.py](links/link_analyzer.py)
链接分析工具

**功能**:
- 分析笔记的链接密度
- 识别高价值笔记(链接数>2)
- 统计知识网络连通性

**使用方法**:
```bash
python links/link_analyzer.py
```

---

## 📝 content/ - 内容处理脚本(预留)

此目录为未来的内容处理脚本预留,例如:
- 内容质量评估
- 自动化归档
- 笔记压缩
- 元数据完善

---

## 🔧 通用使用建议

### Windows编码支持
所有脚本都已添加UTF-8编码支持,可在Windows控制台正常运行。

### 安全执行流程
1. **备份优先**: 执行任何批量操作前,先创建git commit备份
2. **预览模式**: 优先使用`--dry-run`预览效果
3. **验证结果**: 检查生成的清单文件确认修改范围
4. **确认执行**: 验证无误后移除`--dry-run`执行实际操作

### 示例工作流
```bash
# 1. 创建备份
git add .
git commit -m "backup: 执行脚本前的快照"

# 2. 预览效果
python tags/tag_normalizer.py --dry-run

# 3. 检查清单文件
cat 孤立笔记清单_*.md

# 4. 确认后执行
python tags/tag_normalizer.py --phase all

# 5. 验证结果
git diff

# 6. 提交修改
git add .
git commit -m "feat: 标签规范化完成"
```

---

## 📚 相关文档

- [仓库标签管理系统](../../Atlas/Index/仓库标签管理系统.md) - 标签规范说明
- [CLAUDE.md](../../CLAUDE.md) - 项目指南
- [GitHub Issues](https://github.com/duanbiao2000/obsidianDoc/issues) - 问题跟踪

---

## 🛠️ 脚本开发规范

### 新增脚本时
1. **分类放置**: 根据功能放入相应子目录(tags/links/content)
2. **添加文档**: 在本README中添加使用说明
3. **Windows支持**: 添加UTF-8编码处理
4. **备份机制**: 支持自动备份或提供备份建议
5. **预览模式**: 批量操作脚本应支持--dry-run

### 脚本模板
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
脚本功能描述
作者: xxx
日期: 2026-xx-xx
"""

import sys
from pathlib import Path

# Windows 编码支持
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def main():
    """主函数"""
    pass

if __name__ == "__main__":
    main()
```

---

**最后更新**: 2026-01-25
**维护者**: Claude Code
