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
精通Git对软件工程师至关重要，错误的Git操作可能导致代码混乱。
<!--more-->

[🔄 13个Git超速技巧：快速提升你的开发流程_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1XTD2YHEko/?vd_source=7038f96b6bb3b14743531b102b109c43)

### 详细笔记列表：《13个Git超速技巧：快速提升你的开发流程》

#### 1. Git的重要性

- 精通Git对软件工程师至关重要，错误的Git操作可能导致代码混乱。

#### 2. Git基础

- [[Git]] commit：保存代码快照的基本命令。

#### 3. 提交代码的更好方法

- 使用`[[Git]] commit -am`直接提交，自动添加当前工作目录中的所有文件。

#### 4. Git别名

- 使用`[[Git]] config`创建别名，如`ac`（add和commit的缩写）。

#### 5. 修改提交

- 使用`[[Git]] commit --amend`修改最近一次提交。

#### 6. 更新上次提交

- 使用`[[Git]] commit --amend --no-edit`添加新文件到上次提交。

#### 7. 强制推送

- 使用`[[Git]] push -f`覆盖远程分支，但有丢失远程提交的风险。

#### 8. 撤销提交

- 使用`[[Git]] revert`撤销提交，返回到之前的状态。

#### 10. GitHub代码空间

- 在云中设置代码空间，提供VS Code的全部功能。

#### 12. 更改默认分支名

- 将默认分支从`master`更改为`main`或其他名称。

> [!NOTE]
> 更改Git仓库的默认分支名是一个常见的操作，特别是在一些组织和项目中决定不再使用`master`作为默认分支名时。以下是如何将默认分支从`master`更改为`main`或其他名称的具体方法：
> 
> ### 步骤1：本地更改默认分支名
> 1. 首先，确保你的本地分支是最新的，通过执行`[[Git]] pull`来获取所有最新的更改。
> 2. 检出到`master`分支（或当前的默认分支）。
>    ```bash
>    [[Git]] checkout master
>    ```
> 3. 重命名分支为`main`（或你选择的其他名称）。
>    ```bash
>    [[Git]] branch -m master main
>    ```
>    这里的`-m`标志表示移动分支，等同于重命名。
> 
> ### 步骤2：推送更改到远程仓库
> 1. 推送本地的`main`分支到远程仓库，并设置为默认分支。
>    ```bash
>    [[Git]] push -u origin main
>    ```
>    这里的`-u`标志用于设置上游（tracking branch）。
> 
> 2. 如果远程仓库中已经有了`master`分支，你可能需要强制推送，但请注意，这会覆盖远程分支的历史。
>    ```bash
>    [[Git]] push origin --delete master
>    ```
>    然后再次推送`main`分支：
>    ```bash
>    [[Git]] push --set-upstream origin main
>    ```
> 
> ### 步骤3：更新远程仓库的默认分支设置
> 1. 在GitHub、GitLab、Bitbucket等平台上，你需要更新仓库的设置，将`main`（或你选择的新名称）设置为默认分支。
>    - 通常在仓库的“Settings”或“Repository settings”部分，你可以找到“Default branch”或类似的选项。
>    - 选择`main`作为默认分支并保存更改。
> 
> ### 步骤4：更新团队成员的工作流
> 1. 通知团队成员新的默认分支名，并确保他们更新本地的跟踪分支。
>    ```bash
>    [[Git]] branch -m master main
>    [[Git]] branch --unset-upstream master
>    [[Git]] branch -u origin/main
>    ```
> 2. 确保所有团队成员都更新了他们的本地配置，并且知道如何推送到新的默认分支。
> 
> ### 注意事项
> - 在执行这些步骤之前，最好与团队成员沟通，确保每个人都了解更改的流程和原因。
> - 更改默认分支名可能会影响CI/CD流程和其他自动化脚本，确保这些也相应更新。
> - 如果项目中有大量的文档和指导材料提到了`master`分支，也需要进行相应的更新。
> 
> 通过这些步骤，你可以将Git仓库的默认分支从`master`更改为`main`或其他任何你喜欢的名称，以适应项目或组织的命名约定。
> 

#### 13. 查看提交历史

- 使用`[[Git]] log --oneline --graph`查看简化的提交历史。

