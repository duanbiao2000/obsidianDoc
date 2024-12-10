---
aliases: Untitled
createdAt: 2024-11-25 13:57
categories:
  - Mindset
tags:
  - Mindset/Reflection
---
以下是关于认知复杂度的核心内容：

1. **认知复杂度的定义**：
   - 认知复杂度是衡量代码单元直观理解难度的指标，与循环复杂度（Cyclomatic Complexity）不同，后者衡量的是代码测试的难度。

2. **Code Climate工具**：
   - Code Climate可以帮助识别难以理解的方法，并防止将它们引入代码。

3. **认知复杂度的规则**：
   - 代码使用语言提供的简写形式将多个语句合并为一个时，复杂度增加。
   - 代码中每个“代码流中断”都会增加复杂度。
   - 当“流中断结构”嵌套时，复杂度增加。

4. **流中断的例子**：
   - 循环、条件语句、异常捕获、switch或case语句、逻辑运算符序列（例如 `a || b && c || d`）、递归、跳转到标签等。

5. **嵌套的影响**：
   - 代码嵌套得越深，推理就越困难。例如，条件语句、循环、try/catch块等。

6. **认知复杂度的进一步阅读**：
   - 可以查看SonarSource的白皮书《Cognitive Complexity: A new way of measuring understandability》以获取更多细节和例子。

这些核心内容概括了认知复杂度的基本概念、影响因素以及如何通过Code Climate工具来识别和改进代码的认知复杂度。

以下是关于Code Climate可维护性（Maintainability）功能的详尽笔记：

### 可维护性定义
- **可维护性**是依据标准化的10点评估，基于代码库中的**复制（Duplication）**、**循环复杂度（Cyclomatic Complexity）**、**认知复杂度（Cognitive Complexity）**和结构问题来估算技术债务。

### 技术债务估算
- Code Climate在10点检查中识别的每个技术债务问题，都会估算解决问题所需的大致时间，称为**整改时间（remediation time）**。
- 通过聚合这些时间，可以比较不同技术债务项目。

### 文件级别评分
- 根据识别出的技术债务问题的总整改时间，为文件分配A到F的字母等级。
- 如果问题被标记为“Wontfix”或“Invalid”，则不计入评分。

### 代码库级别度量
- 代码库级别的可维护性评分更为复杂，因为大型项目往往得分低于小型项目。
- 为了使代码库级别的可维护性评分更有意义，Code Climate计算技术债务比率，即总估计整改时间除以基于代码库大小的非常高级别的总估计实施时间。技术债务比率越低越好。

### 默认启用的检查
- Code Climate默认启用了10项检查，这些检查将运行在任何支持的可维护性语言编写的文件上。

### 可维护性检查列表
1. **参数数量（Argument count）**：定义了大量参数的方法或函数。
2. **复杂逻辑（Complex logic）**：可能难以理解的布尔逻辑。
3. **文件长度（File length）**：单个文件中的代码行数过多。
4. **相同代码块（Identical blocks of code）**：在语法上完全相同但可能格式不同的重复代码。
5. **方法复杂度（Method complexity）**：可能难以理解的函数或方法（认知复杂度）。
6. **方法数量（Method count）**：定义了大量函数或方法的类。
7. **方法长度（Method length）**：单个函数或方法中的代码行数过多。
8. **嵌套控制流（Nested control flow）**：深层嵌套的控制结构，如if或case。
9. **返回语句（Return statements）**：有大量返回语句的函数或方法。
10. **相似代码块（Similar blocks of code）**：结构相同但变量名可能不同的非完全相同的重复代码。

### 高级配置
- 这些检查都带有默认阈值，可以使用`.codeclimate.yml`或`.codeclimate.json`进行调整。

