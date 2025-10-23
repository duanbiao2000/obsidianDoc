# Streamlit教材：面向大四学生的AI交互界面开发

## 目标
本教材帮助大四学生掌握**Streamlit**，一个基于Python的框架，用于快速构建AI工具的交互界面，重点涵盖组件化设计及与Pandas/Plotly的集成，结合Hugging Face模型开发数据展示和模型交互原型。教材详尽、实用，适合有Python基础的学生，强调快速原型和生产级部署，契合你的Python偏好和AI研究兴趣。

## 前提条件
- **受众**：顶尖大学大四学生，熟悉Python和AI/ML入门。
- **先修知识**：Python（函数、类）、Pandas基础、HTTP、JSON。
- **工具**：Python 3.9+、pip、VS Code、Jupyter、Git。
- **时长**：6小时（1.5小时理论+4.5小时实践）。

---

## 第1章：Streamlit简介

### 1.1 为什么选择Streamlit？
- **优点**：
  - **快速原型**：几行代码构建交互界面，与你的Python偏好契合。
  - **Python原生**：无缝集成Pandas、Plotly、Hugging Face。
  - **交互性**：支持实时用户输入和数据展示。
  - **AI场景**：数据可视化、模型交互（如你的NotebookLM记录习惯）。
- **缺点**：
  - 不适合复杂UI（相比React）。
  - 性能在大规模数据上有限。
- **适用场景**：AI工具原型、数据分析仪表板。
- **反直觉洞察**：Streamlit的简单性是双刃剑，适合快速验证，但生产级应用需结合FastAPI或React优化。

### 1.2 安装与第一个页面
- **步骤**：
  1. 安装：`pip install streamlit`
  2. 创建应用：
     ```python
     import streamlit as st

     st.title("欢迎使用Streamlit！")
     st.write("Hello, AI World!")
     ```
  3. 运行：`streamlit run app.py`，访问`http://localhost:8501`。
- **实践**：运行代码，确认显示“Hello, AI World!”。

---

## 第2章：组件化设计

### 2.1 基本组件
- **文本与输入**：
  ```python
  import streamlit as st

  st.title("情感分析工具")
  text = st.text_input("输入文本", placeholder="请输入...")
  if st.button("预测"):
      st.write(f"你输入了：{text}")
  ```
- **选择器**：
  ```python
  option = st.selectbox("选择情感类型", ["正面", "负面"])
  st.write(f"你选择了：{option}")
  ```
<!--ID: 1761111103882-->


### 2.2 布局
- **列布局**：
  ```python
  col1, col2 = st.columns(2)
  with col1:
      st.write("左列：输入")
      text = st.text_input("文本")
  with col2:
      st.write("右列：结果")
      st.write("待预测...")
  ```
- **侧边栏**：
  ```python
  st.sidebar.title("设置")
  model = st.sidebar.selectbox("选择模型", ["DistilBERT", "BERT"])
  ```

### 2.3 实践
- **任务**：创建情感分析输入表单，包含文本输入、按钮和侧边栏模型选择。
- **代码**：
  ```python
  import streamlit as st

  st.title("情感分析原型")
  st.sidebar.title("模型设置")
  model = st.sidebar.selectbox("选择模型", ["DistilBERT", "BERT"])
  text = st.text_input("输入文本", placeholder="请输入...")
  if st.button("预测"):
      st.write(f"使用{model}预测：{text}")
  ```
- **测试**：输入文本，点击预测，确认显示结果。
<!--ID: 1761111103897-->


---

## 第3章：Pandas集成

### 3.1 Pandas基础
- **加载数据**：
  ```python
  import pandas as pd

  data = pd.DataFrame({
      "文本": ["这很好", "不太好"],
      "预测": ["正面", "负面"]
  })
  ```

### 3.2 Streamlit展示
- **表格**：
  ```python
  import streamlit as st
  import pandas as pd

  st.title("预测历史")
  data = pd.DataFrame({
      "文本": ["这很好", "不太好"],
      "预测": ["正面", "负面"]
  })
  st.dataframe(data)
  ```
- **交互表格**：
  ```python
  st.table(data)
  ```

### 3.3 实践
- **任务**：展示情感预测历史。
- **代码**：
  ```python
  import streamlit as st
  import pandas as pd

  st.title("情感分析历史")
  if "history" not in st.session_state:
      st.session_state.history = pd.DataFrame(columns=["文本", "预测"])
  text = st.text_input("输入文本")
  if st.button("预测"):
      new_row = pd.DataFrame({"文本": [text], "预测": ["正面" if "好" in text else "负面"]})
      st.session_state.history = pd.concat([st.session_state.history, new_row], ignore_index=True)
  st.dataframe(st.session_state.history)
  ```
- **技术债务提示**：Pandas在超大数据集上慢，考虑Polars替换。
<!--ID: 1761111103915-->


---

## 第4章：Plotly集成

### 4.1 Plotly基础
- **柱状图**：
  ```python
  import plotly.express as px

  data = pd.DataFrame({
      "情感": ["正面", "负面"],
      "置信度": [0.9, 0.7]
  })
  fig = px.bar(data, x="情感", y="置信度", title="情感预测置信度")
  ```

