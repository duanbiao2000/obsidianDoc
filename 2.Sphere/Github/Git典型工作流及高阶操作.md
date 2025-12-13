---
aliases: 🔄 13个Git超速技巧：快速提升你的开发流程
date: 2024-11-10 19:41
categories:
  - Effective
tags:
  - Domain/Creativity/Github
  - Status/Workflow
update: 2024-11-10 20:08
view-count: 2
---
```sh
#!/bin/bash

# ============================================================================
# 高级 Git 团队协作工作流 - Monorepo + 多Repo 环境
# 适用于大规模团队：Google/Meta 风格的协作模式
# ============================================================================

# ============================================================================
# 第一部分：Monorepo 核心工作流
# ============================================================================

# 【教练提示】在 monorepo 中，关键是精细化追踪各个模块的依赖关系
# 和所有权（ownership），避免无关改动对整个仓库的影响

# 1. 初始化 monorepo 结构
# 场景：设置一个包含多个微服务的 monorepo（如 Google 内部结构）
mkdir -p monorepo/{services,libs,tools,configs}
cd monorepo
git init

# 关键配置：启用 sparse-checkout（只检出你关心的目录）
git config core.sparseCheckout true

# 【教练提示】这里的 sparse-checkout 能大幅减少本地工作目录的体积
# 对于包含数千个目录的 monorepo 来说，这可以将 git 操作速度提升 10 倍+
echo "services/auth/" >> .git/info/sparse-checkout
echo "services/api/" >> .git/info/sparse-checkout
echo "libs/common/" >> .git/info/sparse-checkout
echo "configs/" >> .git/info/sparse-checkout

# 2. 设置团队级别的 git hook（自动化质量控制）
# 目标：在 commit 前自动检查改动的模块所有权

cat > .githooks/pre-commit << 'EOF'
#!/bin/bash
# 【教练提示】这个 hook 确保开发者不会意外修改不属于他们的模块

CHANGED_FILES=$(git diff --cached --name-only)
OWNED_DIRS="services/auth services/api libs/common"

for file in $CHANGED_FILES; do
  dir=$(echo $file | cut -d'/' -f1-2)
  
  # 检查 CODEOWNERS 文件中的权限
  if ! grep -q "$(whoami)" CODEOWNERS 2>/dev/null; then
    # 允许改动但给出警告
    echo "⚠️  WARNING: $dir might require review from code owner"
  fi
done

exit 0
EOF

chmod +x .githooks/pre-commit

# 【教练提示】让团队成员使用自定义 hooks 目录
# 这样不会被全局 .git/hooks 覆盖
git config core.hooksPath .githooks

# 3. 创建 CODEOWNERS 文件（模块所有权管理）
cat > CODEOWNERS << 'EOF'
# services/auth 模块由 auth-team 负责
services/auth/           @auth-team @security-lead
services/auth/tests/     @auth-team @qa-team

# services/api 模块由 platform-team 负责
services/api/            @platform-team @api-lead
services/api/docs/       @platform-team @tech-writers

# 共享库由多个团队维护
libs/common/             @platform-team @infra-team
libs/common/logging/     @infra-team

# 配置文件由 DevOps 管理
configs/                 @devops-team
EOF

# ============================================================================
# 第二部分：高效的分支策略（Trunk-Based Development 变体）
# ============================================================================

# 【教练提示】大规模团队通常采用 trunk-based development
# 而不是长期存活的 feature branch，这能大幅减少合并冲突

# 4. 设置保护的主分支和开发分支
# 在团队的 Git 服务器配置中（GitHub/GitLab）：
# - main: 生产分支，只接受 rebase merge，需要 code review + CI 通过
# - develop: 集成分支，快速迭代，接受 squash merge

# 5. 创建基于模块的短期特性分支
# 场景：修复 auth 服务的登录问题

# 【教练提示】分支命名规范帮助自动化和追踪：
# 格式：<team>/<feature-name>/<jira-ticket>
# 示例：auth/fix-oauth-token/AUTH-1234

git checkout -b auth/fix-oauth-token/AUTH-1234 develop

# 修改代码示例
echo "// Fix OAuth token expiry bug" >> services/auth/oauth.py

# 【教练提示】在 commit 前，使用 git add -p 精细化暂存
# 这能帮助你在 PR review 时清晰地展示改动意图
git add -p  # 交互式添加，逐个确认 hunk

# 6. 交互式 rebase：保持历史整洁
# 【教练提示】在推送到远程前，整理 commit 历史
# 这样代码审查者能更快地理解改动

# 假设你有 3 个 commit，需要整理
git rebase -i develop

# 在编辑器中操作：
# pick abc1234 Fix OAuth token validation
# squash def5678 Update test cases       （压缩到前一个 commit）
# reword ghi9012 Refactor token logic    （修改 commit message）

# 【教练提示】好的 commit message 格式（Google/Angular 风格）：
# <type>(<scope>): <subject>
# 
# <body>
# 
# <footer>

# 示例：
cat > commit_msg.txt << 'EOF'
fix(auth): resolve OAuth token expiry race condition

Previously, token refresh was not atomic, causing race conditions
in high-concurrency scenarios. This fix uses a distributed lock
mechanism to ensure only one refresh happens at a time.

Fixes AUTH-1234
Related-To: AUTH-1200, INFRA-5600
EOF

git commit --allow-empty -F commit_msg.txt

# 7. 推送到远程（创建 Pull Request）
git push origin auth/fix-oauth-token/AUTH-1234

# ============================================================================
# 第三部分：多 Repo 协调（Workspace 管理）
# ============================================================================

# 【教练提示】在多 repo 环境中，关键是保持各个 repo 的版本一致性
# 和依赖关系的可追踪性

# 8. 使用 git submodule 管理跨 repo 依赖
# 场景：主 repo（monorepo）依赖共享库 repo

# 添加共享库作为 submodule（在主 monorepo 中）
git submodule add https://github.com/company/shared-libs.git libs/shared
git submodule update --init --recursive

# 【教练提示】checkout 特定的 submodule 版本（pinning）
# 这是多 repo 协调的关键：确保所有开发者使用相同的依赖版本
cd libs/shared
git checkout v2.3.1  # 固定到特定版本标签
cd ../..
git add libs/shared .gitmodules
git commit -m "chore: pin shared-libs to v2.3.1"

# 9. 创建跨 repo 改动的协调流程
# 场景：修改在 shared-libs 中的 API，需要同时更新 monorepo

# 步骤 1：在 shared-libs repo 中创建 feature branch
cd ../shared-libs  # 切换到 shared-libs repo
git checkout -b shared/update-api-v3/SHARED-456 develop
echo "// API v3 changes" >> api/core.py
git add -A && git commit -m "feat(api): introduce API v3 endpoints (SHARED-456)"
git push origin shared/update-api-v3/SHARED-456

# 创建 PR，等待合并到 develop

# 步骤 2：在 monorepo 中更新 submodule 引用
cd ../monorepo
# 【教练提示】不要手动修改 submodule commit hash
# 使用自动化方式更新：
git submodule update --remote libs/shared  # 拉取最新的 shared develop
cd libs/shared && git checkout v3.0.0 && cd ../..  # 切换到发布标签
git add libs/shared
git commit -m "chore(deps): update shared-libs to v3.0.0

This includes the new API v3 endpoints. Services can now use the new
endpoints via shared.api.v3 namespace.

Depends-On: shared-libs#PR-789"

# 10. 协调跨 repo 的版本发布
# 【教练提示】使用版本标签来标记 monorepo + submodules 的一致性快照

# 在 monorepo 中创建发布标签
git tag -a release/2024-Q1-v1.5.0 -m "Production release Q1 2024

Includes:
- shared-libs@v3.0.0 (API v3)
- services/auth with OAuth 2.0 refresh fix
- services/api with new endpoints

Breaking Changes:
- Deprecated services.auth.legacy API removed

Migration Guide: docs/migration/v1.4-to-v1.5.md"

git push origin release/2024-Q1-v1.5.0

# ============================================================================
# 第四部分：高效的代码审查流程（Collaborative Workflow）
# ============================================================================

# 【教练提示】Google 风格的代码审查强调快速反馈和异步协作

# 11. 自动化审查的前置检查
# 创建 CI 配置片段（.github/workflows/review-checks.yml 的核心逻辑）

cat > review_checklist.sh << 'EOF'
#!/bin/bash
# 【教练提示】这个脚本在 PR 提交时自动运行，确保质量门槛

BRANCH=$1

# 检查 1：确保 commit message 格式正确
echo "✓ Checking commit message format..."
git log develop..$BRANCH --format=%B | grep -E "^(feat|fix|docs|style|refactor|test|chore)" || {
  echo "❌ Commits don't follow Angular format"
  exit 1
}

# 检查 2：检查改动的模块是否有相应的测试
echo "✓ Checking test coverage..."
CHANGED_MODULES=$(git diff develop..$BRANCH --name-only | cut -d'/' -f1-2 | sort -u)
for module in $CHANGED_MODULES; do
  if [[ ! -d "$module/tests" ]]; then
    echo "⚠️  $module missing tests directory"
  fi
done

# 检查 3：验证 CODEOWNERS 权限
echo "✓ Verifying code ownership..."
AUTHOR=$(git config user.email)
CHANGED_FILES=$(git diff develop..$BRANCH --name-only)
while read -r file; do
  OWNER=$(grep "$file" CODEOWNERS | awk '{print $2}' | head -1)
  if [[ -n "$OWNER" && "$OWNER" != "@*" ]]; then
    echo "  📝 $file owned by $OWNER"
  fi
done <<< "$CHANGED_FILES"

echo "✅ Pre-review checks passed!"
exit 0
EOF

chmod +x review_checklist.sh

# 12. 使用 git rebase 保持分支更新（避免"脏"的 merge commit）
# 【教练提示】当 develop 有更新时，rebase 而不是 merge
# 这样保持线性历史，便于追踪和 bisect

git fetch origin develop
git rebase origin/develop auth/fix-oauth-token/AUTH-1234

# 如果有冲突：
# git status  # 查看冲突文件
# （手动解决冲突）
# git add .
# git rebase --continue

# 13. 推送 force-push（仅在自己的分支上）
# 【教练提示】rebase 后需要 force-push，因为历史已改写
# 使用 --force-with-lease 而不是 --force，更安全
git push origin auth/fix-oauth-token/AUTH-1234 --force-with-lease

# ============================================================================
# 第五部分：合并策略与冲突解决
# ============================================================================

# 14. 配置不同场景的合并策略
# 在 monorepo 中针对不同分支使用不同策略

cat > .git/config << 'EOF'
[branch "develop"]
    # develop 使用 squash merge（保持简洁历史）
    mergeOptions = --squash
    
[branch "main"]
    # main 使用 rebase merge（绝对线性历史）
    mergeOptions = --rebase
    
[pull]
    # 全局 pull 策略：rebase 优于 merge
    rebase = true
    
[merge]
    # 冲突标记风格：更易读
    conflictStyle = diff3
EOF

# 【教练提示】diff3 style 在解决冲突时展示"祖先"版本，
# 帮助你更快地理解改动意图

# 15. 智能冲突解决：使用 re-merge 驱动程序
# 场景：两个分支都修改了同一个文件

# 配置自定义 merge 驱动（例如 Python 代码的智能合并）
git config merge.python.driver '
  if python3 -m py_compile %O %A %B 2>/dev/null; then
    mv %A.merged %A
    exit 0
  else
    exit 1
  fi
'

# 在 .gitattributes 中使用这个驱动
echo "*.py merge=python" >> .gitattributes

# 16. 解决冲突的实战技巧
# 【教练提示】当 rebase 时遇到冲突

# 查看冲突
git status

# 使用 git diff 查看冲突详情
git diff --name-only --diff-filter=U  # 只显示未合并的文件

# 使用第三方合并工具（示例：配置 VS Code 作为合并工具）
git config merge.tool vscode
git config mergetool.vscode.cmd 'code --wait $MERGED'
git mergetool  # 打开 UI 合并工具

# 或者手动解决冲突后
git add services/auth/oauth.py  # 标记为已解决
git rebase --continue

# ============================================================================
# 第六部分：跨团队协作的高级技巧
# ============================================================================

# 17. 创建功能分支的"sync point"
# 【教练提示】在长期特性开发中，定期与 develop 同步
# 防止最后合并时产生巨大冲突

# 长期特性分支（例如 3 周的大重构）
git checkout -b platform/major-refactor/PLAT-999 develop

# 每周与 develop 同步一次
git fetch origin
git rebase origin/develop  # 不是 merge，这样避免额外的 merge commit

# 18. 使用 git cherry-pick 进行选择性合并
# 场景：main 分支需要从开发分支 cherry-pick 一个紧急 bugfix

# 首先找到要 cherry-pick 的 commit
git log auth/fix-oauth-token/AUTH-1234 --oneline -5

# 【教练提示】只 cherry-pick 最后一个（最新的）commit
git checkout main
git fetch origin
git checkout -b hotfix/oauth-token-urgent origin/main
git cherry-pick abc1234  # cherry-pick 特定 commit

# 如果有冲突，解决后：
git cherry-pick --continue

git push origin hotfix/oauth-token-urgent

# 19. 批量操作：更新多个 repo
# 场景：需要在所有 repo 中应用相同的改动（例如更新依赖）

cat > update_all_repos.sh << 'EOF'
#!/bin/bash
# 【教练提示】这个脚本展示了如何协调多个 repo 的改动

REPOS=("monorepo" "shared-libs" "api-gateway" "mobile-sdk")
FEATURE_NAME="security/update-dependencies/SEC-2024"

for repo in "${REPOS[@]}"; do
  echo "Processing $repo..."
  cd "$repo"
  
  # 创建特性分支
  git checkout develop
  git pull origin develop
  git checkout -b "$FEATURE_NAME"
  
  # 执行改动（示例：更新 requirements.txt）
  pip-audit --fix > /dev/null 2>&1 || true
  
  if [[ ! -z $(git diff --cached) ]]; then
    git add -A
    git commit -m "chore(deps): security updates for Q1 2024 (SEC-2024)"
    git push origin "$FEATURE_NAME"
    echo "✓ $repo updated"
  else
    echo "⊘ $repo has no changes"
  fi
  
  cd ..
done

echo "✅ All repositories updated. Create PRs manually or via API."
EOF

chmod +x update_all_repos.sh
./update_all_repos.sh

# ============================================================================
# 第七部分：调试和追踪工具
# ============================================================================

# 20. 使用 git bisect 追踪 buggy commit
# 【教练提示】当一个 bug 出现时，自动化二分查找找到引入的 commit

git bisect start
git bisect bad HEAD        # 当前版本有 bug
git bisect good v2.3.0     # v2.3.0 是好的

# 【教练提示】git 会自动 checkout 中间的 commit
# 你测试当前版本，告诉 git 是否有 bug

git bisect good  # 或 git bisect bad

# 重复直到找到第一个坏 commit
# 完成后：
git bisect reset

# 21. 追踪代码变更的来源
# 【教练提示】当需要了解某行代码为什么存在时

# 查看某行代码的改动历史
git blame services/auth/oauth.py -L 50,100

# 查看更多信息
git log -p services/auth/oauth.py | grep -A 5 -B 5 "specific code"

# 跳过某些 commit（例如格式化提交）
echo "abc1234" >> .git-blame-ignore-revs  # 要忽略的 commit hash
git config blame.ignoreRevsFile .git-blame-ignore-revs
git blame services/auth/oauth.py  # 现在会跳过这些 commit

# 22. 分析项目历史和贡献
# 【教练提示】用于团队健康度评估

# 统计按作者的提交数
git shortlog -sn --all

# 统计最活跃的文件
git log --pretty=format: --name-only | sort | uniq -c | sort -rn | head -20

# 查看最近 30 天的活动
git log --since="30 days ago" --oneline --all | wc -l

# ============================================================================
# 第八部分：团队最佳实践和工作流自动化
# ============================================================================

# 23. 配置全局 git 别名（加速日常操作）
cat > ~/.gitconfig << 'EOF'
[alias]
    # 【教练提示】这些别名大幅加速日常操作，特别是在大型 monorepo 中
    
    # 查看简洁的分支状态
    st = status -sb
    
    # 同步分支：拉取并 rebase
    sync = !git fetch origin && git rebase origin/$(git rev-parse --abbrev-ref HEAD)
    
    # 列出本地修改的文件（快速查看改动范围）
    changes = diff --name-status -M
    
    # 推送当前分支并创建跟踪关系
    pub = push -u origin HEAD
    
    # 创建 WIP（Work In Progress）commit（快速保存进度）
    wip = commit -am "WIP: work in progress"
    
    # 撤销最后一个 commit（但保留改动）
    undo = reset --soft HEAD~1
    
    # 查看分支的完整历史（包括已删除的分支）
    hist = log --graph --oneline --all --decorate
    
    # 找出哪些分支已合并到当前分支
    merged = branch -a --merged
    
    # 找出包含特定 commit 的所有分支
    find = branch -a --contains
    
    # 显示最后改动的 N 个文件
    recent = log -r -n 20 --name-status
EOF

# 24. 创建团队的 Git workflow guide
cat > CONTRIBUTING.md << 'EOF'
# Git Workflow Guide

## 日常流程

### 1. 创建功能分支
\`\`\`bash
git checkout -b team/feature-name/TICKET-123 develop
\`\`\`

### 2. 频繁提交（保持小粒度）
\`\`\`bash
git add -p  # 交互式添加
git commit -m "type(scope): description"
\`\`\`

【教练提示】小的 commit 便于审查和 bisect，推荐 100-200 行代码/commit

### 3. 保持与 develop 同步
\`\`\`bash
git fetch origin develop
git rebase origin/develop
\`\`\`

### 4. 推送并创建 PR
\`\`\`bash
git push -u origin team/feature-name/TICKET-123
\`\`\`

## 代码审查标准

- [ ] 所有 commit 遵循 Angular 格式
- [ ] 添加了测试用例
- [ ] 运行了 linter：\`python -m pylint\`
- [ ] 更新了文档（如需）
- [ ] 没有合并冲突

## 合并规则

- develop: 使用 squash merge（保持简洁）
- main: 使用 rebase merge（绝对线性）

【教练提示】这份指南确保所有团队成员遵循相同的工作流，
减少协调成本和合并冲突。
EOF

# ============================================================================
# 第九部分：处理特殊场景
# ============================================================================

# 25. 处理无意的提交（安全的撤销）
# 场景：推送了不应该推送的内容

# 情况 1：还没推送，只在本地
git reset --soft HEAD~1        # 撤销 commit，保留改动
git reset --mixed HEAD~1       # 撤销 commit 和 stage
git reset --hard HEAD~1        # 完全丢弃最后一个 commit

# 情况 2：已经推送到远程
# 【教练提示】使用 revert 而不是 reset（更安全，不改写历史）
git revert HEAD                # 创建一个新 commit 来撤销上一个
git push origin HEAD

# 26. 处理大文件的意外提交
# 【教练提示】使用 BFG Repo-Cleaner 或 git filter-branch 来移除历史中的大文件

# 安装 BFG：brew install bfg
bfg --delete-files "*.tar.gz" --no-blob-protection

# 27. 跨分支的cherry-pick 批量操作
# 场景：需要将多个 commit 应用到另一个分支

# 方法 1：使用 commit range
git cherry-pick develop..feature/new-api  # cherry-pick 在 develop 之后的所有 commit

# 方法 2：交互式选择
git rebase -i --onto main develop        # 将 develop 上的改动迁移到 main

# ============================================================================
# 第十部分：性能优化（大型 monorepo 特有）
# ============================================================================

# 28. 启用 Git 的高性能特性
# 【教练提示】对于数十 GB 的 monorepo，这些优化至关重要

# 启用 multi-threading
git config core.preloadindex true
git config core.maxObjectsPerCommand 50000

# 启用 object pooling（存储优化）
git config core.alternateRefsCommand true

# 启用 commit graph（加速 log 操作）
git maintenance start

# 29. 使用 git sparse-checkout 只检出需要的目录
# 【教练提示】将工作目录大小从 100GB 减少到 5GB

git sparse-checkout set services/auth libs/common configs

# 查看当前 sparse-checkout 配置
git sparse-checkout list

# 30. 定期 gc 和优化
# 【教练提示】定期清理 git 对象数据库，防止性能降级

git gc --aggressive  # 完全重新压缩（可能需要 30 分钟）
git reflog expire --all --expire=now
git gc --prune=now

# ============================================================================
# 总结：高效团队协作的核心原则
# ============================================================================

# 【教练最后提示】
# 1. 分支短小精悍：2-3 天内合并（避免长期存活分支）
# 2. Commit 原子性：一个逻辑改动 = 一个 commit
# 3. 定期同步：每天 rebase develop，避免大合并
# 4. 代码审查优先：快速反馈循环（< 4 小时）
# 5. 自动化一切：hook、CI、脚本化日常操作
# 6. 追踪可追溯：好的 commit message + 清晰的历史
# 7. 所有权明确：CODEOWNERS 防止无意改动
# 8. 工具辅助：别名、脚本、第三方工具减少摩擦

echo "✅ Git workflow setup complete!"
```