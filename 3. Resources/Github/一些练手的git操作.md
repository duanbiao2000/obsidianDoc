---
aliases: 20241129
createdAt: 2024-11-29 16:51
categories:
  - Diary
tags:
  - Creative/Github
  - Tech/Code
---

总结

<!--more-->

你提供的脚本尝试找到仓库的初始提交（即第一个提交），然后重置当前分支到这个初始提交，并强制推送到远程仓库。以下是对你提供的脚本的解释和一些改进建议：

### 你的脚本

```sh
initial_commit=$(git log | tail -n 5 | head -n 1 | sed -e "s/commit //")
git reset --hard "$initial_commit"
git push -f
```

### 解释

1. **获取初始提交**：
   ```sh
   initial_commit=$(git log | tail -n 5 | head -n 1 | sed -e "s/commit //")
   ```
   - `git log`：显示所有的提交记录。
   - `tail -n 5`：取最后5行，假设这5行中包含初始提交。
   - `head -n 1`：取这5行中的第一行，即假设这是初始提交。
   - `sed -e "s/commit //"`：去掉开头的 `commit` 字样，只保留提交哈希。

2. **重置当前分支到初始提交**：
   ```sh
   git reset --hard "$initial_commit"
   ```
   - `git reset --hard <commit>`：将当前分支重置到指定的提交，并丢弃所有未提交的更改。

3. **强制推送**：
   ```sh
   git push -f
   ```
   - `git push -f`：强制将本地分支推送到远程仓库，覆盖远程分支的历史记录。

### 改进建议

1. **确保获取的是真正的初始提交**：
   - 为了确保获取的是真正的初始提交，可以使用 `--reverse` 选项来按时间顺序正向显示提交记录，然后取第一行。
   - 也可以直接使用 `git rev-list --max-parents=0 HEAD` 来获取第一个提交。

2. **增加错误处理和确认提示**：
   - 在执行危险操作（如 `git reset --hard` 和 `git push -f`）之前，增加确认提示。
   - 检查 `git log` 的输出是否为空，以防止在没有提交记录的情况下执行操作。

3. **完整的改进脚本**：

```sh
# 获取初始提交
initial_commit=$(git rev-list --max-parents=0 HEAD)

# 检查是否有初始提交
if [ -z "$initial_commit" ]; then
  echo "No initial commit found. Aborting."
  exit 1
fi

# 显示初始提交信息
echo "Initial commit: $initial_commit"

# 确认用户是否要继续
read -p "Are you sure you want to reset the branch to the initial commit and force push? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  echo "Operation cancelled."
  exit 1
fi

# 重置当前分支到初始提交
git reset --hard "$initial_commit"

# 强制推送
git push -f
```

### 说明

1. **获取初始提交**：
   ```sh
   initial_commit=$(git rev-list --max-parents=0 HEAD)
   ```
   - `git rev-list --max-parents=0 HEAD`：获取没有父提交的第一个提交。

2. **检查是否有初始提交**：
   ```sh
   if [ -z "$initial_commit" ]; then
     echo "No initial commit found. Aborting."
     exit 1
   fi
   ```

3. **显示初始提交信息并确认用户操作**：
   ```sh
   echo "Initial commit: $initial_commit"
   read -p "Are you sure you want to reset the branch to the initial commit and force push? (y/N) " -n 1 -r
   echo
   if [[ ! $REPLY =~ ^[Yy]$ ]]; then
     echo "Operation cancelled."
     exit 1
   fi
   ```

4. **重置当前分支到初始提交并强制推送**：
   ```sh
   git reset --hard "$initial_commit"
   git push -f
   ```

通过这些改进，脚本变得更加健壮和安全，减少了误操作的风险。