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
---
这段代码展示了在两大主流云平台——AWS SageMaker 和 Google Cloud Vertex AI 上进行机器学习模型训练、部署和推理的流程。它们的核心逻辑都是将你的机器学习代码和数据提交到云端，利用云服务提供的计算资源进行模型训练，然后将训练好的模型部署为可供调用的API接口，最后通过这个接口进行实时预测。

我会将这两个部分的代码执行流程分别解释：

---

### **AWS SageMaker 部分执行流程**

这个 `try...except` 块负责在 AWS SageMaker 上进行 Hugging Face 模型（一个预训练的NLP模型框架）的训练、部署和推理。

1.  **导入必要的库**：
    *   `import boto3`: AWS SDK for Python，用于与AWS服务交互的基础库。虽然这里没有直接使用 `boto3.client` 来操作SageMaker，但SageMaker SDK内部会使用它。
    *   `from sagemaker.huggingface import HuggingFace`: SageMaker Python SDK 提供的高级抽象，用于简化Hugging Face模型的训练和部署。
    *   `import json`: 用于处理模型推理结果的JSON格式。

2.  **初始化 SageMaker Session**：
    *   `session = sagemaker.Session()`: 创建一个SageMaker会话对象。这个对象会管理与SageMaker服务的连接，处理默认S3存储桶（用于模型输出、日志等）、区域配置等。它是与SageMaker交互的起点。

3.  **定义 IAM 角色**：
    *   `role = "arn:aws:iam::account-id:role/SageMakerRole"`: 指定一个IAM（身份和访问管理）角色的ARN（Amazon Resource Name）。这个角色必须拥有足够的权限，允许SageMaker访问S3存储桶中的数据、创建和管理EC2实例进行训练和推理，并将日志写入CloudWatch等。这里的 `account-id` 是一个占位符，实际使用时需要替换为你的AWS账户ID。

4.  **配置 Hugging Face Estimator (训练器)**：
    *   `huggingface_estimator = HuggingFace(...)`: 这一步是设置机器学习训练任务的关键。它定义了训练环境和任务的各种参数：
        *   `entry_point="train.py"`: 指定了实际执行模型训练逻辑的Python脚本文件名。SageMaker会在训练实例上运行这个脚本。
        *   `source_dir="code"`: 指定了包含 `train.py` 及其所有依赖（如其他Python模块）的本地目录。SageMaker会将这个`code`目录打包并上传到S3，然后在训练实例启动时下载下来。
        *   `role=role`: 将之前定义的IAM角色分配给这个训练任务，赋予其在AWS环境中操作的权限。
        *   `instance_type="ml.m5.xlarge"`: 指定用于训练的EC2实例类型，`ml.m5.xlarge` 是一种通用型CPU实例。
        *   `py_version="py39"`: 指定训练环境使用的Python版本。
        *   `transformers_version="4.35.0"` 和 `pytorch_version="2.1.0"`: 指定Hugging Face Transformers库和PyTorch框架的版本。SageMaker会根据这些版本选择或构建合适的Docker镜像来启动训练环境。
        *   `hyperparameters={"model_name": "distilbert-base-uncased"}`: 传递给 `train.py` 脚本的超参数。`train.py` 脚本会读取并使用这些参数来配置模型训练。

5.  **启动训练任务**：
    *   `huggingface_estimator.fit({"training": "s3://my-ai-bucket/data/"})`: 这一行会向SageMaker服务发起一个训练请求。
        *   SageMaker会在后台执行以下操作：
            1.  根据配置的实例类型、Python版本和库版本，拉取或构建相应的Docker训练镜像。
            2.  启动一个或多个 `ml.m5.xlarge` 实例。
            3.  将 `source_dir` (`code` 目录) 和训练数据 (`s3://my-ai-bucket/data/`) 下载到这些实例上。
            4.  在实例中运行 `train.py` 脚本，执行模型训练。
            5.  监控训练过程的日志，并将其发送到AWS CloudWatch。
            6.  训练完成后，将训练好的模型文件（通常是一个`model.tar.gz`压缩包）上传到S3的指定输出路径（通常是会话S3桶下的一个路径）。
        *   `fit` 方法会阻塞，直到训练任务完成（成功或失败）。

6.  **部署模型为实时推理端点**：
    *   `predictor = huggingface_estimator.deploy(...)`: 训练成功后，这一行将训练好的模型部署为一个可供应用程序实时调用的HTTP/HTTPS推理端点。
        *   `initial_instance_count=1`: 指定用于推理的实例数量。
        *   `instance_type="ml.t2.medium"`: 指定用于推理的EC2实例类型。通常推理实例会比训练实例小，以节省成本。
        *   SageMaker在后台会：
            1.  根据模型类型和部署配置，拉取或构建合适的推理Docker镜像。
            2.  启动指定的 `ml.t2.medium` 实例。
            3.  将之前训练好的模型文件从S3下载到这些推理实例上。
            4.  在实例中加载模型，并启动一个Web服务器，提供推理服务。
            5.  返回一个 `predictor` 对象，用于后续向该端点发送请求。

