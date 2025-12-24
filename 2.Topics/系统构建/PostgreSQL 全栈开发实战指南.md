---
view-count: 3
---
# PostgreSQL 单一数据库技术选型栈（Architecture-Only）

## 🎯 核心定位
★ PostgreSQL = 可扩展的 Application Data Platform  
△ 用扩展替代 70–90% 常见中间件  
❗ 适合「复杂度敏感」而非「极端规模」系统

---

## 一、可被 PostgreSQL 吃掉的技术栈（高确定性）

### 1️⃣ 缓存层
★ PostgreSQL + UNLOGGED TABLE  
→ 替代 Redis（读多写少场景）  
△ 优势：零额外系统、强一致  
❗ 边界：不适合 >10k QPS 高频写

---

### 2️⃣ 定时 / 后台任务
★ pg_cron  
→ 替代 Celery / 系统 Cron  
△ 优势：事务内调度、无额外 worker  
❗ 边界：不适合重 CPU / 长任务

---

### 3️⃣ 文档型数据库
★ JSONB + GIN Index  
→ 替代 MongoDB  
△ 优势：关系 + 文档统一建模  
❗ 边界：极端 schema-less / 海量嵌套文档

---

### 4️⃣ 全文搜索
★ TSVECTOR + GIN  
→ 替代 Elasticsearch（80–90% 场景）  
△ 优势：事务一致、写入成本低  
❗ 边界：复杂 relevance tuning / 超大索引

---

### 5️⃣ REST API
★ PostgREST  
→ 替代 Express / FastAPI CRUD 层  
△ 优势：零样板代码、自动权限  
❗ 边界：复杂业务编排逻辑

---

### 6️⃣ GraphQL API
★ pg_graphql  
→ 替代 Apollo Server  
△ 优势：Schema 自动生成  
❗ 边界：高度定制 resolver

---

### 7️⃣ 向量数据库
★ pgvector  
→ 替代 Pinecone / Weaviate（中小规模）  
△ 优势：数据共存、成本极低  
❗ 边界：十亿级向量 / 超低延迟 SLA

---

### 8️⃣ 认证系统
★ pgcrypto + pgjwt  
→ 替代 Auth0（基础认证）  
△ 优势：用户数据不外流  
❗ 边界：复杂 IAM / 企业 SSO

---

### 9️⃣ 实时 / 同步
△ ElectricSQL / Logical Replication  
→ 替代轻量 WebSocket Sync  
❗ 边界：大规模 fan-out 实时系统

---

### 🔟 时序 / 行为分析
△ 列式扩展（pg_mooncake 等）  
→ 替代轻量 Analytics  
❗ 边界：PB 级分析 / 专用 OLAP

---

## 二、PostgreSQL 不该强行承担的领域（红线）

❌ 超高并发写入（>10k QPS sustained）  
❌ 超大数据体量（>100TB 单库）  
❌ 极端低延迟缓存（sub-ms SLA）  
❌ 企业级 IAM / 权限治理  
❌ 超复杂搜索排序与推荐系统

---

## 三、技术选型一句话法则（Decision Rules）

- ★ 想减少系统数量 → PostgreSQL 优先
- ★ 想降低运维成本 → PostgreSQL 优先
- ❗ 想极致规模 / 性能 → 专用系统
- ❗ 想组织解耦 / 独立演进 → 专用系统

---

## 四、推荐使用姿势（长期）

★ 把 PostgreSQL 当「系统核心平台」  
△ 只在**被证伪后**才引入新中间件  
❗ 不要一开始就堆 Redis / ES / MQ

---

## 五、终极选型锚点

> ❗ 不是「PostgreSQL 能不能做」  
> ★ 而是「**引入一个新系统，是否值得增加认知 + 运维成本**」
