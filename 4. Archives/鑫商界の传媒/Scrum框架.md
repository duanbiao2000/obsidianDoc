---
aliases: null
createdAt: 2025-03-01 02:20
updateAt: null
categories:
  - Mindset
tags:
  - Mindset/Reflection
---

燃尽图 (Burndown Chart) 是 **敏捷项目管理，尤其是 Scrum 框架** 中常用的一种 **可视化工具**，用于 **跟踪迭代 (Sprint) 或项目进度的剩余工作量**。 它能够帮助团队和利益相关者 **清晰地了解项目进展情况，及时发现潜在的风险和问题，并进行相应的调整**。

简单来说，燃尽图就像一个 **进度追踪器**，它通过图形化的方式，直观地展示了在迭代或项目周期内，剩余工作量是如何随着时间推移而减少的。

**让我们详细了解燃尽图：**

**1. 燃尽图的定义和目的：**

- **定义：** 燃尽图是一种 **线形图**，它 **纵轴表示剩余工作量** (通常以故事点、理想工时或剩余任务数等单位计量)，**横轴表示时间** (通常是迭代或项目的周期，例如天、周等)。 图表上会绘制一条或多条线，用来展示 **理想状态下的剩余工作量趋势** 和 **实际剩余工作量趋势**。

- **目的：**

  - **可视化进度：** 直观地展示迭代或项目的整体进展情况，让团队和利益相关者一目了然。
  - **跟踪剩余工作量：** 持续跟踪剩余工作量，帮助团队了解是否能够按计划完成迭代目标或项目目标。
  - **识别潜在风险：** 通过观察燃尽图的趋势，及时发现进度偏差和潜在的风险，例如任务延期、工作量估算不准确等。
  - **促进团队协作：** 燃尽图作为一种共享的透明信息，可以促进团队成员之间的沟通和协作，共同努力达成迭代目标。
  - **透明沟通：** 向利益相关者提供项目进度的透明视图，建立信任，并为及时的决策提供依据。

**2. 燃尽图的组成部分：**

一个典型的燃尽图通常包含以下几个关键组成部分：

- **横轴 (X 轴)：时间 (Time)**

  - 表示 **迭代周期或项目周期的时间范围**。 通常以天 (Daily Burndown Chart) 或者迭代周期中的迭代 (Sprint Burndown Chart) 为单位。
  - 例如，如果迭代周期为两周 (10个工作日)，横轴可能就会标示 Day 1, Day 2, Day 3, ..., Day 10。
- **纵轴 (Y 轴)：剩余工作量 (Work Remaining)**

  - 表示在迭代或项目开始时 **估算的总工作量**，以及 **随着时间推移剩余的工作量**。
  - 工作量单位可以是：
    - **故事点 (Story Points):** 敏捷开发中常用的相对估算单位，体现工作量的大小和复杂度 (如图片文字例子中所用)。
    - **理想工时 (Ideal Hours):** 预估完成任务所需的理想工作小时数。
    - **剩余任务数 (Number of Remaining Tasks):** 剩余未完成的任务数量。
- **理想燃尽线 (Ideal Burndown Line)**

  - 通常是一条 **直线**，从迭代开始时的总工作量 **线性下降到迭代结束时的 0**。
  - **理想状态的进度：** 理想燃尽线代表了在 **完美情况下，团队每天应该完成的工作量**，即每天平均完成的工作量。 例如，如果一个迭代周期为 5 天，总工作量为 25 个故事点，理想燃尽线就表示每天应该完成 5 个故事点。
- **实际燃尽线 (Actual Burndown Line)**

  - 是一条 **折线或曲线**，代表了 **实际的剩余工作量** 随时间变化的趋势。 这条线根据 **每日 (或定期) 实际完成的工作量数据** 绘制而成。
  - **实际进度：** 实际燃尽线反映了团队 **真实的开发进度**。 其走势会受到各种因素的影响，例如任务估算偏差、突发问题、需求变更等等。

**3. 如何解读燃尽图？**

通过观察燃尽图的 **实际燃尽线与理想燃尽线的相对位置和趋势**，可以解读出迭代或项目的进度情况和潜在问题：

- **理想情况：** **实际燃尽线大致沿着理想燃尽线下降**。 这表示项目进展顺利，团队按照计划完成了工作，迭代很可能按时完成。