7.  **进行模型推理**：
    *   `result = predictor.predict({"inputs": "I love AI!"})`: 向刚刚部署的SageMaker推理端点发送一个预测请求。`{"inputs": "I love AI!"}` 是一个示例输入，表示要对这句话进行情感分析（或模型训练时设定的任何任务）。
    *   `print(json.loads(result)["predictions"])`: `predictor.predict()` 返回的结果通常是字节流或字符串，需要使用 `json.loads()` 将其解析为Python字典/列表，然后从中提取出实际的预测结果并打印。

8.  **错误处理**：
    *   `except Exception as e: print(f"SageMaker错误：{e}")`: 如果在 `try` 块中的任何一步发生异常（例如，IAM角色权限不足、S3路径错误、实例启动失败、模型训练失败、部署失败等），程序会捕获该异常并打印错误信息。

---

### **Google Cloud Vertex AI 部分执行流程**

这个 `try...except` 块负责在 Google Cloud Vertex AI 上进行自定义训练任务的设置、运行、模型部署和推理。

1.  **导入必要的库**：
    *   `from google.cloud import aiplatform`: Google Cloud Vertex AI Python SDK，用于与Vertex AI服务交互的核心库。

2.  **初始化 Vertex AI 客户端**：
    *   `aiplatform.init(project="my-project", location="us-central1")`: 初始化Vertex AI SDK。
        *   `project="my-project"`: 指定你的Google Cloud项目ID。
        *   `location="us-central1"`: 指定资源将要部署的区域。这是与GCP服务交互的第一步，它设置了操作的上下文。

3.  **定义 Custom Training Job (自定义训练任务)**：
    *   `job = aiplatform.CustomTrainingJob(...)`: 这一步定义了要在Vertex AI上运行的自定义训练任务的元数据和配置。
        *   `display_name="sentiment-training"`: 任务在Vertex AI控制台中的显示名称。
        *   `script_path="train.py"`: 指定本地训练脚本的路径。Vertex AI会自动将这个脚本上传到一个内部管理的GCS暂存桶。
        *   `container_uri="gcr.io/cloud-aiplatform/pytorch-cpu.2-1"`: 指定用于训练的Docker容器镜像URI。这里使用的是Google提供的预构建PyTorch CPU镜像，它包含了PyTorch 2.1及其他必要的库。这意味着你不需要自己构建Docker镜像。
        *   `requirements=["transformers==4.35.0"]`: 指定在训练容器内额外需要安装的Python包及其版本。

4.  **运行训练任务**：
    *   `job.run(...)`: 这一行会向Vertex AI服务发起一个训练请求。
        *   `dataset=aiplatform.CustomDataset(...)`: 指定训练数据。这里通过 `gcs_uri="gs://my-ai-bucket/data/"` 指向存储在Google Cloud Storage上的数据路径。Vertex AI会自动处理数据访问。
        *   `machine_type="n1-standard-4"`: 指定用于训练的虚拟机实例类型。
        *   Vertex AI在后台会：
            1.  在指定的区域中，根据 `machine_type` 启动一个或多个虚拟机。
            2.  拉取 `container_uri` 指定的Docker镜像。
            3.  将 `script_path` (`train.py`) 和 `requirements` 安装到容器内。
            4.  运行 `train.py` 脚本，访问GCS上的训练数据，执行模型训练。
            5.  将训练日志发送到Google Cloud Logging。
            6.  训练完成后，将训练好的模型构件（artifacts）存储在一个Vertex AI管理的GCS位置。
        *   `run` 方法会阻塞，直到训练任务完成。

5.  **部署模型为推理端点**：
    *   `endpoint = job.deploy(machine_type="n1-standard-4")`: 训练成功后，这一行将训练好的模型部署为可供调用的API端点。
        *   `machine_type="n1-standard-4"`: 指定用于推理服务的虚拟机实例类型。
        *   Vertex AI在后台会：
            1.  根据指定的实例类型启动一个或多个虚拟机。
            2.  加载之前训练好的模型。Vertex AI通常可以从训练任务的元数据中推断出合适的模型服务容器（如果需要，也可以显式指定）。
            3.  启动一个HTTP/HTTPS服务器，提供预测服务。
            4.  返回一个 `endpoint` 对象，用于后续向该端点发送预测请求。

6.  **进行模型推理**：
    *   `result = endpoint.predict(instances=[{"inputs": "I love AI!"}])`: 向刚刚部署的Vertex AI端点发送一个预测请求。`instances` 参数是一个列表，因为端点可以同时处理多个输入实例。
    *   `print(result.predictions)`: `endpoint.predict()` 返回的结果中包含了模型的所有预测值，通常通过 `.predictions` 属性访问并打印。

7.  **错误处理**：
    *   `except Exception as e: print(f"Vertex AI错误：{e}")`: 如果在 `try` 块中的任何一步发生异常（例如，项目ID或区域错误、权限问题、训练失败、部署失败等），程序会捕获该异常并打印错误信息。

---

**总结：**

这两段代码都封装了云计算平台提供的高度[[抽象化]]的MLOps（机器学习运维）功能，使得开发者可以通过少量Python代码，就能完成从数据加载、模型训练到部署和推理的整个机器学习生命周期。SageMaker和Vertex AI都在努力**[[降低认知负荷]]**，让开发者可以专注于模型本身，而无需过多管理底层基础设施的细节。它们体现了[[云原生]]AI开发的[[核心范式]]：按需使用、弹性伸缩、平台管理、**[[效率提升]]**。