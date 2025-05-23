---
aliases: 
categories: 
important: false
date: 2024-12-09T12:04:00
update: 2024-12-09T12:11:00
tags:
---
好的，这是根据[[&高效学习卡片原则]]以及Zettelkasten和费曼学习原理的要求，对你的 Transformer 笔记进行整理后的版本：


# ✨ 高效学习卡片：Transformer 模型

> [!tip] 🌱 核心原则
> 理解 Transformer 的核心在于其完全依赖 **自注意力机制 (Self-Attention)** 来捕捉输入数据的依赖关系，摒弃了传统 RNN 的顺序处理和 CNN 的局部性假设。
> * **全局依赖捕捉 (通过自注意力)** > 顺序依赖处理 (RNN) 或 局部依赖处理 (CNN)
> * **高度并行化计算** > 序列计算限制 (RNN)

## 关键方法/组件

*   🧠 **自注意力机制 (Self-Attention):** 允许模型在处理序列中的某个元素时，同时权衡序列中所有其他元素的重要性。它通过计算查询 (Query) 与所有键 (Key) 的相似度得分，并用这些得分对值 (Value) 进行加权求和，来获得该元素的上下文表示。公式核心: $$Attention(Q, K, V) = softmax(QK^T / sqrt(d_k))V$$
*   ✨ **多头注意力 (Multi-head Attention):** 将自注意力过程并行执行多次（形成多个“头”），每个头从不同的表示子空间学习信息。这使得模型能够同时关注来自不同位置和不同方面的特征，并将这些信息整合起来。
*   📍 **位置编码 (Positional Encoding):** 由于 Transformer 缺乏处理序列顺序的内在机制（如 RNN 的循环结构），需要显式地将位置信息添加到输入嵌入中，让模型了解单词的相对或绝对位置。
*   🛠️ **编码器-解码器架构 (Encoder-Decoder Structure):**
    *   **编码器 (Encoder):** 由 N 个相同的层堆叠而成，每层包含一个多头自注意力子层和一个前馈神经网络子层。负责将输入序列映射为连续的上下文表示。
    *   **解码器 (Decoder):** 也由 N 个相同的层堆叠而成，但每层包含三个子层：一个遮蔽的多头自注意力子层（防止看到未来信息）、一个多头注意力子层（关注编码器的输出）和一个前馈神经网络子层。负责根据编码器的输出和已生成的部分，生成目标序列。
*   🔗 **残差连接与层归一化 (Residual Connection & Layer Normalization):** 应用于每个子层的输出之后。残差连接有助于避免梯度消失，促进深层网络的训练；层归一化则用于稳定训练过程中的激活值。





