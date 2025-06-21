# Git与GitHub教程辅助测试：面向大四学生的AI项目版本控制与协作评估

## 目标
评估学生对Git和GitHub核心概念（分支管理、PR、Actions）的掌握情况，以及AI项目协作能力。测试结合理论和实践，适合有Python基础的大四学生，强调开源与自动化。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Git的主要功能是：  
   A. 项目管理  
   B. 版本控制  
   C. 数据分析  
   D. UI设计  
   **答案**：B

2. GitHub PR用于：  
   A. 自动部署  
   B. 代码审查  
   C. 数据存储  
   D. 模型训练  
   **答案**：B

3. GitHub Actions运行在：  
   A. 本地机器  
   B. 云端虚拟机  
   C. 数据库  
   D. 浏览器  
   **答案**：B

4. 分支合并可能导致：  
   A. 数据丢失  
   B. 冲突  
   C. 权限错误  
   D. 网络故障  
   **答案**：B

5. 以下哪个工具用于自动化依赖更新？  
   A. GitHub Issues  
   B. Dependabot  
   C. GitHub Pages  
   D. GitHub CLI  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Git分支和PR的区别，并说明在AI项目中的应用。  
   **参考答案**：  
   - **区别**：分支用于并行开发，PR用于审查和合并代码。  
   - **AI应用**：分支开发新模型功能，PR确保代码质量。  
   - **评分点**：清晰对比，提及AI场景。

2. **问题**：描述GitHub Actions的优点，并说明如何避免技术债务。  
   **参考答案**：  
   - **优点**：自动化测试、构建、部署，提升效率。  
   - **技术债务**：规范化workflow，定期清理旧配置，监控运行时间。  
   - **评分点**：准确描述优点，提到技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：分支与PR（30分）
- **任务**：编写Git命令：
  - 创建`feature/health-endpoint`分支。
  - 添加FastAPI健康检查端点。
  - 提交PR。
- **要求**：
  - 清晰提交信息。
  - 验证PR创建。
- **参考代码**：
  ```python
  # app.py
  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/health")
  def health():
      return {"status": "healthy"}
  ```
  ```bash
  git checkout -b feature/health-endpoint
  git add app.py
  git commit -m "Add health check endpoint"
  git push origin feature/health-endpoint
  gh pr create --title "Add health endpoint" --body "Implements /health endpoint"
  ```
  ```text
  # requirements.txt
  fastapi==0.103.0
  uvicorn==0.23.2
  ```
- **评分标准**：
  - 分支创建（10分）：正确操作。
  - 代码提交（10分）：端点功能正常。
  - PR创建（5分）：描述清晰。
  - 代码结构（5分）：清晰、可读。

### 编程题2：Actions与AI项目（40分）
- **任务**：构建AI情感分析项目：
  - 配置Actions运行测试。
  - 提交PR，包含FastAPI推理端点。
- **要求**：
  - 测试覆盖推理功能。
  - 处理依赖安装错误。
- **参考 code**：
  ```python
  # app.py
  from fastapi import FastAPI
  from transformers import pipeline

  app = FastAPI()
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.get("/predict")
  def predict(text: str):
      result = classifier(text)[0]
      return {"text": text, "prediction": result['label'], "score": result['score']}
  ```
  ```python
  # tests/test_app.py
  from fastapi.testclient import TestClient
  from app import app

  client = TestClient(app)

  def test_predict():
      response = client.get("/predict?text=I love AI!")
      assert response.status_code == 200
      assert response.json()["prediction"] == "POSITIVE"
  ```
  ```yaml
  # .github/workflows/test.yml
  name: Test AI Project
  on: [push, pull_request]
  jobs:
    test:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
  ```
  ```text
  # requirements.txt
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  torch==2.1.0
  pytest==7.4.0
  ```
  ```bash
  git checkout -b feature/sentiment-api
  git add .
  git commit -m "Add sentiment analysis API"
  git push origin feature/sentiment-api
  gh pr create
  ```
- **评分标准**：
  - Actions配置（15分）：测试运行正常。
  - AI端点（15分）：推理功能正确。
  - PR提交（5分）：描述清晰。
  - 代码结构（5分）：清晰、可读。

---

## 注意事项
- **提交**：提交项目文件夹（包含`app.py`、`tests/`、`requirements.txt`、`.github/workflows/`）。
- **测试环境**：Python 3.9+，安装`fastapi`、`transformers`、`pytest`。
- **建议**：用`notebooklm.google.com`记录协作流程，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估协作与自动化能力，强调AI项目。
- **反直觉洞察**：GitHub不仅是工具，更是职业品牌与社区互动的平台。