---
aliases: 🔄 13个Git超速技巧：快速提升你的开发流程
createdAt: 2024-11-10 19:41
categories:
  - Effective
tags:
  - Creative/Github
  - Effective/Workflow
updateAt: 2024-11-10 20:08
---
```ad-tip
title: 压缩提交
每次成功的重构后我都会提交代码，如果待会不小心搞砸了，我便能轻松回滚到上一个可工作的状态。把代码推送（push）到远端仓库前，我会把零碎的修改压缩成一个更有意义的提交（commit）。
```

---

### **1. 初始状态**
假设你正在开发一个项目，当前代码库的状态如下：
```bash
$ git status
On branch main
nothing to commit, working tree clean
```

---

### **2. 开始重构并提交零碎修改**
你在重构过程中，可能会有多个小改动。为了确保每次修改都有记录，你可以频繁提交代码。

#### （1）第一次小改动
- 修改了 `utils.py` 文件中的某个函数。
- 提交改动：
  ```bash
  $ git add utils.py
  $ git commit -m "Refactor: Simplify function logic in utils.py"
  ```

#### （2）第二次小改动
- 修改了 `main.py` 文件中的调用逻辑。
- 提交改动：
  ```bash
  $ git add main.py
  $ git commit -m "Refactor: Update main.py to use simplified function"
  ```

#### （3）第三次小改动
- 修复了一个测试用例以适配新的逻辑。
- 提交改动：
  ```bash
  $ git add tests/test_utils.py
  $ git commit -m "Fix: Update test case for refactored function"
  ```

此时，你的提交历史可能如下：
```bash
$ git log --oneline
abc1234 Fix: Update test case for refactored function
def5678 Refactor: Update main.py to use simplified function
ghi9012 Refactor: Simplify function logic in utils.py
```

---

### **3. 如果搞砸了：轻松回滚**
如果你在后续的重构中不小心引入了错误，可以通过 `git reset` 或 `git revert` 回滚到上一个可工作的状态。

#### （1）回滚到最后一次成功提交
- 使用 `git reset` 回退到上次提交：
  ```bash
  $ git reset --hard HEAD
  ```
  这会丢弃所有未提交的更改，并恢复到最近一次提交的状态。

#### （2）回滚到更早的提交
- 如果需要回滚到之前的某个提交（例如 `ghi9012`），可以运行：
  ```bash
  $ git reset --hard ghi9012
  ```
  注意：这会丢弃该提交之后的所有更改。

---

### **4. 推送前整理提交历史**
在推送代码到远端仓库之前，建议将零碎的提交压缩成一个更有意义的提交。

#### （1）使用 `git rebase` 压缩提交
- 启动交互式变基（interactive rebase）：
  ```bash
  $ git rebase -i HEAD~3
  ```
  这会打开一个编辑器，显示最近的 3 次提交：
  ```
  pick ghi9012 Refactor: Simplify function logic in utils.py
  pick def5678 Refactor: Update main.py to use simplified function
  pick abc1234 Fix: Update test case for refactored function
  ```

- 将后两次提交标记为 `squash`（或简写为 `s`），以便将它们合并到第一次提交中：
  ```
  pick ghi9012 Refactor: Simplify function logic in utils.py
  squash def5678 Refactor: Update main.py to use simplified function
  squash abc1234 Fix: Update test case for refactored function
  ```

- 保存并关闭编辑器后，Git 会提示你为合并后的提交提供一个新的提交信息：
  ```
  Refactor: Simplify function logic and update usage across codebase
  ```

- 最终提交历史变为：
  ```bash
  $ git log --oneline
  jkl3456 Refactor: Simplify function logic and update usage across codebase
  ```

#### （2）强制推送整理后的提交
- 如果分支已经推送到远端，需要使用 `--force` 强制推送：
  ```bash
  $ git push origin main --force
  ```

---

### **5. 总结**
通过以上步骤，你可以：
1. **频繁提交**：在重构过程中随时记录小改动，确保可以轻松回滚。
2. **轻松回滚**：如果搞砸了，可以通过 `git reset` 或 `git revert` 恢复到上一个可工作的状态。
3. **整理提交历史**：在推送前使用 `git rebase` 压缩零碎的提交，使提交历史更加清晰和有意义。

这种工作流不仅能提高代码管理的效率，还能让你在团队协作中保持整洁的提交记录。