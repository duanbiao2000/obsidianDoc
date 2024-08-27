---
id: f2006204-bbb1-432c-9be2-6c0381a45144
---

# 扣子(Coze)实战教程 | AI应用教程
#Omnivore

[Read on Omnivore](https://omnivore.app/me/coze-ai-19000dded4f)
[Read Original](https://bzfree.com/coze/)

## Highlights

> <mark class="hltr-red">广义来说：AI应用开发是指利用人工智能（Artificial Intelligence, AI）技术来设计、构建和维护软件应用程序的过程。</mark> [⤴️](https://omnivore.app/me/coze-ai-19000dded4f#b876c51f-ba7a-4d67-aea7-ebcb75875db4)  ^b876c51f

> <mark class="hltr-red">在我们教程里的**AI应用开发**指的是：**利用大语言模型(LLM) 应用开发平台快速搭建生产级的生成式 AI 应用。**</mark> [⤴️](https://omnivore.app/me/coze-ai-19000dded4f#9021f4b1-8d1f-442a-8457-805d479e8a76)  ^9021f4b1

> <mark class="hltr-yellow">学习AI应用开发可以帮助开发者掌握最新的AI应用开发技能，保持竞争力。你可以通过开发自己的应用，解决公司的复杂的业务流程。如果你开发一款解决某些行业痛点的AI应用，也可以进行出售，赚取利润。 目前AI技术正迅速改变众多行业，学习AI应用开发不仅仅是为了掌握一个特定的工具，更是为了理解和利用AI技术来推动个人和企业的发展。</mark> [⤴️](https://omnivore.app/me/coze-ai-19000dded4f#69d6cf20-33a6-463b-ae59-e5859fd4c932)  ^69d6cf20

> <mark class="hltr-blue">大语言模型(LLM) 应用开发平台目前有很多，例如：扣子(Coze)、Dify、Fastgpt、Langchatchat、Flowise、Langflow、Bisheng等这些都是目前一些主流的开发平台。</mark> [⤴️](https://omnivore.app/me/coze-ai-19000dded4f#014ec590-e023-45f9-acdb-fd124a8f55a3)  ^014ec590

> <mark class="hltr-red">### 1\. 什么是知识库 [​](#%5F1-什么是知识库)</mark>
>
><mark class="hltr-red"> 大语言模型的训练数据一般基于公开的数据，这意味着模型的知识**一般不会包含私有领域的知识**，同时在公开知识领域**存在一定的滞后性**。为了解决这一问题，目前通用的方案是采用 \*\*RAG（检索增强生成）\*\*技术，**使用用户问题来匹配最相关的外部数据**，将检索到的相关内容召回后作为模型提示词的上下文来重新组织回复。</mark> [⤴️](https://omnivore.app/me/coze-ai-19000dded4f#f084feda-6828-4896-9348-d46006e12bac)  ^f084feda

> <mark class="hltr-red">### 1\. 什么是工作流 [​](#%5F1-什么是工作流)</mark>
>
><mark class="hltr-red"> 工作流是可以让用户能够通过**直观的方式**，**灵活地组合插件**、**大型语言模型和代码模块等元素，构建出既复杂又稳固的业务的流程。** 这在执行如旅行规划、报告分析等任务时尤为有效。当面临包含多个步骤的任务场景，并且对输出结果的精确度和格式有着严格标准时，采用工作流配置将是一个理想的选择。</mark> [⤴️](https://omnivore.app/me/coze-ai-19000dded4f#e28a942a-079d-48fa-9d5e-49817b54c543)  ^e28a942a

> <mark class="hltr-yellow">通过变量节点的定义，可以知道：使用变量节点之前要有个前提，就是**首先要有个Bot，并且这个Bot里定义了一变量，否则单独使用变量是没有意义的。**</mark> [⤴️](https://omnivore.app/me/coze-ai-19000dded4f#1b9ddd39-26b1-4a5b-b117-9f551b3e6639)  ^1b9ddd39


---
# 扣子(Coze)实战教程 | AI应用教程

🔊 声明

**教程内容：** 本教程是斜杠君精心为大家准备的，全网最细节AI应用系列教程之一，手把手带你创建AI应用，功能点级细节教程，愿大家能有所收获。

**版权说明：** 著作权归作者所有。转载请 [联系作者](https://www.bzfree.com/about "联系作者")。

## 引言 [​](#引言)

### 1\. 什么是AI应用开发 [​](#%5F1-什么是ai应用开发)

首先明确一下**AI应用开发**的定义。==广义来说：AI应用开发是指利用人工智能（Artificial Intelligence, AI）技术来设计、构建和维护软件应用程序的过程。==

==在我们教程里的==**==AI应用开发==**==指的是：==**==利用大语言模型(LLM) 应用开发平台快速搭建生产级的生成式 AI 应用。==**

例如：如果你是文案编辑人员，你可以利用可以开发一款**文案写作**应用，提高自己的文案写作效率； 如果你是一名**股票玩家**，你可以开发一款股票分析应用，实时分析市场行情，为投资指点迷津。

而且相比代码开发方式，即使你是非技术人员，也能参与到 AI 应用的定义和数据运营过程中。

### 2\. 为什么要学习AI应用开发 [​](#%5F2-为什么要学习ai应用开发)

通过学习AI应用开发，可以帮助你提高工作效率，减少重复性劳动。 ==学习AI应用开发可以帮助开发者掌握最新的AI应用开发技能，保持竞争力。你可以通过开发自己的应用，解决公司的复杂的业务流程。如果你开发一款解决某些行业痛点的AI应用，也可以进行出售，赚取利润。 目前AI技术正迅速改变众多行业，学习AI应用开发不仅仅是为了掌握一个特定的工具，更是为了理解和利用AI技术来推动个人和企业的发展。==

### 3\. AI应用开发平台有哪些 [​](#%5F3-ai应用开发平台有哪些)

==大语言模型(LLM) 应用开发平台目前有很多，例如：扣子(Coze)、Dify、Fastgpt、Langchatchat、Flowise、Langflow、Bisheng等这些都是目前一些主流的开发平台。==在本教程中，我们先来学习扣子(Coze)的应用开发。

---

关注公众号

![斜杠君微信公众号二维码](https://proxy-prod.omnivore-image-cache.app/200x0,sgxWx5jk1OoMMAF_C-F3JqDf-vOSTTocma_fO1iQNQss/https://bzfree.com/images/common/qrcode.jpg)

进群交流

![](https://proxy-prod.omnivore-image-cache.app/200x0,sZCzQPkLfMm-oRK8AAaK3FoHzluoCP5xkt1z_1QGsm_0/https://bzfree.com/images/common/qrcode-1.png)

**如果有任何疑问，欢迎进群交流讨论，备注：斜杠君。**

---

### 1\. 什么是扣子 [​](#%5F1-什么是扣子)

扣子是新一代 AI 应用开发平台。无论你是否有编程基础，都可以在扣子上快速搭建基于大模型的各类 Bot，并将 Bot 发布到各个社交平台、通讯软件或部署到网站等其他渠道。

### 2\. 扣子的功能与优势 [​](#%5F2-扣子的功能与优势)

**用户友好的界面**：Coze的操作界面设计合理，逻辑清晰，易于上手，符合用户的使用习惯。

**功能丰富**：平台提供了包括插件系统、记忆库、工作流等在内的多种功能，用户可以根据自己的需求灵活选择和配置这些功能。

**支持知识库和自定义插件**：用户不仅可以导入数据到知识库，还可以自定义插件来扩展机器人的能力，提高了系统的可定制性。

**多平台部署**：构建的机器人可以部署到微信、飞书等社交媒体平台以及企业内部应用程序，增加了系统的灵活性和适用性。

**无需编程基础**：Coze平台几乎不需要编程基础，模型、插件、知识库等核心技术都进行了封装，使得用户可以快速搭建Bot。

**免费使用**：至少在现阶段，Coze平台是完全免费的，为用户提供了易于使用的AI Bot开发环境。

**集成插件工具集**：Coze平台集成了超过种多样化的插件工具，覆盖了新闻阅读、旅行规划等多个领域，支持用户快速为机器人添加功能。

**增强聊天机器人能力**：Coze平台还提供了工作流、知识库等功能，以及长期记忆和定时任务等，增强了聊天机器人的能力和交互性。

**国际版与国内版**：Coze有国内版和国际版，国际版提供了更完善的GPT-4模型功能，而国内版可能存在一些限制。

### 3\. 注册和基本界面介绍 [​](#%5F3-注册和基本界面介绍)

注册登录Coze平台的步骤比较简单，你可以直接访问Coze官网进行注册，使用邮箱或手机号完成账户信息的填写和验证。

登录成功后，你会看到Coze的基本界面。在界面的左上角，你可以点击"创建 Bot"按钮来创建一个新的Bot。 ![](https://proxy-prod.omnivore-image-cache.app/0x0,s8QvUX8Y7a5ZUfGXvPhLmT1w5yWvvfjzvd_icqEJvwAI/https://bzfree.com/images/coze/login.png)

创建机器人时，你需要输入Bot的基本信息，如名称、头像等。这些信息可以随意填写，主要用于标识你自己使用的机器人。

![](https://proxy-prod.omnivore-image-cache.app/0x0,situndLRj6uRBfRDWQuT5OoKCUG6H7KP2Ys0aiAcjhhc/https://bzfree.com/images/coze/coze2.png)

在机器人配置页面，界面主要分为三栏：

* 最左边是Bot提示词编写页面，可以在这里设定机器人的角色、技能和限制。

![](https://proxy-prod.omnivore-image-cache.app/0x0,ss9_TgG7XVUZ1i31soLvCYekkQhaq14j1v0WVUBFbk4c/https://bzfree.com/images/coze/coze3.png)

* 中间一栏是功能最丰富的地方，可以配置官方提供的插件、自定义工作流、引入知识库内容或创建数据库。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sFFfUh8qkqUFt13kYQw07q9ii-795WxQemKpJ5qGBqxc/https://bzfree.com/images/coze/coze4.png)

* Coze平台提供了Bots、插件、工作流和知识库四个主要功能，这些功能都会在创建机器人的过程中用到。
* 在创建机器人的过程中，你还可以利用Coze提供的数据库功能，创建数据集合，定义字段，类似于传统数据库的表结构设计。
* 最右边是调试页面，在调试页面可以直接和机器人进行对话，查看返回结果是否符合预期。

![](https://proxy-prod.omnivore-image-cache.app/0x0,s2l9WeFNriq-GAkq7SlIlR0lWUuLidVlb84Yi-qTa0wU/https://bzfree.com/images/coze/coze5.png)

* 当你完成所有相关设置后，可以点击右上角的发布按钮，将机器人发布到Coze的应用商店。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sb-MhAS5zEwYx38ii4v5LItD6mcOFUopJSatNovio0Kg/https://bzfree.com/images/coze/coze6.png)

---

关注公众号

![斜杠君微信公众号二维码](https://proxy-prod.omnivore-image-cache.app/200x0,sgxWx5jk1OoMMAF_C-F3JqDf-vOSTTocma_fO1iQNQss/https://bzfree.com/images/common/qrcode.jpg)

进群交流

![](https://proxy-prod.omnivore-image-cache.app/200x0,sZCzQPkLfMm-oRK8AAaK3FoHzluoCP5xkt1z_1QGsm_0/https://bzfree.com/images/common/qrcode-1.png)

**如果有任何疑问，欢迎进群交流讨论，备注：斜杠君。**

---

## 第二章：快速开始 [​](#第二章-快速开始)

🔊 课前提示

本章节带大家快速上手使用扣子，通过本章学习，大家可以掌握扣子(Coze)的使用方法。

### 1\. 创建和编排Bot [​](#%5F1-创建和编排bot)

在界面的左上角，你可以点击"创建 Bot"按钮来创建一个新的Bot。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sejFCBB05cHU7QxqAXNm2HeKHdzOYPguQ1Y2udBfom9Y/https://bzfree.com/images/coze/coze7.png)

### 2\. 设定基本信息和功能 [​](#%5F2-设定基本信息和功能)

例如，这里我要创建一个帮我写爆款小红书文案的Bot。那么我为这个Bot起名为：小红书爆款写作

![](https://proxy-prod.omnivore-image-cache.app/0x0,sqD3vNOIFNTTtNBmIZEsbdB6W2q4dKQCPLkCsHlJoHaM/https://bzfree.com/images/coze/coze8.png)

### 3\. 设定大语言模型 [​](#%5F3-设定大语言模型)

这里选择"moonshot(128k)"模型。moonshot是月之暗面的模型，也就是当前很火热的Kimi使用的模型。

![](https://proxy-prod.omnivore-image-cache.app/0x0,s0SCK1qBJDdOfCp-GOd5Zm3In3kjTCMXAumum_pODRoU/https://bzfree.com/images/coze/coze9.png)

### 4\. 设定人设与回复逻辑 [​](#%5F4-设定人设与回复逻辑)

在这里要对Bot的人物进行设定，以及让Bot如何回复用户的问题。这里涉及到提示词如何撰写的知识，我会在后面的章节为大家讲解，如何写出高质量的关键词。

![](https://proxy-prod.omnivore-image-cache.app/0x0,smqafE8cOqKysTEsZ0AND-sMWFJshQipfECaBMcSMSVc/https://bzfree.com/images/coze/coze10.png)

### 5\. 预览与调试 [​](#%5F5-预览与调试)

在快速开始这个章节，我们先不使用插件，工作流等，目的是为了让大家快速上手。这些功能点我们会在后面的章节逐一讲解，要照顾一下从零起步的同学哦 😊 在这里我提出了一个主题：写一篇华为手机的文案。可以看到Bot快速的帮我生成了文案，质量是相当的高！😍

![](https://proxy-prod.omnivore-image-cache.app/0x0,so3CudeXvj3at7F2fxbDvHjh-MyY9jBrb4Kd0NXD3488/https://bzfree.com/images/coze/coze11.png)

### 6\. 发布Bot [​](#%5F6-发布bot)

Bot创建好以后，我们就可以发布到应用商店供朋友，同事或网友们进行使用了。 点击右上角的 **发布** 按钮。

![](https://proxy-prod.omnivore-image-cache.app/0x0,se8FaxrQnk-j1OmjidtCY6xjd0cWE4MUu26PEu4izR7w/https://bzfree.com/images/coze/coze12.png)

发布之前你可以设置Bot的 **开场白** 和 **预置问题**。

![](https://proxy-prod.omnivore-image-cache.app/0x0,s-NlD3y4q1hmr0R0TnBOXUO9NvnDmihgSAF-6bV1Ov1g/https://bzfree.com/images/coze/coze13.png)

点击展开，可以对开场白进行预览。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sxBQgD6iXu8oKdG7mHhpAR5EBZHsnmNGUoJ3gAvK1LeI/https://bzfree.com/images/coze/coze14.png)

点击 **确认** 按钮进行发布。

![](https://proxy-prod.omnivore-image-cache.app/0x0,s1yi0pRoZWkZ0q22ORiwdKUdraoW3BuYGdthWmpYC_-E/https://bzfree.com/images/coze/coze15.png)

可以看到，Bot可以被发布到多个平台上进行使用。在这里我们只发布到Bot商店，其他的平台我们在之后的章节里讲解。 点击 **发布** 按钮进行发布。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sowfYcjcCuTapxxcpAWRZlDCAvmwdq8ejHzh9EKxCdJI/https://bzfree.com/images/coze/coze16.png)

发布成功！ 🎉🎉🎉

![](https://proxy-prod.omnivore-image-cache.app/0x0,slgmwlBebG9OTPsyGSBG4giorGp9PUGuxMJ7GK6YKUgU/https://bzfree.com/images/coze/coze17.png)

点击 **立即对话**，就可以使用了噢！😊

![](https://proxy-prod.omnivore-image-cache.app/0x0,spnB9lArvnqHN1r_a-BjgzwqZSe3bFOBi0D3I94ZnGT8/https://bzfree.com/images/coze/coze18.png)

💡 小结

这一章我们通过对扣子基本功能的使用，相信大家都可以上手使用扣子了。接下来的章节，我为会大家进一步讲解扣子的更多功能，那么就让我们开始吧！

---

关注公众号

![斜杠君微信公众号二维码](https://proxy-prod.omnivore-image-cache.app/200x0,sgxWx5jk1OoMMAF_C-F3JqDf-vOSTTocma_fO1iQNQss/https://bzfree.com/images/common/qrcode.jpg)

进群交流

![](https://proxy-prod.omnivore-image-cache.app/200x0,sZCzQPkLfMm-oRK8AAaK3FoHzluoCP5xkt1z_1QGsm_0/https://bzfree.com/images/common/qrcode-1.png)

**如果有任何疑问，欢迎进群交流讨论，备注：斜杠君。**

---

## 第三章：插件开发及使用 [​](#第三章-插件开发及使用)

🔊 课前提示

这一章，我们来深入讲解插件的开发及使用。

### 1\. 插件是什么 [​](#%5F1-插件是什么)

简单来说，插件是用来增强Bot的能力的，相当于你在玩游戏时，给你的人物加了一个技能。例如你创建了一个Bot，但这个Bot本身是没有上网查找资料的功能的，这个时候你就可以为你的Bot增加一个带有网页搜索功能的插件，那么当你向Bot提问时，Bot就可以先到网上查找资料，再回答你的回答，让回答更实时可靠。

当然，如果你觉得扣子集成的插件不满足您的使用需求，您还可以创建自定义插件来集成需要使用的 API。

### 2\. 使用插件 [​](#%5F2-使用插件)

让我们先从使用一款插件开始，通过使用一款插件，可以让我们了解插件的基本功能和原理。我们继续第一章的示例，为小红书爆款写作助手增加一个上网搜索的超能力。🏄

#### 2.1 添加插件 [​](#%5F2-1-添加插件)

下图所示部分就是Bot的插件。点击 **+** 按钮，我们可以为插件增加一个工具。

![](https://proxy-prod.omnivore-image-cache.app/0x0,suew-SdVqyCOrUfG-P1NgI-v2isu4sN-ZazDvJeCA520/https://bzfree.com/images/coze/coze19.png)

在这里点击 **添加** 按钮，为插件增加一个 **必应搜索** 工具。

![](https://proxy-prod.omnivore-image-cache.app/0x0,siJ8Z8chMLRkhCMcr7u73IvmIirXkcmho7qoiYPoBPuY/https://bzfree.com/images/coze/coze20.png)

#### 2.2 编写提示词 [​](#%5F2-2-编写提示词)

增加插件后，我们需要在提示词里告诉Bot，在回答之前，先使用插件上网进行搜索内容。如下图所示：

![](https://proxy-prod.omnivore-image-cache.app/0x0,suWDhohnth0UWfHUhLrLbOnNJFkL0jsHR7U4vdXXXFZo/https://bzfree.com/images/coze/coze21.png)

#### 2.3 测试插件 [​](#%5F2-3-测试插件)

接下来测试一下，插件是否被执行了。 如下图所示，必应搜索 插件已经被执行了。👍👍👍

![](https://proxy-prod.omnivore-image-cache.app/0x0,syS8HIyI6xL7UxlIpAIUSo5re5TvErC1CqmAo7nEOudg/https://bzfree.com/images/coze/coze22.png)

可以发现，从网上搜索的内容已经被应用到文章中了。

![](https://proxy-prod.omnivore-image-cache.app/0x0,ssn5j1YwGT4k4dQSVl-6ZChWHcMtj-qbMxY3edUKb01Y/https://bzfree.com/images/coze/coze23.png)

🔊 敲黑板

**使用扣子的重点和难点是，通过提示词让大模型去准确的调用相应的插件。相信通过动手练习，你会很快掌握技能的。**

### 3\. 创建插件 [​](#%5F3-创建插件)

💡 有些情况下，扣子集成的插件并不能满足我们的需求，那么我们就可以通过创建自定义插件来的方式，集成自己的API到插件中来使用。

#### 3.1 初始化插件 [​](#%5F3-1-初始化插件)

点击左侧的 **个人空间**，然后在上面选择 **插件** 标签，点击 **创建插件** 开始创建。

![](https://proxy-prod.omnivore-image-cache.app/0x0,se3L1tv3TslDMERQgvhcx-Lo1wGSyDJFMtXtxtWH4kwE/https://bzfree.com/images/coze/coze24.png)

在弹出的页面中，我们为插件填写基本信息。

![](https://proxy-prod.omnivore-image-cache.app/0x0,shQfmlllDKLQvLXVug5MqEEOFBri84dCw1V7mbYWR8S8/https://bzfree.com/images/coze/coze25.png)

插件工具创建方式这里，我们先选择基于已有服务创建，在CozeIDE中创建的方式我们之后再讲解。

插件URL 这里重点注意一下，这里需要填写接口的根域名。

![](https://proxy-prod.omnivore-image-cache.app/0x0,s6zFpVnIijlbzlmyINkKUycfMcP7NXNcSRAU1H4E3-oY/https://bzfree.com/images/coze/coze26.png)

接下来解释一下授权方式这个选项。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sSxQVBXHuZUmuvUVCo6zWkTN2sNkGDrxt8FQbrulFbyA/https://bzfree.com/images/coze/39eca87c-336e-4bc8-a225-00aecfb06be6.png)

授权方式有三种：不需要授权、Service 和 Oauth。

不需要授权：就是无认何认证环节，请求接口，接口返回值。

Service：服务认证，该认证方式是指 API 通过密钥或令牌校验合法性。就是你要向接口传递令牌信息，后端验证成功才能给你返回值。

OAuth: OAuth 是一种常用于用户代理身份验证的标准，它允许第三方应用程序在不共享用户密码的情况下访问用户下的特定资源。

这里我们使用 不需要授权 做演示。

填写好信息以后，点 确定 按钮，就完成了插件的设置。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sZrSX00eKbvIzJ-mEvbhD-l1YWeIxFo7TOw-MnAYRi9Y/https://bzfree.com/images/coze/coze27.png)

接下要开始在插件中加入工具了。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sTqBtWheOg-6wcUdXsYBA7HBk0JvnCXvpNAMGzvHAECk/https://bzfree.com/images/coze/coze28.png)

#### 3.2 填写基本信息 [​](#%5F3-2-填写基本信息)

![](https://proxy-prod.omnivore-image-cache.app/0x0,snO7tM54UixC2N6tjOdc9OMjThy2iTKINVH1qV0PuhI8/https://bzfree.com/images/coze/coze29.png)

#### 3.3 配置输入参数 [​](#%5F3-3-配置输入参数)

点击 新增参数 按钮为接口增加一个参数。 因为我们使用的接口地址是：

所以参数名称那里我们填写的是id。

![](https://proxy-prod.omnivore-image-cache.app/0x0,syJ_nugZgQFuiv1j_kWyGUWVdKrxew3-iMZzaoitxeSk/https://bzfree.com/images/coze/coze30.png)

传入方法这里说一下，一共有四种：

Body：就是参数放在请求体中的请求。

Path：就是参数作为URL中的一部分。例如下面这个URL，todos参数就是path中的一部分。 <https://jsonplaceholder.typicode.com/posts/2>

Query：参数作为URL中的参数，例如下面这个URL。 <https://jsonplaceholder.typicode.com/posts?id=2>

Header：就是在请求头中传递。

点击 **保存并继续** 按钮，进入下一步。

![](https://proxy-prod.omnivore-image-cache.app/0x0,szYy9sQhqovrng3SGwbrP9pg_48CgvoSMo5ilZG6rOj4/https://bzfree.com/images/coze/coze31.png)

#### 3.4 配置输出参数 [​](#%5F3-4-配置输出参数)

点击 **自动解析** 按钮

![](https://proxy-prod.omnivore-image-cache.app/0x0,sGorqvI2E40EYVc7nSIDnfRToN6PhnJgpKarHDBdbDVw/https://bzfree.com/images/coze/coze32.png)

我们访问这个接口，可以看到，会返回以下参数。

JS

```json
[
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  }
]
```

那么这里我们把id的值设置为2，点击 自动解析 按钮。看自动解析的结果和上面的结构是否一样。

![](https://proxy-prod.omnivore-image-cache.app/0x0,su66cPvnZzV99Op0QZJfxkdg5HMtxKGM_wBf7rA1wKZM/https://bzfree.com/images/coze/coze33.png)

可以看到解析出来的字段和上面代码块中的字段完全一致，说明解析没问题。

![](https://proxy-prod.omnivore-image-cache.app/0x0,s_iwtVJ_qKr9DU5gAYmxR__-xRwSprMmMx0io-o8RWIM/https://bzfree.com/images/coze/coze34.png)

继续下一步，点击 **保存并继续** 按钮。

#### 3.5 调试与校验 [​](#%5F3-5-调试与校验)

把id值设置为2，点击 **运行** 按钮，查看 **Response** 结果。

![](https://proxy-prod.omnivore-image-cache.app/0x0,snUb_7JC6MzGpXQzjyIKdqSpI32FMVhKOSBqD866WyDo/https://bzfree.com/images/coze/coze35.png)

可以看到和上面代码块中的值一致，说明返回结果没问题。

点击 **完成** 按钮，此时插件就创建完成了。

![](https://proxy-prod.omnivore-image-cache.app/0x0,stnmxSrpxA-vR189Z3OvW2FvJBvCvVnIk16K9zrnqkKQ/https://bzfree.com/images/coze/coze36.png)

从上图可以看到，服务状态是 **线下**，这时插件虽然已经创建好了，但还是不能被Bot调用的。

我们需要对插件进行发布以后才能被Bot使用。

### 4\. 发布插件 [​](#%5F4-发布插件)

发布插件很简单，点击 **发布** 按钮即可。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sbncR5F1FWwdNoCailXxuKF-KkO42kdOKlj_MzkaTVtE/https://bzfree.com/images/coze/coze37.png)

发布完成前，需要确认你发布的插件是否会收集、传输用户的个人信息，请如实填写。因为这里是案例教程，我们就直接发布了。

![](https://proxy-prod.omnivore-image-cache.app/0x0,smfNd33K2uYsFaiWQTl3Ur0WmK_KwCRgUGlMYudr6eZw/https://bzfree.com/images/coze/coze38.png)

此时可以看到，插件已经是 **已发布** 状态了。

![](https://proxy-prod.omnivore-image-cache.app/0x0,s-xpZSs_8aEzhXOp7Tn4bSE8RLa411y5NZ2ahdVfAH-E/https://bzfree.com/images/coze/coze39.png)

接下来在Bot中添加插件的时候，在左侧选择 **我的工具**，就可以看到我们刚才创建的插件了。

接来了就可以按照 **插件使用** 教程的方法来使用插件了。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sQHFGXtit0ydX7tdRIOyNSgO1tbszl6F66fbd804Sb0w/https://bzfree.com/images/coze/coze40.png)

### 5\. 导入插件 [​](#%5F5-导入插件)

有的同学可能会问，每次创建插件都需要按照 **创建插件** 的流程写一遍吗？

如果想把已经创建好的插件导入到另一个帐号使用，或者想在已经创建好的插件的基础上稍做改动就可以变成一个新的插件，有没有更简单的方式？

答案是有的。我们可以使用 **导入插件** 的功能。

例如，我们要基于刚才创建好的插件，把工具的名称修改一下，变成一个新的插件，我们可以按以下方式去做。

#### 5.1 复制代码 [​](#%5F5-1-复制代码)

进入我们刚才创建好的插件

![](https://proxy-prod.omnivore-image-cache.app/0x0,sbYj34zCYEfPdyDlcTwELJbD4FKtrVllMgCjfPVxrUVI/https://bzfree.com/images/coze/coze41.png)

点击 **使用代码** 按钮

![](https://proxy-prod.omnivore-image-cache.app/0x0,se4Vvpw0MPdMCsbmFCpdAsMd2r3CQOqPitus-w5mfIKw/https://bzfree.com/images/coze/coze42.png)

可以看到弹出的这个代码界面，我们全选复制右侧这个Yaml格式的代码，把它先放到一个临时的文本文档中进行修改。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sN5fUCPa8h6jqxWaqY3L93nS5zPx00228QHYwoqgTn3c/https://bzfree.com/images/coze/coze43.png)

#### 5.2 修改文件 [​](#%5F5-2-修改文件)

在文档中修改一下插件名称和工具名称。注意插件名称仅支持输入中文、字母、数字、下划线或空格，不能有特殊符号

![](https://proxy-prod.omnivore-image-cache.app/0x0,s9RwH8n9jcLbsMqHkqRUkR2hZLgkG5Lht9bUQNKyzQqs/https://bzfree.com/images/coze/coze44.png)

#### 5.3 保存YAML [​](#%5F5-3-保存yaml)

把文件进行保存，起一个文件名，例如new\_plugin.yaml，这个名称随意写，注意一下扩展名是yaml。

💡 名词解释

简单来说yaml是一种文件格式，使用空白符号缩进等格式，使文档格式有层级递进关系，使文档更易读易写。我们当前复制出来的这段代码就是yaml格式的，所以扩展名也要用yaml。

#### 5.4 导入文件 [​](#%5F5-4-导入文件)

点击 **导入** 按钮

![](https://proxy-prod.omnivore-image-cache.app/0x0,s-M-4VVw-hpHOFXxljno2rn_Q8I_K6aVvDhKwjDbjJhM/https://bzfree.com/images/coze/coze45.png)

选择我们刚才创建的 new\_plugin.yaml 文件进行导入，然后点击 **下一步** 按钮。

![](https://proxy-prod.omnivore-image-cache.app/0x0,syY2P0qT8ElCspcr64uaBUGi_zfqxFx5xE4Zzj5HvdjY/https://bzfree.com/images/coze/coze46.png)

可以看到插件名称和我们修改的一致，说明导入没问题。点击 **确认** 按钮继续。

![](https://proxy-prod.omnivore-image-cache.app/0x0,srXRtuJ9QXYrxze6e6kec3zmA4zsUR0iGBAxvAocgJJw/https://bzfree.com/images/coze/coze47.png)

#### 5.5 调式与效验 [​](#%5F5-5-调式与效验)

确认之后，我们发现调试状态是失败的，如下图所示。

![](https://proxy-prod.omnivore-image-cache.app/0x0,stP76B95bZpJDFZtWKPSooIbUFFRygGZ1ptOIBkqR9qw/https://bzfree.com/images/coze/coze48.png)

这个时候我们需要启用，然后重新调试一下就好了。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sQ6_iDiJkG_n4VkHgfhwQ-TBPfzYDgJUsg4a9l4bgpb4/https://bzfree.com/images/coze/coze49.png)

按之前 **调试教程** 的方式调试后，点击 **完成** 按钮。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sRi-qKrUo97-UEJYtvHSubQbNqSHjFGs6xTdL2qduSIs/https://bzfree.com/images/coze/coze50.png)

可以看插件已成功导入了。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sZYkhGZ9Yrn19WvwckohSa-uwXAv72X0fx-mznuPxILo/https://bzfree.com/images/coze/coze51.png)

💡 小结

这一章我们通过扣子插件的创建、使用、发布和导入等内容进行了讲解，相信大家都可以熟练的使用扣子的插件功能了。接下来的章节，我为会大家进一步讲解扣子的更多功能！

---

关注公众号

![斜杠君微信公众号二维码](https://proxy-prod.omnivore-image-cache.app/200x0,sgxWx5jk1OoMMAF_C-F3JqDf-vOSTTocma_fO1iQNQss/https://bzfree.com/images/common/qrcode.jpg)

进群交流

![](https://proxy-prod.omnivore-image-cache.app/200x0,sZCzQPkLfMm-oRK8AAaK3FoHzluoCP5xkt1z_1QGsm_0/https://bzfree.com/images/common/qrcode-1.png)

**如果有任何疑问，欢迎进群交流讨论，备注：斜杠君。**

---

## 第四章：知识库创建及使用 [​](#第四章-知识库创建及使用)

### ==1. 什么是知识库== ==[​](#%5F1-什么是知识库)==

==大语言模型的训练数据一般基于公开的数据，这意味着模型的知识==**==一般不会包含私有领域的知识==**==，同时在公开知识领域==**==存在一定的滞后性==**==。为了解决这一问题，目前通用的方案是采用 **RAG（检索增强生成）**技术，==**==使用用户问题来匹配最相关的外部数据==**==，将检索到的相关内容召回后作为模型提示词的上下文来重新组织回复。==

扣子提供了一套简单易用的用户界面来方便应用构建者管理个人或者团队的知识库，并能够快速集成至 AI 应用中。你只需准备文本内容，例如：TXT、DOC、DOCX、Excel、PDF 文件，甚至在线网页、飞书文档、Notion页面是也可以的。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sJ7ucRB8svzaczHvAGlQPF1A2fO7FxpBv60SNEZp0gbQ/https://bzfree.com/images/coze/d9AkEAtO2yn5XiOoqUizmbDtm12fBRmXidZs8eqiWv4.png)

### 2\. 创建知识库 [​](#%5F2-创建知识库)

**下面我们写一个示例，例如FuturaTech是一家企业，那我们来为这个企业做一个FAQ。**

点击 **创建知识库** 按钮，开始创建。

如下图所示位置：

![](https://proxy-prod.omnivore-image-cache.app/0x0,sThCm0nPtvvqGm-7zCwaHyW1FVwj5yDwgvQqMSUJqDmY/https://bzfree.com/images/coze/yyH_UJNQlGGj0_KnEVWzcQl2KrfP4kF49EMopoSp7c8.png)

这个知识库我们使用文本格式来创建。例如FuturaTech是一家企业，那我们为这个企业做一个FAQ Bot。

![](https://proxy-prod.omnivore-image-cache.app/0x0,s0niRMp8albC_H6IX1sIjwG3Ss96F7w8vWQ67A7Wu7_c/https://bzfree.com/images/coze/FkZjjPun4ekcUcImeELI5MxQ8SDdfsutl-ZrlowB9jg.png)

**准备文档**

首先，我们准备一个FAQ的文本文档，用TXT格式就可以，例如文件名叫：FAQ.txt。

文本内容如下：

Plain

```groovy
FuturaTech 常见问题解答
Q: FuturaTech是做什么的？ A: FuturaTech是一家领先的技术创新公司，专注于开发和提供先进的人工智能解决方案，旨在帮助企业提高效率和竞争力。
Q: 我可以在哪里找到FuturaTech的产品？ A: 我们的产品可以在FuturaTech的官方网站上找到，也可以通过我们的授权分销商和合作伙伴获取。
Q: FuturaTech提供哪些类型的服务？ A: 我们提供定制化的AI解决方案、数据分析服务、软件开发、技术咨询以及持续的客户支持。
Q: 如何成为FuturaTech的客户？ A: 您可以通过访问我们的网站并填写联系表单来开始合作流程，或者直接致电我们的销售团队。
Q: FuturaTech是否提供试用版本？ A: 是的，我们为许多产品提供有限时间的免费试用版本，以便客户在购买前能够体验产品。
Q: FuturaTech的技术支持团队如何联系？ A: 您可以通过我们的在线帮助中心提交支持请求，或者在工作时间内致电我们的技术支持热线。
Q: FuturaTech是否提供培训服务？ A: 我们提供全面的培训服务，包括在线教程、研讨会和现场培训，以帮助客户最大化地利用我们的产品和服务。
Q: FuturaTech如何保证客户数据的安全？ A: 我们采用行业领先的安全措施和数据加密技术，确保客户数据的安全和隐私。
Q: FuturaTech是否提供定制化解决方案？ A: 是的，我们的专家团队可以根据客户的具体需求，设计和开发定制化的解决方案。
Q: 我如何了解FuturaTech的最新动态和产品更新？ A: 您可以通过订阅我们的新闻通讯、关注我们的社交媒体账号或定期访问我们的网站来获取最新信息。
```

**上传文档**

在这里，把文件进行上传，然后点击 **下一步** 按钮：

![](https://proxy-prod.omnivore-image-cache.app/0x0,s733EoHSXWJPwfta5-mSPRK2LtYNtpjyqy-GjV7PVMRY/https://bzfree.com/images/coze/-tquJMNXd3d6XeEy2gZiXxCaeYNt3YSACSkGQRAA-QU.png)

**分段与清洗**

这里注意一下，内容分段可以更有效地召回与用户查询最相关的内容，从而提升回复的准确性。合理的内容分段对回复的效果有着直接影响。一般没有特殊要求的情况下，我们这里选择 **自动分段与清洗** 即可。

点击 **下一步** 按钮：

![](https://proxy-prod.omnivore-image-cache.app/0x0,sry0EHBpWJ8m7LGXSDwpqW1M-lx1DnGLw0FwmM3F_vIA/https://bzfree.com/images/coze/wK6BCMWKUv1GfU2t4_kCUL67KCe1GFU5kIWKzOdM6lA.png)

这里服务器开始处理，点击 **确认** 不影响数据处理，处理完毕后可进行引用。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sJVPKTZwadsdsdkgnfzG9anSTvjotId3pf8zTOw-BhFQ/https://bzfree.com/images/coze/pMuBU9dHxq-j6pVHzwQkYrvLWNszt4gYRWmi1zr0yKw.png)

处理完成后，可以看到分段后的内容：

![](https://proxy-prod.omnivore-image-cache.app/0x0,sFGFU2x3uP0U_SkJVcJvc6tJnJjFSnosUUsHZ7zEFBqc/https://bzfree.com/images/coze/LB4Pq_dY3q_TB3shCemiE234sV9JmNg3M5TVLNYbVho.png)

到此我们的知识库就创建完毕了。

### 3\. 使用知识库 [​](#%5F3-使用知识库)

  
#### 3.1 创建Bot [​](#%5F3-1-创建bot)

我们通过创建一个Bot来引入知识库。

![](https://proxy-prod.omnivore-image-cache.app/0x0,szUcy3Cd0Y_-74v5Bs5GV253MwqHWD824rPqf5CxK2uw/https://bzfree.com/images/coze/17Fx4b435pZqik7Z3AF3cz6vFJkLnPNgmRj27hjov1g.png)

#### 3.2 **添加知识库** [​](#%5F3-2-添加知识库)

点击 **+** 添加之前建好的知识库

![](https://proxy-prod.omnivore-image-cache.app/0x0,sr0I84NcspX_9YIQS3DZD6dqEH2j5v6BLNov4dnjBmA4/https://bzfree.com/images/coze/JUxpIzHvOANal1VPAG2qjDxJBmJqOQl4doqKC6pjbcQ.png)

**选择知识库**

在知识库列表中搜索FuturaTech关键字，点击 **添加** 按钮

![](https://proxy-prod.omnivore-image-cache.app/0x0,sPWJSP1vL2qfQv1gw7EGSPBqnBk9N_msfHFXiXGjBjJ8/https://bzfree.com/images/coze/xr-hwuLRFHqpxZ8AM0JwP9XzMkuU9puK1rZXjDMzCr8.png)

#### 3.3 **设置知识库** [​](#%5F3-3-设置知识库)

加好知识库后，要对知识库进行一下设置。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sm4XvJPPHlY6JitkSsJ3Hh_nNY1-6ho_4aWDhIMK4FN0/https://bzfree.com/images/coze/VQhyTNAfV9ytGOaUvSNNN1Y2EWv194W_T3DOiPW-cf0.png)

1. **调用方式**

分别解释一下，调用方式这里 **自动调用** 和 **按需调用** 是什么意思。

\*\*自动调用：\*\*是指每一轮对话都会调用知识库，使用召回的内容辅助生成回复。

**按需调用**：是指根据实际需要来调用知识库，使用召回内容辅助生成回复。此时，需要在左侧的人设与回复逻辑区域明确写清楚在什么情况下调用哪个知识库进行回复。

1. **搜索策略**

搜索策略是用来选择如何从知识库中搜索内容片段，不同的检索策略适应于不同的场景。检索到的内容片段的相关性越高，大模型根据召回内容生成的回复的准确性和可用性也越高。

\*\*混合：\*\*结合全文检索和语义检索的优势，并对结果进行综合排序召回相关的内容片段。

\*\*语义：\*\*像人类一样去理解词与词，句与句之间的关系。推荐在需要理解语义关联度和跨语言查询的场景使用。例如下面两组句子，第一组的语义关系就更强。

Plain

```1c
"狼追小羊"和"豺狼追山羊" 
"狼追小羊"和"我爱吃炸猪排"
```

\*\*全文：\*\*基于关键词进行全文检索。推荐当查询内容包含以下场景时使用

* 特定名称或专有名词，术语等，例如比尔盖茨、 特斯拉 Model Y
* 缩写词，例如 SFT
* ID，例如，12s1w1s2系列

基于以上的理解，这里我们设置如下图所示：

![](https://proxy-prod.omnivore-image-cache.app/0x0,sTEbxxXME9ShNPTk9VACMZeAZQhe8jvITOM9iPmsQ2A0/https://bzfree.com/images/coze/topUgCqujkPc0YTzVIk8rc2nK2vyW2IqzVdpd_9qyg8.png)

#### 3.4 编排提示词 [​](#%5F3-4-编排提示词)

接下来设置Bot的 **人设与回复逻辑** 部分\*\*，告诉Bot当客户出问题的时候先到知识库中查找答案。\*\*

![](https://proxy-prod.omnivore-image-cache.app/0x0,swcu5q83E7h33flNSyEwQvS9GiLI9bTZxmFEN1gSlYOE/https://bzfree.com/images/coze/LPRL_doVsNAF0UgkJNq4MpKhMTRA8jyremvbAoKfAgI.png)

提示词：

Plain

```clean
# 角色
你是一个专业且耐心的客服人员，需要通过调用 recallKnowledge 方法从'FuturaTech 常见问题解答'来为用户提供准确全面的服务。

## 技能
### 技能 1: 解答常见问题
1. 当用户提出问题时，优先从'FuturaTech 常见问题解答'中查找答案。
2. 如果在知识库中找到相关问题及答案，准确清晰地回复给用户。
3. 如果知识库中没有相关内容，及时告知用户，并表示会进一步核实。

## 限制:
- 只处理与'FuturaTech 常见问题解答'相关的内容，拒绝回答无关问题。
- 所输出的内容必须按照给定的格式进行组织，不能偏离框架要求。
```

#### 3.5 **预览与调试** [​](#%5F3-5-预览与调试)

接下来我们来测试一下，当我们问Bot问题，Bot是否调用了知识库。

我找到了一条 FAQ.txt 中的问题。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sLKzx--MIQTDVkhG61OPyYqySVG3kw6qJU6HvCb99kck/https://bzfree.com/images/coze/BnLszlUk22zOUIbRKK2NfrPS9_f0ZJjupEa6iCEUNSs.png)

如下图所示，可以看到，Bot调用了知识库并正确的回答了问题。

![](https://proxy-prod.omnivore-image-cache.app/0x0,sgjRw4b1Qc8khOFfjlaDDHkJTHzABfrScjRfr_MWsxMo/https://bzfree.com/images/coze/eahlyx1UwHmYQzqg3YBEPsVLA6-ql8kve9r0RAoADcY.png)

---

关注公众号

![斜杠君微信公众号二维码](https://proxy-prod.omnivore-image-cache.app/200x0,sgxWx5jk1OoMMAF_C-F3JqDf-vOSTTocma_fO1iQNQss/https://bzfree.com/images/common/qrcode.jpg)

进群交流

![](https://proxy-prod.omnivore-image-cache.app/200x0,sZCzQPkLfMm-oRK8AAaK3FoHzluoCP5xkt1z_1QGsm_0/https://bzfree.com/images/common/qrcode-1.png)

**如果有任何疑问，欢迎进群交流讨论，备注：斜杠君。**

---

## 第五章：工作流创建及使用 [​](#第五章-工作流创建及使用)

### ==1. 什么是工作流== ==[​](#%5F1-什么是工作流)==

==工作流是可以让用户能够通过==**==直观的方式==**==，==**==灵活地组合插件==**==、==**==大型语言模型和代码模块等元素，构建出既复杂又稳固的业务的流程。==** ==这在执行如旅行规划、报告分析等任务时尤为有效。当面临包含多个步骤的任务场景，并且对输出结果的精确度和格式有着严格标准时，采用工作流配置将是一个理想的选择。==

### 2\. 工作流的组成 [​](#%5F2-工作流的组成)

如图中所示，工作流是由多个节点组合而成的一整套流程。\*\*节点是组成工作流的基本单元。\*\*例如，插件节点、大语言模型 LLM、自定义代码、判断逻辑等节点。

工作流默认包含了**开始节点**和**结束节点**。

开始节点是工作流的起始节点，可以包含用户输入信息。

结束节点是工作流的末尾节点，用于返回工作流的运行结果。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sM-Bne97LJJ6-HtgUPWQSnmxWvmb7oeCEcb1EqmHt32Q/https://bzfree.com/images/coze/coze52.png)

### 3\. 节点示例详解 [​](#%5F3-节点示例详解)

  
#### 3.1 插件节点 [​](#%5F3-1-插件节点)

与第三章所讲类似，之前讲的是插件直接放到Bot中，通过Bot直接进行调用。而在这里是作为工作流的一个节点，但他们的功能都是一样的，可以访问实时数据和执行外部操作，例如通过搜索引擎搜索信息、图片、时实翻译等。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,so0erjZ5twmEULsy3SIA-eXpweOmAX68zqdLQVO7wP-Y/https://bzfree.com/images/coze/cvViSx8ED90vSOHWdn.png)

**下面我们写一个示例，来获取知乎列表的热榜。**

因为知乎热榜只有一个limit参数，用来获取条数的。这个数量我们让用户来设置。

点击 **试运行** 测试：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sd01bKgrBZ-RyqPDNcjbDdAzmlAkOwCi5PQm2fo5tQic/https://bzfree.com/images/coze/coze54.png)

输入数量

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s23fkDO2-hUFBWicXemBpxOwDM0T3VKxV3rco2DNaom0/https://bzfree.com/images/coze/coze55.png)

查看运行结果，知乎热榜数据已经调用成功了：）

![image](https://proxy-prod.omnivore-image-cache.app/0x0,syz5DgL5-BKQC4p7H2P-EHsXvFfTm9w3fFHmClRvndHM/https://bzfree.com/images/coze/coze56.png)

#### 3.2 大模型节点 [​](#%5F3-2-大模型节点)

可以调用大语言模型，使用变量和提示词来**回答用户的问题或对上一个节点的内容进行分析和总结**。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s6jL8NoXch11RU9p0FjdW-8t7wBsIpiC474lPZsBUvOM/https://bzfree.com/images/coze/coze57.png)

**下面我们写一个示例，用大语言模型来润色用户的文字。**

这里的**模型**我们可以任意选择，我选择的是是通义千问-Max；然后为输入参数起一个变量名text；

注意提示词那里，要引用输入参数text的时候，需要**{{text}}**这样写。

我们这里写的是：**请润色一下用户的给的文字：{{text}}**。这样大模型就能理解我们的指令去润色text文字了。

具体设置如下图所示：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sBfA7GYSHeu9vSotib2IqSugtcwSjpgS08Mrv8ZIBUyM/https://bzfree.com/images/coze/coze58.png)

试运行一下，看看结果：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,suEp1SNRXq9XeeVVcH_Yv-VhuOS_-BBD04L-2U92rXfo/https://bzfree.com/images/coze/coze59.png)

输入"外面的景色真好"，点击 **运行** 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sgsTdZkqbnCmu2NIZDrAjkqdie7Tou6IOwpf3Juj-_WE/https://bzfree.com/images/coze/coze60.png)

查看运行结果，可以看到大模型为我们润色的还是不错的：）

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sG0R6_hH-piMvrjUYyi9TqZP1FAbAInZa111pSBBkPYk/https://bzfree.com/images/coze/C4XACGyv5QOhOK74TtOr9fGq2IYs1LJY13pvUr-OUz4.png)

#### 3.3 代码节点 [​](#%5F3-3-代码节点)

代码节点是用来编写代码，处理输入变量来生成返回值

通过以下这个示例，大家可以一目了然的明白代码节点的作用。用最简单的示例解释了代码节点每个参数的作用，请注意绿色线所标注的各变量之间的对应关系。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s51AenxXhy0sjQXoNkx8VrotJgYCJb5YnixoX29lzYE4/https://bzfree.com/images/coze/Cv5s61qMrx0zh1SiMnc0tlvBGpJbfB5_ViRt0YGxAVo.png)

**编写代码**

点击 **在IDE中编辑** 可以编写代码

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s4pe4Hb6RZcC-hpi-WRrPRo7XCr2zbH4HdzCJDsRYzhY/https://bzfree.com/images/coze/JL5lwiulCVY6ox-ofpqMQ1Fx-DXVyZ4NcpzKYKBm3HM.png)

这个示例代码的作用是：为用户请求参数加一个叹号" ! "，也就是做一个字符串拼接的功能，然后返回新的值。

注意params对象中的值，对应的是输入参数，如果下图所示：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s1xDXatrfKbxWxfJRFzBzsA3CH2vhgLoHVs45OpuilxY/https://bzfree.com/images/coze/3v8IhdCEoDYNRyR3hW7ymEfjr4uO6JRxiExu1UYSqbo.png)

点击 **测试代码**：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,stAfI1A7aFehoa7jse1Klcexia9UoJ7cqp5-yeGVjlV0/https://bzfree.com/images/coze/5mulVWY4zXhNZgSvGaueWrJPmf748utBi2n8CBn8XHk.png)

按图中所示三步进行测试：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sM15uxFzlODlAqOQMnRQaGNguuMa69cawyRH0ovlXf9c/https://bzfree.com/images/coze/badLfbxkqDhHaYALbgdOCtZHxK1w1yRn5vTdWDVTlVo.png)

点击 **确定** 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,swE4NbKuyZgh22U6de2ZFJG8uYZv3wYl9T8ASLF9L1Ks/https://bzfree.com/images/coze/2BjrVLaiAgDrMHqRk6D5Zv4PJzOjXJ7_liu0E--nZh0.png)

作用是把代码中返回的key值，作为输出的key值，以便为了下一个节点使用。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s53V2ycfXCYWUWr6dfl30gSwPr_L1qyDLH3zgIS7Ozvw/https://bzfree.com/images/coze/ob1SSQx6jYPHIWQVuSmJEMOdnSLXuetg5ET-NelQo7s.png)

接下来 **试运行** 一下。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sVTzkwdoNAQJD9E3JHy-fg_i6Ywcmxcz_FJOwd_Hh7sE/https://bzfree.com/images/coze/LwQ6eyXqbg9MhKOWGx4tUnbiRrxuDDymG8-1J-JqW-w.png)

输入"你好啊"，期望输出"你好啊！"，点击 **运行** 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,srmJ0JDOWR7LWqqrnlT09r1c-t56MS6DlMpngoCjQZFM/https://bzfree.com/images/coze/R6QXB9suHyP26dsUWomXpiHmmuoiZE1liFBUXbiinn4.png)

**输出结果**

可以看到，是我们期望的结果了 😊

![image](https://proxy-prod.omnivore-image-cache.app/0x0,snjzJCSulM9O4UEpcCgfXnvMMPmONU1ceJ9h7KuW5ZSw/https://bzfree.com/images/coze/UUeoZGcoNgP07VdkAzAQPdKWaLEN6GQXOpxzgdOcO4Y.png)

---

关注公众号

![斜杠君微信公众号二维码](https://proxy-prod.omnivore-image-cache.app/200x0,sgxWx5jk1OoMMAF_C-F3JqDf-vOSTTocma_fO1iQNQss/https://bzfree.com/images/common/qrcode.jpg)

进群交流

![](https://proxy-prod.omnivore-image-cache.app/200x0,sZCzQPkLfMm-oRK8AAaK3FoHzluoCP5xkt1z_1QGsm_0/https://bzfree.com/images/common/qrcode-1.png)

**如果有任何疑问，欢迎进群交流讨论，备注：斜杠君。**

---

#### 3.4 知识库节点 [​](#%5F3-4-知识库节点)

与 [第四章：扣子知识库使用](https://bzfree.com/coze/#%E7%AC%AC%E5%9B%9B%E7%AB%A0-%E7%9F%A5%E8%AF%86%E5%BA%93%E5%88%9B%E5%BB%BA%E5%8F%8A%E4%BD%BF%E7%94%A8 "扣子知识库使用")， 所讲类似，之前讲的是直接在Bot中引用知识库，通过Bot直接进行调用。而在这里是作为工作流的一个节点，但他们的功能都是一样的，在选定的知识中，根据输入变量召回最匹配的信息，并以列表形式返回。

**下面我们写一个示例，我们还是以第四章中FuturaTech的FAQ咨询为例，写一个工作流，用知识库增强回复的准确性。**

首先看一下下面这个图，在这个示例里，**有一个地方要注意一下，和之前的示例有一些区别。如果我们要使用知识库，还要借助一个大模型节点**，这个大模型节点的作用是：对根用户提问和知识库节点匹配的内容进行重新组合，生成符合提示词要求的内容，返回给用户。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sYMqPqqfRSbb5KRV9HHR1_ikXSK3SEWe-Iw2uHN8jJNk/https://bzfree.com/images/coze/8BZrGiHQucKDNkhVR1bS1kbsdLYkogmYh7I5C7VcBxM.png)

**添加知识库**

点击 **+** 添加知识库：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sxA3mBrEeeoV-5yZWhKJLexaJ9RJOvF7N_U_T_5DLUFM/https://bzfree.com/images/coze/AdECyTSBjZN1AB43pw54jYu-OKVzNG10Bw7lC-0LTuI.png)

选择之前创建好了的知识库，点击 **添加** 按钮：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s6kHk16rKIb-Qj2sfodcK9UvpMELLJPuJ-OqIzbXR4c4/https://bzfree.com/images/coze/OhdSveS2D2_UpQGiAjz90xYBBqvFf0QP7LZ2V7jBF6k.png)

**设置大模型节点**

大模型节点这里，模型这里我使用的是通义千问。模型可以任意选择，在调试的时候可以都测试一下，看哪个效果好就用哪个。要注意的地方是 输入参数 这里，从图中可以看到，引入了两个参数，一个是question，一个是knowledge，分别对应的是用户的提问和知识库节点的输出。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s2W09qqz-QeKASjsPFb6ruZBivgb7AL5kaCE7qjnhzSU/https://bzfree.com/images/coze/ic3sGLMyQf7gTvibwpmD2SHgI1q7uKs75oOciEsyNm4.png)

**设置大模型提示词**

有了这两个变量，接下来我们要结合这两个变量去写提升词。这里也不需要有一个固定的写法，只要把你想要的结果，通过描述告诉大模型就可以了，下面是我写的一个提示词，大家可以在此基础修改成自己的。

Plain

```markdown
# 角色
你是一个专业且耐心的客服人员，你会接收到两个输入参数：
1. {{question}}是用户询问的问题
2. {{knowledge}}是从知识库中根据用户的问题{{question}}查询出来的知识库内容

## 技能
### 技能 1: 解答常见问题
1. 你能完全可以理解{{question}}的问题，并对其中行分析。
2. 基于检索到的信息{{knowledge}}，为用户生成准确、简洁的回答。
3. 如果知识库中没有相关内容，及时告知用户，并表示会进一步核实。

## 限制:
- 只处理与'FuturaTech 常见问题解答'相关的内容，拒绝回答无关问题。
- 所输出的内容必须按照给定的格式进行组织，不能偏离框架要求。
```

具体如下图所示：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sR_-smyNzwyZpyKvfrDE7EjeC-mK_AESYYnZ_e07A8CQ/https://bzfree.com/images/coze/XHL-IZanZmqlrLjjc3FmU8Phc0C6C4jioP7GpYUQA8c.png)

**预览与调试**

如图所示，点击试运行：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sb0f0MJWRykLvmWVcpjNG_Fj1xdIupVQ2FMjbqhff2Zg/https://bzfree.com/images/coze/FccKnGNi1dZ7VDWC-v-_j1XDrl9qlbMObYmUh9LkTEo.png)

输入问题

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sWujq-uXT50s10xq1QGWXADphw0mfYeYNzK_-NM2bWwM/https://bzfree.com/images/coze/y8Ehexmp7j7o7x1J7ykAp-NlMv9SVo4sRWx7umfVLHo.png)

查看结果

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sSwn3j5l0jyDc8YqiUlgpmDNHgm1Rnoj5DRvBZh1Bfzg/https://bzfree.com/images/coze/f4ew7fgrQ4tF4SNbGXA9UOBGlnf_4doo8_-PMpT3DEs.png)

可以看到，是我们期望的回答结果了 😊

#### 3.5 选择器节点 [​](#%5F3-5-选择器节点)

选择器节点是连接多个下游分支，若设定的条件成立则仅运行对应的分支，若均不成立则只运行“否则”分支。

通过以下这个示例，大家可以一目了然的明白选择器节点的作用。用最简单的示例解释了选择器节点每个参数的作用。

我们通过以下这个示例，来解释了 **选择器节点** 分支的作用。

示例所期望的效果是：当用户的输入值为1时，执行**消息一**的流程；当输入其它值时，执行消息流程。

流程的结构如图所示：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sZKD_dLF_K-CNXls6_Dz8RoXBirXpKRLygc-Rns09UIs/https://bzfree.com/images/coze/Z0J2Jcoz-xd9NzxNrRhQjq9hE4H3SKc3v7yDiQEgmJw.png)

当用户输入的参数为 1 时：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sW3OWYfJI5r5bgG9XpscCJsbkxF5POdGuhVVHH98yHDk/https://bzfree.com/images/coze/0xoZTtqnW_shQWfs-qVVCrGEJtRJpAX1aSO_-52Z2a0.png)

可以看到运行的是上面 **消息一** 的流程：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sp-utryZEKzDbaZC2-yhOrPS4D1lvRnMcnm28PKj-28M/https://bzfree.com/images/coze/uRvb8PFF4A2nXDyRfBe-ol7lR55xZpFXhAtJxE5MD-g.png)

当用户输入的参数为 2 时：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sz6NR34gdJz7hguJEZ54JwE0nkqHYjVi3BPLWAiTtXz4/https://bzfree.com/images/coze/HJXlz_1GWlSLxcn6q1OO4PRu6y3eb-BFUTP8LHbBba0.png)

可以看到运行的是上面 **消息二** 的流程：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,soAwHqejDG5oaMk9LP_53KtiOkC4SZIjyUdnmMT17co8/https://bzfree.com/images/coze/psS8gZ8xmjTYIfB7pDxvMvWZ91JRjZeqoOD-d8Yl5b0.png)

可以看到，是我们期望的回答结果了 😊

#### 3.6 消息节点 [​](#%5F3-6-消息节点)

消息节点是支持中间过程的消息输出，支持流式和非流式两种方式。

下面我们通过一个示例，来看一下消息节点的作用。

这个示例是：当用户输入一个漫威人物，大模型会对输入的人物进行介绍。这里要注意的是，消息节点在这里的作用是：在大模型输出结果之前，提示用户"下面为大家介绍一下漫威人物XXX"。

这里要注意一下，如果要单独调试消息节点不容易看到效果，这里我们要借助一个大模型节点来观察效果。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,ssKW1kbn_AIMQOsIBVCzlRtVweKs2CJn4b43SRHv3NYo/https://bzfree.com/images/coze/ElVvor8ac1LuNY-X9RPzhIpDt3EBGd1ez5_3MvzgR8g.png)

试运行一下，我们在输入参数中输入：钢铁侠。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sR51wwsAhDH2UrL7ijqqsWH179fbrzU1MeLz_UCo5wl8/https://bzfree.com/images/coze/NNsuxShrixNd5uzlY1f-HI1aWOJLNzvbw0GDYYpb0-s.png)

这个图可以看到，当大模型节点正在运行的时候，消息节点已经输出了内容："下面为大家介绍一下漫威人物-钢铁侠"，**这个过程放在实际场景中是在让用户等待大模型输出结果。**

![image](https://proxy-prod.omnivore-image-cache.app/0x0,spoMxgIUh9iDIAIN4VXjgrddEW-cwZvqoaM2y9lDEJEM/https://bzfree.com/images/coze/N_BUtL4rL2oYsUgFRcoX4IA-xwMuglrTtlSY_J7YG0g.png)

下图可以看出，在消息结点运行完几秒之后，大模型才输出结果。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s2LsU50fworTunzr2UTwNo_gwHTy4Zj7e1XJOQg7NyRM/https://bzfree.com/images/coze/lCO-MUhDIXtZlLTvNn8Tn3xDyjuYjVFUx2GW_9JHMV0.png)

这就是消息节点的作用。在之后工作流使用过程中，我们还会看到消息节点更实用的作用。😊

#### 3.7 工作流节点 [​](#%5F3-7-工作流节点)

工作流节点是集成已发布好的工作流。也就是把之前发布好的工作流当做一个子任务，嵌套子在任务流中执行。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s59lzAupksN7SI9IMCYPIGSUC111VRo4mjTFVxmvTN58/https://bzfree.com/images/coze/YWJtU8n_USSjeKtYdpGFq8oiDsjLQepIfZ9ULDEOdmU.png)

下面我们通过一个示例，来看一下**如何在一个工作流里嵌套另一个工作流。**

我们把 3.6 消息节点 中讲的示例发布一下，把这个3.6的示例当成一个子任务。放到我们本节这个示例中演示。

这里先提一下，工作流节点，只有发布以后，才能被使用。

如下图所示，先把工作流进行一下发布，点击 **发布** 按钮即可。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sVsS9VxVoG9KmoUnwnyWHHYxnyJl1RVXk15tpbTLnYNM/https://bzfree.com/images/coze/6Bwp4Wnakf4_SY6CbaS4xZ0E9N5jlOJo7sDrCMHUcZo.png)

可以看到，很简单就发布成功了。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sFg3e8qJltiLXrbFlKB3sqrgz5_w3q279Cuo3Kszl0-w/https://bzfree.com/images/coze/chyLnOcHSswmywZkoujw_TRvnoyuWqALBk65kyJ-hn0.png)

接下来我们再创建一个工作流，点击 **创建工作流** 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sreBQb84h_y0SNjoKhbxyZAEkn31JlpqE4Z04zb6LYmI/https://bzfree.com/images/coze/9SSwAOgP5GKVD2yKj1mZXV5LOlYvgKJmzSe9iNZPDSw.png)

为工作流节点起一个名称和描述，然后点击 **确认** 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,syGYgHGY6mbFV3O9GzxTdSoTA_4ohEPAtWLO2sK2sRr0/https://bzfree.com/images/coze/X_x4b5W9EXl59PB1q5kVsjVLEtqO7bhe5CSaFoLkufc.png)

点击 + 添加一个工作流。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sSxe4ZSCAyKhJ1K2kFhJqUk_KHvpEes_83-eiphSPcw8/https://bzfree.com/images/coze/Ia3aK1CuF0O2mpETTYN5EIjcptNs-SLla25e7U4Ydr8.png)

点击 **添加** 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,smXcEMPFLd2gZJ-xj24WYjxP6yM4f-kXUDvSNBz0bHE8/https://bzfree.com/images/coze/8uIdsRkctNyistOJdvVZPgbYG7m1ZLqC_g2Ab_MpZfI.png)

这样就把消息流节点添加进来了。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sllDkB1LZilK5V5Zy03VivIQiCECyPAOeYVWTu-dFAFA/https://bzfree.com/images/coze/zItJBfqYeUiiaZzvDcuE0eSNSJtkmTV1axSO4qhNiQc.png)

接下来我们进行一下测试，把3.6节点，用户的输入替换成当前TestCallMessageNode工作流的query参数。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sWO8MqK3ewfc9PAt9FitskPdlMNn7j-ptGZNNGMXBTFs/https://bzfree.com/images/coze/PwubnM8wmPVITSOAeH3L0LXfXAeejn3XwTQD2oP2hGg.png)

接下来进行一下测试。点击 **试运行** 按钮。输入参数和3.6节所讲一样，还是填入"钢铁侠"，然后点击 **运行** 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,shT_7VGT1d2b5QfQ3R_JOBBoYpO_CNRmCSEF_GarlXX4/https://bzfree.com/images/coze/oaSKTmc7M_TGhWIACGJElJ5MUmohv90_LZ32Kq5__2o.png)

如下图所示，和我们期望结果的一样。我们在 **TestCallMessageNode** 工作流中调用了 MessageNodeWorkFlow，MessageNodeWorkFlow同时作为**TestCallMessageNode** 一个嵌套的子任务，我们得到的结果和3.6节的结果是一样的。😊

![image](https://proxy-prod.omnivore-image-cache.app/0x0,shZGih9vIvfwvcQXF0SXsj3umgVhYuLtU91O6FxZ59nc/https://bzfree.com/images/coze/tmPuSmLgIdCBoSqZYbnZM5F2YDgkTFUqxqJGB-RfJmw.png)

#### 3.8 变量节点 [​](#%5F3-8-变量节点)

变量节点是用于读取和写入Bot中的变量。**变量名称必须与机器人中的变量名称相匹配。**

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sSKmiPpe17RGaopBPCoheeQUnL80EkJIF-nmf3JKA8qk/https://bzfree.com/images/coze/_DFKlHU2y9tasjjgz1sLYypFOnuXakCvX9ed_8iq_xY.png)

我们通过一个示例，如果配合Bot来使用变量节点。

==通过变量节点的定义，可以知道：使用变量节点之前要有个前提，就是==**==首先要有个Bot，并且这个Bot里定义了一变量，否则单独使用变量是没有意义的。==**

所以首先，按创建第二章的方法，先创建一个Bot。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sDfvrrVc3Ba21VeqrIW6-JAA_zwAc0mmzBEu3Ov2AoCg/https://bzfree.com/images/coze/akXDuS54fPYB2FPnJrjINSVLGBt8-PezxU6-O2B06Ts.png)

点击 + 按钮添加变量。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s25lHVdQ4gRXiDLLXbrIMC-KAur-UIMcIyw4OoAmUEkQ/https://bzfree.com/images/coze/eKltTn3wSwfNMSHjWLXMOPUiLc_jn9RjjSzOI-NXXLI.png)

定义一个变量role，来表示漫威的人物

![image](https://proxy-prod.omnivore-image-cache.app/0x0,scONE_Cjfk7_Tig1xKNMTUDWS9gv4gx0Zh7uCp-les7E/https://bzfree.com/images/coze/HvpYS5OmytdEtB7k2UptJPU1M7oGDzDYRwo-LMPec9M.png)

接下来发布一下。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sNEYmeIyKuhveae4VYE80mzzO94sjYyXm-I2FDJqIWjw/https://bzfree.com/images/coze/0oB7XOkrIkAVeAl2owUlDbq_feGHwDJaJkzHNyoQ964.png)

接下来创建带节点变量的工作流。

如图所示，创建了两个变量节点。第一个节点是使用用户的输入值来设置变量role(和Bot中的变量对应)的值，第二个节点是用来获取变量role的值。最后使用role的值输出。

同学们按如下图的方式进行创建。注意红框所标准的位置设轩

![image](https://proxy-prod.omnivore-image-cache.app/0x0,szttZvpjQFTriSEBKpLwRHbMcoDUipbiDlOKrCcL2t1c/https://bzfree.com/images/coze/mGWmDLdodifobLK6eWQX_7DiG1P_IyMh2Q77fzTZ1R8.png)

细节大图：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sEfdgFuQMQ2TW9abulcsYPmjTYQcsV2xsrEfZyeUN8Ic/https://bzfree.com/images/coze/qg1jC9vNuAlBJWPnuxipQDpIpkWr8kiFxjhPK-uXfpo.png)

设置好以后我们运行一下。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,st_CuYi17AWa6jOH3KWPqZXIZhrCvSFh7UyWbgLV0Ynw/https://bzfree.com/images/coze/Iauvyby0d71dyvJyiEihvy-JTGKJVOQllxWZrYIHXZI.png)

可以看到这里就要求我们关联之前创建的Bot了。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sE418M3mLcolR0TkJHkJT8pZAVteBpBlU2JxxbMAlqLY/https://bzfree.com/images/coze/cgheH8WkCI0WXz6RCv8gKS2QF0xWbfzjdj6OgWKHwFE.png)

选择后点击运行，查看结果。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s3qKNNhT7ne1MeDAR3SsNBnEV6PBJEfQgFf8NkBuN7BA/https://bzfree.com/images/coze/nKxVPUAbEJFfDcvAmO2qamNe2dVFnh9YMeDzlDnKR8E.png)

可以看到，成功输出了我们在上一步上设置的role变量的值。😊

#### 3.9 数据库节点 [​](#%5F3-9-数据库节点)

简单来说，数据库是用来存储数据的。那 **数据库节点** 就是在工作流中存储数据的。扣子中的数据库支持放开读写控制，用户可读写其他用户提交的数据。权限由开发者控制。**需要提前在 Bot 的 Database 中添加 Table。**

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s90eT3a8zKmbtdEm4ZGIc7Wqarj4DZFH75e4IMvBQrao/https://bzfree.com/images/coze/2b9Dkqci-vjhlunhm2TtYO6pY7O1vHncQufXx-Y8yB8.png)

我们通过一个示例，如果配合Bot来使用数据库节点。

通过数据库节点的定义，可以知道：数据库节点和变量节点一样。使用之前要有个前提，就是**首先要有个Bot，并且这个Bot里已经创建了数据库，否则是读取不了数据的。**

所以首先，按创建第二章的方法，先创建一个Bot。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sQ_O1FZTL8h0m3TNKLXvIzIqoCskpOWfzuoEAH6mH2Vo/https://bzfree.com/images/coze/MtXWbiWdu4-WLIUSTlL0mBw10eG4VrgDzTVTTchsL9Y.png)

点击 + 添加一个数据表。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sYRyXfw7a5i-68-EpBV89ObxqkrtSuqaitjgp5ljC5eU/https://bzfree.com/images/coze/7SSRq1mvLdyAmBmPx3JwFJ6ta6WKonUoGrYHaERerc8.png)

为数据表新建字段。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sL1lRHtOIqRqL4IGDhOvUJnFthYLD26xtsqV-o72DM88/https://bzfree.com/images/coze/bx6LOxaQAP4XZAB4BdvVRApfH3cc1FdutZPOE02iBYQ.png)

为了演示方便，我们使用模板进行创建。点击 使用模板 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sCmZycdUfnr1KB1lgkv6tMAidbqnFCttIlDyQzxwFwk8/https://bzfree.com/images/coze/-VZmJf9p4jPnV9BdHu6UN-C4pQrzkZhAhbYlsJ5UgII.png)

可以看到，模板建了一个"用于保存读书笔记"的数据表。数据表的名称、描述和字段都已经建好了。点击 保存 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,ssN9jQJvwmhG9ksOaBmzgdDSY97-FRVdJCWxBcDWvnjM/https://bzfree.com/images/coze/Zv40K_tZklEaHEFlJehg8MhFKl9UVcrNJbQmb0GiFsU.png)

可以看到数据表已经创建好了。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,smT7G34kdyQDXyyu9tKT0-ttViwXq1cmz63hShg_WiiA/https://bzfree.com/images/coze/c7Jad-o27BgreboAnuY4HIwhdfCkrjWB0-YjWfWQwlQ.png)

我们来演示一下如何向数据表中插入数据。

向数据库中插入数据，不需要你学习复杂的SQL语言。通过自然语言与 Bot 进行交互，即可插入或查询数据库中的数据。

如下面这个示例：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,siq5_sJQexpCY_2dEF8nu36q8qDSd71O1IQH8x4uKz_U/https://bzfree.com/images/coze/CsP99TyLmcdedv49DzojfVtYtUne305xjfDVBpDsHzY.png)

可以看到，我只是简单的告诉Bot："三国演义这本书很精彩"，Bot就帮我把这本书记录到数据库中了。

再来测试一下查询功能，从下图可以看出，Bot很容易的给出了答案，只有一本我们刚刚插入的《三国演义》这本书。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sVFavE9Faung5Gi-8GsHwvJFwUcOUpy7ZMfMk4AUNvIc/https://bzfree.com/images/coze/zUpBvoPWLhJ95rcjnpvEZnYjwK619C5VmZWoKWA6_3Q.png)

到这里，数据表的建立就完成了。

在这个示例中，我们想实现的效果是：先在数据库中插入一条数据，然后再查询数据表，验证是否插入成功。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sjslEbCLWaItp33tlOsv5D0lJJdxj4ETD6d1DLTn0p4o/https://bzfree.com/images/coze/ManoNln5kZbxkgY1mrDOFxMSc4YmJKJDycKI6eWlMHE.png)

如果你会写SQL也没关系，我们使用 **自动生成** 的功能，在查询目标里输入自然语言描述我们想要的操作：例如"向book\_notes表中插入一条数据"，然后点击 自动生成 按钮，就会成生一条SQL语句。点击 **使用** 按钮，SQL语句就被应用了。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s_SlrM9BWgeWpmoMhT6OafMXPY5pBklr2dggqeL-5wz4/https://bzfree.com/images/coze/bCSgXwQGFBxU1cFezAOzzjYc1YlfnPvCaM4lVWMs94c.png)

这里注意一下，生成完SQL之后，我们需要调整一下这个SQL。生成后的SQL语法是没有问题的，但没有传实际的值，我们要把我们想传的值放到这个SQL中。调整后的效果如下，对应的输入参数的name：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s3vvfh7y3iMw_7xRZQMbooGNKK22T87LTKFN1q9AsUR4/https://bzfree.com/images/coze/B2Nq9AYaBp-xIzcSCztapoXZgaOCy8824GnO7V_p5Kw.png)

试运行，看一下效果：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sFPEOPZSHZt1AZ_DyDKHLRAmOzcEJlGLcB-f1JuFfydA/https://bzfree.com/images/coze/I4sKCSs8V2YdPfcNMv436IOpkg4xFQzZeTpNR7Wt5uU.png)

如图所示产，流程执行没问题。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sY5djtjzIlJnbHZ2vudwXqg5n6nYAZuxoblRbhpzWD8E/https://bzfree.com/images/coze/uozyEpBFikM9rxfkVoHpValGybLPlSeUb8SAXnmt-Hc.png)

接下来用同样的同样的方法，我们把插入SQL改为查询SQL，来验证一下，数据是否被插入到了数据表中。

如图中标示箭头的位置要注意一下，这里的name要和查询的字段对应，当然你还可以加更多的字段，这里只要一个作为演示。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s3r1di1qaQg7ebIJf0vxwD5TDM4S3xYcB5n3KhQbZVGs/https://bzfree.com/images/coze/fCzmkijE-SVobyXGOxfxcBblDeQpB2hB-joYvxEFLBk.png)

可以看到，数据被成功查询出来了。😊

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sTAoNb723YsCA-y6-eyJvaoL2x7FA1pqeK3RorAFTCck/https://bzfree.com/images/coze/iwzt-1a7wwWAvvsjuBgxQq6o1PqgUnKpbIDEkRydmdc.png)

---

关注公众号

![斜杠君微信公众号二维码](https://proxy-prod.omnivore-image-cache.app/200x0,sgxWx5jk1OoMMAF_C-F3JqDf-vOSTTocma_fO1iQNQss/https://bzfree.com/images/common/qrcode.jpg)

进群交流

![](https://proxy-prod.omnivore-image-cache.app/200x0,sZCzQPkLfMm-oRK8AAaK3FoHzluoCP5xkt1z_1QGsm_0/https://bzfree.com/images/common/qrcode-1.png)

**如果有任何疑问，欢迎进群交流讨论，备注：斜杠君。**

---

### 4\. 工作流案例讲解 [​](#%5F4-工作流案例讲解)

本节开始，我要创建一个工作流。结合之前学过的知识，做一个**图书管理工作流**给图书馆的管理员使用。这个工作流的作用是：通过判断图书管理员指令的意图，来执行对应的操作。

我们期望的效果是：当图书管理员输入类似“请帮我查询有哪些书籍”的时候，工作流就返回当前数据库所有的图书。当输入“向数据库录入一本书”的时候，就向数据库加入一本书。当然也可以通过指令删除。

通过上面的分析，我们可以知道：

1、如果要分析用户的意图，我们要需要使用的节点是大模型节点。

2、判断意图后，我们要执行哪个操作，是查询还是添加，还是删除，这里我们要用到选择器节点。

3、要向数据库中录入书籍，肯定是还需要有数据库节点了。

接下来让我们创建这个工作流。

#### 4.1 创建Bot [​](#%5F4-1-创建bot)

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sbVFnUcwlOcy5bYbiHn39WOT0uGogb1xNjxifJx40pTw/https://bzfree.com/images/coze/L_4N5n_ola5JrsV7QeOa4yIRofrbMTP9s7iBX9cxDkw.png)

#### 4.2 创建数据表 [​](#%5F4-2-创建数据表)

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sAAzdvZCp6VJanlNtd0xwdN6119Ocfla3wI2QsttGwDQ/https://bzfree.com/images/coze/wmUR4WKEXKaahAU3gMhgQNS-_u356xQuWtqrGRCHkLM.png)

#### 4.3 添加字段 [​](#%5F4-3-添加字段)

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sIWhbGyR0ac9_vmobm-E7nRNsOw0C6R0HWEd3P9aDs4k/https://bzfree.com/images/coze/s6R_8uVpXQcg5uAQ-X1q3WAeG-z9Ft0wE5iolIPioWU.png)

#### 4.4 创建工作流 [​](#%5F4-4-创建工作流)

进入工作流管理页面，点击 **创建工作流**

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sfOd9dTTUSV_hnswX0n_NLZNDVoBOKHD0olDhPx-AZqY/https://bzfree.com/images/coze/ptc8A_Ofad5RJzhEif8O6HVtQmeVogIIR2r8zdea748.png)

#### 4.5 填写工作流信息 [​](#%5F4-5-填写工作流信息)

![image](https://proxy-prod.omnivore-image-cache.app/0x0,suNMazJnB2aYNFUBHsCGuLAY2vKSdEg-xQtCNJqNhBKU/https://bzfree.com/images/coze/m7x1iD7xoW2hcQaqdweTsx0FQjvlq8TyEMbIdgXGW-g.png)

**我们首先把需要用到的节点先加到视图里，然后再对节点一一进行具体的设置。**

**整体效果预览**

先来看一下最终配置好的整体效果，我们再来一一添加节点到视图中：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,slsa_WEtA9rwmN_qfmUIEDxVwa20zD_XZ1rwcUbyet3w/https://bzfree.com/images/coze/kh73jdmBRCQmgBOjvQaBFdoUOAoiJEvEg1rRZUimjhw.png)

#### 4.6 添加大模型节点 [​](#%5F4-6-添加大模型节点)

先添加 **两个大模型节点，为了更直观的演示流程，这里用两个大模型来分别返回 图书名称 和 操作类型。（正常情况下，一个大模型节点也是可以搞定的，返回一个数据对象**即可，这里大家要理解就可以了。）

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s-qKVNMIhOHitMT4jepBtpgL_BsGAWvT5bgIEg8yaZO4/https://bzfree.com/images/coze/OevM2pJkwdln2IL-s9ZRUH0bfZ_HoBNesuSLkAxZGYI.png)

#### 4.7 添加选择器节点 [​](#%5F4-7-添加选择器节点)

添加 **两个选择器** 节点，先忽略配置。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sC7IQUxyPaqZZG40JSYiS37RiiEFVkZ8Mm8TZbqTusKQ/https://bzfree.com/images/coze/GWlp3fFNN5OivuEeJWg-lja1CTkeTdiYxHkNRjyNYHk.png)

#### 4.8 添加数据库节点 [​](#%5F4-8-添加数据库节点)

添加**三个数据库节点**，分别用来查询，添加和删除

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s60WeeecAKPKLx9cJhRD3ym2l4VpNvX5RQUDIM8tTmew/https://bzfree.com/images/coze/yJxe-dzUGYZKH8yCp_64AWfuYwtsyBEi7j149Kp9ng0.png)

#### 4.9 整体效果预览 [​](#%5F4-9-整体效果预览)

再确认一下整体结构，是否和下图一致，注意各节点之间的连接关系：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,slsa_WEtA9rwmN_qfmUIEDxVwa20zD_XZ1rwcUbyet3w/https://bzfree.com/images/coze/kh73jdmBRCQmgBOjvQaBFdoUOAoiJEvEg1rRZUimjhw.png)

细节图一：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,srjhLMmU6mz8KOeD310LbB5LaBbFxz7i-IjPeRxggRys/https://bzfree.com/images/coze/QIOblTOPqaR00EmRgsE7wD9C0b9rRFmK-9TVcdzLbv8.png)

细节图二：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sXIxc_pdTnmuVg1yEx4uwoHcUqNtr9-6kgBdhEckcO6A/https://bzfree.com/images/coze/M163s1pUnq2knnfnRB2t9lM_HGQfoIBsHqg3L_zaIO0.png)

#### 4.10 配置各节点参数参数 [​](#%5F4-10-配置各节点参数参数)

##### 4.10.1 设置开始节点参数 [​](#%5F4-10-1-设置开始节点参数)

![image](https://proxy-prod.omnivore-image-cache.app/0x0,swddazb1GOc2By-oMTgMG_ByJyDCmPaNPRESEwd0GT8E/https://bzfree.com/images/coze/Hztt3ioV1UMPn4aEx6VWlJkawMPQ4K6CVx9hzX44Ofs.png)

##### 4.10.2 设置大模型参数 [​](#%5F4-10-2-设置大模型参数)

**大模型-操作类型节点** 配置：

1、添加图书 2、删除图书 3、查询列表

![image](https://proxy-prod.omnivore-image-cache.app/0x0,szP3Mi2ZzokgCOakOuVlaMTRMec2e0wQ9RT4iHhM3Sjg/https://bzfree.com/images/coze/D2Vq0zyO61kvSaurCJwAdOn1WcDAdqSeEFWXAzLVxEY.png)

**大模型-提取书名节点** 配置：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sJfprfAHi36fyCuxWLBkoRZArKkVJCZkc_2u3JntyvYo/https://bzfree.com/images/coze/zbBrW7MkRaVaMf5ckO4iUqLe6uDifMVeyPHEUHCRPWk.png)

##### 4.10.3 设置选择器参数 [​](#%5F4-10-3-设置选择器参数)

选择器-1 配置：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sozVwqHRcMeuUxtNIbDaBCqv1dWoJ973MJ5QkSW0juow/https://bzfree.com/images/coze/16mIgFuBARP3W2Dm1MQGYhIDBjRY053ULy9u8Bks4mU.png)

选择器-2配置：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sFssh7shqReRXuj3Lv2LGUdpglK_1HYc54pHJzAkD504/https://bzfree.com/images/coze/Asaog23VBw4TXX_TklxhouTh0Lq0vPC_mWdrBIZ87co.png)

##### 4.10.4 设置数据库参数 [​](#%5F4-10-4-设置数据库参数)

数据库添加节点 参数配置

使用自动生成SQL功能生成

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sS5QQ4yZ0r0XR7L3xR1WB4kf95qmjDmCpGRJPuicub18/https://bzfree.com/images/coze/TAqa58n8KS3gcFiHpheYhVPiHM8yiYRiFNKs3ENsNoo.png)

修改一下SQL的变量，使用

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s_0YjgO47bW3TDa5xjlZX8GH7iIraQAzu08-KMedGNwA/https://bzfree.com/images/coze/KgdM_XZ6YhIi0_19VsDdO-PPFqw9emZIdeR509WEmds.png)

同样的方法修改 **数据库删除节点** 参数配置。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,svts7i8-4kOlJ0s_qLaRWId6LON31myz1GFRF-C6e05M/https://bzfree.com/images/coze/bJt_ZZP4Y7qRcjBogMwygWkBuIjjI5MZxoZ9HLg9v1Y.png)

同样的方法修改 **数据库查询节点** 参数配置，注意图中所示，两个查询的name字段要对应。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sN-J2t72XgJ_ABi5urAdKbpt3pKC6_RJlr6fiCgWGdtM/https://bzfree.com/images/coze/AjpKzjuunKprLJ0xNRHjkLmcf4JPR2_fImi3S_nwz1I.png)

**结束节点参数** 设置

![image](https://proxy-prod.omnivore-image-cache.app/0x0,spDhL1ENvURfBqKWvhdqlXLezlgOAgC6ppw0pbqINyag/https://bzfree.com/images/coze/UPU1UniCY1je1bH2IwUadJOCWMKVLRQX2TrOCTqWcKk.png)

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sfKnRSDJ_yh5lwiTIYIaFiVErbQptWyIsDNsyQBcsILY/https://bzfree.com/images/coze/_y1OEDxCenrZVD_f1YxTYv97JPIN6eu1R5LXazu0Acw.png)

#### 4.11\. 调试工作流 [​](#%5F4-11-调试工作流)

##### 4.11.1 添加一本书 [​](#%5F4-11-1-添加一本书)

到这里，各节点的配置以及连接方式，我们就配置好了。接下来我们调试一下，看看是否符合我们的预期要求。

在工作流中点击试运行，输入：增加一本三国演义。然后选择我们之前创建好的Bot：图书管理助手。点击 运行 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sBuMiRwxZ0Umv-54DiArRQL7M6KwO9qpuEsMQd18X29g/https://bzfree.com/images/coze/D1c3G7m6y4ZP7hkTh-AirsmlDpXCmLBY855VAdU8P4s.png)

可以看到，是按照预期走的 **添加** 的流程：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sc7lif7DGdpzYa0EWw0NBj2EE-LPBJ9nnU6xfDGMoTmA/https://bzfree.com/images/coze/RT32QxNST4iS66xzDb-o7nqfofuBARql_emI1vs6wgA.png)

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sT77X0h4wNLKOGSFTjloaajkU1VXHFoem_RW0aOIyXpw/https://bzfree.com/images/coze/k1pkV9aX084W1noEIcz8ltxU7K--zBP7RTPrnVl4l_4.png)

再增加一本《围城》

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sHkbEkc4hinlrk8ejga5vJq4ueJmQUFhOwdM6z3DbZ6Y/https://bzfree.com/images/coze/7na9wmV7douPYeg8JdfweeVMCbDRsEyHFvbKNXGd3cE.png)

查看结果：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sAn3MGVOVasYJWHx-qQUTH3Wniu0J_aL65Jfqd2wXB-I/https://bzfree.com/images/coze/UVT3qOFKoie_WEf6RmziYKx8FR74mhTKzYzM_NSs_7I.png)

可以看到《围城》已经被成功添加了。

##### 4.11.2 删除一本书 [​](#%5F4-11-2-删除一本书)

我们把之前的添加的《三国演义》删除。点击 **运行** 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sPH9UmElAmcDdNqJbCyecHZhND0ZXKqxFBKEvNCBxycE/https://bzfree.com/images/coze/POwRqqQgpxInW6hCOWTz12imV6k1OXYIYVrQx7RmirE.png)

可以看到，按照预期，《三国演义》被删除了。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sV8B8ZjZRwpcJUuLcfn5gefLZyw-QxTjNPxRkAfOASAA/https://bzfree.com/images/coze/uLQIHr4cCYDoDIJxeweeth8bB1JKVvOaJ0NtZh9c16o.png)

到此为止，我们的图书管理工作流就调试完成了。😊

---

关注公众号

![斜杠君微信公众号二维码](https://proxy-prod.omnivore-image-cache.app/200x0,sgxWx5jk1OoMMAF_C-F3JqDf-vOSTTocma_fO1iQNQss/https://bzfree.com/images/common/qrcode.jpg)

进群交流

![](https://proxy-prod.omnivore-image-cache.app/200x0,sZCzQPkLfMm-oRK8AAaK3FoHzluoCP5xkt1z_1QGsm_0/https://bzfree.com/images/common/qrcode-1.png)

**如果有任何疑问，欢迎进群交流讨论，备注：斜杠君。**

---

#### 4.12 引入工作流 [​](#%5F4-12-引入工作流)

接下来把工作流引入到Bot中进行使用

找到我们已经创建好的图书管理助手Bot。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s-zMaikxOSIBhGe2MBb2OJN_MeJaGtb4s3D2Hd4orIw8/https://bzfree.com/images/coze/x1_7-0Au4pb9qof2R5N4sH-tHMdTUEMdkXng0WmScO8.png)

点击 **+** 引入工作流

![image](https://proxy-prod.omnivore-image-cache.app/0x0,shF0v2kDh7VdBTC1qNJtyhs08Nxu9b2wyH_Q84z5P6Kw/https://bzfree.com/images/coze/hoqjyIHoF8uicLAKPMA9NgFY7mBKC9T_CnGQ9YkZzc4.png)

选择 WorkFlow\_Books 工作流

![image](https://proxy-prod.omnivore-image-cache.app/0x0,s6LtshiVZwqNQ8olk2T_fppW5FMtcaSnqiDxSi4oMBco/https://bzfree.com/images/coze/SioSUIwTY48t2MgCS-xv1jEWT8SmlU5VzosIG0Yrw5Y.png)

编排 **人设与回复逻辑**

![image](https://proxy-prod.omnivore-image-cache.app/0x0,soySDZEty9YDG9t42bAFlZtjF6ZtQOvup9nIwD0Vz6XQ/https://bzfree.com/images/coze/TvKiuAHaKKo607mZbQD9c_z_0oJdn_tPYS7b2XTjXM4.png)

#### 4.13 调试BOT [​](#%5F4-13-调试bot)

添加一本书：

![image](https://proxy-prod.omnivore-image-cache.app/0x0,smNCt0HOaf-ObHMydcfLB_Fa7SM-m0MXqXT99VssWZFQ/https://bzfree.com/images/coze/SDORWssJfxNDlUGNkO86CkzatnI3XSTKjyRpkuzbXr4.png)

提示图书已经成功被添加了。

那么接下来测试一下，图书是否确实加入成功了。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sFWb_ZSedO1onej7nbRot-GEJMf-MVO0AbBlwlL8ivME/https://bzfree.com/images/coze/DHKf_CcrR78dpvJVc95k7-VdXnIE0dnkxuk21L4FdT8.png)

可以看到，《三国演义》图书确实成功加放到了数据库中，说明我们的工作流正确无误。

#### 4.14 发布BOT [​](#%5F4-14-发布bot)

调试好以后，我们接下来就可以把BOT出布出去，让大家来使用了。

自动生成开场白，点击 **确认** 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,slULVFf0DYggFnCjSHyPyUkp-p2nHsjehqzslRAJza1E/https://bzfree.com/images/coze/kzZW4TxtryOh11mSB6HvaYr0P-UdiwVEiQOSekImm88.png)

选择一下想发布的平台，我这里选择的是发布到扣子商店，然后点击 **发布** 按钮。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sBHjdgikmn7I7qd-eeMGOLaT7dxPFIQSePampdxbU_TY/https://bzfree.com/images/coze/EYIWwKGFeWs_qK5gtLgtQt2xf8v_uksnvF_4A3kUCoo.webp)

提示审核中，然后点击 **完成** 按钮，一分钟左右就审核完成了。

![image](https://proxy-prod.omnivore-image-cache.app/0x0,sZibQPmZiWP3u7BFkJ0LPhHjUc84qs8uuoav7SnW6JeY/https://bzfree.com/images/coze/rTaGABNUTPZp8rzsfcMIRjd-vfcYD9iSPUfH5CCO1sY.png)

好了，到这里，我们终于把Bot和工作流的全部流程学习完了，希望大家在本文中能有所收获。😊

---

关注公众号

![斜杠君微信公众号二维码](https://proxy-prod.omnivore-image-cache.app/200x0,sgxWx5jk1OoMMAF_C-F3JqDf-vOSTTocma_fO1iQNQss/https://bzfree.com/images/common/qrcode.jpg)

进群交流

![](https://proxy-prod.omnivore-image-cache.app/200x0,sZCzQPkLfMm-oRK8AAaK3FoHzluoCP5xkt1z_1QGsm_0/https://bzfree.com/images/common/qrcode-1.png)

**如果有任何疑问，欢迎进群交流讨论，备注：斜杠君。**

---

