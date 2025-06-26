# FastAPI教材：面向大四学生的AI服务接口开发

## 目标
本教材帮助大四学生掌握**FastAPI**，一个高性能Python API框架，用于快速构建AI服务接口。教材聚焦RESTful API设计、Pydantic验证、异步编程和OpenAPI文档生成，结合Hugging Face模型开发实用AI应用。内容详尽、注重实践，适合有Python基础的学生，强调效率和生产级开发。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python（函数、类、异步基础）、HTTP、JSON。
- **工具**：Python 3.9+、pip、VS Code、Postman、Git。
- **时长**：8小时（2小时理论+6小时实践）。

---

## 第1章：FastAPI简介

### 1.1 为什么选择FastAPI？
- **优点**：
  - **高性能**：基于Starlette和Uvicorn，支持异步，性能媲美Node.js。
  - **自动文档**：内置OpenAPI（Swagger/Redoc），加速调试。
  - **类型安全**：结合Pydantic，减少运行时错误。
  - **AI集成**：与Hugging Face、PyTorch等无缝衔接，适合你的AI研究兴趣。
- **缺点**：
  - 学习曲线稍陡（需理解异步编程）。
  - 社区较新，生态不如Flask成熟。
- **适用场景**：AI模型API、实时应用、微服务。
- **反直觉洞察**：FastAPI的异步优势在IO密集任务（如模型推理）中显著，但在CPU密集任务（如复杂计算）可能不如同步框架。

### 1.2 安装与第一个API
- **步骤**：
  1. 安装：`pip install fastapi uvicorn`
  2. 创建基本API：
     ```python
     from fastapi import FastAPI
     app = FastAPI()

     @app.get('/')
     async def root():
         return {'message': 'Hello, AI World!'}
     ```
  3. 运行：`uvicorn main:app --reload`，访问`http://localhost:8000`。
- **实践**：运行代码，确认返回`{"message": "Hello, AI World!"}`。
- **访问文档**：打开`http://localhost:8000/docs`，体验Swagger UI。

---

## 第2章：RESTful API设计

### 2.1 路由基础
- **概念**：FastAPI使用装饰器定义HTTP方法（GET、POST等）。
- **示例**：
  ```python
  from fastapi import FastAPI
  app = FastAPI()

  @app.get('/welcome')
  async def welcome():
      return {'message': '欢迎使用FastAPI！'}
  ```

### 2.2 路径与查询参数
- **路径参数**：
  ```python
  @app.get('/user/{username}')
  async def greet_user(username: str):
      return {'message': f'你好，{username}！'}
  ```
- **查询参数**：
  ```python
  @app.get('/search')
  async def search(query: str):
      return {'query': query}
  ```

### 2.3 AI场景：预测API
- **任务**：构建文本预测端点。
  ```python
  @app.post('/predict')
  async def predict(text: str):
      prediction = '正面' if '好' in text else '负面'
      return {'prediction': prediction}
  ```
- **实践**：用Postman发送POST请求（`text=这很好`），验证返回`{"prediction": "正面"}`。
- **技术债务提示**：硬编码逻辑难以扩展，需引入Pydantic和AI模型。

---

## 第3章：Pydantic验证

### 3.1 Pydantic模型
- **概念**：Pydantic定义数据结构，自动验证输入/输出。
- **示例**：
  ```python
  from pydantic import BaseModel
  from fastapi import FastAPI

  app = FastAPI()

  class TextInput(BaseModel):
      text: str

  @app.post('/predict')
  async def predict(input: TextInput):
      return {'prediction': '正面' if '好' in input.text else '负面'}
  ```

### 3.2 验证与错误处理
- **验证**：Pydantic自动检查类型和非空。
  ```python
  class TextInput(BaseModel):
      text: str = Field(..., min_length=1)
  ```
- **错误处理**：
  ```python
  from fastapi import HTTPException

  @app.post('/predict')
  async def predict(input: TextInput):
      try:
          prediction = '正面' if '好' in input.text else '负面'
          return {'prediction': prediction}
      except Exception as e:
          raise HTTPException(status_code=400, detail=str(e))
  ```
- **实践**：发送空输入，确认返回400错误。

---

## 第4章：异步编程

### 4.1 异步基础
- **概念**：FastAPI基于`asyncio`，适合IO密集任务。
- **示例**：
  ```python
  import asyncio
  from fastapi import FastAPI

  app = FastAPI()

  @app.get('/delay')
  async def delay():
      await asyncio.sleep(2)  # 模拟IO延迟
      return {'message': '延迟2秒完成'}
  ```

### 4.2 异步AI调用
- **任务**：异步调用Hugging Face模型。
  ```python
  from transformers import pipeline
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.post('/predict')
  async def predict(input: TextInput):
      result = await asyncio.to_thread(classifier, input.text)
      return {'prediction': result[0]['label'], 'score': result[0]['score']}
  ```