- **进展落后：实际燃尽线位于理想燃尽线之上**。

  - **解读：** 这表明实际完成的工作量 **低于** 理想进度，迭代或项目进展 **落后于计划**。
  - **可能原因：** 任务估算过低、开发过程中遇到困难、团队效率低于预期、需求蔓延等。
  - **应对措施：** 团队需要 **分析原因，及时调整计划**，例如重新评估剩余工作量、调整任务优先级、增加资源、优化工作流程等。 也可能需要与产品负责人沟通，调整迭代范围或延长迭代周期 (但通常应尽量避免延长迭代周期)。

- **进展超前：实际燃尽线位于理想燃尽线之下**。

  - **解读：** 这表明实际完成的工作量 **高于** 理想进度，迭代或项目进展 **超前于计划**。
  - **可能原因：** 任务估算过高、团队效率高于预期、任务拆分过细等。
  - **应对措施：** 虽然进度超前是好事，但也需要 **分析原因**。 可能是任务估算存在系统性偏差，需要改进估算方法。 也可能是团队有余力，可以考虑 **提前完成一些后续迭代的任务，或者优化现有功能**。

- **实际燃尽线趋于平缓或向上：**

  - **解读：** 实际燃尽线 **趋于平缓** 表示 **工作量几乎没有减少**，进度停滞不前。 **实际燃尽线向上** 表示 **剩余工作量反而增加了**，进度严重落后，可能发生了需求变更或新增了大量任务。
  - **可能原因：** 团队遇到了严重的瓶颈或障碍、任务依赖关系处理不当、需求频繁变更、新增了超出迭代计划范围的任务等。
  - **应对措施：** 需要 **立即调查原因，采取紧急措施**。 例如，解决技术难题、调整团队成员、重新规划迭代、与产品负责人沟通需求变更等。 这种情况通常需要团队进行深入的反思和调整。

**4. 在 JIRA 中使用燃尽图：**

如图片文字所示，团队在 JIRA 中建立了 Scrum Sprint 和 Board，并 "采用 JIRA 功能以故事点来绘制燃尽图"。

JIRA 燃尽图与 JIRA 的其他功能 (例如 Backlog 管理、Sprint 计划、任务看板等) 深度集成，方便团队在一个平台上完成所有敏捷管理工作。
- **如何使用 JIRA 燃尽图 (简要步骤)：**
  1. **创建 Scrum 项目和 Sprint：** 在 JIRA 中创建一个 Scrum 项目，并规划 Sprint。
  2. **估算用户故事：** 使用故事点等单位估算 Sprint Backlog 中的用户故事。
  3. **开始 Sprint：** 启动 Sprint。
  4. **更新任务状态：** 在 Sprint 进行过程中，团队成员及时更新任务状态 (例如 "To Do" -> "In Progress" -> "Done")。
  5. **查看燃尽图：** 在 JIRA Sprint 报告中，即可查看自动生成的燃尽图，实时监控 Sprint 进度。



##  7 种燃尽图状态

**1. 理想燃尽 (Ideal Burndown)**

- **燃尽图形状：** 实际燃尽线几乎完美地沿着理想燃尽线平稳下降，并在迭代结束时接近或达到零。
- **团队状态：**
    - **进展顺利：** 团队工作进展非常顺利，几乎完全按照计划执行。
    - **估算准确：** 初始工作量估算比较准确，团队速度与预期相符。
    - **计划有效：** 迭代计划合理可行，团队执行力强。
- **可能的原因：**
    - **经验丰富的团队：** 团队成员协作良好，经验丰富，对任务和工作量有准确的把握。
    - **需求清晰稳定：** 迭代需求非常清晰且在迭代过程中没有发生重大变更。
    - **良好的流程和纪律：** 团队遵循良好的敏捷实践，每日站会、任务看板等机制有效运作。
- **应对行动：**
    - **保持良好势头：** 继续保持当前的工作方式和节奏。
    - **庆祝成功：** 肯定团队的努力和成就，鼓励士气。
    - **反思和总结：** 回顾迭代过程，总结成功的经验，为后续迭代积累最佳实践。

**2. 加速燃尽 (Accelerated Burndown)**

- **燃尽图形状：** 实际燃尽线在迭代初期缓慢下降，但在中期或后期突然加速下降，并在迭代结束前就接近或达到零。
- **团队状态：**
    - **前期慢热，后期加速：** 团队可能在迭代初期启动较慢，但之后逐渐进入状态，效率提升。
    - **提前完成：** 迭代目标可能提前完成，团队有剩余时间。
