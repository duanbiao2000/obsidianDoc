---
tags:
  - Creative/Github
aliases:
  - 第二大脑
source: https://app.khoj.dev/
createdAt: 2024-12-12T15:40:00
updateAt:
---
[GitHub - BookDanny/khoj: Your AI second brain. Self-hostable. Get answers from the web or your docs. Build custom agents...](https://github.com/BookDanny/khoj)

`einops` 是一个用于深度学习和科学计算的 Python 库，它提供了一种简洁、直观的方式来操作多维数组。`einops` 的名字来源于 "Einstein Operations"，它模仿了爱因斯坦求和约定，使得多维数组操作更加直观和易于理解。

### 主要功能

- **重排维度**：`einops.rearrange` 函数可以轻松地重新排列多维数组的维度。
- **切分和合并**：`einops.split` 和 `einops.merge` 函数可以方便地对多维数组进行切分和合并操作。
- **广播**：`einops.broadcast` 函数可以自动处理广播机制，使得不同形状的数组进行运算时更加方便。
- **字符串模板**：`einops` 使用字符串模板来定义操作，使得代码更加清晰和易于维护。

### 用途

- **数据预处理**：在深度学习模型中，经常需要对输入数据进行预处理，`einops` 可以简化这些操作。
- **特征工程**：在数据科学项目中，特征工程是关键步骤，`einops` 可以帮助简化特征转换过程。
- **科学计算**：在科学计算中，多维数组操作是常见的，`einops` 可以简化这些操作，提高代码的可读性和可维护性。

### 注意事项

- **性能**：虽然 `einops` 提供了简洁的操作，但在处理大规模数据时，需要注意性能问题。
- **兼容性**：`einops` 主要与 NumPy 和 PyTorch 等库兼容，确保在使用前安装了相应的依赖库。
- **学习曲线**：`einops` 的字符串模板语法可能需要一些时间来适应，建议先从简单的例子开始学习。

### 示例

```python
import numpy as np
import einops

# 创建一个 3x4 的数组
array = np.arange(12).reshape(3, 4)

# 使用 einops 重排维度
rearranged_array = einops.rearrange(array, 'b c -> c b')
print(rearranged_array)
```

在这个例子中，`einops.rearrange` 函数将原始的 3x4 数组重新排列为 4x3 的数组。

### 总结

`einops` 是一个强大的库，可以帮助简化多维数组操作，提高代码的可读性和可维护性。它特别适合于深度学习和科学计算领域，但需要注意性能和兼容性问题。

Magika 是一个 Python 包，它使用深度学习来识别文件类型。它就像一个由 AI 驱动的文件侦探，可以快速准确地判断文件的类型，例如图像、文档、代码等等。

**主要特点：**

* **准确快速：** Magika 使用一个精简的 Keras 模型（大约 1MB），即使在单 CPU 上也能在几毫秒内准确识别文件类型。平均准确率超过 99%。
* **用途广泛：** 它既可以作为命令行工具使用，也可以作为 Python 模块在代码中调用。
* **轻量级：** 模型大小只有约 1MB，不会占用太多空间。

**安装方法：**

使用 pip 安装：

```bash
pip install magika
```

如果只想在命令行中使用：

```bash
pipx install magika
```

**使用方法：**

* **命令行：**  可以直接在终端中使用 `magika` 命令，后面跟上文件名或文件夹路径。它支持递归扫描、JSON/JSONL 输出、MIME 类型输出等多种选项。 可以使用 `magika --help` 查看所有选项。

   ```bash
   magika examples/*  # 检查 examples 文件夹下的所有文件
   ```

* **Python 模块：**  可以在 Python 代码中导入 `magika` 模块，然后使用 `identify_bytes()` 方法来识别文件类型。

   ```python
   from magika import Magika

   magika = Magika()
   result = magika.identify_bytes(b"# Example\nThis is an example of markdown!")
   print(result.output.ct_label)  # 输出: "markdown"
   ```

## 训练框架

主流的训练框架有很多，以下是一些最常用的深度学习训练框架：

1. **TensorFlow**：由 Google 开发，是最流行的深度学习框架之一。它提供了丰富的 API，支持多种硬件平台，包括 CPU、GPU 和 TPU。TensorFlow 还有一个强大的社区，提供了大量的教程、示例和工具。

2. **PyTorch**：由 Facebook 开发，是一个开源的深度学习框架，以其易用性和灵活性而受到欢迎。PyTorch 提供了动态计算图，使得调试和实验更加方便。它还支持多种硬件平台，包括 CPU、GPU 和 TPU。

3. **Keras**：是一个高层神经网络 API，它可以在 TensorFlow、CNTK 和 Theano 上运行。Keras 以其简单易用和直观的 API 而受到欢迎，特别适合快速原型设计和研究。

4. **Caffe**：由伯克利 AI Research（BAIR）开发，是一个深度学习框架，以其高效和灵活性而受到欢迎。Caffe 特别适合处理大规模图像数据，并且支持多种硬件平台，包括 CPU、GPU 和 FPGA。

5. **MXNet**：由 Apache Software Foundation 开发，是一个开源的深度学习框架，以其高效和灵活性而受到欢迎。MXNet 支持多种硬件平台，包括 CPU、GPU 和 FPGA，并且支持多种编程语言，包括 Python、R、Scala 和 Julia。

6. **Theano**：由蒙特利尔大学开发，是一个 Python 库，用于定义、优化和评估数学表达式，特别是神经网络。Theano 特别适合处理大规模数据，并且支持多种硬件平台，包括 CPU 和 GPU。

7. **PaddlePaddle**：由百度开发，是一个开源的深度学习平台，以其高效和灵活性而受到欢迎。PaddlePaddle 支持多种硬件平台，包括 CPU、GPU 和 FPGA，并且支持多种编程语言，包括 Python 和 C++。

这些框架各有优缺点，选择哪个框架取决于具体的应用场景、硬件环境和个人偏好。
## Khoj简介
这段代码是一个Markdown格式的文档，用于描述一个名为Khoj的AI应用程序。以下是这段文档的主要内容的总结：

- **项目简介**：Khoj是一个个人AI应用程序，用于扩展你的能力。它可以从本地设备上的个人AI无缝扩展到云端的企业AI。
- **功能**：Khoj可以与任何本地或在线的LLM（例如llama3、qwen、gemma、mistral、gpt、claude、gemini）进行聊天，从互联网和你的文档（包括图像、PDF、Markdown、Org-Mode、Word、Notion文件）中获取答案，从浏览器、Obsidian、Emacs、桌面、手机或WhatsApp访问它，创建具有自定义个性、工具和知识库的代理，自动化重复的研究，获取发送到你的收件箱的个人新闻通讯和智能通知，使用我们的高级语义搜索快速轻松地找到相关的文档，生成图像，大声说出你的消息，Khoj是开源的，可自托管的，总是如此，在[你的计算机](https://docs.khoj.dev/get-started/setup)上私有运行或在我们的[云应用程序](https://app.khoj.dev)上尝试它。
- **新功能**：现在任何人都可以创建自定义代理，具有可调个性、工具和知识库，开始任何消息的实验研究模式，阅读关于Khoj在现代检索和推理基准测试中优秀性能的文章。
- **自托管**：要开始自托管Khoj，请阅读[文档](https://docs.khoj.dev/get-started/setup)。
- **贡献者**：感谢我们的优秀贡献者！🎉
- **有兴趣贡献吗？**：我们总是欢迎贡献者帮助我们构建新功能，改进项目文档，或修复错误。如果你有兴趣，请查看我们的[贡献指南](https://docs.khoj.dev/contributing/development)并查看我们的[贡献者项目板](https://github.com/orgs/khoj-ai/projects/4)。

## 主流模型对比

你要求比较`Llama 3`、`Qwen`、`Gemma`、`Mistral`、`GPT`、`Claude` 和 `Gemini` 的特性。这是一个很好的问题，因为这些都是领先的大语言模型 (LLM)，各有优劣。以下是一个表格，总结了它们的主要特性和区别：

| 特性 | Llama 3 | Qwen | Gemma | Mistral | GPT | Claude | Gemini |
|---|---|---|---|---|---|---|---|
| 开发者 | Meta | 阿里巴巴 | Google | Mistral AI | OpenAI | Anthropic | Google |
| 模型大小 | 8B, 70B | 7B, 72B 等 | 2B, 7B | 7B, 8x7B, 8x22B 等 | 多种，例如 GPT-4, GPT-4o | 多种，例如 Claude 3, Claude 3.5 Sonnet | 多种，例如 Gemini Ultra, Pro, Nano |
| 开源 | 是 | 部分 | 是 | 部分 | 否 | 否 | 否 |
| 主要优势 | 高性能，开放，多平台支持 | 多语言支持，多模态能力 | 轻量级，高性能 | 高效推理，开放权重（部分） | 高性能，广泛应用 | 安全性，长文本理解 | 多模态，高性能 |
| 多模态 | Llama 3.1开始支持 | 支持 | 否 | 否 | GPT-4o 支持 | Claude 3 开始支持 | 支持 |
| 上下文窗口 | 较长 | 较长，Qwen-72B可达128k | 较短 | 较长 | 较长，GPT-4o更长 | 较长，Claude 3.5 Sonnet可达100k | 较长，Gemini Pro可达1M |
| 代码能力 | Code Llama表现出色 | 良好 | 一般 | 良好 | 良好，GPT-4o更佳 | 良好 | 良好 |
| 推理能力 | Llama 3提升显著 | 良好 | 良好 | 高效 | 优秀，GPT-4o更佳 | 优秀 | 优秀 |
| 安全性 | 注重安全，提供安全工具 | 良好 | 良好 | 良好 | 注重安全，持续改进 | 高度重视安全 | 良好 |

**一些重要的补充说明：**

* **性能：**  GPT-4o 和 Gemini Ultra 通常被认为是性能最高的模型，但其他模型也在不断改进，并在某些特定任务上可能表现更好。
* **成本：** 开源模型 (Llama, Qwen, Gemma, Mistral) 通常更经济，因为你可以在自己的硬件上运行它们。
* **易用性：**  不同的模型有不同的访问方式和 API，有些更容易使用。
* **特定用途：**  某些模型可能更适合特定任务，例如代码生成、多语言翻译或图像理解。

**建议：**

选择合适的模型取决于你的具体需求和资源。如果你需要最高的性能并且预算充足，可以考虑 GPT-4o 或 Gemini Ultra。如果你需要一个经济高效的解决方案，开源模型是不错的选择。 如果你需要轻量级且高性能的模型，Gemma 是一个不错的选择。 如果你需要多语言支持，Qwen 和 Claude 是不错的选择。

在Docker Compose中，`volumes`用于定义和管理Docker容器之间的数据共享。具体来说，`volumes`可以用于以下场景：

1. **数据持久化**：Docker容器在运行时会创建一个临时的文件系统，当容器停止或删除时，这个文件系统也会被删除。如果需要持久化数据，可以将数据存储在卷中，而不是存储在容器的文件系统中。

2. **数据共享**：多个容器可以共享同一个卷，这使得它们可以共享数据。例如，一个容器可以写入数据到卷中，另一个容器可以读取这些数据。

3. **数据备份和恢复**：卷可以被挂载到多个容器中，这使得数据可以在容器之间共享，从而可以实现数据的备份和恢复。

在你的代码中，`volumes`定义了三个卷：`khoj_config`、`khoj_db`和`khoj_models`。这些卷可以在不同的容器中使用，用于存储配置文件、数据库和模型数据。例如，一个容器可以将配置文件写入`khoj_config`卷中，另一个容器可以从`khoj_config`卷中读取配置文件。

需要注意的是，卷是在Docker主机上创建的，而不是在容器中创建的。这意味着，即使容器停止或删除，卷中的数据仍然存在。


## telemetry

`telemetry`文件夹在代码库中扮演了重要的角色，它主要用于收集和分析Khoj应用程序的使用数据。具体来说，它包含以下文件和功能：

1. **requirements.txt**：列出了运行`telemetry.py`脚本所需的Python依赖包，包括`uvicorn`、`fastapi`、`posthog`和`python-dotenv`。

2. **telemetry.py**：这是主要的 telemetry 服务器脚本，它定义了一个 FastAPI 应用程序，用于接收和处理来自客户端的 telemetry 数据。它包括以下主要功能：
   - `v1_telemetry`：接收 POST 请求中的 telemetry 数据，并将其记录到 PostHog 服务器和 SQLite 数据库中。
   - `main`：当脚本直接运行时，它解析命令行参数并启动 FastAPI 应用程序。

3. **Dockerfile**：定义了如何构建一个 Docker 镜像，该镜像包含 telemetry 服务器及其所有依赖项。这个镜像可以在 Docker 容器中运行，用于收集和分析 telemetry 数据。

4. **dockerize_telemetry_server.yml**：这是一个 GitHub Actions 工作流文件，用于在 GitHub Actions 环境中构建和推送 telemetry 服务器的 Docker 镜像。

### 总结

`telemetry`文件夹的主要作用是收集和分析Khoj应用程序的使用数据，以便更好地理解用户行为和优先开发功能。它通过接收和处理来自客户端的 telemetry 数据，并将这些数据记录到 PostHog 服务器和 SQLite 数据库中来实现这一功能。

Telemetry 服务器是指收集、处理和存储从各种远程来源（例如软件应用程序、网络设备、服务器和传感器）发送的遥测数据的服务器。 它们充当遥测数据的中心枢纽，使组织能够监控系统性能、检测异常并深入了解系统行为。

遥测服务器通常在以下场景中使用：

* **服务器健康状况监控：** 数据中心依靠遥测来监控服务器的健康状况。 遥测服务器收集 CPU 使用率、内存使用率、磁盘 I/O 和网络带宽等指标。 通过持续监控这些服务器参数，数据中心管理员可以检测异常情况、预测潜在故障并采取主动措施来保持服务器的可靠性和正常运行时间。
* **云资源管理：** 云服务提供商依靠遥测来确保其资源的可用性和效率。 遥测服务器收集有关虚拟机、容器、数据库和其他云服务使用情况的数据。 这些数据使云提供商能够有效地分配资源、监控服务质量并根据使用模式管理计费。
* **应用程序性能监控 (APM)：** 软件开发人员使用遥测来监控应用程序的性能和用户行为。 遥测服务器收集响应时间、错误率、用户交互和其他相关指标。 这些数据有助于开发人员识别性能瓶颈、调试问题并改进用户体验。
* **网络监控：** 网络管理员使用遥测来监控网络设备的健康状况和性能。 遥测服务器收集带宽使用率、数据包丢失、延迟和其他网络指标。 这些数据有助于管理员识别网络拥塞、排除故障并优化网络性能。
* **物联网 (IoT)：** 遥测服务器在物联网中发挥着至关重要的作用，用于从连接的设备收集数据。 这些数据可以用于各种目的，例如监控设备性能、跟踪资产以及控制设备行为。

遥测服务器可以使用各种技术来收集数据，包括代理、API 和传感器。 它们还可以使用各种协议来传输数据，例如 HTTP、MQTT 和 gRPC。

