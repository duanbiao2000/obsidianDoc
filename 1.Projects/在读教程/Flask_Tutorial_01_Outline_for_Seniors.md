# Flask Tutorial Outline for Senior Students: Building Small-Scale AI Applications

## Objective
Equip senior computer science students with the skills to use **Flask**, a lightweight Python web framework, to rapidly prototype and deploy small-scale AI applications. This tutorial emphasizes Flask’s simplicity for independent developers, focusing on routing, templates, and blueprints, with integration into AI workflows. Designed for students with basic Python knowledge and interest in AI development.

## Target Audience
- **Big Four Students**: Final-year undergraduates at top universities with Python programming experience.
- **Prerequisites**: Familiarity with Python, basic HTML/CSS, and introductory AI/ML concepts (e.g., scikit-learn or Hugging Face).
- **Goals**: Build a functional AI-powered web app prototype (e.g., text classifier) and understand Flask’s role in AI development.

## Tutorial Duration
- **Total**: 6 hours (2-hour lecture + 4-hour hands-on workshop)
- **Format**: Interactive lecture, coding exercises, and a mini-project.

---

## Tutorial Outline

### 1. Introduction to Flask (30 minutes)
- **Objective**: Understand Flask’s role as a lightweight framework for AI prototyping.
- **Content**:
  - **Why Flask?** 
    - **Pros**: Minimalist, easy to learn, fast setup for small AI apps (e.g., serving ML model predictions).
    - **Cons**: Limited scalability for high-concurrency apps compared to FastAPI or Django.
  - **Use Cases**: Rapid prototyping, small-scale AI APIs, proof-of-concept apps.
  - **Comparison**: Flask vs. FastAPI (async) vs. Django (batteries-included).
  - **Subversive Insight**: Flask’s simplicity is a superpower for solo developers, but over-reliance can lead to messy codebases. Plan for modularity early.
- **Exercise**: Install Flask (`pip install flask`) and run a "Hello, World!" app.
- **Tools**: Python 3.9+, pip, VS Code.

### 2. Core Flask Concepts: Routing (1 hour)
- **Objective**: Master Flask’s routing to handle HTTP requests for AI applications.
- **Content**:
  - **Routing Basics**: Define routes with `@app.route('/')` for GET/POST requests.
  - **Dynamic Routes**: Handle variable URLs (e.g., `/predict/<input_text>`).
  - **Request Handling**: Access query parameters (`request.args`) and form data (`request.form`).
  - **AI Integration**: Serve predictions from a pre-trained model (e.g., scikit-learn classifier).
  - **Technical Debt Warning**: Hardcoded routes can clutter code. Use blueprints for large apps.
- **Exercise**:
  - Create a route `/predict` that accepts a text input and returns a mock sentiment prediction.
  - Test with `curl` or Postman.
- **Code Example**:
  ```python
  from flask import Flask, request
  app = Flask(__name__)

  @app.route('/predict', methods=['POST'])
  def predict():
      text = request.form['text']
      # Mock AI model
      prediction = 'positive' if 'good' in text.lower() else 'negative'
      return {'prediction': prediction}
  ```

### 3. Templates: Building User Interfaces (1 hour)
- **Objective**: Use Flask’s Jinja2 templating to create simple frontends for AI apps.
- **Content**:
  - **Jinja2 Basics**: Render HTML templates with dynamic data (`render_template`).
  - **Template Structure**: Separate HTML/CSS from Python logic.
  - **AI Use Case**: Display model predictions in a web interface (e.g., sentiment analysis result).
  - **Best Practices**: Keep templates minimal to avoid frontend complexity.
  - **Subversive Insight**: Templates are quick for prototypes but can become unmaintainable. Consider Streamlit for AI-focused UIs in production.
- **Exercise**:
  - Create an HTML form (`index.html`) to input text and display predictions.
  - Use Jinja2 to render results dynamically.
- **Code Example**:
  ```html
  <!-- templates/index.html -->
  <!DOCTYPE html>
  <html>
  <body>
      <form method="POST" action="/predict">
          <input type="text" name="text" placeholder="Enter text">
          <input type="submit" value="Predict">
      </form>
      {% if prediction %}
          <p>Prediction: {{ prediction }}</p>
      {% endif %}
  </body>
  </html>
  ```

### 4. Blueprints: Structuring Flask Apps (1 hour)
- **Objective**: Organize Flask apps for modularity and scalability.
- **Content**:
  - **What Are Blueprints?**: Modularize routes into separate files (e.g., `api.py`, `web.py`).
  - **Setup**: Register blueprints with `app.register_blueprint`.
  - **AI Application**: Separate AI model endpoints (e.g., `/predict`) from static pages (e.g., `/home`).
  - **Technical Debt Warning**: Without blueprints, large apps become unmanageable. Plan folder structure early.
  - **Subversive Insight**: Blueprints seem overkill for small apps, but they future-proof your prototype for collaboration or scaling.
