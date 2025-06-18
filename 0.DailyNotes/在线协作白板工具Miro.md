---
date: 2025-06-18 17:15
tags:
  - Domain/Productivity/Tools
---

Miro 是一款**在线协作白板工具**。

它提供了一个无限大的数字画布，团队可以在上面进行头脑风暴、绘制流程图、制作思维导图、规划项目、进行设计冲刺等等。你可以添加便签、文字、图片、视频、文档，并利用各种预设模板。Miro 的核心价值在于**实时协作**，允许多个用户同时在同一块白板上工作，无论他们身处何地，就像面对面一样高效。

### **绘制 AIGC 市场竞争地图 (Miro 链接)**

由于我是一个语言模型，无法直接在 Miro 上创建和分享实际的、可交互的白板。不过，我可以为您**构思一个 AIGC 市场竞争地图的框架和内容**。

您可以将以下结构和元素在 Miro 中绘制出来。这能帮助您和您的团队清晰地理解 AIGC 市场的主要玩家、他们在做什么，以及它们之间的关系。

---

### **AIGC 市场竞争地图框架**

这个地图将按照 AIGC 的核心价值链进行划分，并识别主要参与者。

#### **1. 基础层：基础设施与模型提供商**

---

- **定义：** 提供底层计算能力、大型基础模型以及模型训练与部署平台。它们是 AIGC 生态的基石。
- **主要玩家：**
  - **云计算巨头 (算力与平台):**
    - **Amazon Web Services (AWS):** EC2, Sagemaker, Bedrock (提供模型访问)
    - **Microsoft Azure:** Azure OpenAI Service, Azure ML
    - **Google Cloud:** Vertex AI, Google Gemini API
    - **NVIDIA:** GPU硬件, CUDA, TensorRT (AI推理优化)
  - **基础模型开发者 (通用大模型):**
    - **OpenAI:** GPT系列 (GPT-4, GPT-3.5), DALL-E, Sora
    - **Google DeepMind:** Gemini系列, Imagen
    - **Meta AI:** Llama系列 (开源), Emu
    - **Anthropic:** Claude系列
    - **Mistral AI:** Mistral, Mixtral (开源)
    - **Cohere:** Command, Embed
    - **Stability AI:** Stable Diffusion
    - **Midjourney:** Midjourney (闭源图片生成)
  - **开源社区/模型分发平台:**
    - **Hugging Face:** 大量开源模型、数据集、Spaces，促进模型共享和协作。

#### **2. 中间层：工具链与平台**

---

- **定义：** 构建在基础模型之上，提供开发、部署、管理 AIGC 应用的工具、框架和 API。让开发者更容易地集成和利用 AIGC 能力。
- **主要玩家：**
  - **MaaS (Model-as-a-Service) / API 平台:**
    - **各大基础模型开发者 (OpenAI API, Google Gemini API, Claude API)**
    - **Perplexity AI:** 在线问答与摘要
    - **Replicate:** 提供模型部署 API
  - **Agent/Orchestration Frameworks (智能体/编排框架):**
    - **LangChain:** 构建 LLM 应用和 Agent 的流行框架
    - **LlamaIndex:** 用于构建 RAG (检索增强生成) 应用
    - **AutoGen (Microsoft):** 多 Agent 协作框架
  - **向量数据库 (Vector Databases):**
    - **Pinecone**
    - **Weaviate**
    - **Qdrant**
    - **ChromaDB**
    - **Milvus/Zilliz**
  - **MLeOps 平台 (ML Operations):**
    - **MLflow, Kubeflow, Weights & Biases:** 模型追踪、实验管理、版本控制

#### **3. 应用层：面向终端用户的产品与服务**

---

- **定义：** 直接面向消费者或企业的 AIGC 驱动的应用产品。
- **主要玩家 (按应用类型):**
  - **文本生成/智能写作:**
    - **ChatGPT (OpenAI):** 通用对话与内容生成
    - **Jasper AI:** 营销文案、博客生成
    - **Copy.ai:** 营销内容生成
    - **Notion AI:** 文档智能助手
    - **GitHub Copilot (Microsoft):** 代码生成
  - **图像/视频/音频生成:**
    - **Midjourney:** 高质量图像生成 (独特风格)
    - **DALL-E 3 (OpenAI):** 图像生成
    - **Stability AI (DreamStudio):** Stable Diffusion 商业应用
    - **RunwayML:** 视频生成与编辑
    - **ElevenLabs:** 语音克隆与合成
  - **教育/学习:**
    - **Duolingo Max:** AI 驱动的语言学习
    - **Khan Academy Khanmigo:** AI 导师
  - **设计/创意:**
    - **Adobe Firefly:** AI 图像与设计工具
    - **Canva Magic Studio:** AI 驱动的设计工具
  - **客户服务/销售:**
    - **Gong.io:** 销售对话分析
    - **Intercom, Zendesk (集成 AI):** 智能客服机器人
  - **专业领域应用:**
    - **Legal AI (e.g., Harvey):** 法律研究与文档生成
    - **Medical AI (e.g., Med-PaLM 2):** 医疗诊断与研究
    - **金融 AI (e.g., BloombergGPT):** 金融信息分析

#### **4. 关键趋势与挑战 (可在 Miro 白板上用便签标出)**

---

- **趋势：**
  - **MaaS (模型即服务) 普及化:** API 调用成为主要消费方式。
  - **多模态融合:** 模型处理和生成多种数据类型 (文本、图像、音频、视频)。
  - **Agent (智能体) 崛起:** LLM 具备规划、工具使用和自我修正能力。
  - **RAG (检索增强生成) 成为主流:** 结合外部知识库提升准确性。
  - **开源模型影响力增强:** Llama、Mixtral、Stable Diffusion 等推动创新。
  - **定制化与微调:** 企业寻求基于自身数据微调专属模型。
  - **边缘 AI:** 小型化模型部署到设备端。
- **挑战：**
  - **成本:** 训练和推理的巨大计算成本。
  - **伦理与偏见:** 模型可能生成有害、歧视性内容，或存在偏见。
  - **幻觉 (Hallucination):** 模型生成不准确或虚假信息。
  - **数据隐私与安全:** 训练数据和用户输入的隐私保护。
  - **算力瓶颈:** 高性能计算资源稀缺。
  - **监管不确定性:** 各国政府对 AI 的监管政策尚不明朗。
  - **人才稀缺:** 掌握 AIGC 全栈技能的工程师供不应求。

---

### **如何在 Miro 中绘制**

1. **登录 Miro：** 访问 [miro.com](https://miro.com/) 并登录或注册。
2. **创建新白板：** 选择“New board”。
3. **使用形状工具：**
   - 用大矩形或框架划分“基础层”、“中间层”、“应用层”。
   - 在每个层内部，用小矩形或圆形代表不同的“主要玩家”。
4. **添加文字：** 在每个形状上或旁边添加对应的公司/模型名称。
5. **使用连接线：**
   - 绘制箭头表示数据流或依赖关系（例如，应用层依赖中间层，中间层依赖基础层）。
   - 使用不同颜色的线表示不同的合作关系或竞争关系。
6. **添加便签 (Sticky Notes)：** 在白板的空白区域，用便签标注“关键趋势”和“挑战”。
7. **使用图标 (Optional):** 如果 Miro 的图标库中有相关的图标，可以用来代表不同的服务或技术。
8. **分享白板：** 点击右上角的“Share”按钮，生成一个公开分享链接或邀请团队成员协作。

希望这个框架能帮助您在 Miro 上成功绘制出 AIGC 市场竞争地图！