### 相关链接
- [复制（Duplication）](https://docs.codeclimate.com/docs/duplication-concept)
- [循环复杂度（Cyclomatic Complexity）](https://docs.codeclimate.com/docs/cyclomatic-complexity)
- [认知复杂度（Cognitive Complexity）](https://docs.codeclimate.com/docs/cognitive-complexity)
- [如何计算可维护性评分？](https://docs.codeclimate.com/docs/maintainability-calculation)
- [默认可维护性阈值](https://docs.codeclimate.com/docs/default-analysis-configuration#section-maintainability-checks)

### 更新信息
- 该文档内容最后一次更新是在大约2年前。

这些笔记提供了Code Climate可维护性功能的详细说明，包括技术债务估算、文件和代码库级别的评分方法、默认启用的检查列表以及如何进行高级配置。这些信息有助于理解如何评估和改进代码的可维护性。

以下是关于Code Climate与GitHub Issues集成功能的详尽笔记：

### GitHub Issues集成概述
- Code Climate的GitHub Issues集成允许用户将Code Climate中标记的问题快速转换为GitHub Issues。
- 在Feed页面上，用户可以通过鼠标悬停在一个代码异味（smell）上并点击“ticket”图标来创建GitHub Issue。

### 生成GitHub OAuth Token
1. 为了使Code Climate能够发帖到你的仓库Issues，需要生成一个GitHub OAuth token。
2. 访问GitHub的[设置页面](https://github.com/settings/tokens)生成token。
   - 确保你以具有访问和足够权限的用户身份登录GitHub。
   - Code Climate将以生成token的用户身份打开Issue。
3. 点击**Generate new token**。
4. 如果GitHub提示，可能需要输入密码才能继续。
5. 为token命名（只要没有其他GitHub token共享此名称即可），确保勾选了**repo**范围，然后点击**Generate Token**。
6. 点击“复制到剪贴板”按钮。

### 在Code Climate中配置GitHub Issues
1. 在新的浏览器窗口中，导航到你的Code Climate **Dashboard**。
2. 鼠标悬停在你的仓库名称上并点击**Settings**。
3. 选择**Integrations**标签。
4. 点击**GitHub Issues**旁边的**Set Up**。
5. 在OAuth Token字段中粘贴OAuth token。
6. 在**Project**字段中输入项目名称（即GitHub上的项目名称，例如`user/myapp`）。
7. 在**Labels**字段中输入任何标签，这些标签将与Code Climate创建的任何问题关联。
8. 确保勾选**Active**并点击**Save**。
9. 点击**Test Service**验证GitHub数据是否有效（这将向你的仓库发布一个测试问题）。如果页面顶部出现绿色消息，则一切正常。如果有红色错误消息，请参见下面的故障排除部分。

### 故障排除
- 如果点击**Test Service**后看到红色错误消息：
  - 确保你提供的token周围没有前后空格。
  - 确保你生成的token是具有访问仓库权限的GitHub用户。如果你有多个GitHub用户，请确保你以适当的用户身份登录GitHub。
  - 如果你的仓库是另一个仓库的复刻，请确保你为你的仓库启用了Issues功能。否则，集成将返回404错误。

### GitHub权限请求
- Code Climate请求以下GitHub权限：
  - `user:email`：在GitHub注册时请求。需要电子邮件地址来创建Code Climate用户。
  - `public_repo`：在添加公共仓库到Code Climate时请求。此权限允许我们安装只读SSH密钥、设置webhook并为公共仓库写入提交状态。
  - `repo`：在添加私有仓库到Code Climate时请求。此权限允许我们安装只读SSH密钥、设置webhook并为私有仓库写入提交状态。

### GitHub集成
- Code Climate有两个GitHub集成：一个用于[GitHub Pull Requests](https://docs.codeclimate.com/docs/github#pull-requests)，另一个用于[GitHub Issues](https://docs.codeclimate.com/docs/github#issues)。
- 两个集成都需要创建GitHub个人访问token，确保token没有读写权限：
  - **GitHub Pull Requests**：token应由具有访问仓库权限的任何用户生成。生成token时，确保只选择[repo:status scope](https://developer.github.com/v3/oauth/#scopes)。
  - **GitHub Issues**：token应由具有仓库**只读**访问权限的[GitHub机器用户](https://developer.github.com/guides/managing-deploy-keys/#machine-users)生成。生成token时，确保选择了[repo scope](https://developer.github.com/v3/oauth/#scopes)。

### 更新信息
- 该文档内容最后一次更新是在大约4年前。

这些笔记提供了Code Climate与GitHub Issues集成的详细步骤，包括生成GitHub OAuth Token、在Code Climate中配置集成以及故障排除。这些信息有助于用户将Code Climate中识别的问题有效地转换为GitHub Issues，以便更好地管理和跟踪。