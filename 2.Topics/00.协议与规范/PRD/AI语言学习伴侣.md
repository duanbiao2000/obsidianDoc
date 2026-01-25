---
aliases: null
date: 2025-12-03 10:19
tags:
  - AI-Chat-Engagement
  - Language-Proficiency-Training
  - AI-Agent-Development
  - Content-Translation
  - Domain/AI
  - Domain/AI/Agent
  - Domain/Language
  - Type/Reference
source: null
update: null
rating: null
related: null
view-count: 6
---

## 🔗 相关链接

**上级索引**:
- [[2.Topics\00.协议与规范\PRD\_Index_of_PRD.md|PRD]]
- [[2.Topics\00.协议与规范\_Index_of_00.协议与规范.md|00.协议与规范]]
- [[2.Topics\_Index_of_2.Topics.md|2.Topics]]

**相关主题**:
- [[2.Topics/03.内容创作/AI|03.内容创作]]
- [[3.Resources/Prompt工程/README.md|Prompt工程]]
- [[2.Topics\02.认知系统\学习系统]]

---

## 0. 本质 (The Essence)
- **核心逻辑**：AI 实时对话 + 即时纠正 = 消除“开口跪”焦虑。
- **价值点**：24/7 无压力陪练 + 个性化反馈。
- **定位**：解决“不敢说、没话说、说了没人改”的闭环痛点。

---

## 1. MVP 核心矩阵

| 模块 | 核心能力 | MVP 状态 | 吐槽 |
| :--- | :--- | :--- | :--- |
| **实时对话** | 文本/语音双向交互 | ✅ 包含 | 对话自然度比发音准更重要 |
| **即时纠正** | 语法/词汇自动优化 | ✅ 包含 | 纠正是建立信任的关键 |
| **发音评分** | 音素级声学分析 | ❌ 不含 | 成本太高，初期非刚需 |
| **场景模拟** | 预设 5-10 个真实生活场景 | ✅ 包含 | 没场景用户会陷入“尬聊” |
| **进度跟踪** | 词汇量/学习曲线 | ❌ 不含 | 别在验证阶段做复杂后台 |

---

## 2. 逻辑骨架 (Minimal Stack & Flow)

### **技术栈 (The Simple Stack)**
- **Frontend**: Flutter / React Native (跨平台快)
- **Backend**: Go / Python (Cloud Run 无服务器部署)
- **AI Core**: Gemini / GPT API (MaaS 模式，拒绝自建)
- **Audio**: Google ASR (转文字) + Google TTS (转语音)

### **对话流 (The Minimal Flow)**
`用户语音 -> ASR -> LLM (生成回复 + 纠正建议) -> TTS -> 用户听到回复 + 看到建议`

---

## 3. 避坑指南 (Brutal Truths)

- **不要迷信发音纠正**：87% 的用户更在乎“被理解”而非“伦敦腔”，发音模型会拖慢 50% 的进度。
- **API 成本是死穴**：LLM + ASR + TTS 的组合拳可能让单用户成本高达 $15+/月，必须严控 Token。
- **纠正准确率 > 75% 是底线**：如果 AI 给出的纠正经常出错，用户会瞬间流失。
- **延迟是杀手**：端到端延迟必须 < 2 秒，否则就不叫对话，叫“对讲机”。

---

## 4. 执行决策树

1. **自研模型还是 API？** → 选 API。MVP 是验证市场，不是秀肌肉。
2. **长历史还是短窗口？** → 选短窗口 (最近 5 轮) + 总结。省钱且不降智。
3. **单体还是微服务？** → 选单体。初期复杂度是毒药。
4. **付费模式？** → 14 天免费试用 + 订阅制。验证真实付费意愿。

---

## 5. 成功/失败判定线 (The Audit)

- **成功**：次日留存 ≥ 20% + 满意度评分 ≥ 3.5/5。
- **失败**：次日留存 < 10% 或 API 成本远超 LTV（用户终身价值）。
- **优化路径**：如果留存好但成本高 → 优化 Prompt / 换更便宜的模型。

---

**原则**：Less, but better. 哪怕只有一个场景能聊得丝滑，也比 100 个卡顿的场景有价值。