- **实践**：测试异步端点，确认性能提升。
- **反直觉洞察**：异步在单用户场景收益有限，但在多用户高并发场景（如你的AI服务）显著。

---

## 第5章：OpenAPI文档与测试

### 5.1 自动文档
- **访问**：运行后打开`http://localhost:8000/docs`或`/redoc`。
- **自定义**：
  ```python
  app = FastAPI(title='AI情感分析API', description='高性能AI服务', version='1.0')
  ```

### 5.2 测试工具
- **Postman**：发送JSON请求测试API。
- **Swagger UI**：交互式测试端点。
- **实践**：在`/docs`测试`/predict`，验证响应。

---

## 第6章：集成AI模型

### 6.1 加载Hugging Face模型
- **安装**：`pip install transformers`
- **代码**：
  ```python
  from fastapi import FastAPI, HTTPException
  from pydantic import BaseModel
  from transformers import pipeline

  app = FastAPI()
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  class TextInput(BaseModel):
      text: str = Field(..., min_length=1)

  @app.post('/predict')
  async def predict(input: TextInput):
      try:
          result = await asyncio.to_thread(classifier, input.text)
          return {'prediction': result[0]['label'], 'score': result[0]['score']}
      except Exception as e:
          raise HTTPException(status_code=400, detail=str(e))
  ```

### 6.2 优化与错误处理
- **预加载**：在启动时加载模型，减少延迟。
- **缓存**：使用Redis缓存频繁请求结果。
- **实践**：发送`{"text": "I love AI!"}`，确认返回`{"prediction": "POSITIVE", "score": 0.99}`。

---

## 第7章：迷你项目——AI情感分析API

### 7.1 项目目标
构建一个FastAPI应用，包含：
- 前端：HTML表单输入文本。
- 后端：异步API调用Hugging Face模型。
- 文档：自动生成OpenAPI。

### 7.2 项目结构
```
sentiment_api/
├── main.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── requirements.txt
```

### 7.3 实现
- **主应用**（`main.py`）：
  ```python
  from fastapi import FastAPI, Request
  from fastapi.templating import Jinja2Templates
  from pydantic import BaseModel
  from transformers import pipeline
  import requests

  app = FastAPI(title='AI情感分析API')
  templates = Jinja2Templates(directory='templates')
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  class TextInput(BaseModel):
      text: str = Field(..., min_length=1)

  @app.get('/')
  async def index(request: Request):
      return templates.TemplateResponse('index.html', {'request': request})

  @app.post('/predict')
  async def predict(input: TextInput):
      result = await asyncio.to_thread(classifier, input.text)
      return {'prediction': result[0]['label'], 'score': result[0]['score']}

  @app.post('/')
  async def form_predict(request: Request):
      form = await request.form()
      text = form['text']
      response = requests.post('http://localhost:8000/predict', json={'text': text})
      return templates.TemplateResponse('index.html', {'request': request, 'prediction': response.json()})
  ```
- **模板**（`templates/index.html`）：
  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  </head>
  <body>
      <h1>情感分析API</h1>
      <form method="POST">
          <input type="text" name="text" placeholder="输入文本">
          <input type="submit" value="预测">
      </form>
      {% if prediction %}
          <p>预测：{{ prediction.prediction }} (置信度：{{ '%.2f' % prediction.score }})</p>
      {% endif %}
  </body>
  </html>
  ```
- **样式**（`static/style.css`）：
  ```css
  body { font-family: Arial; margin: 40px; }
  input[type=text] { padding: 8px; width: 300px; }
  input[type=submit] { padding: 8px 16px; background: #007bff; color: white; }
  ```
- **依赖**（`requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  requests==2.31.0
  jinja2==3.1.2
  ```

### 7.4 测试
- 运行：`uvicorn main:app --reload`。
- 测试：访问`http://localhost:8000`，输入“I love AI!”，确认显示“预测：POSITIVE (置信度：0.99)”。

---

## 第8章：部署与进阶

### 8.1 部署
- **本地**：`uvicorn main:app --reload`。
- **生产**：
  - Gunicorn：`gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app`。
  - Docker：
    ```dockerfile
    FROM python:3.9
    WORKDIR /app
    COPY . .
    RUN pip install -r requirements.txt
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    ```
  - Heroku：推送代码，配置`Procfile`。

### 8.2 技术债务管理
- **依赖**：用`pip freeze > requirements.txt`锁定版本。
- **模块化**：分离路由、模型逻辑到不同文件。
- **监控**：用Prometheus跟踪API性能。

### 8.3 进阶
- **前端**：结合React提升UI体验。
- **数据库**：集成Neo4j（你的兴趣）存储知识图谱。
- **缓存**：用Redis优化模型推理。

---

## 资源
- **官方文档**：[FastAPI](https://fastapi.tiangolo.com/)
- **教程**：FastAPI官方教程、Hugging Face指南
- **工具**：VS Code、Postman、Docker、GitHub
- **建议**：用`notebooklm.google.com`记录学习笔记，尝试XMind规划API结构。