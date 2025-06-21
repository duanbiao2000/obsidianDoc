# AWS与GCP教材：面向大四学生的AI模型云部署

## 目标
本教材帮助大四学生掌握**AWS**（SageMaker、S3）和**GCP**（Vertex AI、Cloud Storage），用于AI模型的训练和推理，构建高效的云端AI管道。教材详尽、实用，适合有Python基础的学生，强调与Google生态的契合和AWS的广泛AI服务，契合你的AI研究和效率兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python、Linux命令、REST API、JSON。
- **工具**：Python 3.9+、pip、AWS CLI、Google Cloud SDK、VS Code、Git。
- **时长**：8小时（2小时理论+6小时实践）。

---

## 第1章：AWS与GCP简介

### 1.1 为什么选择AWS和GCP？
- **AWS优点**：
  - **SageMaker**：端到端ML平台，支持训练、推理、托管。
  - **S3**：高可用存储，适合大数据集。
  - **广泛服务**：EC2、Lambda、Rekognition。
- **GCP优点**：
  - **Vertex AI**：统一ML平台，AutoML和自定义训练。
  - **Cloud Storage**：与Google生态（如BigQuery）无缝集成。
  - **Google生态**：契合你的偏好。
- **缺点**：
  - AWS：配置复杂，成本管理难度大。
  - GCP：服务范围较窄，依赖Google生态。
