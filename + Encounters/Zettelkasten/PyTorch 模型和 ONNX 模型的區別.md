---
aliases: 模型導出
theme: null
priority: false
date_created: 2024-12-01 06:22
date_update: null
tags: null
---

# **模型導出**

## 目标 (Purpose)

- 这篇笔记的目标是什么？我为什么要记录这个概念或想法？

## 核心概念 (Core Concept)

**模型導出**
模型導出是將模型轉換為其他格式的過程，例如將 PyTorch 模型導出為 ONNX 模型或 TensorFlow 模型。

**PyTorch 模型和 ONNX 模型的區別**

- **PyTorch 模型**: PyTorch 模型是使用 PyTorch 框架開發的模型，模型的結構和參數是以 PyTorch 的內部格式儲存的。
- **ONNX 模型**: ONNX 模型是使用 ONNX 格式儲存的模型，ONNX 是一個開源的模型格式，支持多種深度學習框架，包括 PyTorch、TensorFlow 和 Caffe。

**PyTorch 模型和 TensorFlow 模型的區別**

- **PyTorch 模型**: PyTorch 模型是使用 PyTorch 框架開發的模型，模型的結構和參數是以 PyTorch 的內部格式儲存的。
- **TensorFlow 模型**: TensorFlow 模型是使用 TensorFlow 框架開發的模型，模型的結構和參數是以 TensorFlow 的內部格式儲存的。

**GGUF**

GGUF 是一個用於模型轉換和優化的工具，GGUF 可以將 PyTorch 模型轉換為 ONNX 模型或 TensorFlow 模型，並且可以對模型進行優化和壓縮。

**GGUF 和模型導出的區別**

- **GGUF**: GGUF 是一個工具，用於模型轉換和優化，GGUF 可以將 PyTorch 模型轉換為 ONNX 模型或 TensorFlow 模型，並且可以對模型進行優化和壓縮。
- **模型導出**: 模型導出是將模型轉換為其他格式的過程，例如將 PyTorch 模型導出為 ONNX 模型或 TensorFlow 模型。

總的來說，GGUF 是一個工具，用於模型轉換和優化，而模型導出是將模型轉換為其他格式的過程。

## 详细说明 (Details)

- 对该概念或想法进行详细说明。包括相关的定义、解释、背景信息、数据等。
```python
import torch
from peft import LoraConfig, prepare_model_for_kbit_training, get_peft_model
from transformers import AutoProcessor, BitsAndBytesConfig, Idefics3ForConditionalGeneration

USE_LORA = False
USE_QLORA = False
model_id = "HuggingFaceM4/Idefics3-8B-Llama3"

processor = AutoProcessor.from_pretrained(
    model_id
)

if USE_QLORA or USE_LORA:
    lora_config = LoraConfig(
        r=8,
        lora_alpha=8,
        lora_dropout=0.1,
        target_modules=['down_proj','o_proj','k_proj','q_proj','gate_proj','up_proj','v_proj'],
        use_dora=False if USE_QLORA else True,
        init_lora_weights="gaussian"
    )
    lora_config.inference_mode = False
    if USE_QLORA:
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16
        )
        
    model = Idefics3ForConditionalGeneration.from_pretrained(
        model_id,
        quantization_config=bnb_config if USE_QLORA else None,
        _attn_implementation="flash_attention_2",
        device_map="auto"
    )
    model.add_adapter(lora_config)
    model.enable_adapters()
    model = prepare_model_for_kbit_training(model)
    model = get_peft_model(model, lora_config)
    print(model.get_nb_trainable_parameters())
else:
    model = Idefics3ForConditionalGeneration.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        _attn_implementation="flash_attention_2",
    ).to(DEVICE)
    
    # if you'd like to only fine-tune LLM
    for param in model.model.vision_model.parameters():
        param.requires_grad = False
```


## 连接的笔记 (Related Notes)

- [[笔记A]] - 相关笔记A的概念或想法。
- [[笔记B]] - 相关笔记B的概念或想法。

## 反思 (Reflection)

- 该概念如何与我的其他知识或理解联系起来？
- 它对我的思想、工作或生活有什么影响？
- 有没有新的思考或问题涌现？

## 参考文献 (References)

- 该笔记来源或相关的资源（如书籍、文章、链接等）。
- [书籍名](https://link) — 相关书籍。
