# Serverless教程辅助测试：面向大四学生的AI轻量API开发评估

## 目标
评估学生对Serverless架构（AWS Lambda、Google Cloud Functions）的掌握情况，以及开发轻量AI API的能力。测试结合理论和实践，适合有Python基础的大四学生，强调自动扩展与低维护。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Serverless架构的主要优势是：  
   A. 固定服务器管理  
   B. 自动扩展与按需计费  
   C. 复杂配置  
   D. 本地部署  
   **答案**：B

2. AWS Lambda的触发器包括：  
   A. API Gateway  
   B. MySQL  
   C. Kubernetes  
   D. Jupyter Notebook  
   **答案**：A

3. Google Cloud Functions的HTTP触发器用于：  
   A. 数据库查询  
   B. REST API调用  
   C. 文件存储  
   D. 模型训练  
   **答案**：B

4. AWS S3用于：  
   A. 函数计算  
   B. 对象存储  
   C. 容器管理  
   D. 网络配置  
   **答案**：B

5. GitHub Actions主要用于：  
   A. 代码托管  
   B. CI/CD自动化  
   C. 数据存储  
   D. 模型推理  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Serverless在AI API开发中的优势，并说明冷启动的挑战。  
   **参考答案**：  
   - **优势**：自动扩展，低维护，快速部署。  
   - **冷启动**：首次调用延迟，需优化内存或使用Provisioned Concurrency。  
   - **评分点**：清晰描述优势与挑战，提及AI场景。

2. **问题**：描述AWS Lambda与Google Cloud Functions的区别，并说明如何避免厂商锁定。  
   **参考答案**：  
   - **区别**：AWS生态更广，GCP集成Google AI工具；AWS支持更多触发器，GCP部署更简单。  
   - **避免锁定**：使用标准化代码，抽象云服务层，结合Docker。  
   - **评分点**：准确对比，提到锁定管理。

---

## 第3部分：编程题（70分）

### 编程题1：AWS Lambda开发（30分）
- **任务**：编写AWS Lambda函数：
  - 接受健康检查文本。
  - 返回固定“healthy”状态。
- **要求**：
  - 配置API Gateway触发器。
  - 验证调用结果。
- **参考代码**：
  ```python
  # lambda_function.py
  import json

  def lambda_handler(event, context):
      text = event.get("queryStringParameters", {}).get("text", "")
      return {
          "statusCode": 200,
          "body": json.dumps({"status": "healthy", "text": text})
      }
  ```
- **部署**：
  ```bash
  zip function.zip lambda_function.py
  aws lambda update-function-code --function-name health-check --zip-file fileb://function.zip
  ```
- **测试**：
  ```bash
  aws lambda invoke --function-name health-check --payload '{"queryStringParameters": {"text": "test"}}' output.json
  ```
- **评分标准**：
  - 函数实现（10分）：正确处理输入。
  - 触发器配置（10分）：API Gateway正常调用。
  - 代码结构（5分）：清晰、可读。
  - 测试验证（5分）：返回正确结果。
<!--ID: 1761111104004-->


### 编程题2：Serverless AI API（40分）
- **任务**：构建Serverless AI情感分析API：
  - AWS Lambda或Google Cloud Functions：推理情感分析。
  - 存储：S3或Cloud Storage保存结果。
  - CI/CD：GitHub Actions部署。
- **要求**：
  - 处理推理错误。
  - 优化冷启动。
- **参考 code**：
  ```python
  # aws/lambda_function.py
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
  ```python
  # gcp/main.py
  from transformers import pipeline
  import functions_framework
  from google.cloud import storage
<!--ID: 1761111104023-->


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
  ```yaml
  # .github/workflows/ci.yml
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
  ```
  ```text
  # aws/requirements.txt
  transformers==4.35.0
  torch==2.1.0
  boto3==1.28.0
  ```
- **测试**：
  ```bash
  curl "https://<api-id>.execute-api.<region>.amazonaws.com/predict?text=I love AI!"
  ```
- **评分标准**：
  - 推理实现（15分）：正确调用Hugging Face模型。
  - 存储集成（10分）：结果保存到S3/Cloud Storage。
  - CI/CD配置（10分）：自动化部署正常。
  - 错误处理（5分）：处理推理错误。
<!--ID: 1761111104040-->


---

## 注意事项
- **提交**：提交项目文件夹（包含`aws/`、`gcp/`、`.github/workflows/`）。
- **测试环境**：Python 3.9+、AWS CLI、GCP SDK，安装`boto3`、`google-cloud-storage`、`transformers`.
- **建议**：用`notebooklm.google.com`记录开发流程，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估AI API开发能力，强调自动扩展与低维护。
- **反直觉洞察**：Serverless通过简化运维加速AI API开发，但冷启动和厂商锁定需谨慎管理。