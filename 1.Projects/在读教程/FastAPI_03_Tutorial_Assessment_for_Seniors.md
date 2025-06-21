# FastAPI教程辅助测试：面向大四学生的AI服务接口评估

## 目标
评估学生对FastAPI核心概念（RESTful API、Pydantic验证、异步编程、OpenAPI文档）的掌握情况，以及构建AI服务接口的能力。测试结合理论和实践，适合有Python基础的大四学生，强调AI场景和高性能API开发。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. FastAPI的核心性能优势来自：  
   A. 内置ORM  
   B. 异步支持  
   C. 模板渲染  
   D. 静态文件服务  
   **答案**：B

2. Pydantic的主要作用是：  
   A. 生成OpenAPI文档  
   B. 数据验证与序列化  
   C. 异步任务调度  
   D. 数据库连接  
   **答案**：B

3. 以下哪个URL用于访问FastAPI的交互式文档？  
   A. `/api`  
   B. `/docs`  
   C. `/swagger`  
   D. `/redoc`  
   **答案**：B（或D，均正确）

4. 异步编程在FastAPI中适合处理：  
   A. CPU密集任务  
   B. IO密集任务  
   C. 静态文件加载  
   D. 数据库迁移  
   **答案**：B

5. 以下哪个工具用于生产部署FastAPI？  
   A. `uvicorn --reload`  
   B. Gunicorn + Uvicorn  
   C. Jupyter Notebook  
   D. Flask  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释FastAPI的异步编程与传统同步编程的区别，并说明在AI模型推理场景中的适用性。  
   **参考答案**：  
   - **区别**：异步编程（`async def`）允许IO操作（如模型推理、数据库查询）并发执行，同步编程按顺序阻塞。  
   - **AI适用性**：异步适合IO密集的模型调用（如Hugging Face推理），提高多用户并发性能；但CPU密集任务（如训练）可能需同步。  
   - **评分点**：清晰对比异步/同步，提及AI场景。

2. **问题**：描述Pydantic在FastAPI中的作用，并说明如何通过Pydantic避免技术债务。  
   **参考答案**：  
   - **作用**：Pydantic定义数据模型，自动验证输入/输出，确保类型安全，生成OpenAPI文档。  
   - **技术债务**：过度复杂的模型增加维护成本。解决方法：定义简洁模型，分离业务逻辑，定期重构。  
   - **评分点**：准确描述Pydantic功能，提到技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：RESTful API与Pydantic（30分）
- **任务**：编写FastAPI应用，包含：
  - `/predict`端点，接受POST请求（JSON输入：`{"text": "xxx"}`），返回模拟情感预测（“正面”或“负面”）。
  - 使用Pydantic验证输入。
- **要求**：
  - 处理空输入错误。
  - 返回JSON响应。
- **参考代码**：
  ```python
  from fastapi import FastAPI, HTTPException
  from pydantic import BaseModel, Field

  app = FastAPI()

  class TextInput(BaseModel):
      text: str = Field(..., min_length=1)

  @app.post('/predict')
  async def predict(input: TextInput):
      try:
          prediction = '正面' if '好' in input.text else '负面'
          return {'prediction': prediction}
      except Exception as e:
          raise HTTPException(status_code=400, detail=str(e))
  ```
- **评分标准**：
  - 路由功能（10分）：正确处理POST请求。
  - Pydantic验证（10分）：有效验证输入。
  - 错误处理（5分）：返回400错误。
  - 代码结构（5分）：清晰、可读。

### 编程题2：异步API与AI集成（40分）
- **任务**：构建FastAPI应用，使用Hugging Face模型，提供异步情感分析API。
- **要求**：
  - 创建`/predict`异步端点，接受JSON输入。
  - 集成Hugging Face模型（`distilbert-base-uncased-finetuned-sst-2-english`）。
  - 添加OpenAPI文档注释。
  - 处理错误（如空输入）。
- **参考代码**：
  ```python
  from fastapi import FastAPI, HTTPException
  from pydantic import BaseModel, Field
  from transformers import pipeline
  import asyncio

  app = FastAPI(title='AI情感分析API', description='异步情感分析服务')

  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  class TextInput(BaseModel):
      text: str = Field(..., min_length=1, description='输入文本')

  @app.post('/predict', summary='情感预测', tags=['AI'])
  async def predict(input: TextInput):
      try:
          result = await asyncio.to_thread(classifier, input.text)
          return {'prediction': result[0]['label'], 'score': result[0]['score']}
      except Exception as e:
          raise HTTPException(status_code=400, detail=str(e))
  ```
- **评分标准**：
  - 异步实现（10分）：正确使用`async`/`await`。
  - AI集成（15分）：Hugging Face模型正常工作。
  - 文档与错误处理（10分）：OpenAPI注释和错误处理。
  - 代码结构（5分）：清晰、注释完善。

---

## 注意事项
- **提交**：提交项目文件夹（包含`main.py`、`requirements.txt`）。
- **测试环境**：Python 3.9+，安装`fastapi`、`uvicorn`、`transformers`。
- **建议**：记录调试过程（如你的`notebooklm.google.com`习惯），便于优化API设计。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估开发能力，强调异步和AI集成。
- **反直觉洞察**：FastAPI的高性能适合AI服务，但初期开发可先用同步逻辑，逐步优化异步。