### 4.2 Streamlit集成
- **展示图表**：
  ```python
  import streamlit as st
  import plotly.express as px
  import pandas as pd

  st.title("情感分析可视化")
  data = pd.DataFrame({
      "情感": ["正面", "负面"],
      "置信度": [0.9, 0.7]
  })
  fig = px.bar(data, x="情感", y="置信度", title="情感预测置信度")
  st.plotly_chart(fig)
  ```

### 4.3 实践
- **任务**：可视化情感预测置信度。
- **代码**：
  ```python
  import streamlit as st
  import plotly.express as px
  import pandas as pd

  st.title("情感预测置信度")
  if "scores" not in st.session_state:
      st.session_state.scores = pd.DataFrame(columns=["情感", "置信度"])
  text = st.text_input("输入文本")
  if st.button("预测"):
      score = 0.9 if "好" in text else 0.7
      new_row = pd.DataFrame({"情感": ["正面" if "好" in text else "负面"], "置信度": [score]})
      st.session_state.scores = pd.concat([st.session_state.scores, new_row], ignore_index=True)
  if not st.session_state.scores.empty:
      fig = px.bar(st.session_state.scores, x="情感", y="置信度", title="预测置信度分布")
      st.plotly_chart(fig)
  ```

---

## 第5章：集成AI模型

### 5.1 加载Hugging Face模型
- **安装**：`pip install transformers`
- **代码**：
  ```python
  import streamlit as st
  from transformers import pipeline

  st.title("情感分析工具")
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
  text = st.text_input("输入文本", placeholder="请输入...")
  if st.button("预测"):
      try:
          if not text:
              st.error("请输入文本！")
          else:
              result = classifier(text)[0]
              st.write(f"预测：{result['label']} (置信度：{result['score']:.2f})")
      except Exception as e:
          st.error(f"错误：{e}")
  ```

### 5.2 优化与错误处理
- **预加载**：启动时加载模型。
- **缓存**：使用`@st.cache_resource`：
  ```python
  @st.cache_resource
  def load_model():
      return pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
  classifier = load_model()
  ```
- **实践**：测试空输入和有效输入，确认错误处理和预测结果。

---

## 第6章：迷你项目——AI情感分析交互应用

### 6.1 项目目标
构建Streamlit应用，包含：
- 表单：用户输入文本。
- 预测：调用Hugging Face模型。
- 展示：Pandas表格+Plotly图表。

### 6.2 项目结构
```
sentiment_app/
├── app.py
└── requirements.txt
```

### 6.3 实现
- **应用**（`app.py`）：
  ```python
  import streamlit as st
  import pandas as pd
  import plotly.express as px
  from transformers import pipeline

  st.title("AI情感分析工具")
  st.sidebar.title("设置")
  model = st.sidebar.selectbox("选择模型", ["DistilBERT", "BERT"])

  @st.cache_resource
  def load_model():
      return pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
  classifier = load_model()

  if "history" not in st.session_state:
      st.session_state.history = pd.DataFrame(columns=["文本", "预测", "置信度"])

  col1, col2 = st.columns(2)
  with col1:
      text = st.text_input("输入文本", placeholder="请输入...")
      if st.button("预测"):
          if not text:
              st.error("请输入文本！")
          else:
              result = classifier(text)[0]
              new_row = pd.DataFrame({
                  "文本": [text],
                  "预测": [result['label']],
                  "置信度": [result['score']]
              })
              st.session_state.history = pd.concat([st.session_state.history, new_row], ignore_index=True)
              st.success(f"预测：{result['label']} (置信度：{result['score']:.2f})")

  with col2:
      st.write("预测历史")
      st.dataframe(st.session_state.history)

  if not st.session_state.history.empty:
      fig = px.bar(st.session_state.history, x="预测", y="置信度", title="置信度分布", hover_data=["文本"])
      st.plotly_chart(fig)
  ```
- **依赖**（`requirements.txt`）：
  ```
  streamlit==1.28.0
  pandas==2.1.0
  plotly==5.18.0
  transformers==4.35.0
  ```

### 6.4 测试
- 运行：`streamlit run app.py`。
- 测试：输入“I love AI!”，确认显示预测、表格和图表。

---

## 第7章：部署与进阶

### 7.1 部署
- **本地**：`streamlit run app.py`。
- **云部署**：
  - Streamlit Cloud：推送GitHub仓库，自动部署。
  - Heroku：配置`Procfile`（`web: streamlit run app.py`）。
- **Docker**：
  ```dockerfile
  FROM python:3.9
  WORKDIR /app
  COPY . .
  RUN pip install -r requirements.txt
  CMD ["streamlit", "run", "app.py"]
  ```

### 7.2 技术债务管理
- **依赖**：用`pip freeze > requirements.txt`锁定版本。
- **模块化**：分离模型逻辑到`models.py`。
- **优化**：用Polars替换Pandas处理大数据。

### 7.3 进阶
- **FastAPI**：后端分离，提升性能。
- **Neo4j**：存储预测关系（如你的兴趣）。
- **React**：复杂UI替换Streamlit。

---

## 资源
- **官方文档**：[Streamlit](https://docs.streamlit.io/)
- **教程**：Streamlit官方教程、Plotly文档
- **工具**：VS Code、Jupyter、Streamlit Cloud、GitHub
- **建议**：用`notebooklm.google.com`记录开发笔记，尝试XMind规划组件布局。