#### 14. 二分查找问题提交

- 使用`[[Git]] bisect`从已知错误的提交开始查找问题。

#### 15. 压缩提交

- 使用`[[Git]] rebase -i`压缩多个提交到一个。

> [!NOTE]
> 压缩提交，也称为“交互式变基”（Interactive Rebase），是一种将多个提交合并为一个或重新组织提交顺序的过程。以下是如何使用`[[Git]] rebase -i`来压缩多个提交到一个的具体方法：
> 
> ### 步骤1：启动交互式变基
> 1. 确定要压缩的提交的范围。例如，如果你想要压缩最近5个提交，你需要确定这5个提交的起始点。
> 2. 运行`[[Git]] rebase -i HEAD~5`命令。这里的`HEAD~5`表示从当前分支的最近5个提交开始变基。
> 
> ### 步骤2：选择要压缩的提交
> 1. [[Git]] 会打开一个文本编辑器，列出最近5个提交的默认消息。
> 2. 每个提交前面都有一个`pick`命令。要压缩提交，你需要将除了第一个提交以外的所有`pick`命令改为`squash`（或简写为`s`）。
> 
> ### 步骤3：保存并退出编辑器
> 1. 保存编辑器中的更改并退出。[[Git]] 将开始变基过程，并尝试将选定的提交压缩到一起。
> 2. 如果有冲突，[[Git]] 会停止并让你解决。解决冲突后，使用`[[Git]] add`添加更改，并使用`[[Git]] rebase --continue`继续变基。
> 
> ### 步骤4：编写最终提交消息
> 1. 一旦所有提交被压缩，[[Git]] 会提示你输入一个新的提交消息，因为它将所有选定的提交合并为一个。
> 2. 编写一个清晰、简洁的提交消息，描述所有更改的总体内容。
> 3. 保存并关闭编辑器，完成压缩提交。
> 
> ### 示例
> 假设你有以下提交历史：
> 
> ```
> commit1: Fix bug in login page
> commit2: Add user registration feature
> commit3: Improve user interface
> commit4: Fix minor UI bugs
> commit5: Optimize database queries
> ```
> 
> 你想要将`commit2`到`commit5`压缩成一个提交。运行`[[Git]] rebase -i HEAD~4`（因为`HEAD~4`会包括从当前HEAD回溯的4个提交），然后编辑如下：
> 
> ```
> pick commit1: Fix bug in login page
> squash commit2: Add user registration feature
> squash commit3: Improve user interface
> squash commit4: Fix minor UI bugs
> squash commit5: Optimize database queries
> ```
> 

#### 16. Git钩子

- 使用`[[Git]] hooks`在特定事件发生时运行代码。
以下是一些具体的方法，展示如何使用Git钩子来实现上述经典使用场景：

