# TensorFlow教材：面向大四学生的AI模型生产部署

## 目标
本教材帮助大四学生掌握**TensorFlow**，开发和部署AI模型，重点涵盖**Keras API**、**TensorFlow Serving**和模型优化，结合Hugging Face数据集构建情感分析模型部署 pipeline。教材详尽、实用，适合有Python基础的学生，强调生产环境和边缘部署，契合你的AI研究和生产力兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python、NumPy、基本深度学习概念、REST API。
- **工具**：TensorFlow 2.x、Keras、TensorFlow Serving、TensorFlow Lite、Python 3.9+、Docker、VS Code、Git.
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：TensorFlow简介

### 1.1 为什么选择TensorFlow？
- **优点**：
  - **生态成熟**：Keras、TF Serving、TF Lite。
  - **生产级**：支持大规模系统、边缘部署。
  - **AI集成**：情感分析、推荐系统。
- **缺点**：
  - 学习曲线较陡。
  - 模型优化需手动调优。
- **适用场景**：企业级AI、移动/边缘推理。
- **反直觉洞察**：TensorFlow的复杂性在生产环境中转化为可靠性和灵活性。

### 1.2 安装与初始化
- **安装**：
  ```bash
  pip install tensorflow==2.15.0
  ```
- **示例**（Keras模型）：
  ```python
  import tensorflow as tf
  from tensorflow.keras import layers

  model = tf.keras.Sequential([
      layers.Dense(10, activation='relu', input_shape=(5,)),
      layers.Dense(1, activation='sigmoid')
  ])
  model.compile(optimizer='adam', loss='binary_crossentropy')
  model.summary()
  ```
- **实践**：运行Keras模型，检查结构。

---

## 第2章：Keras API开发

### 2.1 模型构建
- **示例**（情感分析模型）：
  ```python
  import tensorflow as tf
  from tensorflow.keras import layers
  from tensorflow.keras.preprocessing.text import Tokenizer
  from tensorflow.keras.preprocessing.sequence import pad_sequences

  # 示例数据
  texts = ["I love AI!", "AI is hard"]
  labels = [1, 0]
  tokenizer = Tokenizer(num_words=1000)
  tokenizer.fit_on_texts(texts)
  sequences = tokenizer.texts_to_sequences(texts)
  padded = pad_sequences(sequences, maxlen=10)

  # 模型
  model = tf.keras.Sequential([
      layers.Embedding(1000, 16, input_length=10),
      layers.GlobalAveragePooling1D(),
      layers.Dense(16, activation='relu'),
      layers.Dense(1, activation='sigmoid')
  ])
  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
  model.fit(padded, tf.convert_to_tensor(labels), epochs=10)
  ```
- **数据预处理**：
  ```python
  import tensorflow_datasets as tfds

  dataset, info = tfds.load('imdb_reviews', with_info=True, as_supervised=True)
  train_dataset, test_dataset = dataset['train'], dataset['test']
  ```

### 2.2 实践
- **任务**：训练情感分析模型。
- **测试**：预测新文本，检查准确率。

---

## 第3章：TensorFlow Serving部署

### 3.1 模型导出
- **示例**：
  ```python
  model.save('sentiment_model/1')
  ```

### 3.2 TF Serving配置
- **Docker**：
  ```bash
  docker run -p 8501:8501 \
      -v "$(pwd)/sentiment_model:/models/sentiment_model" \
      -e MODEL_NAME=sentiment_model \
      tensorflow/serving
  ```

### 3.3 API调用
- **REST**：
  ```python
  import requests
  import json

  data = {
      "instances": [{"input_1": pad_sequences(tokenizer.texts_to_sequences(["I love AI!"]), maxlen=10).tolist()}]
  }
  response = requests.post('http://localhost:8501/v1/models/sentiment_model:predict', json=data)
  print(response.json())
  ```

### 3.4 实践
- **任务**：部署模型到TF Serving。
- **测试**：调用API，确认预测结果。

---

## 第4章：模型优化与TF Lite

### 4.1 量化
- **示例**：
  ```python
  converter = tf.lite.TFLiteConverter.from_saved_model('sentiment_model/1')
  converter.optimizations = [tf.lite.Optimize.DEFAULT]
  tflite_model = converter.convert()
  with open('sentiment_model.tflite', 'wb') as f:
      f.write(tflite_model)
  ```

### 4.2 TF Lite推理
- **示例**：
  ```python
  import numpy as np
  interpreter = tf.lite.Interpreter(model_path='sentiment_model.tflite')
  interpreter.allocate_tensors()
  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()

  input_data = np.array(pad_sequences(tokenizer.texts_to_sequences(["I love AI!"]), maxlen=10), dtype=np.float32)
  interpreter.set_tensor(input_details[0]['index'], input_data)
  interpreter.invoke()
  output_data = interpreter.get_tensor(output_details[0]['index'])
  print(output_data)
  ```

