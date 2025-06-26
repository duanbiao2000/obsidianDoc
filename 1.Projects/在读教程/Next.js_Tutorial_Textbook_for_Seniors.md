# Next.js教材：面向大四学生的AI前端开发

## 目标
本教材帮助大四学生掌握**Next.js**，简化React开发流程，构建高效AI前端，重点涵盖页面开发、API集成和Docker部署，结合Hugging Face模型的推理结果展示，减少配置Webpack/ESLint的复杂性。教材详尽、实用，适合有JavaScript基础的学生，强调开发效率，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉JavaScript和AI/ML入门。
- **先修知识**：JavaScript（ES6+）、HTML/CSS、React基础、REST API、JSON。
- **工具**：Next.js 14、Node.js 18+、npm、VS Code、Git、Postman、Docker.
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：Next.js简介

### 1.1 为什么选择Next.js？
- **优点**：
  - **零配置**：内置Webpack、ESLint、TypeScript支持。
  - **SSR/SSG**：提升SEO和性能。
  - **AI集成**：快速展示Hugging Face推理结果。
- **缺点**：
  - SSR增加服务器负载。
  - 学习曲线：服务端逻辑需适应。
- **适用场景**：AI前端、快速原型、SEO敏感应用。
- **反直觉洞察**：Next.js看似复杂，但其约定式开发让AI开发者省去配置精力。

### 1.2 初始化项目
- **安装**：
  ```bash
  npx create-next-app@latest sentiment-frontend
  cd sentiment-frontend
  npm run dev
  ```
- **示例**（`app/page.js`）：
  ```javascript
  export default function Home() {
    return <h1>Hello, Next.js!</h1>;
  }
  ```
- **实践**：初始化项目，运行Hello World。

---

## 第2章：页面与组件开发

### 2.1 文件系统路由
- **示例**（`app/sentiment/page.js`）：
  ```javascript
  export default function Sentiment() {
    return <h1>Sentiment Analysis</h1>;
  }
  ```

### 2.2 组件
- **客户端组件**（`app/components/SentimentInput.js`）：
  ```javascript
  "use client";

  import { useState } from "react";

  export default function SentimentInput({ onPredict }) {
    const [text, setText] = useState("");

    return (
      <div>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text"
        />
        <button onClick={() => onPredict(text)}>Predict</button>
      </div>
    );
  }
  ```

### 2.3 实践
- **任务**：开发情感分析页面。
- **代码**（`app/sentiment/page.js`）：
  ```javascript
  import SentimentInput from "../components/SentimentInput";

  export default function Sentiment() {
    const handlePredict = (text) => {
      alert(`Predicting: ${text}`);
    };

    return (
      <div>
        <h1>Sentiment Analysis</h1>
        <SentimentInput onPredict={handlePredict} />
      </div>
    );
  }
  ```
- **测试**：访问`http://localhost:3000/sentiment`，确认输入触发。

---

## 第3章：API集成与状态管理

### 3.1 API路由
- **示例**（`app/api/sentiment/route.js`）：
  ```javascript
  import { NextResponse } from "next/server";

  export async function GET(request) {
    const { searchParams } = new URL(request.url);
    const text = searchParams.get("text");
    // Mock API call
    return NextResponse.json({ label: "POSITIVE", score: 0.9 });
  }
  ```

### 3.2 React Query
- **安装**：
  ```bash
  npm install @tanstack/react-query
  ```
- **配置**（`app/_app.js`）：
  ```javascript
  import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

  const queryClient = new QueryClient();

  export default function App({ Component, pageProps }) {
    return (
      <QueryClientProvider client={queryClient}>
        <Component {...pageProps} />
      </QueryClientProvider>
    );
  }
  ```
- **使用**（`app/sentiment/page.js`）：
  ```javascript
  import SentimentInput from "../components/SentimentInput";
  import { useQuery } from "@tanstack/react-query";

  async function fetchSentiment(text) {
    const response = await fetch(`/api/sentiment?text=${encodeURIComponent(text)}`);
    return response.json();
  }

  export default function Sentiment() {
    const [text, setText] = React.useState("");
    const { data, refetch } = useQuery({
      queryKey: ["sentiment", text],
      queryFn: () => fetchSentiment(text),
      enabled: false,
    });

    const handlePredict = (input) => {
      setText(input);
      refetch();
    };

    return (
      <div>
        <h1>Sentiment Analysis</h1>
        <SentimentInput onPredict={handlePredict} />
        {data && <p>{data.label} ({data.score})</p>}
      </div>
    );
  }
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
- **测试**：访问`http://localhost:3000/sentiment`，输入“I love AI!”，确认结果显示。

