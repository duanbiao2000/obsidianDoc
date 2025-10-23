# React教程辅助测试：面向大四学生的AI前端开发评估

## 目标
评估学生对React核心概念（组件、Hooks、状态管理、Next.js）的掌握情况，以及构建AI前端应用的能力。测试结合理论和实践，适合有JavaScript基础的大四学生，强调交互式UI和AI集成。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. React的核心优势是：  
   A. 内置数据库支持  
   B. 组件化开发与虚拟DOM  
   C. 自动API生成  
   D. 异步编程  
   **答案**：B

2. Hooks的主要作用是：  
   A. 管理全局状态  
   B. 增强函数组件功能  
   C. 渲染服务端页面  
   D. 处理HTTP请求  
   **答案**：B

3. Next.js的主要特性是：  
   A. 实时通信  
   B. 服务端渲染（SSR）  
   C. 数据库管理  
   D. 中间件处理  
   **答案**：B

4. 以下哪个Hook用于处理副作用？  
   A. useState  
   B. useEffect  
   C. useContext  
   D. useReducer  
   **答案**：B

5. 生产部署React的推荐平台是：  
   A. Postman  
   B. Vercel  
   C. Uvicorn  
   D. PM2  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释React组件和Hooks的区别，并说明在AI前端（如聊天界面）中的应用。  
   **参考答案**：  
   - **区别**：组件是UI的模块化单元，处理渲染；Hooks（如`useState`、`useEffect`）增强函数组件，管理状态和副作用。  
   - **AI应用**：组件渲染聊天输入框，Hooks调用AI API（如Hugging Face）并显示预测结果。  
   - **评分点**：清晰对比两者，提及AI场景。

2. **问题**：描述Next.js的API路由功能，并说明如何避免技术债务。  
   **参考答案**：  
   - **功能**：Next.js的`pages/api/`定义后端端点，代理AI API或处理数据。  
   - **技术债务**：避免硬编码逻辑，分离API到模块，定期更新依赖。  
   - **评分点**：准确描述API路由，提到模块化和依赖管理。

---

## 第3部分：编程题（70分）

### 编程题1：组件与Hooks（30分）
- **任务**：编写React应用，包含：
  - 输入表单组件，接受用户文本。
  - 使用`useState`和`useEffect`调用模拟API，返回情感预测。
- **要求**：
  - 处理空输入错误。
  - 显示预测结果。
- **参考代码**：
  ```javascript
  import { useState, useEffect } from 'react';
<!--ID: 1761111104196-->


  function PredictionForm() {
      const [text, setText] = useState('');
      const [result, setResult] = useState(null);

      useEffect(() => {
          if (text) {
              const prediction = text.includes('好') ? '正面' : '负面';
              setResult({ prediction });
          }
      }, [text]);

      return (
          <div>
              <input
                  type="text"
                  value={text}
                  onChange={e => setText(e.target.value)}
                  placeholder="输入文本"
              />
              {result && <p>预测：{result.prediction}</p>}
              <style jsx>{`
                  div { font-family: Arial; margin: 40px; }
                  input { padding: 8px; width: 300px; }
              `}</style>
          </div>
      );
  }

  export default PredictionForm;
  ```
- **评分标准**：
  - 组件功能（10分）：正确渲染表单。
  - Hooks使用（10分）：`useState`和`useEffect`正常。
  - 错误处理（5分）：处理空输入。
  - 代码结构（5分）：清晰、可读。

### 编程题2：Next.js与AI集成（40分）
- **任务**：构建Next.js应用，包含：
  - 前端页面，接受用户输入。
  - API路由，调用Hugging Face API。
  - 显示预测结果。
- **要求**：
  - 使用`useState`和`axios`。
  - 处理错误（如无效输入）。
- **参考代码**：
  ```javascript
  // pages/index.js
  import { useState } from 'react';
  import axios from 'axios';
<!--ID: 1761111104202-->


  export default function Home() {
      const [text, setText] = useState('');
      const [result, setResult] = useState(null);

      const predict = async () => {
          try {
              if (!text) throw new Error('Text is required');
              const res = await axios.post('/api/predict', { text });
              setResult(res.data);
          } catch (err) {
              setResult({ error: err.message });
          }
      };

      return (
          <div>
              <h1>情感分析应用</h1>
              <input
                  type="text"
                  value={text}
                  onChange={e => setText(e.target.value)}
                  placeholder="输入文本"
              />
              <button onClick={predict}>预测</button>
              {result && <p>预测：{result.label || result.error} (置信度：{result.score?.toFixed(2)})</p>}
              <style jsx>{`
                  div { font-family: Arial; margin: 40px; }
                  input { padding: 8px; width: 300px; }
                  button { padding: 8px 16px; background: #007bff; color: white; }
              `}</style>
          </div>
      );
  }
  ```
  ```javascript
  // pages/api/predict.js
  export default async function handler(req, res) {
      if (req.method === 'POST') {
          try {
              const { text } = req.body;
              if (!text) throw new Error('Text is required');
              const response = await fetch('https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english', {
                  method: 'POST',
                  headers: { Authorization: 'Bearer YOUR_HF_TOKEN' },
                  body: JSON.stringify({ inputs: text })
              });
              const result = await response.json();
              res.json(result[0]);
          } catch (error) {
              res.status(400).json({ error: error.message });
          }
      } else {
          res.status(405).json({ error: 'Method not allowed' });
      }
  }
  ```
- **评分标准**：
  - Next.js页面（10分）：正确渲染。
  - API集成（15分）：Hugging Face API工作。
  - 错误处理（10分）：处理无效输入。
  - 代码结构（5分）：清晰、注释完善。
<!--ID: 1761111104218-->


---

## 注意事项
- **提交**：提交项目文件夹（包含`pages/`、`public/`、`package.json`）。
- **测试环境**：Node.js 16+，安装`next`、`react`、`axios`。
- **建议**：记录调试过程（如你的`notebooklm.google.com`习惯），便于优化组件设计。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估开发能力，强调AI前端集成。
- **反直觉洞察**：React适合复杂UI，但小型AI应用可先用简单组件，逐步引入Next.js。