### 4.3 实践
- **任务**：转换模型为TF Lite。
- **测试**：在本地运行推理，比较性能。

---

## 第5章：集成AI部署管道

### 5.1 CI/CD
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
        run: pip install tensorflow==2.15.0
      - name: Train and export model
        run: python train.py
      - name: Build Docker image
        run: |
          docker build -t ghcr.io/coleam00/sentiment-serving:latest .
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/coleam00/sentiment-serving:latest
  ```

### 5.2 实践
- **任务**：配置CI/CD，部署到TF Serving。
- **测试**：确认镜像推送和API运行。

---

## 第6章：迷你项目——情感分析模型部署

### 6.1 项目目标
构建情感分析模型部署 pipeline：
- Keras：训练模型。
- TF Serving：云端部署。
- TF Lite：边缘部署.

### 6.2 项目结构
```
sentiment-deployment/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
├── model/
│   ├── train.py
│   ├── requirements.txt
├── serving/
│   ├── Dockerfile
├── tflite/
│   ├── convert.py
```

### 6.3 实现
- **训练**（`model/train.py`）：
  ```python
  import tensorflow as tf
  from tensorflow.keras import layers
  from tensorflow.keras.preprocessing.text import Tokenizer
  from tensorflow.keras.preprocessing.sequence import pad_sequences

  texts = ["I love AI!", "AI is hard"]
  labels = [1, 0]
  tokenizer = Tokenizer(num_words=1000)
  tokenizer.fit_on_texts(texts)
  sequences = tokenizer.texts_to_sequences(texts)
  padded = pad_sequences(sequences, maxlen=10)

  model = tf.keras.Sequential([
      layers.Embedding(1000, 16, input_length=10),
      layers.GlobalAveragePooling1D(),
      layers.Dense(16, activation='relu'),
      layers.Dense(1, activation='sigmoid')
  ])
  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
  model.fit(padded, tf.convert_to_tensor(labels), epochs=10)
  model.save('sentiment_model/1')
  ```
- **Serving**（`serving/Dockerfile`）：
  ```dockerfile
  FROM tensorflow/serving
  COPY sentiment_model /models/sentiment_model
  ENV MODEL_NAME=sentiment_model
  ```
- **TF Lite**（`tflite/convert.py`）：
  ```python
  import tensorflow as tf

  converter = tf.lite.TFLiteConverter.from_saved_model('sentiment_model/1')
  converter.optimizations = [tf.lite.Optimize.DEFAULT]
  tflite_model = converter.convert()
  with open('sentiment_model.tflite', 'wb') as f:
      f.write(tflite_model)
  ```

### 6.4 测试
- **TF Serving**：
  ```bash
  docker run -p 8501:8501 -v "$(pwd)/sentiment_model:/models/sentiment_model" -e MODEL_NAME=sentiment_model tensorflow/serving
  curl -d '{"instances": [{"input_1": [[1, 2, 3, 0, 0, 0, 0, 0, 0, 0]]}]}' -X POST http://localhost:8501/v1/models/sentiment_model:predict
  ```
- **TF Lite**：
  ```python
  import numpy as np
  interpreter = tf.lite.Interpreter(model_path='sentiment_model.tflite')
  interpreter.allocate_tensors()
  input_data = np.array([[1, 2, 3, 0, 0, 0, 0, 0, 0, 0]], dtype=np.float32)
  interpreter.set_tensor(interpreter.get_input_details()[0]['index'], input_data)
  interpreter.invoke()
  print(interpreter.get_tensor(interpreter.get_output_details()[0]['index']))
  ```

---

## 第7章：优化与进阶

### 7.1 优化
- **XLA**：
  ```python
  @tf.function(jit_compile=True)
  def model_predict(inputs):
      return model(inputs)
  ```

### 7.2 进阶
- **Neo4j**：结合知识图谱（如你的兴趣）。
- **TPU**：加速训练。
- **GCP AI Platform**：生产部署。

### 7.3 实践
- **任务**：启用XLA，测试性能。
- **测试**：比较优化前后推理时间。

---

## 资源
- **官方文档**：[TensorFlow](https://www.tensorflow.org/)、[TF Serving](https://www.tensorflow.org/tfx/guide/serving)、[TF Lite](https://www.tensorflow.org/lite)
- **教程**：TensorFlow Tutorials、Google Cloud AI
- **工具**：Jupyter Notebook、VS Code、GitHub、Jira、Obsidian
- **建议**：用`notebooklm.google.com`记录训练流程，结合Obsidian或Jira优化任务管理。