---
id: a0ba83bb-1d2e-427b-a0fa-7d3dd58de8ac
---

# ⁡⁡⁤⁡⁣​﻿‬﻿‌⁢⁡​‍‌‬​⁡⁡﻿⁤‬​​‬⁤​‍﻿⁣‌⁡​‍⁢‍⁢⁣‬​⁡⁡‍​⁤‍⁡​‍聊聊Agent、RAG主流开发技术和未来应用【闭门活动报名中 6月15日】 - 飞书云文档
#Omnivore

[Read on Omnivore](https://omnivore.app/me/agent-rag-6-15-1901744caa9)
[Read Original](https://miracleplus.feishu.cn/docx/KT9qd7XEyo7xu6x4kcSc3fyfnBd)

## Highlights

> <mark class="hltr-yellow">All tools agent 于 2023 年 11 月 Dev day 发布，集成了 web searching, code interpreter, DALLE-3 这三个 tools，除此之外还隐式地集成了 web browsing，本地 RAG 这两个功能。使得用户在使用时不用再手动配置自己的 tools，配置tools和选择 tools 的成本转嫁到模型，客观上确实提升了体验。</mark> [⤴️](https://omnivore.app/me/agent-rag-6-15-1901744caa9#8d452b0a-2265-4c4e-8b0b-76e735000eab)  ^8d452b0a

> <mark class="hltr-yellow">这可能意味着“每次回答都用 search”（AI 搜索引擎）的产品形态和“每次回答都不用 search”（ChatBot）的产品形态的定位确实存在差异化的空间。</mark> [⤴️](https://omnivore.app/me/agent-rag-6-15-1901744caa9#c2aee87e-0c71-4e15-9018-a6f3eaeb887a)  ^c2aee87e

> <mark class="hltr-blue">于 2023 年 7 月初发布，主打 ChatGPT 写完代码后可以自动运行，如果代码报错，那么可以自动根据错误来生成新的代码，再尝试运行。如果 ChatGPT 尝试次数达到 3 次或以上，那么会输出“无法完成任务”的回复。</mark> [⤴️](https://omnivore.app/me/agent-rag-6-15-1901744caa9#85f99edd-c22f-4c07-9b85-7005a054933d)  ^85f99edd

> <mark class="hltr-red">后续 code interpreter改名为 data analysis，并且围绕着数据分析 场景做了很多用户体验上的优化，比如数据处理时生成的图片可以进行放大居中，聊天栏变为侧边栏，使得用户可以 chat with figure等。</mark> [⤴️](https://omnivore.app/me/agent-rag-6-15-1901744caa9#593a3274-6896-4da5-bb15-da1c10c417e0)  ^593a3274

> <mark class="hltr-yellow">反而是围绕着代码和数据处理的 code interpreter，和 all-tools agent 具有一定的实用性。</mark> [⤴️](https://omnivore.app/me/agent-rag-6-15-1901744caa9#76e52912-a51c-49bb-a9cc-ec391f644afb)  ^76e52912

> <mark class="hltr-red">一个在使用工具时 work的 agent，必然要在模型层有足够多的关于这个 tool 的语料才行</mark> [⤴️](https://omnivore.app/me/agent-rag-6-15-1901744caa9#1043b942-a01e-4106-8d4b-4168e690fef0)  ^1043b942

> <mark class="hltr-green">一个实用的 agent，开发必然不能仅仅限于 prompt层面的开发，要做很多判断的机制，而且很多机制是用 code 来硬编码的，而不是用自然语言 prompt 来表达的。很讽刺的一点是：用 OpenAI 提供的 agent 开发平台（Assistant）来做写 prompt层面的开发，那么无论如何也做不出来code interpreter 这样的 agent。</mark> [⤴️](https://omnivore.app/me/agent-rag-6-15-1901744caa9#3c0258ae-5b83-4c84-b184-af8a991fd6aa)  ^3c0258ae

> <mark class="hltr-yellow">这同时也解释了为什么 agent应用落地场景的 50%以上都是 RAG 问答，以及 CRUD 的简单任务（因为这些场景老板不会遇到上面那个致命问题）。</mark> [⤴️](https://omnivore.app/me/agent-rag-6-15-1901744caa9#b42c6ca0-9f81-4a35-a7f2-ffd2daff4a6d)  ^b42c6ca0

当涉及到B端智能助理的实例时，以下是两个相关的实际应用案例：

1. RPA（Robotic Process Automation）实例：假设有一家银行，他们需要将客户的电子邮件中的某些信息提取出来，并将其输入到他们的内部系统中。传统的方法是手动复制和粘贴这些信息，但这很费时且容易出错。通过使用RPA技术，银行可以开发一个智能助理来自动提取电子邮件中的信息，并将其自动输入到内部系统中，从而实现自动化的数据处理过程。

2. Flow（工作流）实例：假设一个企业拥有一个复杂的审批流程，需要经过多个部门的审核和批准。在传统方法中，这个过程可能需要通过电子邮件或纸质文件进行来回传递，并可能涉及到手动跟踪和协调。通过使用Flow（工作流）工具，企业可以创建一个自动化的工作流程，定义每个步骤的执行顺序和条件，并将任务自动分派给相关的部门和人员。这使得整个审批流程更加高效、可追踪和可管理。



---
# ⁡⁡⁤⁡⁣​﻿‬﻿‌⁢⁡​‍‌‬​⁡⁡﻿⁤‬​​‬⁤​‍﻿⁣‌⁡​‍⁢‍⁢⁣‬​⁡⁡‍​⁤‍⁡​‍聊聊Agent、RAG主流开发技术和未来应用【闭门活动报名中 6月15日】 - 飞书云文档

如果 agent 犯错并造成了不可挽回损失，那么谁应该为此负责？​

目前通常认为，在企业生产中，agent 的自主性和稳定性这两点是无法兼得的，那么如何在 agent 的自主性和稳定性之间取一个平衡就是个重要的问题。而从目前落地情景和案例来看，企业可能更倾向于稳定性而不是自主性。​

​

算一笔账： 如果一个 agent 可以帮一个员工每天节省 5 分钟，但是代价是：有 5%的概率造成企业内 500 万人民币的损失，那么你是否会为这个 agent 买单？​

​

基于对这两个问题的回答来迭代 agent可能落地的场景，，这样无论是对流程做迭代，还是追责到具体环节都变成了可能。==这同时也解释了为什么 agent应用落地场景的 50%以上都是 RAG 问答，以及 CRUD 的简单任务（因为这些场景老板不会遇到上面那个致命问题）。==​

Zapier 是个典型的 RPA 产品，同时也在尝试往 agent 方向切入。Zapier 的 agent最早亮相于 OpenAI 2023 年 4 月的 plugin store。当时作为一个 plugin 出现，主打一句话生成固定的 workflow (text to workflow)，并且在 OpenAI 2023 年 11 月的 Dev day上亮相。​

LLM 在其中扮演的角色更像是一个 RPA workflow generating copilot，而不是一个 agent。LLM提供的价值在于让人更方便地 生成一个 RPA workflow，而不在于让 LLM 在运行时根据实时环境做决策。为此买单的用户大多都是为了解决 RPA 能够解决的问题，如 Zapier 早期投放时的定位：“如何把一个软件的信息同步到另一个软件”​

类似的产品有很多，如 Make, QuestFlow 等，定位更像是 RPA 在 LLM 时代的延续。特点是完全稳定，完全不会出错，但是自主性不强。​

Dify 最早亮相于 2023 年中，当时提供的是 ChatBot的无代码编辑框架（with or without plugins），后续在 2024 年 4 月推出了 workflow 编辑器。主打的是低代码编辑 workflow，并且在 RAG 方面做了大量的优化。截止六月已经有 30k+ Github Star。​

类似的产品有很多，比如 FastGPT，LangFlow，Flowise，Retool AI等。特点是可以拖拉拽快速编辑一个 agent，不像 RPA 一样限制死 agent 的行为，有 LLM 参与其中少数环节，逻辑判断等则大多都是交给硬逻辑来判断的，淡化 tool use 这些设计，从框架层保证 agent 输出的稳定性。​

flow 这种设计天然就适合解决企业内的 corner case，并且也适合和企业内的流程打通，目前来看，最为广泛的 B 端 agent 落地场景的产品形态属于这种产品形态，比如 RAG chatbot 等。​

agent 设计范式一定是和应用场景是深度绑定的，论文中的几种 agent 设计范式，在实际落地中可以借鉴，但不仅限于此。目前不存在通用的设计范式。需要针对场景 case by case 地设计 agent。如单次 Q&A 任务：用AutoGPT 式的 agent planning 不如 LLM+RAG 单次召回。再比如路径和判定规则清晰的场景（如 24 点游戏），用 Tree of Thought 要比单次召回要有效。故当我们谈论 agent的时候，一定不能把它和场景分开。​

目前 B 端落地场景内的企业普遍更关注稳定性，而不是自主性。让 agent 在可控的范围内运行，还能达成降本增效的目的，这是符合 B 端喜好的产品。合理的产品形态就是 RAG（Agent 场景 50%以上的场景都是 RAG，见 LangChain2023 年末的开发者报告），比如客服，企业内问答等。​

B 端的我更看好的是 Agent 对于传统 SaaS场景的补充，即 Agent powered SaaS，而不是 Agent as a Service。其中传统的 SaaS 可能占 90%，AI 只占 10%。使得企业在特定场景下给予 agent 一定程度的自主能力以赋能现有工作流，而不是让 agent 接管企业内的多数的 API。产品形态和场景强绑定，和传统 SaaS 的形态类似。​

C 端的壁垒和 B 端是不同的。 C 端生产力工具的壁垒可能更多集中在模型侧，或者网络效应（但我目前没看到 AI 时代具有网络效应壁垒的产品），而 B 端产品的壁垒更多是以 SaaS 形式体现的，即行业认知行业地位等，和场景和行业强绑定。这意味着可能初创公司在 AI / agent这一波浪潮中，如果要做生产力场景的产品，可能还是 B 端机会更多一些。​

C 端生产力向的 agent产品可能会越来越向头部模型商集中，B 端机会更广泛，对初创公司更友好。​

讨论 Code 和 Agent 要考虑这两者的相互关系。​

