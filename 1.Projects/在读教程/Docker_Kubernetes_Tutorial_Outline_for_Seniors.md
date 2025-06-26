# Docker Compose与Kubernetes教程大纲：面向大四学生的AI应用部署

## 目标
通过本教程，大四学生将学习如何使用**Docker Compose**快速部署AI应用，并逐步过渡到**Kubernetes（K8s）**，掌握容器编排、服务扩展和自我修复，构建高效的情感分析服务。教程强调Docker Compose的简易性和K8s的强大功能，适合AI应用的容器化部署。

## 目标读者
- **受众**：顶尖大学大四计算机科学学生，具备Python基础，熟悉AI/ML入门概念（如Hugging Face、REST API）。
- **先修知识**：Python、Docker基础、REST API、基本Linux命令。
- **工具**：Docker、Docker Compose、Kubernetes（Minikube或GKE）、Python 3.9+、kubectl、VS Code、Git.
- **时长**：6小时（1.5小时理论+4.5小时实践）。

## 教程形式
- **理论讲解**：介绍Docker Compose和K8s核心概念及AI部署应用。
- **实践环节**：容器化、编排、K8s部署练习。
- **格式**：交互式讲座、终端操作、迷你项目。

---

## 大纲内容

### 1. Docker Compose与K8s简介（30分钟）
- **目标**：了解Docker Compose和K8s在AI部署中的作用。
- **内容**：
  - Docker Compose：多容器编排，快速本地部署。
  - K8s核心：Pod、Deployment、Service、自动扩展。
  - AI场景：部署情感分析服务。
  - **反直觉洞察**：Docker Compose虽简单，但K8s的复杂性在生产环境中带来更大灵活性。
- **练习**：安装Docker Compose和Minikube，运行简单容器。

### 2. Docker Compose部署（1小时）
- **目标**：掌握Docker Compose部署AI服务。
- **内容**：
  - YAML配置：服务、端口、依赖。
  - 构建：Dockerfile+Compose文件。
  - AI用例：FastAPI情感分析服务。
- **练习**：用Docker Compose部署情感分析API。

### 3. K8s基础与Pod管理（1小时）
- **目标**：理解K8s基础，管理Pod。
- **内容**：
  - K8s架构：Node、Pod、Cluster。
  - YAML：Pod定义、Service暴露。
  - AI场景：迁移Compose服务到K8s。
  - **技术债务提示**：K8s配置复杂，需规范化YAML。
- **练习**：在Minikube部署情感分析Pod。

### 4. K8s高级功能（1小时）
- **目标**：掌握K8s Deployment和Service。
- **内容**：
  - Deployment：滚动更新、自我修复。
  - Service：负载均衡、DNS。
  - 工具：kubectl、K8s Dashboard。
- **练习**：配置Deployment，暴露Service。

### 5. 集成AI部署管道（1小时）
- **目标**：结合Docker Compose、K8s和GitHub Actions，构建AI部署流程。
- **内容**：
  - CI/CD：构建镜像，部署到GKE。
  - 工具：Git、Jira、Obsidian（如你的兴趣）。
  - 监控：K8s日志、资源使用。
- **练习**：配置CI/CD，部署到GKE。

### 6. 迷你项目：AI情感分析服务部署（1小时）
- **目标**：从Docker Compose过渡到K8s部署。
- **任务**：
  - Compose：本地部署FastAPI服务。
  - K8s：迁移到Minikube/GKE。
  - CI/CD：GitHub Actions自动化。
- **交付**：运行在K8s上的AI服务。

### 7. 优化与进阶（30分钟）
- **目标**：学习K8s优化和生态集成。
- **内容**：
  - 优化：HPA（水平扩展）、资源限制。
  - 进阶：K8s+Neo4j（如你的兴趣）、Helm。
  - 云部署：GKE、EKS.
- **练习**：配置HPA，优化资源。

### 8. 总结与Q&A（30分钟）
- **内容**：
  - 复习Docker Compose和K8s核心概念。
  - 讨论AI部署实践。
  - 推荐资源：Kubernetes文档、Docker指南。

---

## 学习成果
- 使用Docker Compose快速部署AI应用。
- 掌握K8s Pod、Deployment、Service管理。
- 理解从Compose到K8s的过渡路径。
- 管理技术债务，确保部署可维护。

## 资源
- **官方文档**：[Docker Compose](https://docs.docker.com/compose/)、[Kubernetes](https://kubernetes.io/docs/)
- **教程**：Kubernetes Up & Running、Docker Docs
- **工具**：Minikube、kubectl、VS Code、GitHub、Jira、Obsidian