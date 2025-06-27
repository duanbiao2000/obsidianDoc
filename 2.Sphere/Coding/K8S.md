---
date: 2025-06-27 16:12
tags: null
---

## 一、K8s 的 20% 核心构件 = 能解决 80% 场景的金三角

这三个是你必须熟透的：

| 模块             | 作用                | 掌握重点                                |
| -------------- | ----------------- | ----------------------------------- |
| **Pod**        | 最小运行单元，容器的壳       | 生命周期、共享网络、重启策略                      |
| **Deployment** | 控制 Pod 副本的部署、升级策略 | 副本数、滚动升级、回滚                         |
| **Service**    | 稳定暴露 Pod 的访问入口    | ClusterIP / NodePort / LoadBalancer |

### 你掌握了这三样，就能写出 80% 的 K8s YAML 配置。

---

## 二、最值钱的 20% 能力：掌握声明式 vs 控制器模型

K8s 的本质是：

> **我声明目标状态 → 控制器持续调和当前状态**

这就是 `kubectl apply` 背后的魔法：

- 你写好 YAML（比如希望有 3 个 nginx 副本）

- Deployment Controller 检查实际状态，发现只有 1 个，就会调度 2 个补上

- 一直保证系统处于你**声明的理想状态**

### 建议掌握：

- 控制器模式（如 Deployment、ReplicaSet、Job）

- `kubectl describe/get logs exec` 的调试三板斧

- 滚动升级、回滚策略（Deployment `strategy` 字段）

---

## 三、最常用的 20% 命令组合

这些命令能覆盖你 80% 的日常操作：

```bash
# 查看资源
kubectl get pods / svc / deploy / nodes

# 调试排错
kubectl describe pod <name>
kubectl logs <pod-name>
kubectl exec -it <pod> -- bash

# 应用/更新配置
kubectl apply -f xxx.yaml
kubectl delete -f xxx.yaml

# 快速创建测试
kubectl run test-pod --image=nginx
```

---

## 五、二八策略的学习路线推荐

| 阶段      | 建议重点                                         |
| ------- | -------------------------------------------- |
| **入门期** | 熟练使用 kubectl 命令、理解 Pod-Deployment-Service 关系 |
| **熟练期** | 编写 YAML 模板，掌握配置升级/回滚，日志调试                    |
| **进阶期** | 掌握 ConfigMap、Secret、Volume、Health Check      |
| **专家期** | 自定义 Controller、Operator、调度策略、扩展 CRD          |

---

## 总结：如何用 20% 的知识驾驭 80% 的 Kubernetes

1. **Pod / Deployment / Service = 架构三件套**

2. **kubectl 6 大命令掌控日常**

3. **声明式 vs 调和控制器模型 = K8s 核心哲学**

4. **YAML 模板不要抄，要记住结构套路**

5. **观测和调试是工程师最强的武器（logs/exec/describe）**

---

## 1. Deployment + Service 模板（标准三层部署）

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-app-container
          image: your-image:latest
          ports:
            - containerPort: 8080
          env:
            - name: ENV
              value: "production"

# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  ports:
    - port: 80        # Service 暴露的端口
      targetPort: 8080 # Pod 内部容器端口
  type: ClusterIP     # 可改为 NodePort / LoadBalancer
```

---

## 2. Pod with Volume 挂载模板（挂载 ConfigMap + 持久卷）

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: volume-pod
spec:
  containers:
    - name: app-container
      image: busybox
      command: ["sleep", "3600"]
      volumeMounts:
        - name: config-volume
          mountPath: /etc/config
        - name: data-volume
          mountPath: /data
  volumes:
    - name: config-volume
      configMap:
        name: my-config
    - name: data-volume
      persistentVolumeClaim:
        claimName: my-pvc
```

你需要先创建 `ConfigMap` 和 `PVC`：

```bash
kubectl create configmap my-config --from-literal=key=value
# PVC 略，可使用 hostPath 或静态 NFS 动态 PVC
```

---

## 3. Ingress + LoadBalancer 暴露模板（适合公网服务）

```yaml
# ingress.yaml（基于 nginx ingress controller）
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: your-domain.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-app-service
                port:
                  number: 80
```

### LoadBalancer 方案（裸机/公网直接暴露）

```yaml
# 可替代 ClusterIP/NodePort
apiVersion: v1
kind: Service
metadata:
  name: lb-service
spec:
  selector:
    app: my-app
  ports:
    - port: 80
      targetPort: 8080
  type: LoadBalancer
```

---

# **Kubernetes 精简学习清单（基于二八定律）**

## 一、核心模型：声明式调和 = 精神内核

| 关键概念                 | 核心认知                                 |
| -------------------- | ------------------------------------ |
| **声明式配置**            | YAML 是你对系统的**“理想状态”**声明              |
| **控制器 Controller**   | 实际状态 ≠ 期望状态 → 自动调和到目标状态              |
| **Pod**              | 最小运行单元，封装一个或多个容器，共享网络与存储             |
| **Deployment**       | 控制 Pod 的副本数、滚动升级与回滚                  |
| **Service**          | 稳定暴露一组 Pod，提供服务发现和负载均衡               |
| **Ingress**          | 用域名 + 路由暴露服务，通常搭配 Ingress Controller |
| **ConfigMap/Secret** | 管理配置和敏感信息，支持热更新/解耦                   |

---

## 二、常用命令：Kubernetes 的六把瑞士军刀

| 场景   | 命令模板                                                                              |
| ---- | --------------------------------------------------------------------------------- |
| 查看资源 | `kubectl get pods / svc / deploy / ingress`                                       |
| 诊断排错 | `kubectl describe pod <name>``kubectl logs <pod>``kubectl exec -it <pod> -- bash` |
| 应用配置 | `kubectl apply -f xxx.yaml``kubectl delete -f xxx.yaml`                           |
| 快速测试 | `kubectl run test --image=nginx --restart=Never`                                  |
| 端口转发 | `kubectl port-forward svc/my-svc 8080:80`                                         |
| 编辑配置 | `kubectl edit deployment my-app`                                                  |

---

## 三、YAML 模板套路（务必掌握的三类）

| 类型                          | 用法描述                |
| --------------------------- | ------------------- |
| **Deployment + Service**    | 服务部署三件套，包含副本管理和负载均衡 |
| **Pod + Volume**            | 静态内容挂载、配置注入、日志输出    |
| **Ingress or LoadBalancer** | 暴露公网服务、构建网关流量入口     |

---

## 四、实战模式（20% 模板应对 80% 场景）

| 场景             | 推荐模式                                 |
| -------------- | ------------------------------------ |
| 开发调试           | NodePort + kubectl logs/exec         |
| 生产部署（HTTP）     | Deployment + ClusterIP + Ingress     |
| 生产部署（公网访问）     | Deployment + LoadBalancer            |
| 配置动态注入         | ConfigMap/Secret + Volume/Env        |
| 存储挂载           | PVC + Volume                         |
| 持久任务/一次性任务处理   | Job/CronJob                          |
| 横向扩缩容          | HPA（Horizontal Pod Autoscaler）       |
| 日志/监控/链路追踪（接入） | Sidecar + Prometheus + Loki + Jaeger |

---

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
