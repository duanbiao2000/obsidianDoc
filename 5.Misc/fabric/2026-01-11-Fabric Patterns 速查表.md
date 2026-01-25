---
aliases:
date: 2026-01-11 21:23
tags: ["Type/Reference"]
source:
rating:
related:
  - "[[Prompt管理科学]]"
  - "[[2.Topics/进阶/设计模式|设计模式]]"
view-count: 8
---
以下是 **Fabric 提示范式（Patterns）** 的完整速查表，包含每个范式的 **最佳适用场景（1–3 条）** 和 **关键注意事项**，以表格形式呈现，便于快速查阅与使用。

> ⚠️ 说明：
>
> - 场景基于常见用例提炼；
> - 注意事项聚焦输入格式、输出特性或潜在陷阱；
> - 部分名称相似的 pattern 已合并说明（如 `summarize_*`）。

---

### 📊 Fabric Patterns 速查表

| Pattern 名称                                                            | 最佳适用场景                                                      | 注意事项                                    |
| --------------------------------------------------------------------- | ----------------------------------------------------------- | --------------------------------------- |
| **agility_story**                                                     | 1. 将用户需求转化为敏捷故事；2. 产品 backlog 梳理；3. Scrum 规划会议准备            | 需提供清晰的用户目标或痛点                           |
| **ai**                                                                | 通用 AI 对话入口（兜底 pattern）                                      | 功能较泛，建议优先使用专用 pattern                   |
| **analyze_answers**                                                   | 1. 批量分析问卷/面试回答；2. 提取共性观点；3. 识别矛盾点                           | 输入应为结构化文本（如 Q&A 列表）                     |
| **analyze_bill** / **analyze_bill_short**                             | 1. 解读法律/政策草案；2. 提取关键条款；3. 评估影响群体                            | `short` 版更简洁，适合快速预览                     |
| **analyze_candidates**                                                | 1. 简历筛选；2. 候选人能力对比；3. 面试评估汇总                                | 需提供结构化候选人信息（避免纯自由文本）                    |
| **analyze_cfp_submission**                                            | 1. 技术会议投稿评审；2. 提炼创新点；3. 评估可行性                               | 适用于学术/工程类 CFP                           |
| **analyze_claims**                                                    | 1. 辩论稿事实核查；2. 广告语可信度分析；3. 科研声明验证                            | 输出含“可信度评分”，需谨慎对待主观判断                    |
| **analyze_comments**                                                  | 1. 社交媒体舆情分析；2. 产品反馈聚类；3. 识别极端情绪                             | 对非英文支持有限，中文需加 `-g zh`                   |
| **analyze_debate**                                                    | 1. 政治辩论摘要；2. 论点强弱评估；3. 逻辑漏洞检测                               | 输入需明确标注发言者角色                            |
| **analyze_email_headers**                                             | 1. 钓鱼邮件溯源；2. 邮件路由分析；3. SPF/DKIM 诊断                          | 仅接受原始邮件头（Raw Headers），非全文               |
| **analyze_incident**                                                  | 1. SRE 事故复盘；2. 根因分析（RCA）；3. 改进建议生成                          | 需包含时间线、症状、操作日志                          |
| **analyze_interviewer_techniques**                                    | 1. 面试官话术评估；2. 偏见检测；3. 提问质量打分                                | 依赖对话转录文本，需标注角色                          |
| **analyze_logs**                                                      | 1. 异常日志模式识别；2. 错误聚类；3. 性能瓶颈定位                               | 日志需带时间戳和级别，纯堆栈效果差                       |
| **analyze_malware**                                                   | 1. 恶意软件行为摘要；2. IOC 提取；3. TTPs 映射（MITRE ATT&CK）              | **不替代沙箱**，仅基于文本报告分析                     |
| **analyze_military_strategy**                                         | 1. 战史推演复盘；2. 战术优劣评估；3. 地缘政治影响分析                             | 高度依赖上下文完整性                              |
| **analyze_mistakes**                                                  | 1. 代码错误归因；2. 决策失误复盘；3. 学习过程反思                               | 需明确“错误”与“预期”的对比                         |
| **analyze_paper** / **analyze_paper_simple**                          | 1. 学术论文核心贡献提取；2. 方法复现难点分析；3. 与同类工作对比                        | `simple` 版忽略数学细节，适合非专家                  |
| **analyze_patent**                                                    | 1. 专利权利要求解读；2. 技术新颖性评估；3. 侵权风险初筛                            | 法律效力有限，仅作参考                             |
| **analyze_personality**                                               | 1. MBTI/大五人格推测；2. 沟通风格建议；3. 团队角色匹配                          | **娱乐性质强**，勿用于正式评估                       |
| **analyze_presentation**                                              | 1. PPT 内容逻辑流优化；2. 听众注意力预测；3. 关键信息强化建议                       | 需提供讲稿或逐页备注，非仅标题                         |
| **analyze_product_feedback**                                          | 1. 用户评论情感分类；2. 功能需求聚类；3. NPS 驱动因素挖掘                         | 中文需 `-g zh`，俚语可能误判                      |
| **analyze_proposition**                                               | 1. 商业提案可行性评估；2. 风险收益比分析；3. 利益相关方影响图                         | 需包含具体数据支撑，否则输出空泛                        |
| **analyze_prose** / **analyze_prose_pinker** / **analyze_prose_json** | 1. 写作风格诊断；2. 可读性优化；3. Pinker 风格指南合规检查                       | `json` 版返回结构化指标，适合程序处理                  |
| **analyze_risk**                                                      | 1. 项目风险登记册生成；2. 概率-影响矩阵；3. 缓解措施建议                           | 需明确风险类别（技术/市场/合规等）                      |
| **analyze_sales_call**                                                | 1. 销售话术有效性分析；2. 客户异议归类；3. 成交信号识别                            | 依赖高质量通话转录                               |
| **analyze_spiritual_text**                                            | 1. 宗教经文隐喻解读；2. 跨传统比较；3. 现代生活启示                              | 避免用于敏感信仰讨论                              |
| **analyze_tech_impact**                                               | 1. 新技术社会影响评估；2. 伦理风险识别；3. 监管合规建议                            | 输出偏宏观，缺乏量化指标                            |
| **analyze_terraform_plan**                                            | 1. IaC 变更影响预判；2. 资源依赖可视化；3. 安全策略冲突检测                        | 需输入 `terraform plan -out=...` 的 JSON 格式 |
| **analyze_threat_report** / **_cmds** / **_trends**                   | 1. APT 报告摘要；2. 攻击命令提取；3. 威胁趋势预测                             | `_cmds` 专注 IoC，`_trends` 需多份报告          |
| **answer_interview_question**                                         | 1. 行为面试题回答草稿；2. 技术问题结构化应答；3. STAR 法则优化                      | 需提供具体问题，避免“如何回答面试”                      |
| **apply_ul_tags**                                                     | 1. 无序列表标准化；2. Markdown 清洗；3. HTML 转换辅助                      | 仅处理 `<ul><li>` 结构，不解析内容                 |
| **ask_secure_by_design_questions**                                    | 1. 架构评审安全提问清单；2. DevSecOps 检查项；3. 威胁建模引导                    | 输出为问题列表，非答案                             |
| **ask_uncle_duke**                                                    | 1. 讽刺性商业建议；2. 反常识洞察；3. 打破思维定势                               | 模仿《Dilbert》角色，输出具幽默/批判性                 |
| **capture_thinkers_work**                                             | 1. 哲学家思想摘要；2. 理论框架提取；3. 跨学派对比                               | 需提供原文或可靠二手资料                            |
| **check_agreement**                                                   | 1. 合同条款一致性检查；2. 多版本差异比对；3. 义务-权利匹配                          | 不具备法律效力，仅文本比对                           |
| **clean_text**                                                        | 1. OCR 结果后处理；2. 去除乱码/广告；3. 文本标准化                            | 会删除“非自然语言”内容（如代码块）                      |
| **coding_master**                                                     | 1. 代码重构建议；2. 设计模式应用；3. 性能优化方案                               | 需提供完整函数/类，片段效果差                         |
| **compare_and_contrast**                                              | 1. 产品功能对比；2. 理论异同分析；3. 历史事件类比                               | 需明确比较维度，否则输出松散                          |
| **concall_summary**                                                   | 1. 财报电话会议纪要；2. 管理层指引提取；3. Q&A 重点摘要                          | 依赖结构化转录（区分 CEO/CFO/QA）                  |
| **convert_to_markdown**                                               | 1. HTML/PDF 转 Markdown；2. 富文本清洗；3. Obsidian 兼容格式化           | 复杂表格/公式可能丢失                             |
| **create_5_sentence_summary**                                         | 1. 快速摘要（高管阅读）；2. 新闻简报；3. 论文 elevator pitch                  | 严格限制 5 句，超长内容会截断                        |
| **create_academic_paper**                                             | 1. 论文大纲生成；2. 摘要/引言草稿；3. 相关工作综述                              | **不生成真实引用**，需人工补充                       |
| **create_ai_jobs_analysis**                                           | 1. AI 岗位技能需求分析；2. 薪资趋势预测；3. 职业路径规划                          | 数据基于公开信息，时效性有限                          |
| **create_aphorisms**                                                  | 1. 金句生成；2. 社交媒体文案；3. 书籍章节箴言                                 | 风格偏哲理，避免用于技术文档                          |
| **create_art_prompt**                                                 | 1. Midjourney/Stable Diffusion 提示词；2. 风格+主体+光照描述；3. 多模态创作引导 | 输出为英文提示，中文需后处理                          |
| **create_better_frame**                                               | 1. 问题重定义（Reframing）；2. 创新机会识别；3. 冲突化解视角                     | 需提供原始问题陈述                               |
| **create_coding_feature**                                             | 1. 用户故事转代码规范；2. API 设计草案；3. 测试用例生成                          | 需指定语言/框架                                |
| **create_coding_project**                                             | 1. 项目脚手架生成；2. 技术选型建议；3. 目录结构设计                              | 输出为规划文档，非可执行代码                          |
| **create_command**                                                    | 1. CLI 工具命令生成；2. PowerShell/Bash 脚本草稿；3. 参数说明               | 需描述功能需求，非自然语言命令                         |
| **create_conceptmap**                                                 | 1. 知识点关系可视化；2. 课程设计；3. 头脑风暴整理                               | 输出为文本描述，需手动绘图                           |
| **create_cyber_summary**                                              | 1. 安全事件时间线；2. 攻击链还原；3. 防御建议摘要                               | 需包含 IoC 和日志片段                           |
| **create_design_document**                                            | 1. 系统架构文档草稿；2. 模块接口定义；3. 非功能性需求列表                           | 需提供业务上下文                                |
| **create_diy**                                                        | 1. 手工制作步骤；2. 家居改造指南；3. 材料清单生成                               | 侧重生活场景，非工业级                             |
| **create_excalidraw_visualization**                                   | 1. 手绘风流程图描述；2. 架构草图文本版；3. 协作白板内容                            | 输出为 Excalidraw JSON，需导入工具               |
| **create_flash_cards**                                                | 1. Anki 记忆卡片；2. 术语-定义对；3. Q&A 复习集                           | 默认生成 CSV，可用 `to_flashcards` 转格式         |
| **create_formal_email**                                               | 1. 商务邀约；2. 投诉信；3. 合作提案                                      | 自动包含礼貌用语，避免口语化                          |
| **create_git_diff_commit**                                            | 1. 自动生成 commit message；2. PR 描述草稿；3. 变更影响说明                 | 需输入 `git diff` 输出                       |
| **create_graph_from_input**                                           | 1. 实体关系图描述；2. 知识图谱构建；3. 依赖网络可视化                             | 输出为 Mermaid/Graphviz 代码                 |
| **create_hormozi_offer**                                              | 1. 高转化销售页面框架；2. 价值主张提炼；3. 紧迫感营造                             | 基于 Alex Hormozi 营销方法论                   |
| **create_idea_compass**                                               | 1. 创新方向评估（可行性/影响力）；2. 项目优先级排序；3. 资源分配建议                     | 输出四象限图描述                                |
| **create_investigation_visualization**                                | 1. 事件关联图；2. 嫌疑人网络；3. 时间-地点-人物矩阵                             | 需结构化调查数据                                |
| **create_keynote**                                                    | 1. 演讲故事线；2. 幻灯片要点；3...(内容过长已截断)                             |                                         |
