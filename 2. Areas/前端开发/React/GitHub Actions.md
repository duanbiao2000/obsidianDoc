---
theme: 
tags: 
status: false
created_date:
---

## 订阅Hacker News
订阅Hacker News（HN）每日排名最高的10条新闻，并通过GitHub Actions设置定时任务，将结果记录在项目的issue中，可以通过以下步骤实现：

1. **创建GitHub仓库**：
   - 如果还没有仓库，首先需要在GitHub上创建一个新的仓库。

2. **生成Personal Access Token (PAT)**：
   - 访问GitHub Settings > Developer settings > Personal access tokens。
   - 生成一个具有`repo`权限的token，这样脚本就可以访问你的仓库。

3. **创建GitHub Actions工作流**：
   - 在仓库中创建一个`.github/workflows`目录。
   - 在该目录下创建一个新的YAML文件，例如`hn_top_stories.yml`。

4. **编写工作流脚本**：
   - 编写一个shell脚本或Python脚本，用于获取Hacker News的每日最高排名的帖子。
   - 使用Hacker News的API（如果有的话）或者通过解析网页内容获取数据。

5. **创建Issue并写入数据**：
   - 脚本应该能够创建一个新的issue或者在现有issue中记录数据。

6. **配置工作流的触发条件**：
   - 在YAML文件中设置定时任务，例如每天凌晨执行。

7. **配置工作流的安全性**：
   - 如果脚本需要使用到GitHub Token，确保通过secrets安全地存储和使用。

8. **推送工作流文件到仓库**：
   - 将编写好的YAML文件推送到远程仓库。

9. **启用工作流**：
   - 默认情况下，GitHub Actions工作流是禁用的，需要在仓库的Actions选项卡中启用。

10. **监控工作流执行情况**：
    - 检查Actions的运行日志，确保工作流按预期执行。

11. **设置RSS订阅**（如果需要）：
    - 可以使用第三方服务如IFTTT或Zapier来监控issue的更新，并将其转换为RSS feed。

以下是一个简化版的GitHub Actions工作流YAML文件示例：

```yaml
name: Hacker News Top Stories

on:
  schedule:
    - cron: '0 0 * * *'  # 每天凌晨0点执行

jobs:
  get-hn-top-stories:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: pip install requests

    - name: Get top stories
      run: python script.py
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

    - name: Create or update issue
      run: |
        # 这里需要编写逻辑来检查issue是否存在，并更新内容
        # 如果不存在，则创建新的issue
```

请注意，这只是一个示例，你需要根据实际情况编写获取Hacker News数据的脚本和更新issue的逻辑。此外，确保在项目的`Settings > Secrets`中添加`GITHUB_TOKEN`的secret。



   
```tg
 卡片盒笔记法的原则, 不需要解释,直接列出要点并按有序列表展示
```
- 明确笔记的目的和主题
- 保持笔记的简洁性和可读性
- 使用标准化格式记录信息
- 定期回顾和整理笔记
- 建立笔记之间的联系和索引
- 鼓励思考和创造性联想
- 保持笔记系统的开放性和灵活性
- 重视笔记的实用性和可操作性
- 培养持续记录和更新笔记的习惯  
      

