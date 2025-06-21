# Express教材：面向大四学生的全栈AI应用开发

## 目标
本教材帮助大四学生掌握**Node.js**和**Express**，用于构建全栈AI应用，重点涵盖中间件、REST API和WebSocket，结合Hugging Face API开发实时、交互式Web服务。教材详尽、实用，适合有JavaScript基础的学生，强调快速开发和生产级部署。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉JavaScript（ES6+）和AI/ML入门。
- **先修知识**：JavaScript、HTML/CSS、HTTP、JSON。
- **工具**：Node.js 16+、npm、VS Code、Postman、Git。
- **时长**：8小时（2小时理论+6小时实践）。

---

## 第1章：Express简介

### 1.1 为什么选择Express？
- **优点**：
  - **丰富生态**：Node.js模块支持，与前端（React）无缝集成。
  - **灵活性**：中间件架构适合定制AI API。
  - **实时支持**：WebSocket适配实时AI应用（如聊天机器人）。
  - **AI集成**：易调用Hugging Face或TensorFlow.js，契合你的AI研究兴趣。
- **缺点**：
  - 异步回调复杂，需掌握Promise/async-await。
  - 缺乏内置类型检查（如FastAPI的Pydantic）。
- **适用场景**：全栈AI应用、实时服务、快速原型。
- **反直觉洞察**：Express的简单API看似“过时”，但其灵活性在全栈开发中仍具优势，特别适合与前端结合。

### 1.2 安装与第一个API
- **步骤**：
  1. 安装Node.js：确保版本16+。
  2. 初始化项目：`npm init -y`。
  3. 安装Express：`npm install express`。
  4. 创建基本API：
     ```javascript
     const express = require('express');
     const app = express();

     app.get('/', (req, res) => {
         res.json({ message: 'Hello, AI World!' });
     });

     app.listen(3000, () => console.log('Server running on port 3000'));
     ```
  5. 运行：`node app.js`，访问`http://localhost:3000`。
- **实践**：运行代码，确认返回`{"message": "Hello, AI World!"}`。

---

## 第2章：中间件

### 2.1 中间件基础
- **概念**：中间件是处理请求和响应的函数，位于路由之前。
- **示例**：
  ```javascript
  const express = require('express');
  const app = express();

  app.use((req, res, next) => {
      console.log(`${req.method} ${req.url}`);
      next();
  });

  app.get('/', (req, res) => res.json({ message: 'Hello!' }));
  ```

### 2.2 自定义中间件
- **日志中间件**：
  ```javascript
  const logger = (req, res, next) => {
      console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
      next();
  };
  app.use(logger);
  ```
- **AI用例**：验证输入：
  ```javascript
  const validateInput = (req, res, next) => {
      if (!req.body.text) {
          return res.status(400).json({ error: 'Text is required' });
      }
      next();
  };
  ```

### 2.3 实践
- 创建日志中间件，记录请求时间和URL。
- 添加验证中间件，确保POST请求包含`text`字段。
- **技术债务提示**：中间件过多可能降低性能，优先选择轻量逻辑。

---

## 第3章：REST API设计

### 3.1 路由与参数
- **基本路由**：
  ```javascript
  app.get('/welcome', (req, res) => {
      res.json({ message: '欢迎使用Express！' });
  });
  ```
- **路径参数**：
  ```javascript
  app.get('/user/:username', (req, res) => {
      res.json({ message: `你好，${req.params.username}！` });
  });
  ```
- **查询参数**：
  ```javascript
  app.get('/search', (req, res) => {
      res.json({ query: req.query.q });
  });
  ```

### 3.2 AI预测API
- **任务**：构建`/predict`端点，模拟情感分析。
  ```javascript
  app.use(express.json());

  app.post('/predict', validateInput, (req, res) => {
      const { text } = req.body;
      const prediction = text.includes('好') ? '正面' : '负面';
      res.json({ prediction });
  });
  ```
- **实践**：用Postman发送`{"text": "这很好"}`，确认返回`{"prediction": "正面"}`。

---

## 第4章：WebSocket

### 4.1 WebSocket基础
- **安装**：`npm install ws`。
- **示例**：
  ```javascript
  const WebSocket = require('ws');
  const wss = new WebSocket.Server({ port: 8080 });

  wss.on('connection', ws => {
      ws.on('message', message => {
          const text = message.toString();
          const prediction = text.includes('好') ? '正面' : '负面';
          ws.send(JSON.stringify({ prediction }));
      });
  });
  ```

### 4.2 集成到Express
- **代码**：
  ```javascript
  const express = require('express');
  const http = require('http');
  const WebSocket = require('ws');
  const app = express();
  const server = http.createServer(app);
  const wss = new WebSocket.Server({ server });

  wss.on('connection', ws => {
      ws.on('message', message => {
          const { text } = JSON.parse(message);
          const prediction = text.includes('好') ? '正面' : '负面';
          ws.send(JSON.stringify({ prediction }));
      });
  });

  server.listen(3000);
  ```
- **前端**：
  ```html
  <script>
      const ws = new WebSocket('ws://localhost:3000');
      ws.onmessage = event => {
          const data = JSON.parse(event.data);
          document.getElementById('result').innerText = `预测：${data.prediction}`;
      };
      ws.onopen = () => ws.send(JSON.stringify({ text: '这很好' }));
  </script>
  ```
