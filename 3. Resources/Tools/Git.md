- [[GitHub Actions]]
- [[Github Gist JavaScript 的精彩代码片段]]
- [[2. Areas/BackEnd/Java/github上类似项目.md]]
- [[1. Projects/周月总结/GitHub中文排行榜.md]]
- [[+ Encounters/dailyNotes/手机github笔记试用.md]]
###  git基本用法:

```bash
# 克隆仓库
git clone <仓库地址>
# 查看状态
git status 
# 添加文件到暂存区
git add <文件名> 
# 提交更新
git commit -m "提交信息"
# 推送到远程仓库
git push origin master
# 拉取最新更新
git pull origin master
# 查看提交历史
git log
# 回退到上一个版本
git checkout HEAD^ 
# 新建并切换分支
git checkout -b new-branch
# 切换分支
git checkout master
# 合并分支
git merge new-branch
# 处理冲突后提交
git add .
git commit -m "resolve conflict"
# 删除分支
git branch -d new-branch
```
使用git可以进行版本控制,通过add、commit、push、pull等命令来管理代码。
需要注意处理冲突,保持主分支稳定。熟练使用分支来开发新功能。

`git reset --hard HEAD` 是一个非常强大的 Git 命令，用于将工作目录和暂存区恢复到最近一次提交（即 `HEAD`）的状态。这个命令会丢弃所有未提交的更改，包括已暂存的更改和未暂存的更改。因此，在使用这个命令之前，你需要确保你确实不再需要这些更改，因为它们将无法恢复。

### 命令详解

#### 语法
```sh
git reset --hard HEAD
```

#### 作用
- **工作目录**：将工作目录中的文件恢复到 `HEAD` 状态。
- **暂存区**：将暂存区中的文件恢复到 `HEAD` 状态。

### 使用场景

1. **撤销未提交的更改**：
   - 如果你在本地做了很多更改，但决定放弃这些更改，可以使用 `git reset --hard HEAD` 将工作目录和暂存区恢复到最近一次提交的状态。

2. **解决冲突**：
   - 在合并或拉取过程中出现冲突时，有时需要放弃当前的更改，从头开始解决冲突，可以使用 `git reset --hard HEAD` 来恢复到合并前的状态。

### 示例

假设你在一个项目中做了以下操作：

1. 修改了一些文件。
2. 暂存了一些文件。
3. 决定放弃所有这些更改。

你可以使用以下命令：

```sh
git reset --hard HEAD
```

### 注意事项

1. **丢失未提交的更改**：
   - 使用 `git reset --hard HEAD` 会永久删除所有未提交的更改，包括已暂存的更改和未暂存的更改。因此，在执行这个命令之前，确保你不再需要这些更改。

2. **备份更改**：
   - 如果你不确定是否要丢弃更改，建议先将更改备份到其他地方，然后再执行 `git reset --hard HEAD`。

3. **团队协作**：
   - 在团队协作中，使用 `git reset --hard HEAD` 可能会影响到其他团队成员的工作。确保在团队中沟通清楚，避免不必要的麻烦。

### 替代方案

如果你只是想撤销部分更改，可以考虑以下替代方案：

1. **撤销特定文件的更改**：
   ```sh
   git checkout -- <file>
   ```
   这个命令会将指定文件恢复到 `HEAD` 状态，但不会影响其他文件。

2. **撤销暂存区的更改**：
   ```sh
   git reset
   ```
   这个命令会将暂存区的更改取消，但不会影响工作目录中的更改。

3. **撤销最后一次提交**：
   ```sh
   git reset --soft HEAD~1
   ```
   这个命令会将最后一次提交取消，但保留工作目录和暂存区的更改，方便你重新提交。

### 总结

`git reset --hard HEAD` 是一个非常强大的命令，可以快速恢复到最近一次提交的状态，但使用时需要谨慎，因为它会永久删除未提交的更改。希望这些解释能帮助你更好地理解和使用这个命令。如果有任何其他问题，请随时提问。