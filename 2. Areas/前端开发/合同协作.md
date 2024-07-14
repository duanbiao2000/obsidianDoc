当然可以，下面是一些基本步骤：

1. 创建 GitHub 仓库

在命令行中使用 git 命令创建一个新的 GitHub 仓库，具体操作如下：

```
# 创建一个空目录
mkdir my_project
cd my_project

# 初始化 Git 仓库
git init

# 添加远程仓库地址
git remote add origin https://github.com/username/repo-name.git

# 提交代码并推送到远程分支
git add .
git commit -m "initial commit"
git push -u origin master
```

这将会在 GitHub 上创建一个新项目，并且把你本地项目同步到该项目。其中 `"https://github.com/username/repo-name.git"` 是你自己的 GitHub 仓库地址，需要根据实际情况进行替换。

2. 克隆代码到本地

在命令行中使用 `git clone` 命令克隆项目代码：

```
git clone https://github.com/username/repo-name.git
cd repo-name
```

3. 创建分支

在命令行中使用 `git branch <branch-name>` 命令创建一个新的分支，以便于团队成员在不影响主分支的情况下开展工作：

```
# 创建新分支
git branch fix-bug-xxx

# 切换到新分支
git checkout fix-bug-xxx

# 创建并切换到新分支（两个步骤合并）
git checkout -b fix-bug-xxx
```

4. 修改代码并提交

在新的分支上进行代码修改，修改完成后参考下面的命令提交：

```
# 添加代码变化到缓存区
git add .

# 提交代码变化
git commit -m "Fix bug xxx"

# 推送代码变化到远程分支
git push origin fix-bug-xxx
```

此时你已经向远程仓库推送了一个新的分支，而其他合作者可以通过 PR 的方式进入该分支。

5. 合并代码

为了将分支中的代码合并到主分支中，你需要先切换回主分支：

```
git checkout master
```

然后使用 `git merge` 命令将分支代码合并到主分支中，并将其删除：

```
# 合并分支到主分支
git merge fix-bug-xxx

# 删除分支
git branch -d fix-bug-xxx

# 推送变化
git push origin master
```

6. 发起 Pull Request

最后一步是由开发者自己发起 Pull Request，以便团队成员能够审查和修改所做的工作。这项操作可以通过命令行或者网页版 GitHub 实现。在您完成分支的编辑后，只需：

- 登录 GitHub 页面。
- 找到正在开发的项目。
- 选择新分枝（”Branches“），然后点击 “New pull request”。
- 在提供的对话框中输入有关请求的详细信息，描述代码修改以及相关更改理由等。
- 最后再次单击 “Create pull request” 完成合并请求的创建。

以上就是使用命令行操作共享代码或者协作开发 Github 项目可能用到的基本步骤，通过这些命令，您可以高效而安全地进行 GitHub 协同工作，并且在跟团队互动时更容易成功管理共享。