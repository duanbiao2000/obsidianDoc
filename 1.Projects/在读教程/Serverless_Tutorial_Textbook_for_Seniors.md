# Serverless教材：面向大四学生的AI轻量API开发

## 目标
本教材帮助大四学生掌握**Serverless**架构（AWS Lambda、Google Cloud Functions），开发轻量AI API，重点涵盖函数开发、触发器配置和Hugging Face模型集成，构建高效的情感分析API。教材详尽、实用，适合有Python基础的学生，强调自动扩展与低维护，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python、JSON、REST API、基本云服务概念。
- **工具**：AWS Lambda、Google Cloud Functions、Python 3.9+、boto3、google-cloud-functions、Jupyter Notebook、VS Code、Git、Docker.
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：Serverless简介

### 1.1 为什么选择Serverless？
- **优点**：
  - **自动扩展**：按需分配资源。
  - **低维护**：无需管理服务器。
  - **AI集成**：快速部署轻量推理API。
- **缺点**：
  - 冷启动延迟。
  - 厂商锁定风险。
- **适用场景**：AI API、事件驱动应用、微服务。
- **反直觉洞察**：Serverless虽简化运维，但优化冷启动和成本管理需深思。

### 1.2 配置环境
- **AWS**：
  - 安装AWS CLI：
    ```bash
    pip install awscli
    aws configure
    ```
- **GCP**：
  - 安装GCP SDK：
    ```bash
    gcloud init
    ```
- **示例**（AWS Lambda）：
  ```python
  def lambda_handler(event, context):
      return {"statusCode": 200, "body": "Hello, Lambda!"}
  ```
- **实践**：创建简单Lambda/Cloud Function，测试调用。

---

## 第2章：AWS Lambda开发

### 2.1 函数开发
- **示例**（`lambda_function.py`）：
  ```python
  from transformers import pipeline
  import json

  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  def lambda_handler(event, context):
      text = event["queryStringParameters"]["text"]
      result = classifier(text)[0]
      return {
          "statusCode": 200,
          "body": json.dumps({"label": result["label"], "score": result["score"]})
      }
  ```

### 2.2 触发器
- **API Gateway**：
  - 配置HTTP触发器，映射`/predict`。
- **依赖**：
  ```bash
  pip install transformers torch -t .
  zip -r function.zip .
  ```

### 2.3 实践
- **任务**：部署Lambda情感分析函数。
- **测试**：调用`https://<api-id>.execute-api.<region>.amazonaws.com/predict?text=I love AI!`。

---

## 第3章：Google Cloud Functions开发

### 3.1 函数开发
- **示例**（`main.py`）：
  ```python
  from transformers import pipeline
  import functions_framework

  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @functions_framework.http
  def predict(request):
      text = request.args.get("text")
      result = classifier(text)[0]
      return {"label": result["label"], "score": result["score"]}
  ```

### 3.2 触发器
- **HTTP触发**：
  - 部署函数，获取URL。
- **依赖**（`requirements.txt`）：
  ```
  functions-framework==3.5.0
  transformers==4.35.0
  torch==2.1.0
  ```

### 3.3 实践
- **任务**：部署Cloud Functions情感分析API。
- **部署**：
  ```bash
  gcloud functions deploy predict \
      --runtime python39 \
      --trigger-http \
      --allow-unauthenticated
  ```
- **测试**：调用`https://<region>-<project-id>.cloudfunctions.net/predict?text=I love AI!`。

---

## 第4章：集成AI API管道

### 4.1 Serverless与Hugging Face
- **AWS Lambda**：
  ```python
  import boto3
  import json

  s3 = boto3.client("s3")

  def lambda_handler(event, context):
      text = event["queryStringParameters"]["text"]
      # Mock inference
      result = {"label": "POSITIVE", "score": 0.9}
      s3.put_object(Bucket="sentiment-results", Key=f"{text}.json", Body=json.dumps(result))
      return {"statusCode": 200, "body": json.dumps(result)}
  ```

### 4.2 工具集成
- **Git**：
  ```bash
  git add .
  git commit -m "Add Serverless AI API"
  git push origin main
  ```

### 4.3 实践
- **任务**：配置Serverless API，存储结果到S3/Cloud Storage。
- **测试**：确认结果存储。

---

## 第5章：迷你项目——AI情感分析API

