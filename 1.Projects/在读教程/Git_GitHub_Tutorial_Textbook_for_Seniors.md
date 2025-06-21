# Git与GitHub教材：面向大四学生的AI项目版本控制与协作

## 目标
本教材帮助大四学生掌握**Git**和**GitHub**，用于AI项目版本控制和协作，重点涵盖分支管理、Pull Request（PR）和GitHub Actions，结合Hugging Face模型构建高效开发流程。教材详尽、实用，适合有Python基础的学生，强调独立开发与开源协作，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python、Linux命令、JSON、REST API。
- **工具**：Git、GitHub CLI、Python 3.9+、VS Code、Docker、Jupyter Notebook。
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：Git与GitHub简介

### 1.1 为什么选择Git和GitHub？
- **Git优点**：
  - **分布式**：本地版本控制，离线操作。
  - **分支**：并行开发，实验安全。
  - **AI集成**：管理模型代码、配置文件。
- **GitHub优点**：
  - **协作**：PR、Issues、团队管理。
  - **自动化**：Actions支持CI/CD。
  - **开源**：如你的`github.com/coleam00/Archon`。
- **缺点**：
  - Git：学习曲线陡峭。
  - GitHub：私有仓库需付费。
- **适用场景**：AI代码管理、模型部署、团队协作。
- **反直觉洞察**：GitHub不仅是代码托管，更是职业展示与社区互动平台。

### 1.2 配置环境
- **安装Git**：
  ```bash
  sudo apt install git
  ```
- **配置**：
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```
- **GitHub CLI**：
  ```bash
  gh auth login
  ```
- **实践**：克隆`github.com/coleam00/Archon`，提交初次更改。

---

## 第2章：分支管理

### 2.1 分支操作
- **创建与切换**：
  ```bash
  git branch feature/add-model
  git checkout feature/add-model
  ```
- **合并**：
  ```bash
  git checkout main
  git merge feature/add-model
  ```
- **冲突解决**：
  ```bash
  git mergetool
  ```

### 2.2 工作流
- **feature分支**：
  ```bash
  git checkout -b feature/sentiment-api
  ```
- **AI用例**：为情感分析添加新API端点。

### 2.3 实践
- **任务**：创建分支，添加FastAPI端点。
- **代码**（`app.py`）：
  ```python
  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/predict")
  def predict(text: str):
      return {"text": text, "prediction": "positive"}
  ```
- **提交**：
  ```bash
  git add app.py
  git commit -m "Add sentiment analysis API"
  git push origin feature/sentiment-api
  ```

---

## 第3章：Pull Request（PR）

### 3.1 PR流程
- **创建PR**：
  ```bash
  gh pr create --title "Add sentiment API" --body "Implements basic sentiment prediction"
  ```
- **审查**：添加审查者，响应评论。
- **合并**：
  ```bash
  gh pr merge
  ```

### 3.2 最佳实践
- **描述**：清晰说明变更目的。
- **自动化**：配置Actions检查PR。

### 3.3 实践
- **任务**：提交PR到`github.com/coleam00/Archon`。
- **测试**：确认PR通过审查并合并。

---

## 第4章：GitHub Actions

### 4.1 Actions基础
- **workflow示例**（`.github/workflows/test.yml`）：
  ```yaml
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

### 4.2 AI用例
- **任务**：自动化情感分析测试。
- **测试代码**（`tests/test_app.py`）：
  ```python
  from fastapi.testclient import TestClient
  from app import app

  client = TestClient(app)

  def test_predict():
      response = client.get("/predict?text=I love AI!")
      assert response.status_code == 200
      assert response.json()["prediction"] == "positive"
  ```

### 4.3 实践
- **任务**：配置Actions运行测试。
- **依赖**（`requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  pytest==7.4.0
  ```
- **测试**：推送代码，确认Actions通过。

---

## 第5章：集成AI项目管道

### 5.1 代码管理
- **Dockerfile**：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- **提交**：
  ```bash
  git add Dockerfile
  git commit -m "Add Dockerfile for sentiment API"
  ```

### 5.2 协作与自动化
- **PR**：提交Dockerfile更改。
- **Actions**：构建并推送镜像。
  ```yaml
  name: Build and Push
  on: [push]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v3
      - name: Build Docker image
        run: docker build -t sentiment-app:latest .
      - name: Push to GitHub Packages
        run: |
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker tag sentiment-app:latest ghcr.io/coleam00/sentiment-app:latest
          docker push ghcr.io/coleam00/sentiment-app:latest
  ```

### 5.3 实践
- **任务**：配置CI/CD管道，推送镜像。
- **测试**：确认镜像在`ghcr.io/coleam00/sentiment-app`。

---

## 第6章：迷你项目——AI情感分析GitHub协作

### 6.1 项目目标
构建AI情感分析项目，包含：
- FastAPI推理服务。
- 分支管理与PR协作。
- Actions自动化测试与部署。

### 6.2 项目结构
```
sentiment_project/
├── .github/
│   ├── workflows/
│   │   ├── test.yml
│   │   ├── build.yml
├── app.py
├── tests/
│   ├── test_app.py
├── Dockerfile
├── requirements.txt
```

### 6.3 实现
- **应用**（`app.py`）：
  ```python
  from fastapi import FastAPI
  from transformers import pipeline

  app = FastAPI()
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.get("/predict")
  def predict(text: str):
      result = classifier(text)[0]
      return {"text": text, "prediction": result['label'], "score": result['score']}
  ```
- **测试**（`tests/test_app.py`）：
  ```python
  from fastapi.testclient import TestClient
  from app import app

  client = TestClient(app)

  def test_predict():
      response = client.get("/predict?text=I love AI!")
      assert response.status_code == 200
      assert response.json()["prediction"] == "POSITIVE"
  ```
- **workflow**（`.github/workflows/test.yml`）：
  ```yaml
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
- **依赖**（`requirements.txt`）：
  ```
  fastapi==0.103.0
  uvicorn==0.23.2
  transformers==4.35.0
  torch==2.1.0
  pytest==7.4.0
  ```

### 6.4 测试
- **运行**：
  ```bash
  git checkout -b feature/sentiment-api
  git add .
  git commit -m "Add sentiment analysis API"
  git push origin feature/sentiment-api
  gh pr create
  ```
- **测试**：确认PR通过Actions测试并合并。

---

## 第7章：优化与进阶

### 7.1 优化
- **分支清理**：
  ```bash
  git branch -d feature/sentiment-api
  git push origin --delete feature/sentiment-api
  ```
- **Actions性能**：
  ```yaml
  jobs:
    test:
      runs-on: ubuntu-latest
      strategy:
        matrix:
          python-version: ['3.9', '3.10']
  ```

### 7.2 进阶
- **Neo4j**：版本控制关系数据（如你的兴趣）。
- **Dependabot**：自动化依赖更新。
- **云部署**：GCP Cloud Run、AWS ECS。

### 7.3 实践
- **任务**：配置Dependabot，优化workflow。
- **测试**：确认自动化更新PR。

---

## 资源
- **官方文档**：[Git](https://git-scm.com/doc)、[GitHub](https://docs.github.com/)
- **教程**：GitHub Learning Lab、Pro Git
- **工具**：VS Code、GitHub CLI、Jira、Obsidian
- **建议**：用`notebooklm.google.com`记录协作流程，结合Obsidian或Jira优化任务管理。