> [!NOTE]
> ### 1. pre-commit（预提交钩子）
> **目的**：在提交前检查代码风格和运行单元测试。
> **方法**：
> - 在`.[[Git]]/hooks`目录下创建或编辑`pre-commit`文件，并给予执行权限（`chmod +x pre-commit`）。
> - 编写脚本，例如使用Shell脚本或Python，执行代码检查和测试命令。
> - 如果检查或测试失败，使用`exit 1`退出脚本，阻止提交。
> 
> ```bash
> #!/bin/sh
> # 运行代码风格检查和单元测试
> npm run lint
> npm test
> if [ $? -ne 0 ]; then
>   echo "Tests failed or code style issues found"
>   exit 1
> fi
> ```
> 
> ### 2. pre-push（预推送钩子）
> **目的**：在推送前确保本地分支是最新的。
> **方法**：
> - 在`.[[Git]]/hooks`目录下创建或编辑`pre-push`文件，并给予执行权限。
> - 编写脚本，检查当前分支是否已经更新。
> 
> ```bash
> #!/bin/sh
> # 检查远程分支的最新状态
> remote=$([[Git]] rev-parse --symbolic-full-name @{u})
> behind=$([[Git]] rev-list --left-right --count ${remote}...HEAD)
> if [ $behind -gt 0 ]; then
>   echo "You are behind the remote branch. Please pull changes."
>   exit 1
> fi
> ```
> 
> ### 3. post-merge（合并后钩子）
> **目的**：在合并后自动格式化代码。
> **方法**：
> - 在`.[[Git]]/hooks`目录下创建或编辑`post-merge`文件，并给予执行权限。
> - 编写脚本，使用代码格式化工具格式化代码。
> 
> ```bash
> #!/bin/sh
> # 格式化代码
> npm run format
> ```
> 
> ### 4. post-checkout（检出后钩子）
> **目的**：在检出后更新项目依赖。
> **方法**：
> - 在`.[[Git]]/hooks`目录下创建或编辑`post-checkout`文件，并给予执行权限。
> - 编写脚本，执行依赖安装命令。
> 
> ```bash
> #!/bin/sh
> # 安装依赖
> npm install
> ```
> 
> ### 5. post-receive（接收后钩子）
> **目的**：在接收推送后自动部署代码。
> **方法**：
> - 在服务器上的`.[[Git]]/hooks`目录下创建或编辑`post-receive`文件，并给予执行权限。
> - 编写脚本，执行部署命令。
> 
> ```bash
> #!/bin/sh
> # 部署代码
> [[Git]] checkout -b deploy-branch
> npm run deploy
> ```
> 
> ### 6. pre-rebase（变基前钩子）
> **目的**：阻止在包含未提交更改的分支上执行变基。
> **方法**：
> - 在`.[[Git]]/hooks`目录下创建或编辑`pre-rebase`文件，并给予执行权限。
> - 编写脚本，检查是否有未提交的更改。
> 
> ```bash
> #!/bin/sh
> # 检查未提交的更改
> if [ -n "$([[Git]] status --porcelain)" ]; then
>   echo "You have uncommitted changes. Please commit or stash them before rebasing."
>   exit 1
> fi
> ```
> 
> ### 7. prepare-commit-msg（准备提交消息钩子）
> **目的**：自动填充提交消息模板。
> **方法**：
> - 在`.[[Git]]/hooks`目录下创建或编辑`prepare-commit-msg`文件，并给予执行权限。
> - 编写脚本，根据需要修改提交消息。
> 
> ```bash
> #!/bin/sh
> # 自动填充提交消息模板
> COMMIT_MSG_FILE=$1
> COMMIT_HASH=$2
> AUTHOR=$3
> COMMITTER=$4
> echo "Enter a conventional commit message:"
> echo "feat: add new feature" > $COMMIT_MSG_FILE
> ```
> 
> 这些脚本示例提供了基本的框架，你可以根据具体需求进行调整和扩展。记得在编写脚本后，确保它们具有执行权限，并在团队中共享这些钩子脚本，以便所有成员都能使用。
> 

#### 17. 与远程仓库同步

- 使用`[[Git]] fetch`和`[[Git]] reset --hard`返回到远程仓库的状态。

> [!NOTE]
> 如果你想要放弃本地的更改并使本地仓库的状态与远程仓库同步，可以使用以下步骤：
> 
> 1. **获取远程仓库的最新状态**：
>    - 使用 `[[Git]] fetch` 命令来获取远程仓库的最新更改，但不会自动合并到你的当前分支。
> 
> 2. **重置本地分支到远程状态**：
>    - 使用 `[[Git]] reset --hard <remote>/<branch>` 命令，其中 `<remote>` 通常是 `origin`，`<branch>` 是你想要同步的远程分支名称，比如 `main` 或 `master`。这个命令会将你的本地分支强制重置到与远程分支相同的状态，放弃本地所有未提交的更改和提交。
> 
> 例如，如果你想要将本地的 `main` 分支重置到与远程 `origin/main` 相同的状态，你可以执行以下命令：
> 
> ```bash
> [[Git]] fetch origin
> [[Git]] reset --hard origin/main
> ```
> 
> 请注意，这个操作是不可逆的，它会丢失所有本地未推送的更改。因此，在执行这些操作之前，确保你确实想要放弃这些更改，或者已经将它们备份到别的地方。

#### 18. 清理未跟踪文件
- 使用`[[Git]] clean`删除未跟踪的文件。

#### 19. 切换回上一个分支
- 使用`[[Git]] checkout -`快速切换回上一个分支。