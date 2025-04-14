# LangChain和LangGraph的分工与合作

## LangChain

LangChain是一个用于构建复杂AI系统的库，它允许开发者创建具有多种技能的AI代理，并支持多代理系统。LangChain的核心是LangChain Agent，它是一个可以执行各种任务（如浏览器、编辑器、研究者、审查者、修订者、编写者、发布者）的AI代理。

## LangGraph

LangGraph是LangChain的一个扩展，它提供了构建具有状态和多个AI代理的应用程序的能力。LangGraph的核心是LangChain Flow，它是一个可以执行一系列任务（如规划、数据收集与分析、审查与修订、撰写与提交、发布）的AI代理。

## 分工与合作

在GPT Researcher项目中，LangChain和LangGraph被用来构建一个多代理系统，该系统能够自动执行从规划到发布的整个研究过程。具体来说：

- **LangChain**：用于创建具有多种技能的AI代理，如浏览器、编辑器、研究者、审查者、修订者、编写者、发布者。这些代理可以执行各种任务，如浏览网页、编辑文本、进行深度研究、审查研究结果、修订研究结果、撰写报告、发布报告等。

- **LangGraph**：用于创建一个能够执行一系列任务的AI代理，如规划、数据收集与分析、审查与修订、撰写与提交、发布。LangGraph能够协调多个LangChain代理，使其能够协同工作，共同完成整个研究过程。

通过LangChain和LangGraph的分工与合作，GPT Researcher能够实现一个高度自动化和高效的研究过程，大大提高了研究质量和效率。