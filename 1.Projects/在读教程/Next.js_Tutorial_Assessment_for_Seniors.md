# Next.js教程辅助测试：面向大四学生的AI前端开发评估

## 目标
评估学生对Next.js核心概念（页面开发、API集成、部署）的掌握情况，以及构建高效AI前端的能力。测试结合理论和实践，适合有JavaScript基础的大四学生，强调简化React生态的开发效率。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Next.js的主要优势是：  
   A. 数据分析  
   B. 零配置与SSR  
   C. 数据库管理  
   D. 模型训练  
   **答案**：B

2. Next.js的API路由位于：  
   A. app/components  
   B. app/api  
   C. pages/api  
   D. public/api  
   **答案**：B

3. React Query用于：  
   A. 页面路由  
   B. 数据获取与缓存  
   C. 容器化  
   D. 图像优化  
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

1. **问题**：解释Next.js SSR的优势，并说明在AI前端中的应用。  
   **参考答案**：  
   - **优势**：提升SEO，预渲染内容，加速首屏加载。  
   - **AI应用**：快速展示情感分析结果，优化用户体验。  
   - **评分点**：清晰描述优势，提及AI场景。

2. **问题**：描述Next.js API路由的作用，并说明如何避免技术债务。  
   **参考答案**：  
   - **作用**：创建后端端点，简化前后端集成。  
   - **技术债务**：规范化路由，添加测试，优化性能。  
   - **评分点**：准确描述作用，提到技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：页面与组件开发（30分）
- **任务**：编写Next.js页面：
  - 页面：`/health`显示健康状态。
  - 组件：HealthCheck输入框。
- **要求**：
  - 使用客户端组件。
  - 验证输入触发。
- **参考代码**：
  ```javascript
  // app/components/HealthCheck.js
  "use client";

  import { useState } from "react";

  export default function HealthCheck({ onCheck }) {
    const [text, setText] = useState("");

    return (
      <div>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text"
        />
        <button onClick={() => onCheck(text)}>Check</button>
      </div>
    );
  }
  ```
  ```javascript
  // app/health/page.js
  import HealthCheck from "../components/HealthCheck";

  export default function Health() {
    const handleCheck = (text) => {
      alert(`Checking: ${text}`);
    };

    return (
      <div>
        <h1>Health Check</h1>
        <HealthCheck onCheck={handleCheck} />
      </div>
    );
  }
  ```
- **测试**：
  ```bash
  npm run dev
  ```
- **评分标准**：
  - 页面开发（10分）：正确定义路由。
  - 组件实现（10分）：触发与显示正常。
  - 代码结构（5分）：清晰、可读。
  - 测试验证（5分）：功能运行正常。

### 编程题2：API集成与Docker（40分）
- **任务**：构建Next.js AI情感分析前端：
  - 页面：`/sentiment`展示预测结果。
  - API：调用FastAPI端点。
  - Docker：容器化前端。
- **要求**：
  - 使用React Query。
  - 处理API调用错误。
- **参考 code**：
  ```javascript
  // app/sentiment/page.js
  import SentimentInput from "../components/SentimentInput";
  import { useQuery } from "@tanstack/react-query";

  async function fetchSentiment(text) {
    const response = await fetch(`http://localhost:8000/predict?text=${encodeURIComponent(text)}`);
    if (!response.ok) throw new Error("API error");
    return response.json();
  }

  export default function Sentiment() {
    const [text, setText] = React.useState("");
    const { data, error, refetch } = useQuery({
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
        {error && <p>Error: {error.message}</p>}
        {data && <p>{data.label} ({data.score})</p>}
      </div>
    );
  }
  ```
  ```javascript
  // app/components/SentimentInput.js
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
  curl http://localhost:3000/sentiment
  ```
- **评分标准**：
  - API集成（15分）：正确调用FastAPI。
  - React Query（10分）：数据获取与错误处理正常。
  - Docker配置（10分）：容器化成功。
  - CI/CD配置（5分）：自动化运行正常。

---

## 注意事项
- **提交**：提交项目文件夹（包含`app/`、`Dockerfile`、`.github/workflows/`、`backend/`）。
- **测试环境**：Node.js 18+、Docker、Python 3.9+，安装`next`、`@tanstack/react-query`、`fastapi`、`transformers`.
- **建议**：用`notebooklm.google.com`记录开发流程，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估AI前端开发能力，强调效率与集成。
- **反直觉洞察**：Next.js通过零配置和SSR大幅简化React开发，让AI开发者聚焦核心功能。