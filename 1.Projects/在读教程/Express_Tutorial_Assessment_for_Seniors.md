# Express教程辅助测试：面向大四学生的全栈AI应用评估

## 目标
评估学生对Express核心概念（中间件、REST API、WebSocket）的掌握情况，以及构建全栈AI应用的能力。测试结合理论和实践，适合有JavaScript基础的大四学生，强调实时AI场景和高性能开发。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Express的主要优势是：  
   A. 内置ORM  
   B. 丰富生态与灵活性  
   C. 自动类型检查  
   D. 内置前端框架  
   **答案**：B

2. 中间件的作用是：  
   A. 渲染HTML模板  
   B. 处理请求和响应  
   C. 管理数据库连接  
   D. 调用AI模型  
   **答案**：B

3. WebSocket在Express中适合：  
   A. 静态文件服务  
   B. 实时双向通信  
   C. 数据库查询  
   D. 路由定义  
   **答案**：B

4. 以下哪个库用于Express的HTTP请求处理？  
   A. axios  
   B. ws  
   C. express  
   D. redis  
   **答案**：C

5. 生产部署Express的推荐工具是：  
   A. `node app.js`  
   B. PM2 + Nginx  
   C. Postman  
   D. TensorFlow.js  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Express中间件和WebSocket的区别，并说明在AI实时预测场景中的适用性。  
   **参考答案**：  
   - **区别**：中间件处理HTTP请求/响应（如验证、日志），WebSocket支持持久双向通信（如实时预测）。  
   - **AI适用性**：中间件验证API输入，WebSocket推送实时模型输出（如情感分析结果）。  
   - **评分点**：清晰对比两者功能，提及AI场景。

2. **问题**：描述REST API在Express中的设计原则，并说明如何避免技术债务。  
   **参考答案**：  
   - **原则**：遵循REST规范（资源导向、HTTP方法、JSON响应），确保路由清晰。  
   - **技术债务**：避免硬编码逻辑，分离路由到模块，定期更新依赖。  
   - **评分点**：准确描述REST设计，提到模块化和依赖管理。

---

## 第3部分：编程题（70分）

### 编程题1：中间件与REST API（30分）
- **任务**：编写Express应用，包含：
  - 日志中间件，记录请求时间和URL。
  - `/predict`端点，接受POST请求（JSON输入：`{"text": "xxx"}`），返回模拟情感预测。
- **要求**：
  - 处理空输入错误。
  - 返回JSON响应。
- **参考代码**：
  ```javascript
  const express = require('express');
  const app = express();
  app.use(express.json());

  const logger = (req, res, next) => {
      console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
      next();
  };

  app.use(logger);

  app.post('/predict', (req, res) => {
      const { text } = req.body;
      if (!text) return res.status(400).json({ error: 'Text is required' });
      const prediction = text.includes('好') ? '正面' : '负面';
      res.json({ prediction });
  });

  app.listen(3000);
  ```
- **评分标准**：
  - 中间件（10分）：正确记录日志。
  - REST API（10分）：处理POST请求。
  - 错误处理（5分）：返回400错误。
  - 代码结构（5分）：清晰、可读。

### 编程题2：WebSocket与AI集成（40分）
- **任务**：构建Express应用，使用WebSocket调用Hugging Face API，提供实时情感分析。
- **要求**：
  - 创建`/predict` REST端点和WebSocket端点。
  - 调用Hugging Face API（`distilbert-base-uncased-finetuned-sst-2-english`）。
  - 处理错误（如无效输入）。
- **参考 code**：
  ```javascript
  const express = require('express');
  const http = require('http');
  const WebSocket = require('ws');
  const axios = require('axios');
  const app = express();
  const server = http.createServer(app);
  const wss = new WebSocket.Server({ server });
<!--ID: 1761111104868-->


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

  wss.on('connection', ws => {
      ws.on('message', async message => {
          try {
              const { text } = JSON.parse(message);
              if (!text) throw new Error('Text is required');
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

  server.listen(3000);
  ```
- **评分标准**：
  - WebSocket（15分）：实时通信正常。
  - AI集成（15分）：Hugging Face API工作。
  - 错误处理（5分）：处理无效输入。
  - 代码结构（5分）：清晰、注释完善。

---

## 注意事项
- **提交**：提交项目文件夹（包含`app.js`、`public/`、`package.json`）。
- **测试环境**：Node.js 16+，安装`express`、`ws`、`axios`。
- **建议**：记录调试过程（如你的`notebooklm.google.com`习惯），便于优化API设计。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估开发能力，强调WebSocket和AI集成。
- **反直觉洞察**：Express适合快速全栈开发，但需谨慎管理中间件和WebSocket状态。