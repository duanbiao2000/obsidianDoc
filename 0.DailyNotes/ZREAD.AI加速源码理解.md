---
aliases:
date: 2025-08-29 07:49
tags:
source:
  - https://zread.ai/moeru-ai/airi/3-installation-guide
---

AIRI 的桌面版构建采用了 Rust 编程语言和 Tauri 框架的组合，这一选择主要基于两者的技术特性：

- **Rust** 作为系统级编程语言，具备内存安全、高性能和低资源占用的特点，适合处理桌面应用中涉及的底层逻辑、原生功能交互（如系统资源调用、音频处理等）以及对性能要求较高的任务（如本地 AI 模型推理），同时其严格的类型系统能减少运行时错误，提升应用稳定性。

- **Tauri** 是一个基于 Rust 的跨平台桌面应用框架，它允许开发者使用网页技术（如 HTML、CSS、JavaScript）构建界面，同时通过 Rust 实现原生功能扩展。对 AIRI 而言，Tauri 既简化了跨平台（Windows、macOS、Linux）开发流程，又能借助 Rust 的性能优势，让桌面版获得比纯网页应用更强的系统集成能力（如全局热键、后台运行、GPU 加速等），兼顾了开发效率与原生体验。

这种组合使 AIRI 桌面版在保持跨平台兼容性的同时，具备了接近原生应用的性能和系统级功能访问能力。

---

```rust
# 安装 Rustup（Rust 工具链安装程序）
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
 
# 选择项目中指定的 nightly 版本
rustup toolchain install nightly-2025-05-25
rustup default nightly-2025-05-25
 
# 添加必需组件
rustup component add rustc cargo rustfmt rust-analyzer clippy
```

`rustup component add rustc cargo rustfmt rust-analyzer clippy` 是 Rust 工具链管理工具 `rustup` 的一条命令，作用是安装或添加 Rust 开发相关的核心组件，各组件功能简要解析如下：

- **rustc**：Rust 的编译器，负责将 Rust 源代码编译为可执行文件或库。
- **cargo**：Rust 的构建工具和包管理器，用于创建项目、管理依赖、编译代码、运行测试等。
- **rustfmt**：Rust 代码格式化工具，可自动按照社区规范格式化代码，保证代码风格一致。
- **rust-analyzer**：Rust 语言服务器，为编辑器（如 VS Code、IntelliJ 等）提供代码补全、语法高亮、跳转定义等智能编辑功能。
- **clippy**：Rust 代码静态分析工具，能检测代码中的常见错误、不规范写法和性能问题，并给出改进建议。

执行该命令后，`rustup` 会下载并安装这些组件，完善 Rust 开发环境，满足编译、管理、格式化、分析等开发需求。

---