- **可能的原因：**
    - **前期准备不足：** 迭代初期可能存在一些准备工作不足的情况，例如环境配置、依赖问题等，导致进度缓慢。
    - **后期效率提升：** 团队在迭代过程中逐渐熟悉任务，解决障碍，效率提高。
    - **任务难度分布不均：** 迭代初期任务难度较高，后期任务相对简单。
    - **提前完成部分任务：** 团队可能提前完成了部分后续迭代的任务。
- **应对行动：**
    - **分析加速原因：** 了解后期效率提升的原因，例如是流程优化、技能提升还是任务难度降低等。
    - **重新评估剩余时间：** 如果迭代目标提前完成，可以考虑在剩余时间内增加新的价值，例如处理技术债务、优化现有功能、提前规划下一个迭代等。
    - **改进启动阶段：** 在后续迭代中，改进迭代启动阶段的准备工作，例如提前进行技术调研、环境配置等，避免前期启动缓慢。

**3. 延迟燃尽 (Delayed Burndown)**

- **燃尽图形状：** 实际燃尽线在迭代初期快速下降，但在中期或后期趋于平缓，甚至停滞，在迭代结束时仍然高于零。
- **团队状态：**
    - **前期快速，后期乏力：** 团队在迭代初期进展迅速，但后期遇到阻碍，速度减慢。
    - **迭代延期风险：** 迭代目标可能无法按时完成，存在延期风险。
- **可能的原因：**
    - **前期任务简单：** 迭代初期任务难度较低，容易完成。
    - **后期遇到难题：** 迭代后期遇到技术难题、集成问题、依赖问题、突发Bug 等阻碍，导致进度受阻。
    - **估算偏差：** 后期任务的工作量可能被低估。
    - **团队能力不足：** 团队在某些方面能力不足，无法有效解决后期遇到的问题。
- **应对行动：**
    - **立即调查原因：** 尽快查明后期进度缓慢的原因，例如是技术难题、人员瓶颈还是需求变更等。
    - **解决障碍：** 集中团队力量，共同解决遇到的难题，例如寻求专家帮助、重新分配任务、简化方案等。
    - **重新评估和调整计划：** 根据实际情况，重新评估剩余工作量和迭代计划，必要时与产品负责人沟通，调整迭代范围或优先级。
    - **关注风险：** 密切关注燃尽图，及时预警迭代延期风险。

**4. 锯齿状燃尽 (Sawtooth Burndown)**

- **燃尽图形状：** 实际燃尽线呈现锯齿状，有明显的上下波动，每天工作量完成情况起伏较大，但总体趋势仍然是下降的。
- **团队状态：**
    - **工作不稳定：** 团队每日的工作效率波动较大，有些天进展顺利，有些天进展缓慢。
    - **任务依赖性强：** 任务之间可能存在较强的依赖关系，导致某些任务完成后才能集中精力完成后续任务。
- **可能的原因：**
    - **任务依赖关系复杂：** 任务之间存在较强的依赖关系，导致团队需要等待前置任务完成后才能开始后续任务，造成工作量波动。
    - **外部依赖：** 团队工作可能依赖于外部团队或资源的交付，外部依赖的延迟会影响团队进度。
    - **团队成员技能不均衡：** 团队成员技能分布不均衡，导致某些任务只能由特定成员完成，造成任务分配不均和工作量波动。
    - **会议或非开发活动过多：** 某些天可能安排了较多的会议、评审、培训等非开发活动，影响了实际开发时间。
- **应对行动：**
    - **分析波动原因：** 深入分析锯齿状波动的原因，例如是任务依赖关系、外部依赖还是会议安排等。
    - **优化任务依赖：** 尽可能地解耦任务，减少任务之间的依赖关系，使任务更独立和可并行。
    - **管理外部依赖：** 提前识别和管理外部依赖，与相关团队或资源保持沟通，减少外部依赖带来的延迟。
    - **平衡团队技能：** 提升团队成员的技能，或者调整团队结构，使团队技能更均衡，减少任务分配不均的情况。
    - **合理安排会议和活动：** 合理安排会议和非开发活动，尽量减少对开发时间的干扰。

**5. 范围蔓延 (Scope Creep) 或 需求变更 (Scope Change) 燃尽**

- **燃尽图形状：** 实际燃尽线在一段时间内下降，但突然 **向上反弹或持平**，然后可能再次下降，但整体剩余工作量增加，理想燃尽线也可能向上调整。
- **团队状态：**
    - **范围蔓延或需求变更：** 在迭代过程中，新增了计划外的用户故事或需求变更，导致总工作量增加。
    - **计划失效：** 原有的迭代计划受到较大影响，需要重新调整。
