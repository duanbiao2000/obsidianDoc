---
date: 2025-06-17 14:47
tags:
  - Domain/Creativity/Product
---

Current time is Monday, June 16, 2025 at 11:37:12 PM PDT.

太棒了！选择 `vis-network` 作为 MVP 的渲染库是一个明智的决定，它将帮助您更快地实现核心功能。

现在，让我们来规划一个 MVP (Minimum Viable Product) 的 Obsidian 插件应用，专注于实现“**LLM 生成三元组 -> vis-network 渲染到自定义代码块**”的核心流程。

### MVP 目标

1. 用户可以在 Obsidian 插件设置中输入 **Gemini API Key**。
2. 用户可以通过一个**命令或按钮**触发 LLM 调用。
3. 插件获取当前笔记内容，发送给 **Gemini Flash 2.5 API** 进行三元组提取（限定 Top 20）。
4. 插件将返回的三元组数据**格式化为 JSON 并写入**当前笔记的 `triplet-graph` 代码块。
5. 插件注册一个 **Markdown 代码块处理器**，能够解析 `triplet-graph` 代码块中的 JSON 数据。
6. 处理器使用 **`vis-network` 库**在 Obsidian 预览模式下渲染出交互式图谱。
7. 处理基本的**加载状态**和**错误提示**。

### 技术栈

- **语言：** TypeScript
- **Obsidian API：** 用于插件开发
- **网络请求：** `fetch` (浏览器原生) 或 `axios` (如果需要更高级的请求处理)
- **图谱渲染：** `vis-network` (vis.js 的网络图模块)

### MVP 实现步骤（代码骨架和关键点）

#### 1. 初始化 Obsidian 插件项目

使用 Obsidian 官方推荐的 TypeScript 模板。

Bash

```
# 假设你已经安装了 npm
git clone https://github.com/obsidianmd/obsidian-sample-plugin.git your-triplet-graph-plugin
cd your-triplet-graph-plugin
npm install
# 修改 package.json 中的 name, version 等信息
```

#### 2. 插件设置 (`settings.ts` 和 `main.ts`)

- **`settings.ts`：**

  TypeScript

  ```
  // settings.ts
  export interface TripletGraphPluginSettings {
      geminiApiKey: string;
  }

  export const DEFAULT_SETTINGS: TripletGraphPluginSettings = {
      geminiApiKey: ''
  }
  ```

