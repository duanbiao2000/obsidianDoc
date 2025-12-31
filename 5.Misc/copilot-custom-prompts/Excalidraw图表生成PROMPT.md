---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 1752846074463
---
请根据我提供的文章内容,创建一个美观的 ExcaliDraw 兼容图表来可视化表达文本内容｡
输出要求:
1. 文件格式
严格按照以下结构输出,不得有任何修改:
excalidraw-plugin: parsed
tags: [excalidraw]
==⚠ Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check plugin settings under 'Saving'
# Excalidraw Data
## Text Elements
%%
## Drawing
[在这里放入JSON数据] ```json
%%
2. JSON 内容要求
创建完整的 ExcaliDraw JSON 格式,包含所有必要字段:
{
"type": "excalidraw",
"version": 2,
"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.13.0", "files": {} "elements": [...], "appState": {...},
}
- 所有文本元素使用 `fontFamily: 5`(excalifont 手写字体)
- 文本中的双引号一律替换为『』
- 文本中的圆括号一律替换为｢｣
- 确保 JSON 格式正确且包含所有 ExcaliDraw 必需字段
3. 设计原则
- **层次清晰**:使用不同颜色和形状区分不同层级的信息
- **布局合理**:元素间距适当,整体布局美观
- **颜色搭配**:使用和谐的配色方案
- **图形元素**:适当使用矩形框､圆形､箭头等元素来组织信息
- **字体大小**:根据内容重要性设置合适的字体大小(16-28px)

## Excalidraw 图表类型整理指南
根据内容特性,选择合适的图表表达形式,以提升理解力与视觉吸引力｡
1. 流程图(Flowchart)
- **使用场景**:步骤说明､工作流程､任务执行顺序
- **做法**:用箭头连接各步骤,清晰表达流程走向
- **适合案例**:
- 自动化流程拆解
- 注册流程､用户路径
- 视频或课程制作流程
2. 思维导图(Mind Map)
- **使用场景**:概念发散､主题分类､灵感捕捉
- **做法**:以中心为核心向外发散,放射状结构
- **适合案例**:
- 知识框架构建
- 提示词设计分类
- 文章写作思路整理
3. 层级图(Hierarchy Tree)
- **使用场景**:组织结构､内容分级､系统拆解
- **做法**:自上而下或自左至右构建层级节点
- **适合案例**:
- 企业架构图
- 项目分解结构(WBS)
- 课程章节层级整理
4. 关系图(Relationship Diagram)
- **使用场景**:要素之间的影响､依赖､互动关系
- **做法**:图形之间用连线表示关联,必要时添加箭头与说明文字
- **适合案例**:
- 工具之间的数据流关系
- 模块间协作路径
- 用户角色与权限关系图
5. 自由结构图(Freeform Layout)
- **使用场景**:内容零散､灵感记录､初步信息收集
- **做法**:无需结构限制,自由放置图块与箭头连接
- **适合案例**:
- 读书/文章随手笔记
- 视频大纲草图
- 未成形的创意草稿
6. 对比图(Comparison Diagram)
- **使用场景**:两种以上方案或观点的对照分析
- **做法**:常见结构为左右两栏或表格形式,标明比较维度
- **适合案例**:
- ChatGPT vs Claude
- 不同课程对比
- 工具选择指南
7. 时间线图(Timeline)
- **使用场景**:事件发展､项目进度､模型演化
- **做法**:以时间为横轴或纵轴,标出关键时间点与事件说明
- **适合案例**:
- AI 技术演变时间轴
- 项目开发节点
- 创作历程回顾
8. 矩阵图(Matrix Map)
- **使用场景**:双维度分类､任务优先级､定位分析
- **做法**:建立 X 与 Y 两个分类维度,在坐标平面中安置信息
- **适合案例**:
- 重要紧急四象限
- 产品定位矩阵
- 内容类型价值分析
9. 场景剧本图(Scenario Script)
- **使用场景**:角色行动与系统响应､用户路径演练
- **做法**:从用户角度出发,绘制“角色-操作-AI反应”顺序结构
- **适合案例**:
- AI 工具应用脚本
- Prompt 使用情境演示
- 服务体验流程设计
10. 图文混排笔记(Visual Notes)
- **使用场景**:说明性内容､教学图解､重点整理
- **做法**:组合插图､箭头､说明文字,以视觉导向清晰表达概念
- **适合案例**:
- 概念图解
- 技术说明图
- 课程重点摘要页

其他要求
5. Text Elements 处理
- `## Text Elements` 部分留空,用 `%%` 结束
- Obsidian ExcaliDraw 插件会根据 JSON 数据自动填充文本元素
- 不需要手动列出所有文本内容
7. 技术细节
- `elements` 数组包含所有图形元素(文本､矩形､圆形､箭头等)
- 每个元素需要唯一的 `id`(可以是随机字符串)
- 坐标系统:左上角为原点 (0,0)
- 确保所有元素在合理的坐标范围内(建议在 0-1200 x 0-800 区域内)
- `appState` 包含画布视图设置和当前工具状态
- 必须包含 `files: {}` 字段
8. 元素属性示例
```json
"id": "unique-id",
"type": "text|rectangle|ellipse|arrow|diamond", "x": 100, "y": 100,
"width": 200, "height": 50,
"angle": 0, "strokeColor": "#1e1e1e", "backgroundColor": "transparent", "fillStyle": "solid",
"strokeWidth": 2,
"strokeStyle": "solid", "roughness": 1, "opacity": 100, "groupIds": [], "frameId": null,
"index": "a1", "roundness": {"type": 3}, // 或 null
"seed": 123456789,
"version": 1,
"versionNonce": 987654321,
"isDeleted": false,
"boundElements": [],
"link": null, "updated": 1751928342106,
"locked": false, // 文本特有属性
"text": "显示文本", "rawText": "显示文本",
"fontSize": 20,
"fontFamily": 5, "textAlign": "center", "verticalAlign": "middle",
"containerId": null, // 或包含元素的ID
"originalText": "显示文本",
"autoResize": true,
"lineHeight": 1.25
}
```

请现在开始根据我提供的文章内容创建对应的 ExcaliDraw 图表｡