- **可能的原因：**
    - **需求理解不清晰：** 迭代初期对用户需求理解不透彻，导致在迭代过程中不断发现新的需求。
    - **需求变更频繁：** 产品负责人或客户在迭代过程中频繁提出新的需求变更。
    - **范围管理不足：** 团队对迭代范围管理不足，未能有效控制范围蔓延。
- **应对行动：**
    - **明确需求变更流程：** 建立清晰的需求变更流程，规范需求变更的提出、评审和批准流程。
    - **评估变更影响：** 每次需求变更都需要评估对迭代计划的影响，包括工作量、时间、资源等，并与产品负责人沟通。
    - **调整迭代计划：** 根据需求变更的影响，及时调整迭代计划，包括调整 Sprint Backlog、重新估算工作量、调整迭代目标等。
    - **加强需求沟通和理解：** 在迭代计划会议和每日站会上，加强与产品负责人的沟通，确保对需求的充分理解。
    - **范围控制：** 加强迭代范围控制，严格控制非必要的范围蔓延。

**6. 平缓燃尽 (Flat Burndown)**

- **燃尽图形状：** 实际燃尽线几乎呈水平直线，几乎没有下降，即使迭代结束时仍然接近初始工作量。
- **团队状态：**
    - **进展停滞：** 团队在迭代期间几乎没有完成任何工作，迭代进度严重停滞。
    - **严重问题：** 可能存在非常严重的问题，阻碍了团队正常工作。
- **可能的原因：**
    - **团队遇到严重阻碍：** 例如，遇到技术难题无法解决、关键人员离职、环境崩溃、外部依赖彻底中断等。
    - **计划会议或启动会议未完成：** 迭代计划会议或启动会议可能没有有效完成，导致团队没有明确的迭代目标和计划。
    - **团队士气低落：** 团队可能士气低落，缺乏工作动力。
    - **工具或流程问题：** 工具或流程出现严重问题，影响团队工作效率。
- **应对行动：**
    - **紧急介入：** Scrum Master 或项目经理需要立即紧急介入，了解问题的根源。
    - **深度诊断：** 与团队成员深入沟通，诊断问题的具体原因，例如技术难题、人员问题、流程问题等。
    - **排除障碍：** 优先解决阻碍团队工作的关键问题，例如协调资源、解决技术难题、调整人员等。
    - **重新评估迭代：** 根据问题解决情况，重新评估迭代计划的可行性，必要时可能需要取消或重新规划迭代。
    - **关注团队士气：** 关注团队士气，采取措施提振团队信心。

**7. 陡峭下降后平缓 (Steep Drop then Flat Burndown)**

- **燃尽图形状：** 实际燃尽线在迭代初期快速陡峭下降，但之后迅速趋于平缓，变成水平直线，几乎不再下降。
- **团队状态：**
    - **前期完成部分简单任务：** 团队在迭代初期快速完成了部分较为简单或容易的任务。
    - **后期遇到困难，停滞不前：** 后期任务难度较高或遇到阻碍，导致进度停滞。
    - **任务分配不均：** 可能存在任务分配不均的情况，部分成员在前期快速完成任务，但后续任务分配不足，或者后续任务难度过高超出能力范围。
- **可能的原因：**
    - **迭代计划不合理：** 迭代计划可能没有充分考虑任务难度和依赖关系，导致任务分配不均衡。
    - **前期任务过于简单：** 迭代初期安排的任务可能过于简单，容易快速完成。
    - **后期任务难度过高：** 迭代后期任务难度较高，超出团队能力范围，或者没有及时寻求帮助。
    - **技能瓶颈：** 团队在某些技能方面存在瓶颈，无法有效解决后期遇到的难题。
- **应对行动：**
    - **重新审视任务计划：** 重新审视迭代计划，检查任务分解和依赖关系是否合理，任务分配是否均衡。
    - **调整任务分配：** 根据团队成员技能和任务难度，重新调整任务分配，确保任务分配合理均衡。
    - **技能提升：** 针对团队技能瓶颈，提供相应的培训和学习资源，提升团队技能水平。
    - **寻求外部支持：** 如果团队遇到技术难题无法解决，可以考虑寻求外部专家或技术支持。
    - **关注后期任务：** 在后续迭代计划中，更加关注后期任务的难度和风险，提前做好准备。