- **`main.ts` (部分内容)：**

  TypeScript

  ````
  // main.ts
  import { App, Plugin, PluginSettingTab, Setting, MarkdownPostProcessorContext } from 'obsidian';
  import { TripletGraphPluginSettings, DEFAULT_SETTINGS } from './settings';
  import { Network } from 'vis-network'; // 导入 vis-network

  // 定义 LLM 返回的三元组接口
  interface Triplet {
      subject: string;
      predicate: string;
      object: string;
  }

  // 定义 vis-network 节点和边的接口 (简化版)
  interface VisNode {
      id: string;
      label: string;
  }

  interface VisEdge {
      from: string;
      to: string;
      label: string;
  }

  export default class TripletGraphPlugin extends Plugin {
      settings: TripletGraphPluginSettings;

      async onload() {
          await this.loadSettings();

          // 添加设置选项卡
          this.addSettingTab(new TripletGraphSettingTab(this.app, this));

          // 注册命令
          this.addCommand({
              id: 'generate-triplet-graph',
              name: 'Generate Triplet Graph for Current Note',
              callback: () => this.generateTripletGraph(),
          });

          // 注册自定义代码块处理器
          this.registerMarkdownCodeBlockProcessor('triplet-graph', async (source, el, ctx) => {
              // 这个处理器将在 Markdown 预览模式下被调用
              // source: 代码块内部的文本内容 (JSON字符串)
              // el: 将图谱渲染到的 HTML 元素
              // ctx: 上下文信息，如文件路径等
              console.log("Processing triplet-graph block:", source);
              try {
                  const data = JSON.parse(source);
                  if (data && Array.isArray(data.nodes) && Array.isArray(data.edges)) {
                      this.renderGraph(el, data.nodes, data.edges);
                  } else if (data && Array.isArray(data)) { // 如果 LLM 直接返回三元组数组
                      const { nodes, edges } = this.convertTripletsToVisData(data);
                      this.renderGraph(el, nodes, edges);
                  }
                   else {
                      el.createEl('p', { text: 'Invalid triplet-graph data format.' });
                  }
              } catch (e) {
                  console.error("Error parsing triplet-graph data:", e);
                  el.createEl('p', { text: 'Error rendering graph: Invalid JSON data.' });
              }
          });
      }

      async onunload() {
          console.log('unloading plugin');
      }

      async loadSettings() {
          this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
      }

      async saveSettings() {
          await this.saveData(this.settings);
      }

      // --- 核心功能方法 ---

      // 将 LLM 返回的三元组转换为 vis-network 需要的节点和边格式
      convertTripletsToVisData(triplets: Triplet[]) {
          const nodesMap = new Map<string, VisNode>();
          const edges: VisEdge[] = [];

          triplets.forEach(t => {
              // 添加主语节点
              if (!nodesMap.has(t.subject)) {
                  nodesMap.set(t.subject, { id: t.subject, label: t.subject });
              }
              // 添加宾语节点
              if (!nodesMap.has(t.object)) {
                  nodesMap.set(t.object, { id: t.object, label: t.object });
              }
              // 添加边
              edges.push({ from: t.subject, to: t.object, label: t.predicate });
          });

          return { nodes: Array.from(nodesMap.values()), edges };
      }

      // 渲染 Graph View
      renderGraph(containerEl: HTMLElement, nodes: VisNode[], edges: VisEdge[]) {
          // 确保每次渲染前清空容器，防止重复渲染
          containerEl.empty();
          // 设置容器大小，确保图谱可见
          containerEl.style.width = '100%';
          containerEl.style.height = '400px'; // 可以根据需要调整高度

          const data = {
              nodes: nodes,
              edges: edges,
          };

          const options = {
              nodes: {
                  shape: 'box', // 可以是 'dot', 'circle', 'box', 'text' 等
                  font: { multi: 'html', size: 14, color: '#333' },
                  color: {
                      border: '#2B7CE9',
                      background: '#97C2FC',
                      highlight: { border: '#2B7CE9', background: '#D2E5FF' },
                      hover: { border: '#2B7CE9', background: '#D2E5FF' }
                  }
              },
              edges: {
                  arrows: 'to', // 显示箭头
                  color: { inherit: 'from' }, // 边颜色继承自节点颜色
                  font: { multi: 'html', size: 12, color: '#333', strokeWidth: 0 },
                  smooth: {
                      enabled: true,
                      type: "dynamic",
                      roundness: 0.5
                  }
              },
              layout: {
                  // 使用力导向布局，可以调整参数
                  hierarchical: false,
                  // 具体布局选项，可以尝试'barnesHut', 'forceAtlas2Based', 'repulsion'等
                  // physics: {
                  //     enabled: true,
                  //     barnesHut: {
                  //         gravitationalConstant: -2000,
                  //         centralGravity: 0.3,
                  //         springLength: 95,
                  //         springConstant: 0.04,
                  //         damping: 0.09,
                  //         avoidOverlap: 0
                  //     }
                  // }
              },
              physics: {
                  enabled: true,
                  solver: 'barnesHut', // 默认力学模型，适合多数情况
                  barnesHut: {
                      gravitationalConstant: -2000,
                      centralGravity: 0.3,
                      springLength: 95,
                      springConstant: 0.04,
                      damping: 0.09,
                      avoidOverlap: 0 // 避免节点重叠
                  }
              },
              interaction: {
                  dragNodes: true, // 允许拖拽节点
                  zoomView: true,  // 允许缩放
                  tooltipDelay: 300, // 鼠标悬停提示延迟
                  hideEdgesOnDrag: false,
                  hideNodesOnDrag: false
              }
          };

          // 创建网络图实例
          new Network(containerEl, data, options);
      }


      // 触发 LLM 调用并更新笔记的方法
      async generateTripletGraph() {
          // 1. 获取当前活动的笔记
          const activeFile = this.app.workspace.getActiveFile();
          if (!activeFile) {
              new Notice("No active note found.");
              return;
          }

          // 2. 获取笔记内容
          const noteContent = await this.app.vault.read(activeFile);
          const noteTitle = activeFile.basename;

          // 3. 显示加载状态
          const loadingNotice = new Notice("Generating graph... Please wait.", 0); // 0 表示不自动关闭

          try {
              // 4. 调用 LLM API
              const triplets = await this.callGeminiAPI(noteTitle, noteContent);

              // 5. 将三元组数据转换为 JSON 字符串
              const graphDataJson = JSON.stringify(triplets, null, 2); // 格式化 JSON

              // 6. 查找并更新/插入代码块
              await this.updateNoteWithGraphData(activeFile, graphDataJson);

              loadingNotice.hide(); // 隐藏加载提示
              new Notice("Graph generated and updated!");

          } catch (error) {
              loadingNotice.hide();
              console.error("Error generating triplet graph:", error);
              new Notice(`Error generating graph: ${error.message}`);
          }
      }

      // 调用 Gemini API 的方法（需要实现）
      async callGeminiAPI(noteTitle: string, noteContent: string): Promise<Triplet[]> {
          if (!this.settings.geminiApiKey) {
              throw new Error("Gemini API Key is not set in plugin settings.");
          }

          // TODO: 构建适合 Gemini Flash 2.5 的 Prompt
          const prompt = `
          你是一个专业的知识图谱构建助手。你的任务是从提供的Markdown笔记内容中，提取核心概念及其之间最重要的三元组关系（主语-谓语-宾语），并根据与笔记主题的关联性进行排序。

          请严格按照以下JSON数组格式输出，并确保只输出最重要的20组关系。每组关系包含 'subject', 'predicate', 'object' 三个键。

          笔记主题: ${noteTitle}

          笔记内容:
          \`\`\`markdown
          ${noteContent}
          \`\`\`

          输出格式（JSON数组）：
          [
            {"subject": "主体", "predicate": "谓语", "object": "宾语"},
            // ...
          ]
          `;

          const API_URL = `https://generativelanguage.googleapis.com/v1beta/models/gemini-flash:generateContent?key=${this.settings.geminiApiKey}`;

          const requestBody = {
              contents: [
                  {
                      parts: [
                          { text: prompt }
                      ]
                  }
              ],
              // 可选的配置，例如温度等
              generationConfig: {
                  temperature: 0.1, // 较低的温度更适合事实提取
                  topK: 1,
                  topP: 1,
                  maxOutputTokens: 2048, // 确保有足够输出空间
              },
              safetySettings: [ // 确保安全性设置宽松，否则可能过滤内容
                  {
                      category: "HARM_CATEGORY_HATE_SPEECH",
                      threshold: "BLOCK_NONE"
                  },
                  // ... 其他类别也设为 BLOCK_NONE 或 BLOCK_LOW_AND_ABOVE 以减少过滤
              ]
          };

          const response = await fetch(API_URL, {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(requestBody),
          });

          if (!response.ok) {
              const errorText = await response.text();
              throw new Error(`API request failed: ${response.status} - ${errorText}`);
          }

          const data = await response.json();
          // 解析 LLM 返回的 JSON 字符串
          // Gemini API 返回的实际内容可能在 data.candidates[0].content.parts[0].text 中
          let llmOutputText = data?.candidates?.[0]?.content?.parts?.[0]?.text;

          if (!llmOutputText) {
              throw new Error("LLM returned empty or unexpected content.");
          }

          // 尝试从可能的 Markdown 代码块中提取 JSON
          const jsonMatch = llmOutputText.match(/```json\n([\s\S]*?)\n```/);
          if (jsonMatch && jsonMatch[1]) {
              llmOutputText = jsonMatch[1];
          } else if (llmOutputText.startsWith('[') && llmOutputText.endsWith(']')) {
              // 如果直接是JSON数组
              // do nothing
          } else {
              // 尝试清理可能的前缀或后缀，确保是有效的JSON
              llmOutputText = llmOutputText.trim();
              // 更多清理，如删除可能存在的多余字符
          }

          // 确保能解析为 Triplet[]
          const triplets: Triplet[] = JSON.parse(llmOutputText);

          // 额外的检查，确保是数组且包含正确字段
          if (!Array.isArray(triplets) || triplets.some(t => !t.subject || !t.predicate || !t.object)) {
              throw new Error("LLM returned invalid triplet format.");
          }

          // 截取前20组
          return triplets.slice(0, 20);
      }

      // 更新笔记中 triplet-graph 代码块的方法（需要实现）
      async updateNoteWithGraphData(file: TFile, graphDataJson: string) {
          let content = await this.app.vault.read(file);
          const codeBlockRegex = /```triplet-graph\n([\s\S]*?)\n```/; // 匹配现有代码块

          const newCodeBlock = `\`\`\`triplet-graph\n${graphDataJson}\n\`\`\``;

          if (content.match(codeBlockRegex)) {
              // 如果存在，则替换
              content = content.replace(codeBlockRegex, newCodeBlock);
          } else {
              // 如果不存在，则添加到笔记末尾
              content += `\n\n${newCodeBlock}`;
          }

          await this.app.vault.modify(file, content);
      }
  }

  // 设置选项卡类
  class TripletGraphSettingTab extends PluginSettingTab {
      plugin: TripletGraphPlugin;

      constructor(app: App, plugin: TripletGraphPlugin) {
          super(app, plugin);
          this.plugin = plugin;
      }

      display(): void {
          const { containerEl } = this;
          containerEl.empty();

          containerEl.createEl('h2', { text: 'Triplet Graph Settings' });

          new Setting(containerEl)
              .setName('Gemini API Key')
              .setDesc('Enter your Google Gemini API Key (e.g., AIza... ). Your note content will be sent to Google for processing.')
              .addText(text => text
                  .setPlaceholder('Enter your API Key')
                  .setValue(this.plugin.settings.geminiApiKey)
                  .onChange(async (value) => {
                      this.plugin.settings.geminiApiKey = value;
                      await this.plugin.saveSettings();
                  }));

          // 可以添加更多设置，例如默认图谱高度等
      }
  }
  ````

