# Vue.js教材：面向大四学生的轻量AI前端开发

## 目标
本教材帮助大四学生掌握**Vue.js**，用于开发轻量级AI前端，重点涵盖组件化开发、Pinia状态管理和后端API集成，结合Hugging Face模型的推理结果展示，构建高效、适合小型项目的AI前端。教材详尽、实用，适合有JavaScript基础的学生，强调Vue.js的简洁性，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉JavaScript和AI/ML入门。
- **先修知识**：JavaScript（ES6+）、HTML/CSS、REST API、JSON。
- **工具**：Vue.js 3、Node.js 18+、npm、VS Code、Git、Postman、Docker。
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：Vue.js简介

### 1.1 为什么选择Vue.js？
- **优点**：
  - **轻量**：构建快速，适合小型项目。
  - **响应式**：数据驱动视图更新。
  - **AI集成**：展示Hugging Face推理结果。
- **缺点**：
  - 生态较React小。
  - 大型项目需额外规划。
- **适用场景**：AI前端展示、快速原型、单页应用。
- **反直觉洞察**：Vue.js虽简单，但在小型AI项目中可通过Pinia和Vite实现企业级功能。

### 1.2 初始化项目
- **安装**：
  ```bash
  npm create vue@latest
  ```
- **运行**：
  ```bash
  npm install
  npm run dev
  ```
- **示例**：
  ```vue
  <!-- App.vue -->
  <template>
    <h1>Hello, Vue.js!</h1>
  </template>
  ```
- **实践**：初始化项目，运行Hello World。

---

## 第2章：组件化开发

### 2.1 组件创建
- **示例**（`src/components/SentimentInput.vue`）：
  ```vue
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

### 2.2 组件复用
- **父组件**（`src/App.vue`）：
  ```vue
  <template>
    <SentimentInput @predict="handlePredict" />
    <p>{{ result }}</p>
  </template>

  <script>
  import SentimentInput from './components/SentimentInput.vue';

  export default {
    components: { SentimentInput },
    data() {
      return { result: '' };
    },
    methods: {
      handlePredict(text) {
        this.result = `Predicting: ${text}`;
      }
    }
  };
  </script>
  ```

### 2.3 实践
- **任务**：开发情感分析输入组件。
- **测试**：输入“I love AI!”，确认事件触发。

---

## 第3章：状态管理与API集成

### 3.1 Pinia状态管理
- **安装**：
  ```bash
  npm install pinia
  ```
- **Store**（`src/stores/sentiment.js`）：
  ```javascript
  import { defineStore } from 'pinia';
  import axios from 'axios';

  export const useSentimentStore = defineStore('sentiment', {
    state: () => ({
      predictions: []
    }),
    actions: {
      async predict(text) {
        const response = await axios.get('http://localhost:8000/predict', { params: { text } });
        this.predictions.push({ text, ...response.data });
      }
    }
  });
  ```

### 3.2 API集成
- **组件**（`src/App.vue`）：
  ```vue
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

### 3.3 实践
- **任务**：集成FastAPI情感分析端点。
- **后端**（`backend/app.py`）：
  ```python
  from fastapi import FastAPI
  from transformers import pipeline

  app = FastAPI()
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.get("/predict")
  def predict(text: str):
      result = classifier(text)[0]
      return {"label": result['label'], "score": result['score']}
  ```
- **测试**：访问`http://localhost:8080`，输入“I love AI!”，确认结果显示。

---

## 第4章：Docker与部署

### 4.1 Dockerfile
- **示例**：
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

### 4.2 Docker Compose
- **示例**（`docker-compose.yml`）：
  ```yaml
  version: '3.8'
  services:
    frontend:
      build: .
      ports:
        - "8080:80"
      depends_on:
        - backend
    backend:
      build: ./backend
      ports:
        - "8000:8000"
  ```

### 4.3 实践
- **任务**：容器化Vue.js前端。
- **运行**：
  ```bash
  docker-compose up
  ```
- **测试**：访问`http://localhost:8080`，确认前端运行。

---

## 第5章：集成AI前端管道

### 5.1 代码管理
- **GitHub**：
  ```bash
  git add .
  git commit -m "Add Vue.js sentiment frontend"
  git push origin main
  ```

### 5.2 CI/CD
- **GitHub Actions**（`.github/workflows/ci.yml`）：
  ```yaml
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

### 5.3 实践
- **任务**：配置CI/CD，推送镜像。
- **测试**：确认镜像在`ghcr.io/coleam00/sentiment-frontend`。

---

## 第6章：迷你项目——AI情感分析前端

### 6.1 项目目标
构建Vue.js AI前端，包含：
- 组件：输入框、结果展示。
- API：调用FastAPI情感分析端点。
- 部署：Docker+GitHub Actions。

### 6.2 项目结构
```
sentiment-frontend/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
├── src/
│   ├── components/
│   │   ├── SentimentInput.vue
│   ├── stores/
│   │   ├── sentiment.js
│   ├── App.vue
├── backend/
│   ├── app.py
│   ├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── package.json
```

### 6.3 实现
- **输入组件**（`src/components/SentimentInput.vue`）：
  ```vue
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
- **主组件**（`src/App.vue`）：
  ```vue
  <template>
    <SentimentInput @predict="predict" />
    <ul>
      <li v-for="pred in sentimentStore.predictions" :key="pred.text">
        {{ pred.text }}: {{ pred.label }} ({{ pred.score }})
      </li>
    </ul>
  </template>
<!--ID: 1761111103730-->


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
- **Store**（`src/stores/sentiment.js`）：
  ```javascript
  import { defineStore } from 'pinia';
  import axios from 'axios';
<!--ID: 1761111103736-->


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
- **后端**（`backend/app.py`）：
  ```python
  from fastapi import FastAPI
  from transformers import pipeline
<!--ID: 1761111103757-->


  app = FastAPI()
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.get("/predict")
  def predict(text: str):
      result = classifier(text)[0]
      return {"label": result['label'], "score": result['score']}
  ```
- **依赖**（`package.json`）：
  ```json
  {
    "dependencies": {
      "vue": "^3.2.0",
      "pinia": "^2.0.0",
      "axios": "^1.6.0"
    }
  }
  ```
- **后端依赖**（`backend/requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  torch==2.1.0
  ```
<!--ID: 1761111103776-->


### 6.4 测试
- **运行**：
  ```bash
  npm install
  docker-compose up
  ```
- **测试**：访问`http://localhost:8080`，输入“I love AI!”，确认结果显示。

---

## 第7章：优化与进阶

### 7.1 优化
- **懒加载**：
  ```javascript
  const SentimentInput = defineAsyncComponent(() => import('./components/SentimentInput.vue'));
  ```
- **性能监控**：Vue Devtools。

### 7.2 进阶
- **Neo4j**：展示关系数据（如你的兴趣）。
- **Vite**：更快构建工具。
- **TypeScript**：增强类型安全。

### 7.3 实践
- **任务**：添加懒加载，监控加载时间。
- **测试**：比较优化前后性能。

---

## 资源
- **官方文档**：[Vue.js](https://vuejs.org/guide/introduction.html)、[Pinia](https://pinia.vuejs.org/)
- **教程**：Vue Mastery、Vue.js官方教程
- **工具**：VS Code、GitHub、Jira、Obsidian、Node.js
- **建议**：用`notebooklm.google.com`记录开发流程，结合Obsidian或Jira优化任务管理。