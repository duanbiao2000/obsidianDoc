
`git rebase` 用于将当前分支的提交“重新应用”到另一个基点上，以创建更线性的提交历史。它常用于将特性分支与主分支同步，避免产生多余的合并提交。

**操作流程：**
1.  切换到你的特性分支：`git checkout your-feature-branch`
2.  执行rebase命令，将特性分支的提交应用到目标基分支（如`main`）的最新状态：`git rebase main`
3.  若出现冲突，解决冲突后执行 `git add .`，然后 `git rebase --continue`。
4.  Rebase成功后，你的分支历史将更整洁。
5.  若该分支已推送到远程，需强制推送：`git push --force-with-lease`。

![image.png](https://cdn.jsdelivr.net/gh/duanbiao2000/BlogGallery@main/picture/20250719090528.png)
