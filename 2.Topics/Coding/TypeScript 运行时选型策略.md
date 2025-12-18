---
view-count: 3
---

## ★ JS/TS 运行时选型：核心锚点
- ★ 运行时选型→场景驱动
- ★ 成熟生态→Node.js
- ★ 默认安全模型→Deno
- ★ 极致性能→Bun
- ★ 边缘计算→Isolate/Deno
- ★ 桌面应用→Electron
- △ 轻量桌面→Neutralino
- △ 嵌入引擎→QuickJS
- △ RN 优化→Hermes

## ★ 服务端 / 工具链决策模式
- ★ 企业后端→Node.js
- △ 现代 TS 原生→Deno
- △ CLI 启动速度→Bun
- ❗ 生态成熟≠开发效率
- ❗ 性能瓶颈→运行时+工具链

## ★ 边缘与 Serverless
- ★ Edge→低冷启动
- ★ Isolate→高并发
- △ Runtime即服务→RaaS
- △ 边缘函数→请求级执行
- ❗ Node 不适配 Edge

## ★ 技术演进路径
- ★ V1 Node→生态优先
- ★ V2 Node+TS→工程化
- ★ V3 Deno→安全标准化
- ★ V4 Bun→性能一体化
- ★ V5 Edge→架构转型

## △ 通用迁移原则
- △ 生态优势→长期成本↓
- △ 内建工具→心智负担↓
- △ 性能收益→工程规模↑
- △ 标准库控制→安全性↑
- ❗ 运行时≠部署模型

## ❗ 反直觉结论
- ❗ Node≠最优DX
- ❗ 新运行时≠小众
- ❗ Edge≠Serverless
- ❗ 性能问题多源于工具链
