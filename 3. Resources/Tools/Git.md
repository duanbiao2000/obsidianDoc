- [[GitHub Actions]]
- [[Github Gist JavaScript 的精彩代码片段]]
- [[2. Areas/BackEnd/Java/github上类似项目.md]]
- [[GitHub中文榜]]
- [[+ Encounters/dailyNotes/手机github笔记试用.md]]
###  git基本用法:

```bash

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

`git reset --hard HEAD` 是一个非常强大的 Git 命令，用于将工作目录和暂存区恢复到最近一次提交（即 `HEAD`）的状态。这个命令会丢弃所有未提交的更改，包括已暂存的更改和未暂存的更改。因此，在使用这个命令之前，你需要确保你确实不再需要这些更改，因为它们将无法恢复。

### 命令详解

#### 语法
```sh
git reset --hard HEAD
```


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