- **实践**：发送WebSocket消息，确认实时返回预测。

---

## 第5章：集成AI模型

### 5.1 调用Hugging Face API
- **安装**：`npm install axios`。
- **代码**：
  ```javascript
  const express = require('express');
  const axios = require('axios');
  const app = express();
  app.use(express.json());

  app.post('/predict', async (req, res) => {
      try {
          const { text } = req.body;
          if (!text) throw new Error('Text is required');
          const response = await axios.post('https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english', 
              { inputs: text },
              { headers: { Authorization: 'Bearer YOUR_HF_TOKEN' } }
          );
          res.json(response.data[0]);
      } catch (error) {
          res.status(400).json({ error: error.message });
      }
  });

  app.listen(3000);
  ```
- **实践**：获取Hugging Face API密钥，测试`/predict`端点。

### 5.2 优化
- **缓存**：用`node-cache`缓存频繁请求。
- **错误处理**：处理API超时或无效密钥。
- **反直觉洞察**：本地模型（如TensorFlow.js）可能比云API更适合低延迟场景。

---

## 第6章：迷你项目——AI情感分析Web应用

### 6.1 项目目标
构建全栈应用，包含：
- 前端：HTML表单+WebSocket实时显示。
- 后端：Express REST API调用Hugging Face。
- 部署：本地+Heroku。

### 6.2 项目结构
```
sentiment_app/
├── app.js
├── public/
│   ├── index.html
│   └── style.css
├── package.json
└── node_modules/
```

### 6.3 实现
- **后端**（`app.js`）：
  ```javascript
  const express = require('express');
  const http = require('http');
  const WebSocket = require('ws');
  const axios = require('axios');
  const app = express();
  const server = http.createServer(app);
  const wss = new WebSocket.Server({ server });

  app.use(express.json());
  app.use(express.static('public'));

  app.post('/predict', async (req, res) => {
      try {
          const { text } = req.body;
          if (!text) throw new Error('Text is required');
          const response = await axios.post('https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english', 
              { inputs: text },
              { headers: { Authorization: 'Bearer YOUR_HF_TOKEN' } }
          );
          res.json(response.data[0]);
      } catch (error) {
          res.status(400).json({ error: error.message });
      }
  });

  wss.on('connection', ws => {
      ws.on('message', async message => {
          try {
              const { text } = JSON.parse(message);
              const response = await axios.post('https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english', 
                  { inputs: text },
                  { headers: { Authorization: 'Bearer YOUR_HF_TOKEN' } }
              );
              ws.send(JSON.stringify(response.data[0]));
          } catch (error) {
              ws.send(JSON.stringify({ error: error.message }));
          }
      });
  });

  server.listen(3000, () => console.log('Server running on port 3000'));
  ```
- **前端**（`public/index.html`）：
  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <link rel="stylesheet" href="style.css">
  </head>
  <body>
      <h1>情感分析应用</h1>
      <input type="text" id="inputText" placeholder="输入文本">
      <button onclick="sendPrediction()">预测</button>
      <p id="result"></p>
      <script>
          const ws = new WebSocket('ws://localhost:3000');
          ws.onmessage = event => {
              const data = JSON.parse(event.data);
              document.getElementById('result').innerText = `预测：${data.label} (置信度：${data.score.toFixed(2)})`;
          };
          function sendPrediction() {
              const text = document.getElementById('inputText').value;
              ws.send(JSON.stringify({ text }));
          }
      </script>
  </body>
  </html>
  ```
- **样式**（`public/style.css`）：
  ```css
  body { font-family: Arial; margin: 40px; }
  input[type=text] { padding: 8px; width: 300px; }
  button { padding: 8px 16px; background: #007bff; color: white; }
  ```
- **依赖**（`package.json`）：
  ```json
  {
      "name": "sentiment_app",
      "version": "1.0.0",
      "dependencies": {
          "express": "^4.18.2",
          "ws": "^8.13.0",
          "axios": "^1.6.0"
      },
      "scripts": {
          "start": "node app.js"
      }
  }
  ```

### 6.4 测试
- 运行：`npm start`。
- 测试：访问`http://localhost:3000`，输入“I love AI!”，确认WebSocket显示预测结果。

---

## 第7章：部署与进阶

### 7.1 部署
- **本地**：`npm start`。
- **生产**：
  - PM2：`npm install -g pm2; pm2 start app.js`。
  - Docker：
    ```dockerfile
    FROM node:16
    WORKDIR /app
    COPY . .
    RUN npm install
    CMD ["npm", "start"]
    ```
  - Heroku：推送代码，配置`Procfile`（`web: npm start`）。

### 7.2 技术债务管理
- **依赖**：用`npm list --depth=0`检查版本。
- **模块化**：分离路由到`routes/`文件夹。
- **监控**：用Winston记录日志。

### 7.3 进阶
- **前端**：结合React（如你的社交媒体分享兴趣）。
- **数据库**：集成Neo4j存储知识图谱。
- **优化**：用Redis缓存API响应。

---

## 资源
- **官方文档**：[Express](https://expressjs.com/)、[Node.js](https://nodejs.org/)
- **教程**：MDN Node.js指南、Hugging Face API文档
- **工具**：VS Code、Postman、Docker、GitHub
- **建议**：用`notebooklm.google.com`记录开发笔记，尝试XMind规划项目结构。