#### 3. 将 `vis-network` 添加到插件

1. **安装 `vis-network`：**

   Bash

   ```
   npm install vis-network @types/vis-network # 安装库和TypeScript类型定义
   ```

2. **插件 `manifest.json`：** (确保 `vis-network` 在生产环境中被打包) 默认情况下 `npm run build` 会将 `node_modules` 中的依赖打包。您不需要在 `manifest.json` 中额外声明。

#### 4. 开发和测试

1. **将项目文件夹复制到 Obsidian 的插件目录：**
   - Windows: `C:\Users\YourUsername\Documents\VaultName\.obsidian\plugins\`
   - macOS: `~/Library/Application Support/Obsidian/VaultName/.obsidian/plugins/`
   - Linux: `~/.config/obsidian/VaultName/.obsidian/plugins/`
2. **启用插件：**
   - 打开 Obsidian，进入“设置” -> “第三方插件”，找到您的插件并启用它。
3. **配置 API Key：**
   - 进入插件设置，输入您的 Gemini API Key。
4. **测试：**
   - 打开一个笔记，按下 `Ctrl+P` (或 `Cmd+P`)，搜索并运行 "Generate Triplet Graph for Current Note" 命令。
   - 观察控制台（按 `Ctrl+Shift+I` 或 `Cmd+Option+I` 打开开发者工具）是否有错误，以及笔记内容是否更新。
   - 切换到预览模式，检查图谱是否正确渲染。

### 关键注意事项和下一步完善

- **API Key 安全：** 尽管 Obsidian 会加密保存插件设置，但告知用户其数据会被发送到外部是强制性的。
- **Prompt 优化：** 上面的 Prompt 只是一个起点。您可能需要迭代优化 Prompt，以获得更准确和相关性更高的三元组。可以尝试 Few-shot 示例。
- **错误处理：** 强化 `callGeminiAPI` 和 `renderGraph` 中的错误处理，给用户提供更友好的提示。
- **图谱样式和交互：** `renderGraph` 中的 `options` 只是一个基础配置。您可以根据需求调整节点颜色、形状、边样式、布局算法等，使其更美观和易读。
- **图谱大小动态调整：** 可以根据 `containerEl` 的实际大小来初始化 `Network`，或提供设置让用户调整默认高度。
- **性能监控：** 密切关注浏览器开发者工具中的性能面板，确保渲染不会导致卡顿。
- **LLM 输出解析健壮性：** `callGeminiAPI` 中解析 `llmOutputText` 的部分可能需要更复杂的逻辑来处理 LLM 可能返回的各种非标准 JSON 格式，例如在 JSON 前后有额外文本，或者 JSON 本身不完整等。可以考虑使用 `try-catch` 配合更宽松的 JSON 解析策略。
- **测试：** 对不同长度、内容、语言的笔记进行测试。

有了这个骨架，您就可以开始着手开发了。祝您成功！