[Prompt Engineering Tools \| moeru-ai/airi \| Zread](https://zread.ai/moeru-ai/airi/11-prompt-engineering-tools)
### 2. 性格特征系统

游乐场使用一个复杂的特征系统，包含四个关键性格维度，每个维度按0-10的等级评分：

|特征|描述|对角色的影响|
|---|---|---|
|**俏皮性**|角色的幽默和调皮程度|较高值会导致更多玩笑和戏弄行为|
|**好奇心**|角色学习和探索的欲望|较高值会产生更多问题和对新话题的兴趣|
|**思考性**|反思和哲学思考的深度|较高值会创造更内省和深刻的回应|
|**表现性**|情感表达的开放程度|较高值会导致更戏剧化和情感化的表达|

Copy code

```typescript
const traits = reactive<Traits>({
  playfulness: 7,
	curiosity: 8,
	thoughtfulness: 6,
	expressiveness: 8,})
```

### 3. 情感状态管理

角色可以表达不同的情感，每种情感都有独特的行为模式：

- **开心**：充满活力和愉快的回应，带有积极表达
- **好奇**：好奇和质疑的行为
- **深思**：沉思和哲学性的回应
- **顽皮**：调皮和戏弄的互动
- **烦恼**：轻微的沮丧，回应较短
- **兴奋**：高度热情和充满活力的反应

系统根据特征水平和当前情感状态动态生成个性描述，创造细致入微且符合情境的回应。

来源：[useCharacterPrompt.ts#L42-L51](https://zread.ai/moeru-ai/airi/apps/playground-prompt-engineering/src/composables/useCharacterPrompt.ts#L42-L51), [ControlPanel.vue#L130-L160](https://zread.ai/moeru-ai/airi/apps/playground-prompt-engineering/src/components/ControlPanel.vue#L130-L160)

## 高级功能

### 上下文感知对话

游乐场支持多种对话上下文，每种都有量身定制的回应模式：

- **日常**：友好、日常的对话
- **技术**：关于AI和技术的技术讨论
- **哲学**：关于存在和意识的深入讨论
- **动漫**：关于动漫和游戏的热情对话
- **自定义**：用户定义的对话场景

每个上下文都包含特定的示例互动，展示角色在不同情况下应如何回应。

来源：[useCharacterPrompt.ts#L53-L62](https://zread.ai/moeru-ai/airi/apps/playground-prompt-engineering/src/composables/useCharacterPrompt.ts#L53-L62), [ControlPanel.vue#L162-L190](https://zread.ai/moeru-ai/airi/apps/playground-prompt-engineering/src/components/ControlPanel.vue#L162-L190)

### 组件库系统

为了快速角色开发，游乐场包含一个组件库，提供预构建的个性和言语模式模块：

**个性组件：**

- 动漫爱好者：角色热爱动漫并经常引用节目
- 技术爱好者：对技术和AI发展着迷
- 哲学性：思考关于存在的深刻问题
- 顽皮戏弄：喜欢轻松的玩笑和戏弄

**言语模式组件：**

- 动漫言语：包含日语表达和表情符号模式
- 第三人称：有时用第三人称称呼自己
- 网络俚语：使用现代网络缩写
- 表情符号丰富：频繁使用表情符号和表情

这些组件可以点击自动添加到角色的个性中，使快速构建复杂角色变得容易。

## 有效提示词工程的最佳实践

基于游乐场的设计和功能，以下是关键的最佳实践：

1. **从模板开始**：使用现有模板作为基础，而不是从头开始
2. **迭代和测试**：频繁使用聊天模拟器验证角色行为
3. **监控令牌计数**：保持提示词简洁，同时保持必要的细节
4. **平衡性格特征**：避免极端值，除非它们有特定目的
5. **上下文很重要**：针对不同对话上下文定制回应
6. **使用组件**：利用组件库进行快速开发
7. **测试边缘情况**：尝试不寻常的输入，查看角色如何回应

提示词工程游乐场将角色创作的复杂艺术转化为直观、可视化的过程，使开发者能够自信而精确地创建丰富、引人入胜的AI个性。

# 基于组件的 AI 交互

[Component-Based AI Interactions \| moeru-ai/airi \| Zread](https://zread.ai/moeru-ai/airi/12-component-based-ai-interactions)

基于组件的AI交互代表着构建智能用户界面的革命性方法，AI模型可以根据用户请求动态调用和渲染UI组件。这种范式从传统的纯文本响应转变为丰富的交互式体验，AI能够选择并配置合适的视觉组件以最佳方式满足用户需求。

组件调用的核心与AI系统中的函数调用或工具使用类似，但不同的是，它不执行后端函数，而是调用前端UI组件。这使得AI能够以更有意义且符合上下文的方式呈现信息。例如，当用户询问天气时，AI不仅可以简单地用文字描述，还可以渲染一个包含图标、温度和天气状况的天气小部件。

该系统通过定义带有描述其属性的模式（schema）的组件来工作，使AI模型能够发现和使用这些组件。当AI确定某个组件可以增强其响应时，它会生成一个包含必要参数的结构化调用，然后实时解析并渲染该组件。

---
## Silero VAD

Silero VAD 是由 Silero AI 团队开发的一个高效、轻量级的语音活动检测（Voice Activity Detection, VAD）模型。它专门用于检测音频流中是否存在人类语音，在语音处理领域有广泛应用。

### 主要特点：

1. **高精度**：在多种语言和声学环境中表现出色

2. **轻量级**：模型体积小，计算资源需求低，适合嵌入式设备和边缘计算

3. **低延迟**：处理速度快，适合实时应用场景

4. **多语言支持**：对多种语言的语音都有良好的检测能力

5. **易于集成**：提供了简单的 API，支持多种编程语言（尤其是 Python）

### 常见应用场景：

- 语音助手唤醒检测

- 语音录制自动启停

- 电话系统中的静音检测

- 语音识别前的预处理

- 音频会议中的发言检测

### 技术细节：

- 基于深度学习技术构建

- 可以处理不同采样率的音频（通常支持 8kHz 和 16kHz）

- 输出音频片段中包含语音的概率

- 支持批处理和流式处理两种模式

在你的 Tauri 代码中，正是通过 `silero_vad_processor` 来使用这个模型进行语音活动检测推理，判断输入的音频数据中是否包含语音。

如果需要使用这个模型，通常需要先下载预训练权重并初始化处理器，这也是你代码中检查 "Silero VAD model is not loaded" 的原因。

---

## 婴儿代码

```typescript
async function handleChatSendMessage() {
  if (!audioContext.value) {
    audioContext.value = new AudioContext()
  }
 
  streamingMessage.value = { role: 'assistant', content: '' }
  messages.value.push({ role: 'user', content: sendingMessage.value })
  messages.value.push(streamingMessage.value)
 
  const response = await streamText({
    baseURL: baseUrl.value,
    apiKey: apiKey.value,
    model: model.value,
    messages: messages.value.slice(0, messages.value.length - 1).map(msg => toRaw(msg)),
  })
 
  for await (const chunk of response.chunkStream) {
    const text = chunk.choices[0].delta.content || ''
 
    if (text !== '') {
      sendPayload({
        'xi-api-key': voiceApiKey.value,
        text,
      })
    }
 
    streamingMessage.value.content += text
  }
 
  sendPayload({
    'xi-api-key': voiceApiKey.value,
    'text': '',
  })
}
```

### 婴儿版本

```typescript
// 发送聊天消息的函数
async function sendChatMessage() {
  // 准备好听声音的工具，如果还没有的话
  if (!audioContext.value) {
    audioContext.value = new AudioContext();
  }

  // 准备一个空消息，用来显示助手正在说的话
  let assistantMessage = { role: 'assistant', content: '' };
  
  // 把用户说的话加到消息列表里
  messages.value.push({ role: 'user', content: sendingMessage.value });
  // 再把助手的空消息加进去，等下慢慢填内容
  messages.value.push(assistantMessage);

  // 发送消息给电脑大脑，等它回复
  const response = await streamText({
    baseURL: baseUrl.value,
    apiKey: apiKey.value,
    model: model.value,
    // 只发之前的消息，不含刚加的空消息
    messages: messages.value.slice(0, messages.value.length - 1).map(msg => toRaw(msg)),
  });

  // 一点一点接收电脑大脑的回复
  for await (const chunk of response.chunkStream) {
    // 取出这一小段文字（如果有的话）
    const newText = chunk.choices[0].delta.content || '';

    // 如果有新文字，就发给读文字的工具
    if (newText !== '') {
      sendPayload({
        'xi-api-key': voiceApiKey.value,
        text: newText,
      });
    }

    // 把新文字加到助手的消息里，让用户能看到
    assistantMessage.content += newText;
  }

  // 告诉读文字的工具，话说完了
  sendPayload({
    'xi-api-key': voiceApiKey.value,
    'text': '',
  });
}
```
### 伪代码

```plaintext
做一个发消息的事情:
  要是没有听声音的工具, 就弄一个
  
  准备一个助手的空消息
  把用户说的话记下来
  把助手的空消息也记下来
  
  把消息发给电脑, 等回复
  
  电脑一点一点回消息:
    拿到新的小段落文字
    要是有新文字, 就让读文字的工具读出来
    把新文字加到助手的消息里, 让大家看见
  
  告诉读文字的工具: 说完啦

```

```plaintext
下面是这段Tauri命令代码的"婴儿伪代码"解释，用简单易懂的方式描述其功能：

1. 定义了一个叫ipc_audio_transcription的工具
2. 这个工具需要三个东西：
   - 应用程序的控制权
   - 一段音频数据（像小积木一样的声音片段）
   - 可选的语言设置（比如告诉它是中文还是英文）

3. 工作步骤：
   - 首先说一声"开始处理音频啦"
   - 拿到之前准备好的Whisper模型处理器
   - 设定转录的配置（比如指定用什么语言）
   - 把音频片段交给处理器进行转换
   - 如果成功，就返回转换好的文字
   - 如果失败，就告诉我们哪里出错了

简单说，这个工具就像一个会听声音的小机器人，你给它一段声音，它就能把听到的内容写成文字给你。
```

---
## `composables` 和 `components`

在前端框架（尤其是Vue）的组件库设计中，`composables` 和 `components` 是两种不同的代码组织方式，分别承担不同的功能角色，以你提到的 `@proj-airi/stage-ui` 为例：

### 1. `components`（组件）：可视化UI元素

`components` 目录下的 `AudioSpectrum` 是**实际的UI组件**，它是一个可以直接在模板中使用的可视化元素，包含了具体的HTML结构、样式和基础交互逻辑。

- **作用**：负责“展示”和基础“交互界面”。比如 `AudioSpectrum` 可能是一个能在页面上显示音频频谱波形的可视化组件（有自己的DOM结构、颜色、动画等）。

- **使用方式**：在模板中像标签一样引用，例如：

```vue

<template>

<!-- 直接使用组件展示频谱 -->

<AudioSpectrum />

</template>

```

- **特点**：是“看得见”的UI单元，专注于呈现和基础用户交互（如点击、拖拽等）。

### 2. `composables`（组合式函数）：逻辑复用工具

`composables` 目录下的 `useAudioSpectrum` 是**组合式函数**（通常以 `use` 开头命名），它封装了与“音频频谱”相关的**业务逻辑、数据处理或功能方法**，但不包含UI展示。

- **作用**：负责“逻辑处理”和“数据提供”。比如 `useAudioSpectrum` 可能包含：

- 音频数据的采集、解析（如何从音频中提取频谱数据）；

- 频谱数据的处理（如降噪、格式化）；

- 相关的工具方法（如启动/停止监听音频、调整频谱灵敏度等）。

- **使用方式**：在组件的逻辑部分（如 `setup` 或 `<script setup>`）中调用，获取它提供的数据或方法，再传递给UI组件使用：

```vue

<script setup>

// 引入逻辑处理函数

import { useAudioSpectrum } from '@proj-airi/stage-ui/composables'

// 调用函数获取数据和方法

const { spectrumData, startListening } = useAudioSpectrum()

// 启动音频监听，获取频谱数据

startListening()

</script>

<template>

<!-- 将处理后的数据传给UI组件展示 -->

<AudioSpectrum :data="spectrumData" />

</template>

```

- **特点**：是“看不见”的逻辑单元，专注于数据处理和功能实现，方便在多个组件间复用相同的逻辑。

### 总结：核心区别

| 维度   | `components`（组件）        | `composables`（组合式函数）  |
| ---- | ----------------------- | --------------------- |
| 本质   | 可视化UI元素（带HTML/CSS/基础交互） | 逻辑封装工具（纯JavaScript逻辑） |
| 作用   | 负责“展示”和“界面交互”           | 负责“数据处理”和“功能逻辑”       |
| 使用场景 | 直接在模板中渲染                | 在组件逻辑中调用，提供数据/方法      |
| 设计目的 | 复用UI结构和样式               | 复用业务逻辑和数据处理逻辑         |

简单说：`components` 是“画出来的东西”，`composables` 是“让东西动起来/工作起来的逻辑”，两者常配合使用——用组合式函数处理数据，再交给组件展示。

---


```vue
<script setup lang="ts">
import { useAudioSpectrum } from '@proj-airi/stage-ui/composables'
import { AudioSpectrum } from '@proj-airi/stage-ui/components'
 
const { audioData, isRecording } = useAudioSpectrum()
</script>
 
<template>
  <AudioSpectrum :data="audioData" :active="isRecording" />
</template>
```

这段代码是一个使用Vue 3的`<script setup>`语法编写的组件，主要功能是展示音频频谱。让我们逐步解析它的工作原理：

### 代码解析

1. **引入依赖**：

- 从组件库导入了`useAudioSpectrum`组合式函数（逻辑处理）

- 导入了`AudioSpectrum`组件（UI展示）

2. **使用组合式函数**：

```typescript

const { audioData, isRecording } = useAudioSpectrum()

```

这行代码调用了`useAudioSpectrum`函数，获取了两个关键数据：

- `audioData`：音频频谱的原始数据（可能是一组表示不同频率音量的数值）

- `isRecording`：一个布尔值，表示当前是否正在录制音频

3. **模板渲染**：

```html

<AudioSpectrum :data="audioData" :active="isRecording" />

```

这里将获取到的数据传递给`AudioSpectrum`组件：

- `:data="audioData"`：将音频频谱数据传给组件，用于绘制频谱图形

- `:active="isRecording"`：根据录音状态控制频谱是否激活（可能影响动画效果或显示状态）

### 工作流程

1. `useAudioSpectrum`负责处理音频相关的逻辑（如录音、音频分析等）

2. 它会实时生成`audioData`（频谱数据）和`isRecording`（录音状态）

3. `AudioSpectrum`组件接收这些数据，将其可视化（可能以柱状图、波形图等形式展示）

4. 当`isRecording`为`true`时，频谱会实时响应声音变化；为`false`时可能静止或隐藏

这种分离方式体现了Vue的最佳实践：组合式函数处理数据逻辑，UI组件专注于展示，使代码更清晰、可维护。

---
## Leantime “精益（Lean）”理念
Leantime中的“lean”很可能源自“精益（Lean）”理念，通常表示“精简的、高效率的”。 “精益”理念最早由丰田汽车公司提出，强调通过消除流程中的浪费和优化资源配置，以最少的投入实现最大的产出。Leantime作为项目管理系统，可能旨在借鉴这一理念，打造精简、高效的项目管理流程，帮助用户以更高效的方式完成工作任务，减少不必要的操作和时间浪费，就如同“精益生产”追求生产过程的高效与优化一样。


## 画布模块：战略规划工具

除了核心实体，Leantime 还包含多个**画布模块**，提供专门的战略规划工具。每种画布类型都有自己的数据模型，针对特定方法量身定制：

- **Leancanvas**：精益创业方法
- **Goalcanvas**：目标设定和跟踪
- **Retrospectives**：敏捷回顾会议
- **SWOT**：优势、劣势、机会、威胁分析
- **Valuecanvas**：价值主张设计
- **Strategy**：战略规划
