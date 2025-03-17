---
aliases: 
createdAt: 2025-02-24 11:18
updateAt: 
categories:
  - Mindset
tags:
  - Mindset/Reflection
  - Tech/Code
  - Action/Writing
---
[DeepSeek](https://www.deepseek.com/)

## 关键术语解释

- **MoE (Mixture of Experts)**: 混合专家模型，一种神经网络架构，通过将不同的“专家”网络组合起来处理不同的输入，从而提高模型性能。
- **Dense**: 密集连接层，神经网络中最常见的层类型，每个神经元都与前一层的所有神经元相连。
- **Activated Params**: 被激活的参数数量，指模型在运行过程中实际参与计算的参数数量。MoE 模型通常只有一部分参数被激活。
- **Total Params**: 总参数数量，指模型中所有参数的总数。
- **EM (Exact Match)**: 精确匹配，指模型答案与标准答案完全一致的比例。
- **F1 (F1-score)**: F1 分数，精确率 (precision) 和召回率 (recall) 的调和平均值，用于综合评估模型的性能。
- **Acc. (Accuracy)**: 准确率，指模型预测正确的比例。
- **Pass@1**: 一次尝试答对的比例。
- **COT (Chain-of-Thought)**: 思维链，一种提示技术，通过引导模型生成一系列中间推理步骤来提高解决复杂问题的能力。

## AI 核心概念

- **模型架构**: 指模型的网络结构，例如 MoE 或 Dense。不同的架构适用于不同的任务和数据。
- **参数数量**: 模型中可学习的参数数量，通常来说，参数越多，模型的容量越大，但也更容易过拟合。
- **语言理解**: 指模型理解自然语言的能力，例如 MMLU、DROP 等测试集考察的就是模型在这方面的能力。
- **代码能力**: 指模型生成和理解代码的能力，例如 HumanEval-Mul、LiveCodeBench 等测试集考察的就是模型在这方面的能力。
- **数学能力**: 指模型进行数学推理和计算的能力，例如 AIME 2024、MATH-500 等测试集考察的就是模型在这方面的能力。
- **中文能力**: 指模型理解和使用中文的能力，例如 CLJEWSC、C-Eval 等测试集考察的就是模型在这方面的能力。





- **GPQA-Diamond (Pass@1)**: GPQA-Diamond 可能是某个问答测试集，专注于考察模型在特定领域的知识。Pass@1 指的是模型在一次尝试中答对的比例。

## 代码测试基准 (Code)

- **HumanEval-Mul (Pass@1)**: HumanEval-Mul 可能是评估模型生成代码能力的测试集，Mul 可能指 multiple (多个)，表示测试集中包含多个问题。Pass@1 指的是模型在一次尝试中生成的代码能够通过所有测试用例的比例。
- **LiveCodeBench (Pass@1-COT)**: LiveCodeBench 可能是评估模型在真实场景下编写代码能力的测试集。Pass@1-COT 指的是模型在一次尝试中生成的代码，借助思维链 (Chain-of-Thought, COT) 的提示，能够通过所有测试用例的比例。
- **LiveCodeBench (Pass@1)**: 与上一个测试集相同，但不使用思维链提示。
- **Codeforces (Percentile)**: Codeforces 是一个在线编程竞赛平台，Percentile 指的是模型在 Codeforces 上的表现超过了多少百分比的参赛者。
- **SWE Verified (Resolved)**: SWE 可能是 Software Engineering (软件工程) 的缩写，Verified (Resolved) 指的是模型生成的代码通过了验证，并且解决了问题。
- **Aider-Edit (Acc.)**: Aider-Edit 可能是评估模型在代码编辑任务上的表现，Acc. 指的是准确率。
- **Aider-Polyglot (Acc.)**: Aider-Polyglot 可能是评估模型在多种编程语言之间进行转换或处理代码能力的表现，Acc. 指的是准确率。
"Aider-Polyglot"并不是一个标准的英语单词或固定搭配。从字面上看，可以将其拆分为两个部分：“Aider”和“Polyglot”。其中，“Aider”可以理解为帮助者或助手；“Polyglot”指的是通晓多种语言的人。因此，“Aider-Polyglot”可能是指一个能够帮助使用多种语言的人或系统。




