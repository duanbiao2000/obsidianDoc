---
aliases: 
categories: 
high_priority: false
createdAt: 2024-12-09T12:04:00
updateAt: 2024-12-09T12:11:00
tags:
---

<< [[2024-11-14]] | [[2024-11-16]] >>

# Transformer

Transformer是一种深度学习模型，它完全依赖于自注意力机制（self-attention mechanism），摒弃了传统的循环神经网络（RNN）和卷积神经网络（CNN）的架构。Transformer最初由Vaswani等人在2017年的论文《Attention is All You Need》中提出，并迅速成为自然语言处理（NLP）任务中的主流模型架构。

以下是Transformer的基本结构：

### 编码器（Encoder）
编码器是Transformer的一部分，负责接收输入序列并将其转换为一个上下文相关的表示。一个完整的编码器由多个相同的层堆叠而成，每一层包含两个子层：
1. **多头自注意力机制（Multi-head Self-Attention）**：这个子层允许模型关注输入序列中的不同位置，从而捕捉序列中单词之间的关系。通过使用多头，模型可以同时从不同的表示空间中学习信息。
2. **前馈神经网络（Feed-Forward Neural Network）**：这是一个简单的全连接层，应用于每个位置的元素。

每经过一个多头自注意力机制和前馈神经网络之后，都会有一个残差连接（residual connection），然后跟一个归一化层（Layer Normalization）。

### 解码器（Decoder）
解码器同样由多个相同的层组成，但每一层有三个子层：
1. **遮蔽的多头自注意力机制（Masked Multi-head Self-Attention）**：与编码器类似，但为了防止位置看到后续的位置，对未来的标记进行了遮蔽。
2. **多头注意力机制（Multi-head Attention）**：这个子层让解码器专注于编码器输出的特定部分。它将编码器的输出作为键（key）和值（value），而查询（query）来自解码器的前一层。
3. **前馈神经网络（Feed-Forward Neural Network）**：与编码器相同，是一个应用于每个位置的全连接层。

解码器的每个子层后也有残差连接和归一化层。

### 位置编码（Positional Encoding）
由于Transformer没有像RNN那样的内在顺序，所以需要加入位置编码来给模型提供关于序列中元素相对或绝对位置的信息。位置编码被加到输入的嵌入向量上。

### 输出线性变换和Softmax
解码器的最终输出会通过一个线性变换和一个softmax函数，得到下一个预测词的概率分布。

### 注意力机制（Attention Mechanism）
这是Transformer的核心。注意力函数可以被认为是在一系列键值对（key-value pairs）中查找查询（query）的过程。具体来说，它计算查询和所有键之间的相似度得分，然后通过softmax函数将这些得分转换为权重，最后用这些权重对值进行加权求和。

### 多头注意力（Multi-head Attention）
多头注意力允许模型在不同的表示子空间中多次执行注意力函数。这有效地让模型可以关注不同类型的特征。

这就是Transformer的基本结构。由于其高效的并行化能力，Transformer已经被广泛用于各种任务，包括但不限于机器翻译、文本摘要、问答系统等。

## 随机名言
> [!quote] I can't change the direction of the wind, but I can adjust my sails to always reach my destination.
> — Jimmy Dean

## 每日一图

![photo by Robert Lukeman(https://unsplash.com/@robertlukeman?utm_source=templater_proxy&utm_medium=referral) on Unsplash](https://images.unsplash.com/photo-1472214103451-9374bd1c798e?crop=entropy&cs=srgb&fm=jpg&ixid=M3w2NDU1OTF8MHwxfHJhbmRvbXx8fHx8fHx8fDE3MzE2NDM5NDh8&ixlib=rb-4.0.3&q=85&w=800&h=800)







