---
tags:
  - Tech/DeepWiki
  - Method
  - Domain/Creativity/Product
  - Checklist-防呆清单
source:
  - https://deepwiki.com/bmadcode/BMAD-METHOD
view-count: 10
---
# Checklist：防错核对表

Checklist = 结构化文档，确保关键步骤不遗漏。

---

## 核心类型

**architect-checklist.md**
- 系统边界
- 服务拆分
- 容错降级
- 监控日志追踪
- 数据一致性（CAP）
- 水平扩展
- 安全扫描（OWASP）
- 灾难恢复

**pm-checklist.md**
- 需求评审签字
- 用户画像场景
- 原型UX评审
- 技术方案对齐
- MVP范围优先级
- 用户测试/AB实验
- 数据分析指标
- 运营客服培训

**story-dod-checklist.md**（DoD = Definition of Done）
- 代码合并主干
- 单元测试通过（≥90%）
- 集成测试通过
- UI/UX一致
- 文档完整（API/手册）
- Code Review
- 预发环境验证
- 无严重Bug（P0/P1）
- 监控指标配置

**其他类型**
```
deployment-checklist.md  → 备份、灰度、回滚
security-checklist.md    → HTTPS、注入防护、合规
onboarding-checklist.md  → 账号、工具培训
release-checklist.md     → 客户通知、回滚方案
```

---

## 角色对照

| 角色      | 何时使用           | 关注点           |
|-----------|-------------------|-----------------|
| architect | 设计阶段           | 架构、稳定性     |
| pm        | 需求评审、发布前    | 需求、体验       |
| dev/qa    | 每个故事闭环       | 功能完成标准     |
| devops    | 每次发布前         | 上线、风险控制   |
| security  | 审计、渗透测试     | 漏洞、合规       |

---

## 角色依赖

| 角色      | 核心指令                          | 依赖模板/文档                    |
|-----------|----------------------------------|--------------------------------|
| analyst   | 项目简报、市场调研、竞品分析        | 简报模板、调研模板、头脑风暴指南  |
| pm        | PRD、Epic、分片                   | PRD模板、Epic指南               |
| architect | 全栈/后端/前端架构                 | 架构模板                        |
| sm        | 故事起草、流程修正、清单检查        | 故事创建、修正文档               |
| po        | 验证故事、文档分片、待办管理        | 检查清单、验证指南               |
| qa        | 评审                              | 评审文档、技术偏好               |
| ux-expert | 前端规范、UI提示                   | 前端模板、AI提示指南             |

---

**核心**：不同角色在不同阶段的防错核对表。团队越复杂，越需要。