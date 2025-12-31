---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 1752963020793
---
1. 任务步骤
- 深入阅读:通读文章,抓取核心论点与关键事实。
- 信息分层:按照「主题￫子主题￫关键要点」三级结构梳理内容。
- 布局规划：坐标系以画布中心(0,0)为根节点位置；同层节点横向排列,层级向下/右递进。间距基准为节点间水平≥320px，垂直≥200px。节点尺寸：主主题≈320×140px；子主题≈260×120px；关键要点≈220×100px。连线规则为直接从父节点底边连到子节点顶边,使用直线；复杂/跨级关系,用曲线并设置toEnd:"arrow"。
- 颜色与风格：采用简洁商务配色，主主题#4A90E2，子主题#50E3C2，关键要点#F5A623；若需Obsidian预设色号，用"4"、"5"、"3"分别对应绿、青、黄；群组背景可淡灰#F7F7F7，backgroundStyle:"ratio"。
- 节点内容：文本精炼，每节点≤2行、≤60字；避免长段落。重要数据或公式可放入file节点，并在相邻文本节点中简要说明。
- ID与编码：所有id采用8~12位随机十六进制；oJSON中中文双引号替换为『』，中文单引号替换为｢｣，英文双引号需转义。
- 完整性检查：确认nodes、edges、groups(如有)均已定义；检查无坐标重叠、无孤立节点；总体视觉居中、左右权重平衡。
- 输出格式：完整符合《JSON Canvas Specification for Obsidian》的Obsidian Canvas文件；不添加其他解释文字；结果可直接由Obsidian打开。

1. 其他必须遵守的原则
- styleAttributes(可选但建议写空对象)：节点与连线均允许带"styleAttributes":{}字段。若暂时不自定义样式,务必输出空对象而不是省略。
- group.label 必填：所有type:"group"节点请填写label,哪怕只是占位,如｢分组1｣。
- 节点与分组的层级顺序(z-index)：输出nodes数组时,先写最底层的背景/大分组,再写子分组,最后写最上层的普通文本/链接节点。
- 颜色写法：颜色可用预设数字"1"~"6"或HEX；若使用HEX,推荐统一大写；避免在同一Canvas混用数字与HEX。
- 连线缺省端点：fromEnd和toEnd如果使用默认值,可省略；若需要箭头,一律写"arrow"。
- 文件与链接节点：type:"file"节点必须含file路径,若直指某段落可附subpath:"#章节标题"。type:"link"节点使用url字段指向完整的https://…。
- JSON基本格式：顶层仅包含"nodes"与"edges",不要额外包裹在对象或数组里。整个JSON不要换行注释；中文引号替换规则为中文双引号￫『』，中文单引号￫｢｣，英文双引号需要反斜杠转义\\"。

3. JSON CANVAS SPECIFICATION FOR OBSIDIAN
- TOP LEVEL：包含nodes(可选,节点数组)和edges(可选,边缘数组)两个数组。
- NODES：是画布中的对象，可分为text、file、link、group类型；按z-index升序排列在数组中，数组中第一个节点显示在最下方，最后一个显示在最上方。
  - 通用节点属性：id(必填,字符串,节点唯一ID)；type(必填,字符串,节点类型)；x(必填,整数,节点x坐标,单位像素)；y(必填,整数,节点y坐标,单位像素)；width(必填,整数,节点宽度,单位像素)；height(必填,整数,节点高度,单位像素)；color(可选,canvasColor,节点颜色)。
  - Text类型节点：除通用属性外，包含text(必填,字符串,带Markdown语法的纯文本)。
  - File类型节点：除通用属性外，包含file(必填,字符串,系统内文件路径)；subpath(可选,字符串,链接到标题或块的子路径,以#开头)。
  - Link类型节点：除通用属性外，包含url(必填,字符串,URL)。
  - Group类型节点：除通用属性外，包含label(可选,字符串,分组文本标签)；background(可选,字符串,背景图片路径)；backgroundStyle(可选,字符串,背景图片渲染风格,有效值为cover、ratio、repeat)。
- EDGES：连接节点的线。
  - 属性：id(必填,字符串,边缘唯一ID)；fromNode(必填,字符串,连接开始的节点id)；fromSide(可选,字符串,边缘开始的边,有效值为top、right、bottom、left)；fromEnd(可选,字符串,边缘起点的端点形状,默认none,有效值为none、arrow)；toNode(必填,字符串,连接结束的节点id)；toSide(可选,字符串,边缘结束的边,有效值为top、right、bottom、left)；toEnd(可选,字符串,边缘终点的端点形状,默认arrow,有效值为none、arrow)；color(可选,canvasColor,线的颜色)；label(可选,字符串,边缘的文本标签)。
- COLOR：canvasColor类型用于编码节点和边缘的颜色数据，颜色属性为字符串，可采用十六进制格式(如"#FF0000")或预设颜色(如"1"代表红色)；六个预设颜色对应为"1"红、"2"橙、"3"黄、"4"绿、"5"青、"6"紫。