---
date: 2025-06-27 16:12
tags: null
---
## 一、核心模型：声明式调和 = 精神内核
| 关键概念                 | 核心认知                                 |
| -------------------- | ------------------------------------ |
| **声明式配置**            | YAML 是你对系统的**“理想状态”**声明              |
| **控制器 Controller**   | 实际状态 ≠ 期望状态 → 自动调和到目标状态              |
| **Pod**              | 最小运行单元，封装一个或多个容器，共享网络与存储             |
| **Deployment**       | 控制 Pod 的副本数、滚动升级与回滚                  |
| **Service**          | 稳定暴露一组 Pod，提供服务发现和负载均衡               |
| **Ingress**          | 用域名 + 路由暴露服务，通常搭配 Ingress Controller |

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
| 场景             | 推荐模式                                 |
| -------------- | ------------------------------------ |
| 开发调试           | NodePort + kubectl logs/exec         |
| 生产部署（HTTP）     | Deployment + ClusterIP + Ingress     |
| 生产部署（公网访问）     | Deployment + LoadBalancer            |
| 配置动态注入         | ConfigMap/Secret + Volume/Env        |
| 存储挂载           | PVC + Volume                         |
| 持久任务/一次性任务处理   | Job/CronJob                          |
| 横向扩缩容          | HPA（Horizontal Pod Autoscaler）       |

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
