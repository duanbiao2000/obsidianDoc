# 备份与回滚指南

## 📦 备份信息

**备份时间**: 2026-01-23
**备份Tag**: `pre-copilot-cleanup-20260123`
**Commit ID**: b47503a
**文件总数**: 288个copilot-custom-prompts文件
**备份内容**:
- 所有288个提示词文件的完整状态
- 分析报告（CSV格式）
- 清理执行指南

---

## 🔄 回滚操作

### 方式1：回滚到备份Tag（推荐）

```bash
# 查看备份状态
git tag -l "pre-copilot-cleanup-20260123"
git show pre-copilot-cleanup-20260123

# 完全回滚（恢复所有文件）
git checkout pre-copilot-cleanup-20260123 -- .

# 只回滚copilot-custom-prompts目录
git checkout pre-copilot-cleanup-20260123 -- 5.Misc/copilot-custom-prompts/

# 提交回滚
git commit -m "revert: 回滚到清理前的备份状态"

# 推送到远程（如果需要）
git push origin main
git push origin pre-copilot-cleanup-20260123
```

### 方式2：只回滚特定文件

```bash
# 回滚单个文件
git checkout pre-copilot-cleanup-20260123 -- 5.Misc/copilot-custom-prompts/文件名.md

# 回滚多个文件
git checkout pre-copilot-cleanup-20260123 -- 5.Misc/copilot-custom-prompts/苏格拉底式*.md

# 查看特定文件的备份状态
git show pre-copilot-cleanup-20260123:5.Misc/copilot-custom-prompts/文件名.md
```

### 方式3：比较差异

```bash
# 查看备份与当前差异
git diff pre-copilot-cleanup-20260123 -- 5.Misc/copilot-custom-prompts/

# 查看特定文件的差异
git diff pre-copilot-cleanup-20260123 -- 5.Misc/copilot-custom-prompts/文件名.md

# 查看备份的文件列表
git ls-tree -r pre-copilot-cleanup-20260123 --name-only | grep "copilot-custom-prompts"
```

---

## 🚨 紧急回滚场景

### 场景1：清理后发现重要文件被误删

```bash
# 立即停止所有清理操作
# 恢复所有删除的文件
git checkout pre-copilot-cleanup-20260123 -- 5.Misc/copilot-custom-prompts/
git add 5.Misc/copilot-custom-prompts/
git commit -m "urgent: 恢复误删的提示词文件"
```

### 场景2：合并后发现功能丢失

```bash
# 查看被合并的原始文件
git show pre-copilot-cleanup-20260123:5.Misc/copilot-custom-prompts/原始文件.md

# 创建新分支从备份提取特定功能
git checkout -b restore-feature
git checkout pre-copilot-cleanup-20260123 -- 5.Misc/copilot-custom-prompts/原始文件.md
# 提取需要的功能并合并回主分支
```

### 场景3：索引文件损坏

```bash
# 恢复索引文件
git checkout pre-copilot-cleanup-20260123 -- 5.Misc/copilot-custom-prompts/_Index_of_copilot-custom-prompts.md
git add 5.Misc/copilot-custom-prompts/_Index_of_copilot-custom-prompts.md
git commit -m "fix: 恢复损坏的索引文件"
```

---

## 📊 备份对比

### 清理前状态（备份）
- 文件总数: 288个
- 高价值核心: 25个
- 中价值辅助: ~150个
- 低价值冗余: ~113个

### 预期清理后状态
- 文件总数: ~195个
- 高价值核心: 25个（保持不变）
- 中价值辅助: ~120个
- 低价值冗余: ~50个（大幅减少）

### 减少量
- 删除: ~80个文件（28%）
- 合并: ~15个文件
- 净减少: ~93个文件（32%）

---

## ✅ 验证清理结果

### 验证步骤

```bash
# 1. 检查文件数量
find 5.Misc/copilot-custom-prompts -name "*.md" | wc -l

# 2. 检查核心文件是否保留
ls 5.Misc/copilot-custom-prompts/苏格拉底式提问.md
ls 5.Misc/copilot-custom-prompts/费曼学习法教学专家.md

# 3. 检查低价值文件是否删除
ls 5.Misc/copilot-custom-prompts/Remove URLs.md  # 应该失败

# 4. 重新生成索引
# 使用Zoottelkeeper插件或手动更新索引文件

# 5. 测试常用提示词
# 在Obsidian中测试几个常用的提示词是否能正常工作
```

### 性能验证

```bash
# 检查文件大小
du -sh 5.Misc/copilot-custom-prompts/

# 查看最大的文件
find 5.Misc/copilot-custom-prompts -name "*.md" -exec du -h {} \; | sort -rh | head -10

# 查看未使用的文件（基于last-used字段）
grep -r "copilot-command-last-used: 0" 5.Misc/copilot-custom-prompts/
```

---

## 🎯 下一步行动

### 立即执行（第一阶段）
- [x] 创建备份commit
- [x] 创建备份tag
- [x] 创建回滚指南
- [ ] 执行60个文件的删除操作
- [ ] 验证删除结果

### 本周执行（第二阶段）
- [ ] 执行30个文件的合并操作
- [ ] 更新索引文件
- [ ] 测试合并后的功能
- [ ] 创建新的commit

### 本月执行（第三阶段）
- [ ] 实施目录分类重构
- [ ] 创建使用指南文档
- [ ] 建立文件质量评估机制
- [ ] 创建最终commit

---

## 📞 问题排查

### 如果git checkout失败

```bash
# 可能的原因：
1. 文件有未提交的更改
2. Git工作区脏乱

# 解决方案：
git stash
git checkout pre-copilot-cleanup-20260123 -- 5.Misc/copilot-custom-prompts/
git stash pop
```

### 如果tag无法访问

```bash
# 检查tag是否存在
git tag -l

# 如果tag不存在，从commit恢复
git checkout b47503a -- 5.Misc/copilot-custom-prompts/
git commit -m "restore: 从commit恢复备份"
```

### 如果文件路径有问题

```bash
# Windows路径问题
# 使用双引号包裹路径
git checkout pre-copilot-cleanup-20260123 -- "5.Misc/copilot-custom-prompts/"

# 或使用正斜杠
git checkout pre-copilot-cleanup-20260123 -- 5.Misc/copilot-custom-prompts/
```

---

## 📝 备份清单

- [x] 所有文件已提交到git
- [x] 创建了备份commit (b47503a)
- [x] 创建了备份tag (pre-copilot-cleanup-20260123)
- [x] 创建了回滚指南（本文档）
- [ ] 开始执行清理操作
- [ ] 验证清理结果
- [ ] 提交清理后的更改
- [ ] 创建清理完成tag

---

**重要提醒**:
1. 在每次大的清理操作后，都要创建新的checkpoint
2. 定期push到远程仓库
3. 如果发现任何问题，立即使用此指南回滚
4. 保留备份tag至少3个月

**回滚命令速查**:
```bash
# 完全回滚
git checkout pre-copilot-cleanup-20260123 -- 5.Misc/copilot-custom-prompts/
git commit -m "revert: 回滚到清理前状态"
```
