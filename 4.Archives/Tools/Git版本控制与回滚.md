---
view-count: 5
related:
  - "[[commit 和 PR的选择]]"
  - "[[单一职责commit范例100例]]"
  - "[[2025-12-20-常用开发标记]]"
  - "[[变更日志 (Change Log)]]"
  -
---

# Git 撤销与追踪协议：时空管理实战

## 1. 核心逻辑：指针系统与快照

Git 的本质是**不可变快照（Commit）**与**移动指针（Branch/HEAD）**。版本控制的核心在于：通过操作指针，在不同快照间实现安全回溯。

## 2. 撤销指令矩阵 (Comparison)

| 指令                     | 机制                 | 适用场景 (ROI)              | 风险等级      |
| :--------------------- | :----------------- | :---------------------- | :-------- |
| **`git revert`**       | **新增**一个提交来抵消指定变更。 | **公共分支**：不破坏他人历史，最安全。   | ⚪ 低 (推荐)  |
| **`git reset --soft`** | 移动 HEAD，保留修改在暂存区。  | **本地清理**：合并多个琐碎提交。      | 🟡 中      |
| **`git reset --hard`** | 强制抹除指定提交后的所有更改。    | **彻底废弃**：当前尝试完全失败，推倒重来。 | 🔴 高 (慎用) |

## 3. 行动指南：撤销三步走 (Actionable)

1. **定位（Locate）**：
   - `git log --oneline -n 5`：快速锁定目标提交的哈希值。
2. **执行（Execute）**：
   - *本地写坏了？* $\rightarrow$ `git reset --hard <hash>`。
   - *推送到远程写坏了？* $\rightarrow$ `git revert <hash>`。
3. **验证（Verify）**：
   - `git status`：检查当前工作区状态。

## 4. 决策指南：场景短路 (Scenario)

- **场景 A：我想看看 3 天前的代码，但不改变现状**
  - *Action*：`git checkout <hash>` (进入分离 HEAD 状态) $\rightarrow$ 阅后 `git switch -` 返回。
- **场景 B：刚提交完发现漏了一个文件**
  - *Action*：`git add <file>` $\rightarrow$ `git commit --amend --no-edit`。
- **场景 C：误删了分支或执行了错误的 reset --hard**
  - *Action*：`git reflog`（Git 的后悔药，记录所有指针变动） $\rightarrow$ 找回哈希值并重置。

## 5. 质量红线 (Safeguards)

- [ ] **严禁**对已推送到远程的分支执行 `git reset`（除非是个人独立分支且确定无冲突）。
- [ ] **优先**使用 `git switch` 和 `git restore`（Git 2.23+ 新语法），语义更清晰，降低心智负担。

---

### 质量自检

- **压缩率**：约 70% (剔除命令输出示例与定义性说明)
- **层级**：2 层 (核心逻辑/矩阵/行动指南/决策指南/红线)
- **5秒测试**：一眼可见 `revert` 与 `reset` 的本质区别及适用红线。
