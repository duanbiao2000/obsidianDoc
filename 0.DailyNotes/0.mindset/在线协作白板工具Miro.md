---
date: 2025-06-18 17:15
tags:
  - Domain/Mindset/Tools
---
好的，这是根据您的要求，使用指定符号对笔记 [[在线协作白板工具Miro]] 进行改写后的版本：

---

## 在线协作白板工具Miro (符号版)

---
date: 2025-06-18 17:15
tags:
  - Domain/Mindset/Tools
---

Miro 是一款**在线协作白板工具**。

它提供了一个无限大的数字画布。`团队 → 头脑风暴/流程图/思维导图/项目规划/设计冲刺`。`可添加便签/文字/图片/视频/文档 + 预设模板`。Miro 的核心价值在于**实时协作**。`多用户同时工作 (无论何地) → 像面对面一样高效`。

### **绘制 AIGC 市场竞争地图 (Miro 链接)**

`我无法直接在Miro创建/分享实际可交互白板`。`可构思AIGC市场竞争地图框架/内容`。

`以下结构/元素 → Miro绘制 → 帮助团队清晰理解AIGC市场玩家/做什么/关系`。

---

### **AIGC 市场竞争地图框架**

`地图 → 按AIGC核心价值链划分 → 识别主要参与者`。

#### **1. 基础层：基础设施与模型提供商**

---

-   **定义：** 提供底层计算能力、大型基础模型以及模型训练与部署平台。`它们 → AIGC生态基石`。
-   **主要玩家：**
    -   **云计算巨头 (算力与平台):**
        -   Amazon Web Services (AWS): EC2, Sagemaker, Bedrock (提供模型访问)
        -   Microsoft Azure: Azure OpenAI Service, Azure ML
        -   Google Cloud: Vertex AI, Google Gemini API
        -   NVIDIA: GPU硬件, CUDA, TensorRT (AI推理优化)
    -   **基础模型开发者 (通用大模型):**
        -   OpenAI: GPT系列 (GPT-4, GPT-3.5), DALL-E, Sora
        -   Google DeepMind: Gemini系列, Imagen
        -   Meta AI: Llama系列 (开源), Emu
        -   Anthropic: Claude系列
        -   Mistral AI: Mistral, Mixtral (开源)
        -   Cohere: Command, Embed
        -   Stability AI: Stable Diffusion
        -   Midjourney: Midjourney (闭源图片生成)
    -   **开源社区/模型分发平台:**
        -   Hugging Face: `大量开源模型/数据集/Spaces → 促进模型共享/协作`。

#### **2. 中间层：工具链与平台**

---

-   **定义：** `构建于基础模型之上 → 提供AIGC应用开发/部署/管理工具/框架/API`。`开发者 → 更易集成/利用AIGC能力`。
-   **主要玩家：**
    -   **MaaS (Model-as-a-Service) / API 平台:**
        -   各大基础模型开发者 (OpenAI API, Google Gemini API, Claude API)
        -   Perplexity AI: 在线问答与摘要
        -   Replicate: 提供模型部署 API
    -   **Agent/Orchestration Frameworks (智能体/编排框架):**
        -   LangChain: 构建 LLM 应用和 Agent 的流行框架
        -   LlamaIndex: 用于构建 RAG (检索增强生成) 应用
        -   AutoGen (Microsoft): 多 Agent 协作框架
    -   **向量数据库 (Vector Databases):**
        -   Pinecone
        -   Weaviate
        -   Qdrant
        -   ChromaDB
        -   Milvus/Zilliz
    -   **MLeOps 平台 (ML Operations):**
        -   MLflow, Kubeflow, Weights & Biases: 模型追踪、实验管理、版本控制

#### **3. 应用层：面向终端用户的产品与服务**

---

-   **定义：** `直接面向消费者/企业 → AIGC驱动应用产品`。
-   **主要玩家 (按应用类型):**
    -   **文本生成/智能写作:**
        -   ChatGPT (OpenAI): 通用对话与内容生成
        -   Jasper AI: 营销文案、博客生成
        -   Copy.ai: 营销内容生成
        -   Notion AI: 文档智能助手
        -   GitHub Copilot (Microsoft): 代码生成
    -   **图像/视频/音频生成:**
        -   Midjourney: 高质量图像生成 (独特风格)
        -   DALL-E 3 (OpenAI): 图像生成
        -   Stability AI (DreamStudio): Stable Diffusion 商业应用
        -   RunwayML: 视频生成与编辑
        -   ElevenLabs: 语音克隆与合成
    -   **教育/学习:**
        -   Duolingo Max: AI 驱动的语言学习
        -   Khan Academy Khanmigo: AI 导师
    -   **设计/创意:**
        -   Adobe Firefly: AI 图像与设计工具
        -   Canva Magic Studio: AI 驱动的设计工具
    -   **客户服务/销售:**
        -   Gong.io: 销售对话分析
        -   Intercom, Zendesk (集成 AI): 智能客服机器人
    -   **专业领域应用:**
        -   Legal AI (e.g., Harvey): 法律研究与文档生成
        -   Medical AI (e.g., Med-PaLM 2): 医疗诊断与研究
        -   金融 AI (e.g., BloombergGPT): 金融信息分析

#### **4. 关键趋势与挑战 (可在 Miro 白板上用便签标出)**

---

-   **趋势：**
    -   MaaS (模型即服务) 普及化 `↑`。`API调用 → 主要消费方式`。
    -   多模态融合 `↑`。
    -   Agent (智能体) 崛起 `↑`。
    -   RAG (检索增强生成) 成为主流 `↑`。`结合外部知识库 → 准确性↑`。
    -   开源模型影响力增强 `↑`。`推动创新↑`。
    -   定制化与微调 `↑`。
    -   边缘 AI `↑`。
-   **挑战：**
    -   △成本 `↑`。
    -   △伦理与偏见。
    -   △幻觉。
    -   △数据隐私与安全。
    -   △算力瓶颈。
    -   △监管不确定性。
    -   △人才稀缺。