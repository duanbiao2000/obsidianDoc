---
tags:
  - Creative/Github
  - Tech/Code
  - 当下时刻的觉察
  - Agent
  - 概念网络
aliases:
  - 第二大脑
source: https://app.khoj.dev/
createdAt: 2024-12-12T15:40:00.000Z
updateAt: 2025-03-27 23:32
---

[GitHub - BookDanny/khoj: Your AI second brain. ](https://github.com/BookDanny/khoj)

## Khoj简介

这段代码是一个Markdown格式的文档，用于描述一个名为Khoj的AI应用程序。以下是这段文档的主要内容的总结：

- **项目简介**：Khoj是一个个人AI应用程序，用于扩展你的能力。它可以从本地设备上的个人AI无缝扩展到云端的企业AI。
- **功能**：Khoj可以与任何本地或在线的LLM（例如llama3、qwen、gemma、mistral、gpt、claude、gemini）进行聊天，从互联网和你的文档（包括图像、PDF、Markdown、Org-Mode、Word、Notion文件）中获取答案，从浏览器、Obsidian、Emacs、桌面、手机或WhatsApp访问它，创建具有自定义个性、工具和知识库的代理，自动化重复的研究，获取发送到你的收件箱的个人新闻通讯和智能通知，使用我们的高级语义搜索快速轻松地找到相关的文档，生成图像，大声说出你的消息，Khoj是开源的，可自托管的，总是如此，在[你的计算机](https://docs.khoj.dev/get-started/setup)上私有运行或在我们的[云应用程序](https://app.khoj.dev)上尝试它。



在Docker Compose中，`volumes`用于定义和管理Docker容器之间的数据共享。具体来说，`volumes`可以用于以下场景：

1. **数据持久化**：Docker容器在运行时会创建一个临时的文件系统，当容器停止或删除时，这个文件系统也会被删除。如果需要持久化数据，可以将数据存储在卷中，而不是存储在容器的文件系统中。

2. **数据共享**：多个容器可以共享同一个卷，这使得它们可以共享数据。例如，一个容器可以写入数据到卷中，另一个容器可以读取这些数据。

3. **数据备份和恢复**：卷可以被挂载到多个容器中，这使得数据可以在容器之间共享，从而可以实现数据的备份和恢复。

在你的代码中，`volumes`定义了三个卷：`khoj_config`、`khoj_db`和`khoj_models`。这些卷可以在不同的容器中使用，用于存储配置文件、数据库和模型数据。例如，一个容器可以将配置文件写入`khoj_config`卷中，另一个容器可以从`khoj_config`卷中读取配置文件。


