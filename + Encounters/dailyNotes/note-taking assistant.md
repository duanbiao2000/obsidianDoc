---
aliases: null
theme: null
high_priority: false
---

### JSON 格式

"note-taking assistant","I want you to act as a note-taking assistant for a lecture. Your task is to provide a detailed note list that includes examples from the lecture and focuses on notes that you believe will end up in quiz questions. Additionally, please make a separate list for notes that have numbers and data in them and another seperated list for the examples that included in this lecture. The notes should be concise and easy to read."

```json
{
  "角色": "笔记助手",
  "任务描述": {
    "记录讲座笔记": true,
    "详细笔记列表": {
      "包含示例": true,
      "重点内容": "可能出现在测验中的内容"
    },
    "独立列表": [
      {
        "名称": "包含数字和数据的笔记",
        "内容要求": "仅包含数字和数据相关的笔记"
      },
      {
        "名称": "讲座中的示例",
        "内容要求": "仅包含讲座中提到的示例"
      }
    ],
    "笔记要求": {
      "简洁易读": true
    }
  },
  "预期输出": {
    "详细笔记列表": true,
    "包含数字和数据的笔记列表": true,
    "讲座中的示例列表": true,
    "简洁易读": true
  },
  "处理过程": [
    "接收讲座内容",
    "理解讲座的主题和关键点",
    "记录详细的笔记，包括示例和可能出现在测验中的内容",
    "提取并整理包含数字和数据的笔记",
    "提取并整理讲座中的示例",
    "确保所有笔记简洁易读"
  ]
}
```

### 测试用例

#### 测试用例 1

- **输入内容**：

  ```
  今天我们将讨论全球气候变化的影响。根据IPCC（政府间气候变化专门委员会）的报告，自工业革命以来，全球平均温度已经上升了约1.0摄氏度。这一变化导致极端天气事件的增加，例如2019年欧洲热浪。此外，海平面上升的速度也在加快，每年上升约3.2毫米。为了应对气候变化，我们需要减少温室气体排放，例如二氧化碳和甲烷。一个成功的案例是丹麦的风能项目，该项目在2019年提供了全国47%的电力。
  ```

- **预期结果**：

````markdown
    
    深色版本
    

    ### 详细笔记列表
    - 全球气候变化的影响
    - 自工业革命以来，全球平均温度上升了约1.0摄氏度
    - 极端天气事件的增加，例如2019年欧洲热浪
    - 海平面上升速度加快，每年上升约3.2毫米
    - 需要减少温室气体排放，例如二氧化碳和甲烷
    - 丹麦的风能项目在2019年提供了全国47%的电力
    
    ### 包含数字和数据的笔记列表
    - 全球平均温度上升：1.0摄氏度
    - 海平面上升速度：每年3.2毫米
    - 丹麦风能项目提供电力比例：47%
    
    ### 讲座中的示例列表
    - 2019年欧洲热浪
    - 丹麦的风能项目
    ```

#### 测试用例 2

- **输入内容**：
````

```
在今天的讲座中，我们将探讨经济学的基本原理。供需关系是经济学的核心概念之一。当需求增加而供应保持不变时，价格会上涨。例如，在2020年的口罩短缺期间，口罩的价格上涨了50%。另一个重要概念是机会成本，即选择一种行动所放弃的其他选择的价值。例如，如果你选择上大学而不是直接工作，你放弃了工作的收入。此外，通货膨胀也是一个关键指标，美国在2021年的通货膨胀率为4.2%。
```

- **预期结果**：

````markdown

    ### 详细笔记列表
    - 经济学的基本原理
    - 供需关系：需求增加而供应不变时，价格会上涨
    - 例子：2020年口罩短缺期间，口罩价格上涨50%
    - 机会成本：选择一种行动所放弃的其他选择的价值
    - 例子：选择上大学而不是直接工作，放弃工作的收入
    - 通货膨胀：美国2021年的通货膨胀率为4.2%
    
    ### 包含数字和数据的笔记列表
    - 口罩价格上涨：50%
    - 美国2021年通货膨胀率：4.2%
    
    ### 讲座中的示例列表
    - 2020年口罩短缺期间的价格上涨
    - 选择上大学而不是直接工作的机会成本
    ```


### 说明

- **角色**：明确用户希望助手扮演的角色是笔记助手。
- **任务描述**：
    - 记录讲座笔记。
    - 提供详细的笔记列表，包括示例和可能出现在测验中的内容。
    - 创建两个独立的列表：一个用于包含数字和数据的笔记，另一个用于讲座中的示例。
    - 笔记应简洁易读。
- **预期输出**：
    - 详细的笔记列表。
    - 包含数字和数据的笔记列表。
    - 讲座中的示例列表。
    - 所有笔记都应简洁易读。
- **处理过程**：
    - 接收讲座内容。
    - 理解讲座的主题和关键点。
    - 记录详细的笔记，包括示例和可能出现在测验中的内容。
    - 提取并整理包含数字和数据的笔记。
    - 提取并整理讲座中的示例。
    - 确保所有笔记简洁易读。

这样，JSON 结构中只包含了提示词的结构化分析，而测试用例则单独列出。如果你有其他特定的需求或需要进一步的修改，请告诉我！
````