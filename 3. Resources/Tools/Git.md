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