### 5.1 项目目标
构建Serverless AI情感分析API，包含：
- Lambda/Cloud Functions：推理情感分析。
- 触发器：HTTP API调用。
- 存储：S3/Cloud Storage保存结果.

### 5.2 项目结构
```
sentiment-serverless/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
├── aws/
│   ├── lambda_function.py
│   ├── requirements.txt
├── gcp/
│   ├── main.py
│   ├── requirements.txt
├── Dockerfile
```

### 5.3 实现
- **AWS Lambda**（`aws/lambda_function.py`）：
  ```python
  from transformers import pipeline
  import json
  import boto3

  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
  s3 = boto3.client("s3")

  def lambda_handler(event, context):
      try:
          text = event["queryStringParameters"]["text"]
          result = classifier(text)[0]
          data = {"label": result["label"], "score": result["score"]}
          s3.put_object(Bucket="sentiment-results", Key=f"{text}.json", Body=json.dumps(data))
          return {"statusCode": 200, "body": json.dumps(data)}
      except Exception as e:
          return {"statusCode": 500, "body": str(e)}
  ```
- **Google Cloud Functions**（`gcp/main.py`）：
  ```python
  from transformers import pipeline
  import functions_framework
  from google.cloud import storage

  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
  storage_client = storage.Client()

  @functions_framework.http
  def predict(request):
      try:
          text = request.args.get("text")
          result = classifier(text)[0]
          data = {"label": result["label"], "score": result["score"]}
          bucket = storage_client.bucket("sentiment-results")
          blob = bucket.blob(f"{text}.json")
          blob.upload_from_string(json.dumps(data))
          return data
      except Exception as e:
          return {"error": str(e)}, 500
  ```
- **Dockerfile**（用于本地测试）：
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY aws/requirements.txt .
  RUN pip install -r requirements.txt
  COPY aws/ .
  CMD ["python", "lambda_function.py"]
  ```
- **GitHub Actions**（`.github/workflows/ci.yml`）：
  ```yaml
  name: CI/CD
  on: [push]
  jobs:
    deploy:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r aws/requirements.txt
      - name: Deploy to AWS Lambda
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        run: |
          zip -r function.zip aws/
          aws lambda update-function-code --function-name sentiment-api --zip-file fileb://function.zip
      - name: Deploy to Google Cloud Functions
        env:
          GOOGLE_CREDENTIALS: ${{ secrets.GOOGLE_CREDENTIALS }}
        run: |
          gcloud auth activate-service-account --key-file=- <<< "$GOOGLE_CREDENTIALS"
          gcloud functions deploy predict \
            --runtime python39 \
            --trigger-http \
            --allow-unauthenticated \
            --source gcp/
  ```
- **依赖**（`aws/requirements.txt`、`gcp/requirements.txt`）：
  ```
  transformers==4.35.0
  torch==2.1.0
  boto3==1.28.0  # AWS only
  google-cloud-storage==2.10.0  # GCP only
  functions-framework==3.5.0  # GCP only
  ```

### 5.4 测试
- **AWS**：
  ```bash
  aws lambda invoke --function-name sentiment-api --payload '{"queryStringParameters": {"text": "I love AI!"}}' output.json
  ```
- **GCP**：
  ```bash
  curl "https://<region>-<project-id>.cloudfunctions.net/predict?text=I love AI!"
  ```
- **测试**：确认S3/Cloud Storage存储结果。

---

## 第6章：优化与进阶

### 6.1 优化
- **AWS Lambda**：
  ```python
  # 增加内存分配
  aws lambda update-function-configuration --function-name sentiment-api --memory-size 512
  ```
- **Google Cloud Functions**：
  ```bash
  gcloud functions deploy predict --memory 512MB
  ```

### 6.2 进阶
- **Neo4j**：结合知识图谱（如你的兴趣）。
- **DynamoDB**：存储推理结果。
- **AWS Step Functions**：编排多函数工作流。

### 6.3 实践
- **任务**：优化冷启动，部署到生产环境。
- **测试**：比较优化前后延迟。

---

## 资源
- **官方文档**：[AWS Lambda](https://docs.aws.amazon.com/lambda/)、[Google Cloud Functions](https://cloud.google.com/functions/docs)
- **教程**：AWS Training、GCP Qwiklabs
- **工具**：AWS CLI、GCP SDK、Jupyter Notebook、VS Code、GitHub、Jira、Obsidian
- **建议**：用`notebooklm.google.com`记录开发流程，结合Obsidian或Jira优化任务管理。