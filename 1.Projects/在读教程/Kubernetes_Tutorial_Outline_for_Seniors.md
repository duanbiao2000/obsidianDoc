# Kubernetes教程大纲：面向大四学生的容器化AI应用管理

## 目标
通过本教程，大四学生将学习如何使用**Kubernetes**管理容器化AI应用，掌握Pod、Service和Helm，构建高可用、可扩展的AI服务部署管道。教程强调Kubernetes在AI规模化中的关键作用，适合未来生产级需求。

## 目标读者
- **受众**：顶尖大学大四计算机科学学生，具备Python、Docker基础，熟悉AI/ML入门概念（如Hugging Face、FastAPI）。
- **先修知识**：Python、Docker、Linux命令、YAML、REST API。
- **工具**：Kubernetes（Minikube或GKE/EKS）、kubectl、Helm、Docker Desktop、Python 3.9+、VS Code、Git。
- **时长**：8小时（2小时理论+6小时实践）。

## 教程形式
- **理论讲解**：介绍Kubernetes核心概念和AI应用管理。
- **实践环节**：Pod配置、Service暴露、Helm部署练习。
- **格式**：交互式讲座、终端操作、迷你项目。

---

## 大纲内容

### 1. Kubernetes简介（30分钟）
- **目标**：了解Kubernetes在AI部署中的优势。
- **内容**：
  - Kubernetes核心：容器编排、高可用性、自动扩展。
  - 与Docker Compose对比：生产级管理。
  - AI场景：扩展情感分析推理服务。
  - **反直觉洞察**：Kubernetes复杂性高，但简化大规模AI部署。
- **练习**：安装Minikube，运行`kubectl get nodes`。

### 2. Pod管理（1.5小时）
- **目标**：掌握Pod运行AI容器。
- **内容**：
  - Pod定义：YAML配置、生命周期。
  - 控制器：Deployment、StatefulSet。
  - AI用例：运行Hugging Face推理容器。
- **练习**：部署FastAPI情感分析Pod。

### 3. Service与网络（1.5小时）
- **目标**：使用Service暴露AI服务。
- **内容**：
  - Service类型：ClusterIP、NodePort、LoadBalancer。
  - Ingress：路由管理。
  - AI场景：暴露情感分析API。
  - **技术债务提示**：Service配置需规划，避免端口冲突。
- **练习**：创建Service，访问情感分析API。

### 4. Helm部署（1.5小时）
- **目标**：使用Helm简化AI应用部署。
- **内容**：
  - Helm核心：Chart、模板、版本管理。
  - 自定义Chart：参数化配置。
  - AI用案：打包情感分析应用。
- **练习**：创建Helm Chart，部署应用。

### 5. 集成AI管道（1.5小时）
- **目标**：结合Python、Hugging Face和Kubernetes，构建AI部署管道。
- **内容**：
  - 容器化：Docker+FastAPI。
  - Kubernetes部署：Pod+Service+Helm。
  - 错误处理：容器崩溃、资源超限。
- **练习**：部署容器化情感分析服务。

### 6. 迷你项目：AI情感分析Kubernetes部署（1小时）
- **目标**：开发完整的Kubernetes AI应用。
- **任务**：
  - Docker：构建FastAPI推理镜像。
  - Kubernetes：部署Pod、Service。
  - Helm：打包应用。
- **交付**：运行在Minikube的推理服务。

### 7. 优化与进阶（1小时）
- **目标**：学习Kubernetes优化和技术债务管理。
- **内容**：
  - 优化：资源限制、自动扩展。
  - 云部署：GKE、EKS。
  - 进阶：Kubernetes+Neo4j（如你的兴趣）、ArgoCD。
- **练习**：配置HPA（水平Pod自动扩展）。

### 8. 总结与Q&A（30分钟）
- **内容**：
  - 复习Kubernetes核心概念。
  - 讨论AI规模化部署实践。
  - 推荐资源：Kubernetes文档、Helm指南。

---

## 学习成果
- 管理容器化AI应用。
- 掌握Pod、Service、Helm。
- 理解Kubernetes在AI高可用性中的优势与局限。
- 管理技术债务，确保管道可维护。

## 资源
- **官方文档**：[Kubernetes](https://kubernetes.io/docs/)、[Helm](https://helm.sh/docs/)
- **教程**：Kubernetes官方教程、Hugging Face部署指南
- **工具**：Minikube、kubectl、Helm、VS Code、GitHub