# Neo4j教程辅助测试：面向大四学生的知识图谱与AI应用评估

## 目标
评估学生对Neo4j核心概念（Cypher查询、图数据库设计、RAG集成）的掌握情况，以及构建知识图谱和AI应用的能力。测试结合理论和实践，适合有Python基础的大四学生，强调复杂关系查询和RAG场景。

## 测试形式
- **类型**：选择题（10分）、简答题（20分）、编程题（70分）
- **时长**：90分钟
- **评分标准**：正确性（50%）、代码结构（30%）、创新性（20%）

---

## 第1部分：选择题（10分，每题2分）

1. Neo4j的主要用途是：  
   A. 关系型数据库  
   B. 图数据库  
   C. 文档数据库  
   D. 键值存储  
   **答案**：B

2. Cypher中的MATCH用于：  
   A. 创建节点  
   B. 查询图谱  
   C. 删除关系  
   D. 更新属性  
   **答案**：B

3. RAG的核心组件是：  
   A. 检索+生成  
   B. 训练+推理  
   C. 存储+查询  
   D. 索引+缓存  
   **答案**：A

4. 创建索引的Cypher命令是：  
   A. CREATE INDEX ON  
   B. ADD INDEX TO  
   C. SET INDEX FOR  
   D. BUILD INDEX WITH  
   **答案**：A

5. GitHub Actions主要用于：  
   A. 代码托管  
   B. CI/CD自动化  
   C. 数据存储  
   D. 模型推理  
   **答案**：B

---

## 第2部分：简答题（20分，每题10分）

1. **问题**：解释Neo4j知识图谱在RAG中的作用，并说明其优势。  
   **参考答案**：  
   - **作用**：存储实体与关系，增强检索精度。  
   - **优势**：高效查询复杂关系，支持语义推理。  
   - **评分点**：清晰描述作用，提及RAG场景。

2. **问题**：描述Cypher查询的优化策略，并说明如何避免技术债务。  
   **参考答案**：  
   - **优化**：使用索引、分析查询计划、减少路径遍历。  
   - **技术债务**：规范化图谱设计，定期清理冗余数据。  
   - **评分点**：准确描述优化，提到技术债务管理。

---

## 第3部分：编程题（70分）

### 编程题1：Cypher查询与图设计（30分）
- **任务**：编写Cypher脚本：
  - 创建Tweet与Sentiment节点和关系。
  - 查询包含“AI”的Tweet及其Sentiment。
- **要求**：
  - 使用索引优化。
  - 验证查询结果。
- **参考代码**：
  ```cypher
  CREATE INDEX ON :Tweet(text);
  CREATE (t:Tweet {id: "1", text: "I love AI!"})
  CREATE (s:Sentiment {label: "POSITIVE"})
  CREATE (t)-[:HAS_SENTIMENT]->(s);
  MATCH (t:Tweet)-[:HAS_SENTIMENT]->(s:Sentiment)
  WHERE t.text CONTAINS "AI"
  RETURN t.text, s.label;
  ```
- **测试**：
  - Neo4j Browser运行查询。
- **评分标准**：
  - 图创建（10分）：节点与关系正确。
  - 查询实现（10分）：返回正确结果。
  - 代码结构（5分）：清晰、可读。
  - 索引优化（5分）：正确使用索引。

### 编程题2：RAG管道与Docker（40分）
- **任务**：构建Neo4j RAG应用：
  - 加载CSV数据到知识图谱。
  - Cypher查询相关实体。
  - 集成Hugging Face生成回答。
  - 容器化应用。
- **要求**：
  - 处理查询错误。
  - 配置GitHub Actions。
- **参考 code**：
  ```python
  # src/rag.py
  from neo4j import GraphDatabase
  from transformers import pipeline
  import polars as pl

  class SentimentGraph:
      def __init__(self, uri, user, password):
          self.driver = GraphDatabase.driver(uri, auth=(user, password))

      def close(self):
          self.driver.close()

      def load_data(self, csv_file):
          try:
              df = pl.read_csv(csv_file)
              with self.driver.session() as session:
                  for record in df.iter_rows(named=True):
                      session.run(
                          "CREATE (t:Tweet {id: $id, text: $text}) "
                          "CREATE (s:Sentiment {label: $label}) "
                          "CREATE (t)-[:HAS_SENTIMENT]->(s)",
                          id=record["id"], text=record["text"], label=record["label"]
                      )
          except Exception as e:
              print(f"Error: {e}")

      def query_graph(self, keyword):
          try:
              with self.driver.session() as session:
                  result = session.run(
                      "MATCH (t:Tweet)-[:HAS_SENTIMENT]->(s:Sentiment) "
                      "WHERE t.text CONTAINS $keyword "
                      "RETURN t.text, s.label",
                      keyword=keyword
                  )
                  return [(record["t.text"], record["s.label"]) for record in result]
          except Exception as e:
              print(f"Query error: {e}")
              return []

  class RAGPipeline:
      def __init__(self, graph, model_name):
          self.graph = graph
          self.generator = pipeline("text-generation", model=model_name)

      def run(self, query, keyword):
          context = self.graph.query_graph(keyword)
          prompt = f"Query: {query}\nContext: {context}\nAnswer:"
          return self.generator(prompt, max_length=50)[0]["generated_text"]

  if __name__ == "__main__":
      graph = SentimentGraph("bolt://localhost:7687", "neo4j", "password")
      graph.load_data("data/tweets.csv")
      rag = RAGPipeline(graph, "distilgpt2")
      answer = rag.run("What is the sentiment about AI?", "AI")
      print(answer)
      graph.close()
  ```
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .
  CMD ["python", "src/rag.py"]
  ```
  ```yaml
  # .github/workflows/ci.yml
  name: CI/CD
  on: [push]
  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run RAG pipeline
        run: python src/rag.py
      - name: Build Docker image
        run: docker build -t ghcr.io/coleam00/sentiment-neo4j:latest .
      - name: Push to GitHub Packages
        run: |
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/coleam00/sentiment-neo4j:latest
  ```
  ```text
  # requirements.txt
  neo4j==5.12.0
  transformers==4.35.0
  polars==0.20.0
  ```
- **测试**：
  ```bash
  docker build -t sentiment-neo4j .
  docker run sentiment-neo4j
  ```
- **评分标准**：
  - 图加载（10分）：CSV数据正确导入。
  - Cypher查询（10分）：检索正确。
  - RAG集成（10分）：生成回答正常。
  - Docker与CI/CD（10分）：容器化与自动化成功。

---

## 注意事项
- **提交**：提交项目文件夹（包含`src/`、`Dockerfile`、`requirements.txt`、`.github/workflows/`、`data/`）。
- **测试环境**：Python 3.9+、Docker、Neo4j Desktop，安装`neo4j`、`transformers`、`polars`。
- **建议**：用`notebooklm.google.com`记录图谱设计，结合Obsidian或Jira跟踪任务。

## 评分总结
- **选择题**：考察基础概念。
- **简答题**：测试理论和设计思维。
- **编程题**：评估知识图谱与RAG开发能力，强调复杂关系查询。
- **反直觉洞察**：Neo4j虽复杂，但在RAG和AI推理中通过高效关系查询大幅提升性能。