- **Exercise**:
  - Refactor the `/predict` route into a blueprint (`ai_blueprint.py`).
  - Test the modular app structure.
- **Code Example**:
  ```python
  # ai_blueprint.py
  from flask import Blueprint, request
  ai_bp = Blueprint('ai', __name__)

  @ai_bp.route('/predict', methods=['POST'])
  def predict():
      text = request.form['text']
      return {'prediction': 'positive' if 'good' in text.lower() else 'negative'}

  # app.py
  from flask import Flask
  from ai_blueprint import ai_bp
  app = Flask(__name__)
  app.register_blueprint(ai_bp, url_prefix='/api')
  ```

### 5. Integrating AI Models with Flask (1.5 hours)
- **Objective**: Deploy a pre-trained AI model via Flask API.
- **Content**:
  - **Model Loading**: Load a pre-trained model (e.g., scikit-learn or Hugging Face Transformers).
  - **API Endpoint**: Create a `/predict` endpoint to serve model predictions.
  - **Input Validation**: Use `request.json` for JSON inputs and validate with Pydantic (optional).
  - **Error Handling**: Return meaningful HTTP status codes (e.g., 400 for bad input).
  - **Performance Tip**: Preload models at app startup to reduce latency.
- **Exercise**:
  - Load a pre-trained Hugging Face sentiment model (`distilbert-base-uncased-finetuned-sst-2-english`).
  - Create a `/predict` endpoint to accept text and return sentiment.
- **Code Example**:
  ```python
  from flask import Flask, request, jsonify
  from transformers import pipeline
  app = Flask(__name__)
  classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

  @app.route('/predict', methods=['POST'])
  def predict():
      try:
          data = request.json
          text = data['text']
          result = classifier(text)[0]
          return jsonify({'prediction': result['label'], 'score': result['score']})
      except Exception as e:
          return jsonify({'error': str(e)}), 400
  ```

### 6. Mini-Project: AI-Powered Sentiment Analysis Web App (1 hour)
- **Objective**: Build a complete Flask app integrating routing, templates, blueprints, and an AI model.
- **Tasks**:
  - Create a homepage with a form to input text.
  - Use a blueprint for the `/api/predict` endpoint with a Hugging Face model.
  - Display predictions in a styled HTML template.
  - Handle errors gracefully (e.g., empty input).
- **Deliverable**: A running Flask app accessible at `localhost:5000`.
- **Subversive Insight**: Prototypes don’t need to be perfect. Focus on functionality, then refactor for production with FastAPI or Docker.

### 7. Deployment and Next Steps (30 minutes)
- **Objective**: Understand Flask deployment and plan for production.
- **Content**:
  - **Local Testing**: Run Flask with `app.run(debug=True)`.
  - **Production Deployment**: Use Gunicorn + Nginx or cloud platforms (e.g., Heroku, GCP).
  - **Scaling Limits**: Flask’s synchronous nature limits high-concurrency apps. Consider FastAPI for async needs.
  - **Technical Debt Management**:
    - Use `requirements.txt` for dependency tracking.
    - Modularize with blueprints to ease future refactoring.
    - Document API with OpenAPI (e.g., Flask-RESTX).
  - **Next Steps**:
    - Integrate with Docker for portability.
    - Explore FastAPI for async AI APIs.
    - Learn React for advanced frontends.
- **Exercise**: Generate a `requirements.txt` and deploy the mini-project to Heroku.

### 8. Q&A and Wrap-Up (30 minutes)
- **Content**:
  - Address student questions on Flask, AI integration, or technical debt.
  - Discuss real-world use cases (e.g., your `ragas_rag_agent_knowledge_graph.cypher` could be served via Flask).
  - Recommend resources: Flask docs, Hugging Face tutorials, Real Python.
- **Subversive Insight**: Flask is a starting point, not an endgame. Its simplicity lets you ship fast, but plan to migrate to scalable frameworks as your AI apps grow.

---

## Learning Outcomes
- Build and deploy a Flask app with routing, templates, and blueprints.
- Integrate an AI model (e.g., Hugging Face) into a web API.
- Understand Flask’s strengths (simplicity) and limitations (scalability).
- Manage technical debt by planning modular code and dependencies.

## Resources
- **Official Docs**: [Flask Documentation](https://flask.palletsprojects.com/)
- **Tutorials**: Real Python’s Flask series, Hugging Face Transformers guide.
- **Tools**: VS Code, Postman, Heroku, GitHub for version control.

## Instructor Notes
- Emphasize hands-on coding over theory.
- Use your `notebooklm.google.com` habit to encourage students to document their Flask experiments.
- Highlight Flask’s role in rapid AI prototyping, aligning with your AI research interest.
- Warn against over-engineering small apps but stress modularity for future growth.