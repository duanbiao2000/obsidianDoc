---
aliases: 
<<<<<<< HEAD
theme: 
priority: false
=======
categories: 
high_priority: false
>>>>>>> 93a933e (refactor(dailyNotes): update metadata structure for daily notes)
tags:
---
# Git命名规范
## 分支规范
在软件开发中，分支命名是一个重要的实践，它有助于团队成员更好地理解和管理代码库。常用的分支命名大类通常包括以下几种：

### 1. 主分支

主分支是项目的核心分支，通常包含稳定且经过测试的代码。

- **`main` 或 `master`**：这是项目的主分支，包含了最新的、稳定的代码。许多项目已经从 `master` 迁移到 `main` 作为默认的主分支名称。
- **`develop`**：这是一个集成分支，用于合并来自特性分支和修复分支的更改。`develop` 分支通常包含最新的开发代码，但可能还没有经过完整的测试。

### 2. 特性分支

特性分支用于开发新功能或改进现有功能。

- **`feature/`**：用于开发新功能的分支。例如：
    - `feature/user-authentication`
    - `feature/new-payment-gateway`

### 3. 修复分支

修复分支用于修复 bug 或进行小的改进。

- **`fix/`**：用于修复特定问题的分支。例如：
    - `fix/login-bug`
    - `fix/performance-issue`

### 4. 发布分支

发布分支用于准备即将发布的版本。

- **`release/`**：用于准备即将发布的版本。例如：
    - `release/v1.0.0`
    - `release/2023-10-01`

### 5. 热修复分支

热修复分支用于紧急修复生产环境中的问题。

- **`hotfix/`**：用于紧急修复生产环境中的问题。例如：
    - `hotfix/critical-bug`
    - `hotfix/security-vulnerability`

### 6. 其他常见分支

除了上述主要类别外，还有一些其他常见的分支命名方式：

- **`bugfix/`**：类似于 `fix/`，用于修复特定的 bug。
- **`refactor/`**：用于重构代码，不添加新功能，只优化现有代码结构。
- **`docs/`**：用于更新文档。
- **`chore/`**：用于一些非功能性的工作，如构建脚本的更新、依赖管理等。
- **`test/`**：用于添加或改进测试代码。
- **`experiment/`**：用于实验性的功能或技术探索。
- **`revert/`**：用于回滚之前的提交或更改。

### 示例

假设你正在开发一个电子商务应用，以下是一些示例分支命名：

- **主分支**：
    
    - `main`
    - `develop`
- **特性分支**：
    
    - `feature/cart-functionality`
    - `feature/product-reviews`
- **修复分支**：
    
    - `fix/payment-gateway-error`
    - `fix/user-login-issue`
- **发布分支**：
    
    - `release/v1.0.0`
    - `release/2023-10-01`
- **热修复分支**：
    
    - `hotfix/critical-security-bug`
    - `hotfix/performance-degradation`
- **其他分支**：
    
    - `refactor/order-processing`
    - `docs/user-guide-update`
    - `chore/update-build-script`
    - `test/unit-tests-improvement`
    - `experiment/new-ui-framework`


## commit&PR命名规范
在软件开发中，遵循一致的命名规范对于 `commit` 提交和 `Pull Request (PR)` 的命名非常重要。这不仅有助于团队成员更好地理解代码变更的目的和内容，还能提高代码审查的效率。以下是一些常见的命名规范建议：

### Commit 提交命名规范

#### 1. 格式
通常使用以下格式来命名 `commit` 消息：
```
<type>(<scope>): <subject>
```

- **`<type>`**：提交的类型，例如 `feat`（新功能）、`fix`（修复 bug）、`refactor`（重构）、`docs`（文档更新）等。
- **`<scope>`**：可选的范围，通常是受影响的模块或文件名。
- **`<subject>`**：简短的描述，说明这次提交的主要内容。

#### 2. 示例
- `feat(user-auth): 添加用户登录功能`
- `fix(payment): 修复支付网关错误`
- `refactor(api): 优化 API 请求处理逻辑`
- `docs(readme): 更新 README 文件`

#### 3. 常见类型
- **`feat`**：添加新功能。
- **`fix`**：修复 bug。
- **`refactor`**：重构代码，不改变功能。
- **`docs`**：更新文档。
- **`style`**：代码风格或格式化修改。
- **`test`**：添加或更新测试。
- **`chore`**：构建过程、依赖管理等非功能性更改。
- **`ci`**：持续集成相关的更改。
- **`perf`**：性能改进。
- **`revert`**：回滚之前的提交。

#### 4. 其他建议
- **简洁明了**：保持消息简洁，但要足够描述清楚变更的内容。
- **使用现在时态**：例如，“Add new feature” 而不是 “Added new feature”。
- **避免使用句号**：`commit` 消息不需要以句号结尾。

### Pull Request (PR) 命名规范

#### 1. 格式
通常使用以下格式来命名 `Pull Request`：
```
<type>: <description>
```

- **`<type>`**：PR 的类型，类似于 `commit` 类型，例如 `feat`、`fix`、`refactor` 等。
- **`<description>`**：简短的描述，说明 PR 的主要内容。

#### 2. 示例
- `feat: 添加用户登录功能`
- `fix: 修复支付网关错误`
- `refactor: 优化 API 请求处理逻辑`
- `docs: 更新 README 文件`

#### 3. 常见类型
- **`feat`**：添加新功能。
- **`fix`**：修复 bug。
- **`refactor`**：重构代码，不改变功能。
- **`docs`**：更新文档。
- **`style`**：代码风格或格式化修改。
- **`test`**：添加或更新测试。
- **`chore`**：构建过程、依赖管理等非功能性更改。
- **`ci`**：持续集成相关的更改。
- **`perf`**：性能改进。
- **`revert`**：回滚之前的提交。

#### 4. 其他建议
- **清晰描述**：确保 PR 名称能够清楚地描述其内容和目的。
- **关联 Issue**：如果 PR 是为了解决某个特定的 Issue，可以在名称中引用该 Issue 的编号，例如 `fix: 修复 #123 支付网关错误`。
- **保持简洁**：PR 名称应简洁明了，避免过长。

### 综合示例

假设你正在开发一个电子商务应用，并且需要创建一些 `commit` 和 `Pull Request`：

#### Commit 示例
- `feat(cart): 添加购物车功能`
- `fix(payment): 修复支付网关错误`
- `refactor(api): 优化 API 请求处理逻辑`
- `docs(readme): 更新 README 文件`

#### Pull Request 示例
- `feat: 添加购物车功能`
- `fix: 修复支付网关错误`
- `refactor: 优化 API 请求处理逻辑`
- `docs: 更新 README 文件`

通过遵循这些命名规范，你可以确保你的 `commit` 和 `Pull Request` 更具一致性、可读性和易于管理。如果你所在的团队有特定的命名规范，请确保遵循团队的规定。如果有任何其他问题或需要进一步的帮助，请告诉我！