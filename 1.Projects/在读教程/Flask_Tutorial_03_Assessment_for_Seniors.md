# Flask教程辅助测试：面向大四学生的AI应用开发评估

## 目标
评估学生对Flask核心概念（路由、模板、蓝图）以及AI模型集成的掌握情况，确保能够快速构建小型AI应用原型。测试结合理论和实践，适合有Python基础的大四学生，强调实用性和AI场景。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Flask的主要优势是什么？  
   A. 高并发处理能力  
   B. 轻量级，适合快速原型  
   C. 内置ORM和用户认证  
   D. 自动生成前端UI  
   **答案**：B

2. 以下哪个方法用于处理POST请求中的表单数据？  
   A. `request.args`  
   B. `request.form`  
   C. `request.json`  
   D. `request.params`  
   **答案**：B

3. 蓝图（Blueprint）的主要作用是：  
   A. 渲染HTML模板  
   B. 模块化路由组织  
   C. 优化数据库查询  
   D. 管理AI模型  
   **答案**：B

4. 在Flask中，`render_template`的作用是：  
   A. 发送JSON响应  
   B. 加载静态CSS文件  
   C. 渲染Jinja2模板  
   D. 处理HTTP路由  
   **答案**：C

5. 以下哪个工具适合部署Flask生产应用？  
   A. `app.run(debug=True)`  
   B. Gunicorn + Nginx  
   C. Jupyter Notebook  
   D. Postman  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Flask中路由和模板的区别，并举例说明如何结合两者实现用户输入的AI预测功能。  
   **参考答案**：  
   - **路由**：定义URL到Python函数的映射，处理HTTP请求。如`@app.route('/predict', methods=['POST'])`处理用户提交的文本。  
   - **模板**：使用Jinja2渲染动态HTML，如`index.html`显示预测结果。  
   - **示例**：用户通过表单提交文本，路由调用AI模型（如Hugging Face）预测，模板显示结果。  
   - **评分点**：清晰区分路由（后端逻辑）和模板（前端展示），提及AI集成。

2. **问题**：描述蓝图在Flask项目中的作用，并说明如何避免技术债务。  
   **参考答案**：  
   - **作用**：蓝图将路由分组，模块化代码（如`ai_blueprint.py`处理AI端点），提高可维护性。  
   - **技术债务**：不用蓝图会导致路由混乱。解决方法：初期规划项目结构，使用蓝图分离功能，定期重构。  
   - **评分点**：准确描述蓝图功能，提到模块化和技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：基础路由与模板（30分）
- **任务**：编写一个Flask应用，包含：
  - 一个主页路由（`/`），渲染`index.html`模板，包含文本输入表单。
  - 一个预测路由（`/predict`），接受POST请求，返回“正面”或“负面”（基于输入是否包含“好”）。
- **要求**：
  - 使用Jinja2模板显示结果。
  - 添加基本CSS样式。
- **参考代码**：
  ```python
  # app.py
  from flask import Flask, render_template, request
  app = Flask(__name__)

  @app.route('/', methods=['GET', 'POST'])
  def index():
      if request.method == 'POST':
          text = request.form['text']
          prediction = '正面' if '好' in text else '负面'
          return render_template('index.html', prediction=prediction)
      return render_template('index.html')
  ```
  ```html
  <!-- templates/index.html -->
  <!DOCTYPE html>
  <html>
  <head>
      <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  </head>
  <body>
      <h1>简单情感分析</h1>
      <form method="POST">
          <input type="text" name="text" placeholder="输入文本">
          <input type="submit" value="预测">
      </form>
      {% if prediction %}
          <p>预测：{{ prediction }}</p>
      {% endif %}
  </body>
  </html>
  ```
  ```css
  /* static/style.css */
  body { font-family: Arial; margin: 40px; }
  input[type=text] { padding: 8px; width: 200px; }
  input[type=submit] { padding: 8px 16px; }
  ```
- **评分标准**：
  - 路由功能（10分）：正确处理GET/POST。
  - 模板渲染（10分）：动态显示预测。
  - 样式（5分）：CSS应用正确。
  - 代码结构（5分）：清晰、可读。

### 编程题2：蓝图与AI集成（40分）
- **任务**：构建一个Flask应用，使用蓝图和Hugging Face模型，提供情感分析API。
- **要求**：
  - 创建蓝图`ai_blueprint.py`，包含`/predict`端点（接受JSON输入，返回预测和置信度）。
  - 主应用渲染模板，显示API调用结果。
  - 处理错误（如空输入）。
- **参考代码**：
  ```python
  # ai_blueprint.py
  from flask import Blueprint, request, jsonify
  from transformers import pipeline
  ai_bp = Blueprint('ai', __name__)
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @ai_bp.route('/predict', methods=['POST'])
  def predict():
      try:
          data = request.json
          text = data['text']
          if not text:
              return jsonify({'error': '文本不能为空'}), 400
          result = classifier(text)[0]
          return jsonify({'prediction': result['label'], 'score': result['score']})
      except Exception as e:
          return jsonify({'error': str(e)}), 400
  ```
  ```python
  # app.py
  from flask import Flask, render_template, request
  from ai_blueprint import ai_bp
  import requests

  app = Flask(__name__)
  app.register_blueprint(ai_bp, url_prefix='/api')

  @app.route('/', methods=['GET', 'POST'])
  def index():
      prediction = None
      if request.method == 'POST':
          text = request.form['text']
          response = requests.post('http://localhost:5000/api/predict', json={'text': text})
          prediction = response.json()
      return render_template('index.html', prediction=prediction)
  ```
  ```html
  <!-- templates/index.html -->
  <!DOCTYPE html>
  <html>
  <head>
      <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  </head>
  <body>
      <h1>情感分析工具</h1>
      <form method="POST">
          <input type="text" name="text" placeholder="输入文本">
          <input type="submit" value="预测">
      </form>
      {% if prediction %}
          <p>预测：{{ prediction.prediction }} (置信度：{{ '%.2f' % prediction.score }})</p>
      {% endif %}
  </body>
  </html>
  ```
- **评分标准**：
  - 蓝图实现（10分）：正确模块化。
  - AI集成（15分）：Hugging Face模型正常工作。
  - 错误处理（10分）：处理空输入或异常。
  - 代码结构（5分）：清晰、注释完善。

---

## 注意事项
- **提交**：学生需提交项目文件夹（包含`app.py`、`ai_blueprint.py`、`templates/`、`static/`）。
- **测试环境**：Python 3.9+，安装`flask`和`transformers`。
- **建议**：记录调试过程（如你的`notebooklm.google.com`习惯），便于复盘和优化。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论理解和设计思维。
- **编程题**：评估实际开发能力，强调AI集成和代码结构。
- **反直觉洞察**：Flask简单易用，但成功的关键在于模块化设计和错误处理，为未来扩展（如你的Neo4j兴趣）打基础。