# Streamlit教程辅助测试：面向大四学生的AI交互界面评估

## 目标
评估学生对Streamlit核心概念（组件化设计、Pandas/Plotly集成）的掌握情况，以及构建AI交互界面的能力。测试结合理论和实践，适合有Python基础的大四学生，强调数据展示和模型交互。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Streamlit的主要优势是：  
   A. 高并发处理  
   B. 快速构建交互界面  
   C. 内置AI模型  
   D. 复杂UI支持  
   **答案**：B

2. 以下哪个Streamlit组件用于输入文本？  
   A. `st.write`  
   B. `st.text_input`  
   C. `st.dataframe`  
   D. `st.plotly_chart`  
   **答案**：B

3. Pandas在Streamlit中常用于：  
   A. 实时通信  
   B. 数据展示  
   C. 模型训练  
   D. 布局管理  
   **答案**：B

4. Plotly与Streamlit集成的函数是：  
   A. `st.plot`  
   B. `st.plotly_chart`  
   C. `st.chart`  
   D. `st.graph`  
   **答案**：B

5. Streamlit生产部署的推荐平台是：  
   A. Postman  
   B. Streamlit Cloud  
   C. Uvicorn  
   D. PM2  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Streamlit组件和Pandas集成的区别，并说明在AI数据展示中的应用。  
   **参考答案**：  
   - **区别**：组件（如`st.text_input`）构建交互UI，Pandas处理和展示结构化数据（如`st.dataframe`）。  
   - **AI应用**：组件接受用户输入（如文本），Pandas展示预测历史表格。  
   - **评分点**：清晰对比两者，提及AI场景。

2. **问题**：描述Streamlit的部署流程，并说明如何避免技术债务。  
   **参考答案**：  
   - **部署**：本地用`streamlit run`，云端用Streamlit Cloud或Heroku，需配置`requirements.txt`。  
   - **技术债务**：模块化代码，锁定依赖版本，定期重构。  
   - **评分点**：准确描述部署，提到模块化和依赖管理。

---

## 第3部分：编程题（70分）

### 编程题1：组件与Pandas（30分）
- **任务**：编写Streamlit应用，包含：
  - 文本输入表单，接受用户输入。
  - 使用Pandas展示预测历史表格。
- **要求**：
  - 处理空输入错误。
  - 显示模拟预测结果。
- **参考代码**：
  ```python
  import streamlit as st
  import pandas as pd

  st.title("情感分析原型")
  if "history" not in st.session_state:
      st.session_state.history = pd.DataFrame(columns=["文本", "预测"])

  text = st.text_input("输入文本", placeholder="请输入...")
  if st.button("预测"):
      if not text:
          st.error("请输入文本！")
      else:
          new_row = pd.DataFrame({"文本": [text], "预测": ["正面" if "好" in text else "负面"]})
          st.session_state.history = pd.concat([st.session_state.history, new_row], ignore_index=True)
          st.success(f"预测：{'正面' if '好' in text else '负面'}")

  st.write("预测历史")
  st.dataframe(st.session_state.history)
  ```
- **评分标准**：
  - 组件功能（10分）：正确渲染表单。
  - Pandas展示（10分）：表格正常显示。
  - 错误处理（5分）：处理空输入。
  - 代码结构（5分）：清晰、可读。

### 编程题2：Plotly与AI集成（40分）
- **任务**：构建Streamlit应用，包含：
  - 文本输入，调用Hugging Face模型。
  - 使用Plotly可视化预测置信度。
- **要求**：
  - 使用`@st.cache_resource`优化模型加载。
  - 处理错误（如无效输入）。
- **参考 code**：
  ```python
  import streamlit as st
  import pandas as pd
  import plotly.express as px
  from transformers import pipeline

  st.title("AI情感分析工具")
  @st.cache_resource
  def load_model():
      return pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
  classifier = load_model()

  if "history" not in st.session_state:
      st.session_state.history = pd.DataFrame(columns=["文本", "预测", "置信度"])

  text = st.text_input("输入文本", placeholder="请输入...")
  if st.button("预测"):
      try:
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
      except Exception as e:
          st.error(f"错误：{e}")

  if not st.session_state.history.empty:
      st.write("预测历史")
      st.dataframe(st.session_state.history)
      fig = px.bar(st.session_state.history, x="预测", y="置信度", title="置信度分布", hover_data=["文本"])
      st.plotly_chart(fig)
  ```
- **评分标准**：
  - AI集成（15分）：Hugging Face模型工作。
  - Plotly可视化（10分）：图表正确显示。
  - 错误处理（10分）：处理无效输入。
  - 代码结构（5分）：清晰、注释完善。

---

## 注意事项
- **提交**：提交项目文件夹（包含`app.py`、`requirements.txt`）。
- **测试环境**：Python 3.9+，安装`streamlit`、`pandas`、`plotly`、`transformers`。
- **建议**：记录调试过程（如你的`notebooklm.google.com`习惯），便于优化界面设计。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估开发能力，强调Pandas/Plotly和AI集成。
- **反直觉洞察**：Streamlit适合快速AI原型，但需规划模块化以应对未来扩展。