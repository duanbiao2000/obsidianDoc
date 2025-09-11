---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
---
def build_pareto_card_prompt(topic, level="中级", lang="中文", max_cards=15):
    return f"""
你是我的学习助理，请基于“{topic}”这个主题生成符合帕累托法则的学习卡片，输出最多 {max_cards} 张。
要求：
- 输出语言：{lang}
- 技术深度：{level}
- 输出格式：Markdown 表格，列名为 Question | Answer
- 卡片应覆盖四类：概念定义、核心原理、高频操作、常见陷阱
"""