---

## 第4章：Docker与部署

### 4.1 Dockerfile
- **示例**：
  ```dockerfile
  FROM node:18-alpine
  WORKDIR /app
  COPY package*.json ./
  RUN npm install
  COPY . .
  RUN npm run build
  EXPOSE 3000
  CMD ["npm", "start"]
  ```

### 4.2 Docker Compose
- **示例**（`docker-compose.yml`）：
  ```yaml
  version: '3.8'
  services:
    frontend:
      build: .
      ports:
        - "3000:3000"
      depends_on:
        - backend
    backend:
      build: ./backend
      ports:
        - "8000:8000"
  ```

### 4.3 实践
- **任务**：容器化Next.js前端。
- **运行**：
  ```bash
  docker-compose up
  ```
- **测试**：访问`http://localhost:3000`，确认前端运行。

---

## 第5章：集成AI前端管道

### 5.1 代码管理
- **GitHub**：
  ```bash
  git add .
  git commit -m "Add Next.js sentiment frontend"
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
- **测试**：确认镜像在`ghcr.io/coleam00/sentiment-frontend`.

---

## 第6章：迷你项目——AI情感分析前端

### 6.1 项目目标
构建Next.js AI前端，包含：
- 页面：输入框、结果展示。
- API：调用FastAPI情感分析端点。
- 部署：Docker+GitHub Actions.

### 6.2 项目结构
```
sentiment-frontend/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
├── app/
│   ├── api/
│   │   ├── sentiment/
│   │   │   ├── route.js
│   ├── components/
│   │   ├── SentimentInput.js
│   ├── sentiment/
│   │   ├── page.js
│   ├── _app.js
├── backend/
│   ├── app.py
│   ├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── package.json
```

### 6.3 实现
- **输入组件**（`app/components/SentimentInput.js`）：
  ```javascript
  "use client";

  import { useState } from "react";

  export default function SentimentInput({ onPredict }) {
    const [text, setText] = useState("");

    return (
      <div>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text"
        />
        <button onClick={() => onPredict(text)}>Predict</button>
      </div>
    );
  }
  ```
- **页面**（`app/sentiment/page.js`）：
  ```javascript
  import SentimentInput from "../components/SentimentInput";
  import { useQuery } from "@tanstack/react-query";

  async function fetchSentiment(text) {
    const response = await fetch(`http://localhost:8000/predict?text=${encodeURIComponent(text)}`);
    return response.json();
  }

  export default function Sentiment() {
    const [text, setText] = React.useState("");
    const { data, refetch } = useQuery({
      queryKey: ["sentiment", text],
      queryFn: () => fetchSentiment(text),
      enabled: false,
    });

    const handlePredict = (input) => {
      setText(input);
      refetch();
    };

    return (
      <div>
        <h1>Sentiment Analysis</h1>
        <SentimentInput onPredict={handlePredict} />
        {data && <p>{data.label} ({data.score})</p>}
      </div>
    );
  }
  ```
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
- **依赖**（`package.json`）：
  ```json
  {
    "dependencies": {
      "next": "^14.0.0",
      "@tanstack/react-query": "^5.0.0"
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

### 6.4 测试
- **运行**：
  ```bash
  npm install
  docker-compose up
  ```
- **测试**：访问`http://localhost:3000/sentiment`，输入“I love AI!”，确认结果显示。

---

## 第7章：优化与进阶

### 7.1 优化
- **图像优化**：
  ```javascript
  import Image from "next/image";

  export default function Sentiment() {
    return <Image src="/logo.png" alt="Logo" width={100} height={100} />;
  }
  ```
- **懒加载**：
  ```javascript
  import dynamic from "next/dynamic";

  const SentimentInput = dynamic(() => import("../components/SentimentInput"), { ssr: false });
  ```

### 7.2 进阶
- **Neo4j**：展示知识图谱数据（如你的兴趣）。
- **TypeScript**：增强类型安全。
- **Vercel**：一键部署。

### 7.3 实践
- **任务**：添加图像优化，监控加载时间。
- **测试**：比较优化前后性能。

---

## 资源
- **官方文档**：[Next.js](https://nextjs.org/docs)、[React Query](https://tanstack.com/query)
- **教程**：Next.js官方教程、Vercel文档
- **工具**：VS Code、GitHub、Jira、Obsidian、Node.js
- **建议**：用`notebooklm.google.com`记录开发流程，结合Obsidian或Jira优化任务管理。