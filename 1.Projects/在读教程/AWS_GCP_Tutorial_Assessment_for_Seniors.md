# AWS与GCP教程辅助测试：面向大四学生的AI模型云部署评估

## 目标
评估学生对AWS（SageMaker、S3）和GCP（Vertex AI、Cloud Storage）核心概念的掌握情况，以及部署AI模型的能力。测试结合理论和实践，适合有Python基础的大四学生，强调云端训练和推理。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. AWS SageMaker的主要功能是：  
   A. 数据可视化  
   B. 端到端ML平台  
   C. 数据库管理  
   D. UI框架  
   **答案**：B[](https://aws.amazon.com/sagemaker/)

2. GCP Vertex AI支持：  
   A. AutoML和自定义训练  
   B. 图像处理  
   C. SQL查询  
   D. 文件加密  
   **答案**：A[](https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform)

3. Amazon S3用于：  
   A. 模型训练  
   B. 云存储  
   C. 推理端点  
   D. 实时通信  
   **答案**：B

4. Google Cloud Storage的生命周期管理用于：  
   A. 模型部署  
   B. 数据归档  
   C. 训练管道  
   D. 权限分配  
   **答案**：B

5. 以下哪个工具用于AWS成本监控？  
   A. CloudWatch  
   B. BigQuery  
   C. Cloud Run  
   D. pgAdmin  
   **答案**：A

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：比较AWS SageMaker和GCP Vertex AI在AI模型部署中的优劣，并说明适用场景。  
   **参考答案**：  
   - **SageMaker**：灵活，支持多种框架，适合复杂定制；配置复杂，成本高。  
   - **Vertex AI**：简单，Google生态集成好，适合快速原型；服务范围较窄。  
   - **场景**：SageMaker适合企业级ML，Vertex AI适合Google生态用户。  
   - **评分点**：清晰对比，提及AI场景。[](https://matoffo.com/tech-articles/amazon-sagemaker-vs-vertex-ai-a-detailed-comparison-for-machine-learning-pipelines/)

2. **问题**：描述S3和Cloud Storage的权限管理，并说明如何避免技术债务。  
   **参考答案**：  
   - **权限**：S3用IAM策略，Cloud Storage用ACL/IAM，控制读写访问。  
   - **技术债务**：避免硬编码凭证，定期审查权限，自动化部署脚本。  
   - **评分点**：准确描述权限，提到技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：S3与Cloud Storage（30分）
- **任务**：编写Python脚本：
  - 上传`sentiment.csv`到S3和Cloud Storage。
  - 下载并验证文件。
- **要求**：
  - 处理权限错误。
  - 使用`boto3`和`google-cloud-storage`。
- **参考代码**：
  ```python
  import boto3
  from google.cloud import storage
  import pandas as pd

  # AWS S3
  try:
      s3 = boto3.client("s3")
      s3.upload_file("sentiment.csv", "my-ai-bucket", "data/sentiment.csv")
      s3.download_file("my-ai-bucket", "data/sentiment.csv", "downloaded_s3.csv")
      print(pd.read_csv("downloaded_s3.csv").head())
  except Exception as e:
      print(f"S3错误：{e}")

  # Google Cloud Storage
  try:
      client = storage.Client()
      bucket = client.get_bucket("my-ai-bucket")
      blob = bucket.blob("data/sentiment.csv")
      blob.upload_from_filename("sentiment.csv")
      blob.download_to_filename("downloaded_gcs.csv")
      print(pd.read_csv("downloaded_gcs.csv").head())
  except Exception as e:
      print(f"GCS错误：{e}")
  ```
- **评分标准**：
  - 上传功能（10分）：正确上传。
  - 下载验证（10分）：文件正确下载。
  - 错误处理（5分）：处理权限错误。
  - 代码结构（5分）：清晰、可读。

### Programming Question 2: SageMaker and Vertex AI Deployment (40 points)
- **Task**: Write a Python script to:
  - Train a Hugging Face model on SageMaker.
  - Deploy it to a SageMaker endpoint.
  - Perform inference with a sample input.
- **Requirements**:
  - Use `boto3` for SageMaker.
  - Handle errors (e.g., missing role).
  - Bonus: Include a similar Vertex AI deployment.
- **Reference code**:
  ```python
  import boto3
  from sagemaker.huggingface import HuggingFace
  import json

  # SageMaker Training
  try:
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
      
      # Deploy
      predictor = huggingface_estimator.deploy(
          initial_instance_count=1,
          instance_type="ml.t2.medium"
      )
      result = predictor.predict({"inputs": "I love AI!"})
      print(json.loads(result)["predictions"])
  except Exception as e:
      print(f"SageMaker错误：{e}")
  ```
  ```python
  # Vertex AI (Bonus)
  from google.cloud import aiplatform

  try:
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
      endpoint = job.deploy(machine_type="n1-standard-4")
      result = endpoint.predict(instances=[{"inputs": "I love AI!"}])
      print(result.predictions)
  except Exception as e:
      print(f"Vertex AI错误：{e}")
  ```
- **Scoring Criteria**:
  - Training (15 points): Correct SageMaker training setup.
  - Deployment (10 points): Successful endpoint deployment.
  - Inference (10 points): Correct prediction output.
  - Error Handling (5 points): Handle role or connection errors.

---

## Notes
- **Submission**: Submit project folder (containing `script.py`, `train.py`, `sentiment.csv`, `requirements.txt`).
- **Test Environment**: Python 3.9+, install `boto3`, `google-cloud-aiplatform`, `google-cloud-storage`, `transformers`.
- **Suggestion**: Document deployment steps in `notebooklm.google.com` (aligned with your habits) to optimize cloud architecture.

## Scoring Summary
- **Multiple Choice**: Tests core concepts.
- **Short Answer**: Evaluates theoretical understanding and design thinking.
- **Programming Questions**: Assesses deployment skills, emphasizing SageMaker and Vertex AI.
- **Unconventional Insight**: AWS offers flexibility but requires expertise; GCP’s simplicity suits Google ecosystem users but limits advanced customization.[](https://superwise.ai/blog/sagemaker-vs-vertex-ai/)