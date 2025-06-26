# Vue.js教程辅助测试：面向大四学生的轻量AI前端开发评估

## 目标
评估学生对Vue.js核心概念（组件化、Pinia、API集成）的掌握情况，以及开发轻量AI前端的能力。测试结合理论和实践，适合有JavaScript基础的大四学生，强调快速开发与小型项目适用性。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Vue.js的主要优势是：  
   A. 数据分析  
   B. 轻量与响应式  
   C. 数据库管理  
   D. 模型训练  
   **答案**：B

2. Pinia用于：  
   A. 组件开发  
   B. 状态管理  
   C. API调用  
   D. 容器化  
   **答案**：B

3. v-bind用于：  
   A. 条件渲染  
   B. 数据绑定  
   C. 事件处理  
   D. 循环渲染  
   **答案**：B

4. Dockerfile的EXPOSE指令用于：  
   A. 安装依赖  
   B. 声明端口  
   C. 复制文件  
   D. 构建镜像  
   **答案**：B

5. GitHub Actions主要用于：  
   A. 代码托管  
   B. CI/CD自动化  
   C. 数据存储  
   D. 模型推理  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Vue.js组件化的优势，并说明在AI前端中的应用。  
   **参考答案**：  
   - **优势**：模块化、可复用、易维护。  
   - **AI应用**：输入组件与结果展示组件分离，提升开发效率。  
   - **评分点**：清晰描述优势，提及AI场景。

2. **问题**：描述Pinia与Axios在Vue.js中的作用，并说明如何避免技术债务。  
   **参考答案**：  
   - **作用**：Pinia管理状态，Axios调用API。  
   - **技术债务**：规范化Store，优化API调用，自动化测试。  
   - **评分点**：准确描述作用，提到技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：组件开发（30分）
- **任务**：编写Vue.js组件：
  - 输入框组件：触发predict事件。
  - 主组件：显示输入文本。
- **要求**：
  - 使用v-model绑定。
  - 验证事件触发。
- **参考代码**：
  ```vue
  <!-- src/components/Input.vue -->
  <template>
    <div>
      <input v-model="text" placeholder="Enter text" />
      <button @click="$emit('predict', text)">Predict</button>
    </div>
  </template>

  <script>
  export default {
    data() {
      return { text: '' };
    }
  };
  </script>
  ```
  ```vue
  <!-- src/App.vue -->
  <template>
    <Input @predict="handlePredict" />
    <p>{{ result }}</p>
  </template>

  <script>
  import Input from './components/Input.vue';

  export default {
    components: { Input },
    data() {
      return { result: '' };
    },
    methods: {
      handlePredict(text) {
        this.result = `Input: ${text}`;
      }
    }
  };
  </script>
  ```
- **测试**：
  ```bash
  npm run dev
  ```
- **评分标准**：
  - 组件开发（10分）：正确实现输入组件。
  - 事件处理（10分）：触发与显示正常。
  - 代码结构（5分）：清晰、可读。
  - 测试验证（5分）：功能运行正常。

### 编程题2：API集成与Docker（40分）
- **任务**：构建Vue.js AI情感分析前端：
  - Pinia：存储预测结果。
  - Axios：调用FastAPI端点。
  - Docker：容器化前端。
- **要求**：
  - 处理API调用错误。
  - 配置GitHub Actions。
- **参考 code**：
  ```vue
  <!-- src/App.vue -->
  <template>
    <SentimentInput @predict="predict" />
    <ul>
      <li v-for="pred in sentimentStore.predictions" :key="pred.text">
        {{ pred.text }}: {{ pred.label }} ({{ pred.score }})
      </li>
    </ul>
  </template>

  <script>
  import { useSentimentStore } from './stores/sentiment';
  import SentimentInput from './components/SentimentInput.vue';

  export default {
    components: { SentimentInput },
    setup() {
      const sentimentStore = useSentimentStore();
      return { sentimentStore };
    },
    methods: {
      async predict(text) {
        await this.sentimentStore.predict(text);
      }
    }
  };
  </script>
  ```
  ```javascript
  // src/stores/sentiment.js
  import { defineStore } from 'pinia';
  import axios from 'axios';

  export const useSentimentStore = defineStore('sentiment', {
    state: () => ({
      predictions: []
    }),
    actions: {
      async predict(text) {
        try {
          const response = await axios.get('http://localhost:8000/predict', { params: { text } });
          this.predictions.push({ text, ...response.data });
        } catch (error) {
          console.error('API error:', error);
        }
      }
    }
  });
  ```
  ```dockerfile
  FROM node:18
  WORKDIR /app
  COPY package*.json ./
  RUN npm install
  COPY . .
  RUN npm run build
  FROM nginx:alpine
  COPY --from=0 /app/dist /usr/share/nginx/html
  EXPOSE 80
  CMD ["nginx", "-g", "daemon off;"]
  ```
  ```yaml
  # .github/workflows/ci.yml
  name: CI/CD
  on: [push]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v3
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      - name: Install dependencies
        run: npm install
      - name: Build
        run: npm run build
      - name: Build Docker image
        run: docker build -t ghcr.io/coleam00/sentiment-frontend:latest .
      - name: Push to GitHub Packages
        run: |
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/coleam00/sentiment-frontend:latest
  ```
- **测试**：
  ```bash
  docker-compose up
  curl http://localhost:8080
  ```
- **评分标准**：
  - Pinia与API（15分）：状态管理和调用正常。
  - Docker配置（10分）：容器化成功。
  - Actions配置（10分）：CI/CD运行正常。
  - 错误处理（5分）：处理API错误。

---

## 注意事项
- **提交**：提交项目文件夹（包含`src/`、`Dockerfile`、`.github/workflows/`、`backend/`）。
- **测试环境**：Node.js 18+、Docker、Python 3.9+，安装`vue`、`pinia`、`axios`、`fastapi`、`transformers`。
- **建议**：用`notebooklm.google.com`记录开发流程，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估AI前端开发能力，强调轻量与集成。
- **反直觉洞察**：Vue.js虽轻量，但在小型AI项目中通过Pinia和Vite可实现高性能与企业级功能。