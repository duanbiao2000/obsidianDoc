---
view-count: 4
date: 2025-06-27 16:12
update: 2026-01-07 00:54
related:
  - "[[Kubernetes实战练习项目]]"
  - "[[云原生微服务架构]]"
---

## 🧠 一、Kubernetes 的本质是什么？

> **Kubernetes 是一个声明式、以控制循环为核心的分布式系统管理平台。**

换句话说：

- 它是操作容器集群的“**操作系统内核**”

- 是一种对“**服务编排**”和“**期望状态控制**”的自动化平台

- 目标是：“我声明我想要什么状态”，K8s 自动达到并维持它

---

## 🔍 二、Kubernetes 的第一性原理

> Kubernetes 本质上是围绕“期望状态”进行自动闭环控制的系统。

| 核心机制             | 第一性原理说明                                                 |
| ---------------- | ------------------------------------------------------- |
| 声明式 API          | 所有资源都由 YAML 定义，它描述“我期望系统是什么样”（Desired State）            |
| 控制器 Control Loop | 控制器不断比对“实际状态”和“期望状态”，若不同则调整，形成 **控制闭环（Reconcile Loop）** |
| 可扩展的资源模型         | 一切皆资源（Pod/Service/Ingress/CRD），便于自动化与生态集成               |
| 去中心化调度           | 资源调度、弹性伸缩、滚动更新、服务发现，全是分布式异步系统思维                         |
| 基于标签的解耦          | 不再按“机器部署”，而是按“标签 + 选择器”自由组合资源与服务                        |

**K8s 不是容器运行时，而是容器编排平台，运行时是 containerd/cri-o 等，K8s 只调度和编排它们。**

---

## 🧩 三、Kubernetes 的知识结构体系图谱

可以用如下结构理解：

```
Kubernetes 知识结构
├── 1. 核心概念
│   ├── Node（工作节点）
│   ├── Pod（最小调度单元）
│   ├── Controller（控制器：Deployment、StatefulSet…）
│   ├── Service（服务发现、负载均衡）
│   └── Volume（存储）
├── 2. 核心机制
│   ├── 控制循环（Controller Manager）
│   ├── 调度器（Scheduler）
│   ├── API Server（统一入口）
│   ├── etcd（状态存储）
│   └── kubelet（Node 上的 agent）
├── 3. 网络模型
│   ├── CNI（插件架构）
│   ├── Service ClusterIP / NodePort / LoadBalancer
│   ├── DNS / CoreDNS
│   └── Ingress / Gateway API
├── 4. 存储模型
│   ├── PV/PVC（持久化卷）
│   ├── CSI 插件
│   └── 动态卷分配
├── 5. 配置与密钥
│   ├── ConfigMap / Secret
│   └── 环境注入与挂载
├── 6. 安全与认证
│   ├── RBAC（权限）
│   ├── NetworkPolicy（网络隔离）
│   └── Pod 安全上下文（SecurityContext）
├── 7. 编排与运维
│   ├── Deployment / StatefulSet / DaemonSet
│   ├── 滚动更新 / 灰度发布 / 回滚
│   └── HPA/VPA（弹性扩缩）
├── 8. 扩展与生态
│   ├── Helm（包管理）
│   ├── Operator（自动化管理）
│   ├── CRD（自定义资源）
│   └── GitOps（ArgoCD）
├── 9. 云原生实践
│   ├── K3s/K0s/MicroK8s（轻量化）
│   ├── EKS/GKE/ACK（云托管）
│   └── Service Mesh（Istio、Linkerd）
```

---

## 一、核心模型：声明式调和 = 精神内核

| 关键概念               | 核心认知                                 |
| ------------------ | ------------------------------------ |
| **声明式配置**          | YAML 是你对系统的**“理想状态”**声明              |
| **控制器 Controller** | 实际状态 ≠ 期望状态 → 自动调和到目标状态              |
| **Pod**            | 最小运行单元，封装一个或多个容器，共享网络与存储             |
| **Deployment**     | 控制 Pod 的副本数、滚动升级与回滚                  |
| **Service**        | 稳定暴露一组 Pod，提供服务发现和负载均衡               |
| **Ingress**        | 用域名 + 路由暴露服务，通常搭配 Ingress Controller |

## 二、常用命令：Kubernetes 的六把瑞士军刀

| 场景   | 命令模板                                                                              |
| ---- | --------------------------------------------------------------------------------- |
| 查看资源 | `kubectl get pods / svc / deploy / ingress`                                       |
| 诊断排错 | `kubectl describe pod <name>``kubectl logs <pod>``kubectl exec -it <pod> -- bash` |
| 应用配置 | `kubectl apply -f xxx.yaml``kubectl delete -f xxx.yaml`                           |
| 快速测试 | `kubectl run test --image=nginx --restart=Never`                                  |
| 端口转发 | `kubectl port-forward svc/my-svc 8080:80`                                         |

## 三、YAML 模板套路（务必掌握的三类）

| 类型                       | 用法描述                |
| ------------------------ | ------------------- |
| **Deployment + Service** | 服务部署三件套，包含副本管理和负载均衡 |
| **Pod + Volume**         | 静态内容挂载、配置注入、日志输出    |
|                          |                     |

## 四、实战模式（20% 模板应对 80% 场景）

| 场景           | 推荐模式                             |
| ------------ | -------------------------------- |
| 开发调试         | NodePort + kubectl logs/exec     |
| 生产部署（HTTP）   | Deployment + ClusterIP + Ingress |
| 生产部署（公网访问）   | Deployment + LoadBalancer        |
| 配置动态注入       | ConfigMap/Secret + Volume/Env    |
| 存储挂载         | PVC + Volume                     |
| 持久任务/一次性任务处理 | Job/CronJob                      |
| 横向扩缩容        | HPA（Horizontal Pod Autoscaler）   |

## 五、最佳实践关键词（打牢工程力）

- **健康探针**：readinessProbe / livenessProbe
- **资源限制**：resources.limits & requests（防暴走）
- **滚动升级**：strategy.type: RollingUpdate + maxUnavailable
- **多环境配置切换**：通过 Namespace + ConfigMap 隔离
- **观测闭环**：trace_id + log + metrics 三合一接入

---

## 六、排障思维模型（出问题不慌）

```text
kubectl get  → 资源状态是否存在？
kubectl describe → 创建/调度是否成功？
kubectl logs → 程序运行是否报错？
kubectl exec → 能否进入容器进行内部排查？
```

### 快速定位三板斧：

1. 是不是容器没起来（Image、端口、权限）
2. 是不是 Pod 没调度成功（资源、Node、taint）
3. 是不是配置没注入（ENV、Volume、文件路径）

---

## 七、学习路线图（实战导向）

| 阶段      | 核心目标                                 |
| ------- | ------------------------------------ |
| Day 1   | 跑通 Pod、Deployment、Service 三件套        |
| Day 2-3 | 自定义配置注入、数据挂载、Pod 调试                  |
| Day 4-5 | 用 Ingress 公开服务、用 Job 处理任务、配置 HPA     |
| Day 6-7 | 部署监控链路（Prometheus + Loki + Jaeger）   |
| Week 2+ | 理解 Operator、编排 Helm、探索 Serverless/边缘 |
