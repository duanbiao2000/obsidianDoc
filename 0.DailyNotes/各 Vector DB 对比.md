---
view-count: 3
---

## 📊 各 Vector DB 对比

| Vector DB    | 🔑 Key Features                            | ✅ Pros                                 | ⚠️ Cons                 | 📌 适用场景            |
| ------------ | ------------------------------------------ | -------------------------------------- | ----------------------- | ------------------ |
| **Pinecone** | Fully managed, serverless; 支持 HNSW & SPANN | Auto-scaling, SLA-backed, 易集成          | Vendor lock-in, 成本随规模上升 | 快速上线、无需运维的 SaaS 场景 |
| **Weaviate** | GraphQL API, 内置向量化模块                       | 支持 Hybrid Query（metadata + vector），模块化 | 部署需 Kubernetes，运维复杂     | 需要灵活扩展、支持多模态的企业应用  |
| **Milvus**   | GPU 加速索引；支持 IVF, HNSW, ANNOY               | 高性能，适合大规模数据，动态索引                       | 运维复杂，需要独立系统             | 超大规模向量检索（金融、推荐系统）  |
| **Qdrant**   | 轻量级，实时更新，payload filtering                 | 简单易用，支持混合查询                            | 缺乏原生关系型 join，集群一致性为最终一致 | 中小规模应用，快速原型开发      |
| **Vectara**  | 托管服务，内置语义排序 & re-ranking                   | 高相关性结果，集成简单                            | 专有系统，索引控制有限             | 需要高质量语义搜索的 SaaS 产品 |

---

## 🧭 决策建议

- **想要零运维、快速上线** → Pinecone / Vectara
- **需要灵活扩展、支持多模态** → Weaviate
- **大规模高性能检索（金融/推荐/风控）** → Milvus
- **轻量级、快速原型** → Qdrant
- **关注搜索质量（语义相关性）** → Vectara

---

✅ 总结：

- **Pinecone / Vectara** → SaaS 化，省心但受限。
- **Weaviate / Milvus** → 自主可控，适合大规模企业部署。
- **Qdrant** → 轻量灵活，适合中小团队。
