---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
view-count: 2
---
将笔记改写为“经验主义证据（Empirical Evidence）”风格，意味着要**剥离主观情绪**，将内容转化为**基于观察、数据和可验证事实**的描述。

这种风格通常用于科学报告、学术摘要或数据分析。它要求用“观察到了什么”代替“我觉得什么”，用“相关性”代替“因为”。

以下为您提供三个不同侧重点的提示词（Prompt）：

### 选项一：严谨学术报告版（适合将观点转化为理论假设）

这个版本会将你的笔记看作是一个“定性研究”的结论，用学术界常用的“假设-观察-结论”框架来重写。

> **优化后的 Prompt：**
> 
> **角色**：你是一位严谨的科学研究员，专注于基于实证的研究（Empirical Research）。  
> **任务**：请将这段笔记内容 {activeNote} 重写为一段**基于实证证据的学术综述**。
> 
> **改写要求**：
> 
> 1. **去主观化**：移除所有第一人称（"I", "me"）和主观形容词（如 "good", "bad"）。改用被动语态或客观主语（如 "The data suggests", "Observations indicate"）。
>     
> 2. **术语替换**：
>     
>     - 将“想法”转化为“假设”（Hypothesis）。
>         
>     - 将“经历”转化为“观察数据”（Observed data）。
>         
>     - 将“结果”转化为“统计显著性”或“相关性”（Correlation/Causality）。
>         
> 3. **结构**：按照“现象描述 -> 证据/机制分析 -> 结论推导”的逻辑撰写。
>     
> 
> **语调**：冷静、客观、分析性强。请使用类似 "It has been demonstrated that...", "Empirical findings support the notion that..." 这样的句式。

---

### 选项二：数据分析师风格（适合具体的流程或复盘笔记）

如果你的笔记包含具体做事的步骤或反馈，这个版本会将其转化为类似“实验报告”的风格，强调变量和结果。

> **优化后的 Prompt：**
> 
> **任务**：请以数据分析师的视角，将 {activeNote} 改写为一份**实验观察报告**。
> 
> **核心指令**：
> 
> - **定义变量**：找出笔记中的核心因素，将其定义为独立变量（Independent Variable）和因变量（Dependent Variable）。
>     
> - **描述机制**：用“输入-输出”的逻辑描述笔记中的事件。例如，不要说“我很累”，要说“系统显示出能量水平显著下降”。
>     
> - **证据导向**：使用“Evidentiary support”（证据支持）的口吻。如果笔记中没有具体数字，请用定性指标描述（如 "High frequency", "Significant deviation"）。
>     
> 
> **输出格式**：
> 
> - **Observation (观察)**：[客观描述发生了什么]
>     
> - **Methodology (机制)**：[笔记中的逻辑路径]
>     
> - **Empirical Conclusion (实证结论)**：[基于事实得出的推论]
>     

---

### 选项三：行为科学观察版（适合个人感悟或日记）

如果你的笔记是关于个人习惯或心理活动的，这个版本会把你当作“实验对象（Subject）”来描述，非常有趣且客观。

> **优化后的 Prompt：**
> 
> **请重写：** {activeNote}
> 
> **风格设定**：行为心理学观察记录（Behavioral Science Observation）。
> 
> **具体要求**：
> 
> 1. 将笔记作者视为“受试者（The Subject）”。
>     
> 2. 将笔记中的情绪或心理活动描述为“可观测的行为模式”或“神经认知反应”。
>     
> 3. **关键词使用**：请大量使用如 manifested（表现出）, correlated with（与...相关）, longitudinal patterns（纵向模式）, stimulus-response（刺激-反应） 等词汇。
>     
> 4. **目标**：证明笔记中的观点不是“凭空想象”，而是有“可重复的某种规律”支撑的。
>     

---

### 💡 风格对比示例

假设你的笔记是：

> "我觉得早起很难，因为晚上总想刷手机，结果第二天效率很低。"

- **普通改写**：It is hard to get up early because of phone usage at night.
    
- **Empirical Evidence风格（选项一/三）**：
    
    > "Observational data indicates a strong negative correlation between late-night screen exposure (independent variable) and subsequent morning cognitive performance. The subject exhibited a recurring pattern of delayed sleep onset due to digital stimuli, resulting in a quantifiable decrease in productivity metrics the following day. This supports the hypothesis that circadian rhythm disruption is a primary factor in efficiency loss."  
    > (观察数据表明，深夜屏幕接触（自变量）与随后的早晨认知表现之间存在强烈的负相关。受试者表现出一种因数字刺激而延迟入睡的反复模式，导致次日生产力指标量化下降。这支持了昼夜节律紊乱是效率损失主要因素的假设。)