- **适用场景**：AI模型训练、推理、数据存储。
- **反直觉洞察**：GCP的简单性适合快速原型，AWS的复杂性带来更大灵活性。[](https://matoffo.com/tech-articles/amazon-sagemaker-vs-vertex-ai-a-detailed-comparison-for-machine-learning-pipelines/)

### 1.2 配置环境
- **AWS CLI**：
  ```bash
  pip install awscli
  aws configure
  ```
- **Google Cloud SDK**：
  ```bash
  gcloud init
  ```
- **实践**：配置AWS和GCP凭证，验证访问。

---

## 第2章：Amazon S3与Google Cloud Storage

### 2.1 Amazon S3
- **创建桶**：
  ```python
  import boto3

  s3 = boto3.client("s3")
  s3.create_bucket(Bucket="my-ai-bucket")
  ```
- **上传文件**：
  ```python
  s3.upload_file("sentiment.csv", "my-ai-bucket", "data/sentiment.csv")
  ```

### 2.2 Google Cloud Storage
- **创建桶**：
  ```python
  from google.cloud import storage

  client = storage.Client()
  bucket = client.create_bucket("my-ai-bucket")
  ```
- **上传文件**：
  ```python
  blob = bucket.blob("data/sentiment.csv")
  blob.upload_from_filename("sentiment.csv")
  ```

### 2.3 AI用例
- **任务**：上传情感分析数据集。
- **实践**：上传`sentiment.csv`到S3和Cloud Storage，验证文件存在。

---

## 第3章：AWS SageMaker

### 3.1 训练模型
- **任务**：训练Hugging Face模型。
  ```python
  import sagemaker
  from sagemaker.huggingface import HuggingFace

  session = sagemaker.Session()
  role = "arn:aws:iam::account-id:role/SageMakerRole"

  huggingface_estimator = HuggingFace(
      entry_point="train.py",
      source_dir="code",
      role=role,
      instance_type="ml.m5.xlarge",
      py_version="py39",
      transformers_version="4.35.0",
      pytorch_version="2.1.0",
      hyperparameters={"model_name": "distilbert-base-uncased"}
  )
  huggingface_estimator.fit({"training": "s3://my-ai-bucket/data/"})
  ```

### 3.2 部署推理
- **代码**：
  ```python
  predictor = huggingface_estimator.deploy(
      initial_instance_count=1,
      instance_type="ml.t2.medium"
  )
  result = predictor.predict({"inputs": "I love AI!"})
  print(result)
  ```

### 3.3 实践
- **任务**：训练并部署情感分析模型。
- **测试**：调用端点，预测“I love AI!”。

---

## 第4章：GCP Vertex AI

### 4.1 训练模型
- **任务**：训练Hugging Face模型。
  ```python
  from google.cloud import aiplatform

  aiplatform.init(project="my-project", location="us-central1")
  job = aiplatform.CustomTrainingJob(
      display_name="sentiment-training",
      script_path="train.py",
      container_uri="gcr.io/cloud-aiplatform/pytorch-cpu.2-1",
      requirements=["transformers==4.35.0"]
  )
  job.run(
      dataset=aiplatform.CustomDataset(
          display_name="sentiment-data",
          gcs_uri="gs://my-ai-bucket/data/"
      ),
      machine_type="n1-standard-4"
  )
  ```

### 4.2 部署推理
- **代码**：
  ```python
  endpoint = job.deploy(machine_type="n1-standard-4")
  result = endpoint.predict(instances=[{"inputs": "I love AI!"}])
  print(result.predictions)
  ```

### 4.3 实践
- **任务**：部署情感分析模型到Vertex AI端点。
- **测试**：调用端点，预测“I love AI!”。

---

## 第5章：集成AI管道

### 5.1 数据准备
- **代码**：
  ```python
  import pandas as pd
  from transformers import AutoTokenizer

  df = pd.read_csv("sentiment.csv")
  df = df.dropna()
  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
  df["tokens"] = df["text"].apply(lambda x: tokenizer.encode(x, truncation=True))
  df.to_csv("cleaned.csv")
  ```

### 5.2 云存储与调用
- **AWS**：
  ```python
  import boto3

  s3 = boto3.client("s3")
  s3.upload_file("cleaned.csv", "my-ai-bucket", "data/cleaned.csv")
  ```
- **GCP**：
  ```python
  from google.cloud import storage

  client = storage.Client()
  bucket = client.get_bucket("my-ai-bucket")
  blob = bucket.blob("data/cleaned.csv")
  blob.upload_from_filename("cleaned.csv")
  ```

### 5.3 实践
- **任务**：清洗数据，上传到S3/Cloud Storage，调用SageMaker/Vertex AI端点。
- **测试**：确认数据上传和推理结果。

---

## 第6章：迷你项目——AI情感分析云部署

### 6.1 项目目标
构建AWS和GCP的AI情感分析管道，包含：
- 数据：存储到S3/Cloud Storage。
- 模型：训练并部署到SageMaker/Vertex AI。
- 推理：调用端点，显示预测。

### 6.2 项目结构
```
sentiment_cloud/
├── train.py
├── app.py
├── sentiment.csv
└── requirements.txt
```

### 6.3 实现
- **训练脚本**（`train.py`）：
  ```python
  from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments
  import pandas as pd

  df = pd.read_csv("s3://my-ai-bucket/data/cleaned.csv")  # 或gs://
  tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
  model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")

  # 训练逻辑
  training_args = TrainingArguments(output_dir="./results", num_train_epochs=3)
  trainer = Trainer(model=model, args=training_args)
  trainer.train()
  model.save_pretrained("model")
  tokenizer.save_pretrained("model")
  ```
- **推理脚本**（`app.py`）：
  ```python
  import boto3
  from google.cloud import aiplatform
  import pandas as pd

  # AWS推理
  sagemaker = boto3.client("sagemaker-runtime")
  response = sagemaker.invoke_endpoint(
      EndpointName="sentiment-endpoint",
      ContentType="application/json",
      Body='{"inputs": "I love AI!"}'
  )
  print(response["Body"].read().decode())

  # GCP推理
  aiplatform.init(project="my-project", location="us-central1")
  endpoint = aiplatform.Endpoint("endpoint-id")
  result = endpoint.predict(instances=[{"inputs": "I love AI!"}])
  print(result.predictions)
  ```
- **依赖**（`requirements.txt`）：
  ```
  boto3==1.28.0
  google-cloud-aiplatform==1.60.0
  google-cloud-storage==2.10.0
  pandas==2.1.0
  transformers==4.35.0
  torch==2.1.0
  ```

### 6.4 测试
- 运行：执行`app.py`，调用AWS和GCP端点。
- 测试：输入“I love AI!”，确认预测结果。

---

## 第7章：优化与进阶

### 7.1 优化
- **成本管理**：
  - AWS：使用Spot实例训练。
  - GCP：配置自动扩展。
- **监控**：
  - AWS CloudWatch：跟踪端点性能。
  - GCP Monitoring：分析资源使用。

### 7.2 替代方案
- **AWS Lambda**：轻量推理。
- **GCP Cloud Run**：无服务器部署。

### 7.3 进阶
- **Neo4j**：存储模型关系（如你的兴趣）。
- **BigQuery**：GCP数据分析。
- **SageMaker Pipelines**：自动化ML工作流。

---

## 资源
- **官方文档**：[AWS SageMaker](https://docs.aws.amazon.com/sagemaker/)、[GCP Vertex AI](https://cloud.google.com/vertex-ai)
- **教程**：AWS ML Specialty、Google Cloud Next
- **工具**：VS Code、Jupyter Notebook、AWS Console、GCP Console
- **建议**：用`notebooklm.google.com`记录部署流程，尝试XMind规划云架构。