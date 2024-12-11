
### LMDeploy 和 TurboMind 进化表 (2023-2024)

| **日期**       | **更新内容**                                                                                          |
|----------------|-------------------------------------------------------------------------------------------------------|
| **2023/07**    | - TurboMind 支持 Llama-2 70B with GQA。<br> - TurboMind 支持 Llama-2 7B/13B。<br> - TurboMind 支持 InternLM 的张量并行推理。 |
| **2023/08**    | - TurboMind 支持 flash-attention2。<br> - TurboMind 支持 Qwen-7B, 动态 NTK-RoPE 缩放和动态 logN 缩放。<br> - TurboMind 支持 Windows (tp=1)。<br> - TurboMind 支持 4-bit 推理，比 FP16 快 2.4 倍，是最快的开源实现。<br> - LMDeploy 在 HuggingFace Hub 上线，提供即用型 4-bit 模型。<br> - LMDeploy 支持使用 AWQ 算法进行 4-bit 量化。 |
| **2023/09**    | - TurboMind 支持 Qwen-14B。<br> - TurboMind 支持 InternLM-20B。<br> - TurboMind 支持 Code Llama 的所有特性：<br>   &nbsp;&nbsp;• 代码补全<br>   &nbsp;&nbsp;• 内填<br>   &nbsp;&nbsp;• 聊天 / 指令<br>   &nbsp;&nbsp;• Python 专家<br> - TurboMind 支持 Baichuan2-7B。 |
| **2023/11**    | - Turbomind 支持多模态输入。<br> - Turbomind 支持直接加载 Hugging Face 模型。 |
| **2023/11**    | - TurboMind 重大升级：<br>   &nbsp;&nbsp;• 分页注意力机制<br>   &nbsp;&nbsp;• 更快的注意力内核，无序列长度限制<br>   &nbsp;&nbsp;• KV8 内核提速 2 倍<br>   &nbsp;&nbsp;• Split-K 解码（Flash 解码）<br>   &nbsp;&nbsp;• sm_75 的 W4A16 推理 |
| **2024/01**    | - 开放 AOE 与 LMDeploy Serving Service 无缝集成。<br> - 支持多模型、多机、多卡推理服务。<br> - 支持 PyTorch 推理引擎，完全用 Python 开发，降低开发者门槛，快速实验新功能和技术。 |
| **2024/02**    | - 支持 Qwen 1.5, Gemma, Mistral, Mixtral, Deepseek-MOE 等。 |
| **2024/03**    | - 支持 DeepSeek-VL 离线推理管道和服务。<br> - 支持 VLM 离线推理管道和服务。 |
| **2024/04**    | - 支持 Llama3 及更多 VLMs，如 InternVL v1.1, v1.2, MiniGemini, InternLMXComposer2。<br> - TurboMind 添加在线 int8/int4 KV 缓存量化和推理支持。<br> - TurboMind 最新升级提升 GQA，使 internlm2-20b 模型推理速度达到 16+ RPS，比 vLLM 快约 1.8 倍。<br> - 支持 Qwen1.5-MOE 和 dbrx。 |
| **2024/05**    | - 在部署 VLMs 时平衡视觉模型，尤其是在多 GPU 环境下。<br> - 支持 4-bits 权重量化及推理，适用于 InternVL v1.5, LLaVa, InternLMXComposer2 等 VLMs。 |
| **2024/06**    | - PyTorch 引擎支持 DeepSeek-V2 和多个 VLMs，如 CogVLM2, Mini-InternVL, LlaVA-Next。 |
| **2024/07**    | - 支持 Llama3.1 8B, 70B 及其工具调用。<br> - 支持 InternVL2 全系列模型，InternLM-XComposer2.5 及其函数调用。 |
| **2024/08**    | - LMDeploy 集成到 modelscope/swift 中作为 VLMs 推理的默认加速器。 |
| **2024/09**    | - LMDeploy PyTorchEngine 增加对华为 Ascend 的支持。<br> - LMDeploy PyTorchEngine 在 Llama3-8B 推理中通过引入 CUDA 图形实现了 1.3 倍的速度提升。 |
| **2024/10**    | - PyTorchEngine 在 Ascend 平台上支持图形模式，使推理速度加倍。 |
| **2024/11**    | - 支持 Mono-InternVL 与 PyTorch 引擎。 |

这份进化表展示了 LMDeploy 和 TurboMind 在过去一年半中的显著进展，包括对多种模型的支持、性能优化以及对不同硬件平台的支持等。这不仅体现了技术上的不断创新，也反映了社区和企业对于提高深度学习模型推理效率的需求。