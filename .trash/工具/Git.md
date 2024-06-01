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

 使用Git进行版本控制的一般步骤是:

1. 初始化本地仓库
```
git init
```
2. 添加和提交修改
- 检查文件状态
```
git status
```
- 添加修改到暂存区
```
git add <filename>
```
- 提交更新,添加提交信息
```
git commit -m "commit message" 
```
3. 查看提交历史
```
git log
```
4. 版本回退
```
git reset --hard <commit-id>
```
5. 创建分支
```
git branch <branchname>
```
6. 切换分支
```
git checkout <branchname>
```
7. 合并分支
```
git merge <branchname>
```
8. 推送到远程仓库
```
git push origin master
```
9. 从远程仓库拉取
```
git pull origin master
```
通过上述命令可以在本地对代码进行版本控制,并推送到远程仓库中。

####  GitHub基本知识:

1. 版本控制
- 初始化仓库、添加提交修改、查看日志等基本命令
```
git init
git add .
git commit -m "init repo" 
git log
```
- 分支管理、合并、tag等高级命令
```
git branch feature-x
git checkout feature-x
git merge feature-x
git tag v1.0.0
```
2. 远程协作 
- clone、pull、push、fetch等远程同步命令
```
git clone url
git pull origin master
git push origin master
```
- 创建Pull Request进行代码review
- 解决冲突
3. GitHub Pages建立静态页面
- 创建gh-pages分支
- 配置GitHub Pages
4. 使用GitHub Actions实现持续集成
- 添加workflow配置文件
- 在push、pull request等事件触发自动化流程
5. 发布包到GitHub Packages
- 配置 .npmrc 和 package.json
- 发布包 npm publish
  掌握这些知识可以大大提高工作效率,进行开源项目协作。

####  GitHub Pages个人网站

使用GitHub Pages搭建个人网站的步骤如下:

1. 创建仓库
  创建一个公开仓库,仓库名为<用户名>.github.io
2. 添加网页内容
  在仓库中创建一个index.html文件,并添加一些简单的网页内容。
3. 推送到GitHub
  将代码推送到GitHub远程仓库。
4. 启用GitHub Pages
  在仓库设置页面,找到GitHub Pages选项,选择master branch作为源,保存。
5. 访问网站
  访问 https://<用户名>.github.io 即可看到部署的个人网站。
6. 自定义域名
  可以在GitHub Pages设置中配置自定义域名,绑定到这个网站上。
7. 主题和构建
  可以使用Jekyll等静态站点生成器,或者添加CSS/JS脚本来美化网站主题和功能。
8. 持续迭代
  随时通过push新的内容来持续迭代个人网站。
  以上步骤就可以使用GitHub Pages快速搭建一个静态个人网站,并持续维护更新。