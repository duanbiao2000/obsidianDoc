# TensorFlow教程辅助测试：面向大四学生的AI模型生产部署评估

## 目标
评估学生对TensorFlow（Keras、TF Serving、TF Lite）的掌握情况，以及开发和部署AI模型的能力。测试结合理论和实践，适合有Python基础的大四学生，强调生产和边缘部署。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. TensorFlow Serving的主要用途是：  
   A. 模型训练  
   B. 模型部署与服务  
   C. 数据预处理  
   D. 模型优化  
   **答案**：B

2. Keras API属于：  
   A. 低级TensorFlow API  
   B. 高级建模接口  
   C. 数据库接口  
   D. 部署工具  
   **答案**：B

3. TF Lite用于：  
   A. 云端推理  
   B. 移动/边缘设备  
   C. 数据可视化  
   D. 分布式训练  
   **答案**：B

4. 模型量化的作用是：  
   A. 增加模型参数  
   B. 减少模型大小和延迟  
   C. 提高训练速度  
   D. 增强模型精度  
   **答案**：B

5. GitHub Actions主要用于：  
   A. 代码托管  
   B. CI/CD自动化  
   C. 数据存储  
   D. 模型推理  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释TensorFlow在生产部署中的优势，并说明TF Serving的局限性。  
   **参考答案**：  
   - **优势**：生态成熟，支持大规模和边缘部署，Google背书。  
   - **局限性**：冷启动延迟，版本管理复杂。  
   - **评分点**：清晰描述优势与局限，提及部署场景。

2. **问题**：描述模型量化的作用，并说明在边缘部署中的注意事项。  
   **参考答案**：  
   - **作用**：减小模型大小，降低推理延迟。  
   - **注意事项**：确保精度损失可控，测试设备兼容性。  
   - **评分点**：准确描述作用，提到注意事项。

---

## 第3部分：编程题（70分）

### 编程题1：Keras模型开发（30分）
- **任务**：编写Keras模型：
  - 实现健康状态分类（二分类）。
  - 使用Sequential API。
- **要求**：
  - 包含数据预处理。
  - 验证模型训练。
- **参考代码**：
  ```python
  import tensorflow as tf
  from tensorflow.keras import layers
  import numpy as np

  # 模拟数据
  X = np.random.rand(100, 5)
  y = np.random.randint(0, 2, 100)

  model = tf.keras.Sequential([
      layers.Dense(16, activation='relu', input_shape=(5,)),
      layers.Dense(1, activation='sigmoid')
  ])
  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
  model.fit(X, y, epochs=10, validation_split=0.2)
  ```
- **测试**：
  ```bash
  python model.py
  ```
- **评分标准**：
  - 模型构建（10分）：正确定义结构。
  - 数据预处理（10分）：正确处理输入。
  - 代码结构（5分）：清晰、可读。
  - 训练验证（5分）：模型正常训练。

### 编程题2：TF Serving与TF Lite部署（40分）
- **任务**：部署情感分析模型：
  - Keras：训练模型。
  - TF Serving：云端部署。
  - TF Lite：边缘优化。
- **要求**：
  - 处理推理错误。
  - 配置CI/CD。
- **参考 code**：
  ```python
  # model/train.py
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
  ```dockerfile
  # serving/Dockerfile
  FROM tensorflow/serving
  COPY sentiment_model /models/sentiment_model
  ENV MODEL_NAME=sentiment_model
  ```
  ```python
  # tflite/convert.py
  import tensorflow as tf

  converter = tf.lite.TFLiteConverter.from_saved_model('sentiment_model/1')
  converter.optimizations = [tf.lite.Optimize.DEFAULT]
  tflite_model = converter.convert()
  with open('sentiment_model.tflite', 'wb') as f:
      f.write(tflite_model)
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
        run: pip install tensorflow==2.15.0
      - name: Train and export
        run: python model/train.py
      - name: Build Docker image
        run: |
          docker build -t ghcr.io/coleam00/sentiment-serving:latest ./serving
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/coleam00/sentiment-serving:latest
  ```
  ```python
  # test_serving.py
  import requests
  import json
  import numpy as np
  from tensorflow.keras.preprocessing.text import Tokenizer
  from tensorflow.keras.preprocessing.sequence import pad_sequences

  tokenizer = Tokenizer(num_words=1000)
  tokenizer.fit_on_texts(["I love AI!", "AI is hard"])
  data = {
      "instances": [{"input_1": pad_sequences(tokenizer.texts_to_sequences(["I love AI!"]), maxlen=10).tolist()}]
  }
  try:
      response = requests.post('http://localhost:8501/v1/models/sentiment_model:predict', json=data)
      print(response.json())
  except Exception as e:
      print(f"Error: {e}")
  ```
- **测试**：
  ```bash
  docker run -p 8501:8501 -v "$(pwd)/sentiment_model:/models/sentiment_model" -e MODEL_NAME=sentiment_model tensorflow/serving
  python test_serving.py
  ```
- **评分标准**：
  - Keras训练（10分）：模型正确训练。
  - TF Serving部署（10分）：API正常调用。
  - TF Lite转换（10分）：模型优化成功。
  - CI/CD配置（10分）：自动化部署正常。

---

## 注意事项
- **提交**：提交项目文件夹（包含`model/`、`serving/`、`tflite/`、`.github/workflows/`）。
- **测试环境**：Python 3.9+、Docker、TensorFlow 2.15.0。
- **建议**：用`notebooklm.google.com`记录部署流程，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估AI部署能力，强调生产和边缘环境。
- **反直觉洞察**：TensorFlow通过生态支持简化生产部署，但优化和版本管理需谨慎。