---
aliases: 
theme: 
source: 
author: 
tags: 
date: 
categories: 
important: false
---


1. **流程图 (Flowchart)**:
   ```mermaid
   graph TD;
     A[开始] --> B[过程1]
     B --> C{决策点}
     C -->|是| D[结果1]
     C -->|否| E[结果2]
     D --> F[结束]
     E --> F
   ```

2. **序列图 (Sequence Diagram)**:
   ```mermaid
   sequenceDiagram
     Alice->>Bob: Hello Bob, how are you?
     Bob-->>Alice: I am good thanks!
     Alice->>Bob: Glad to hear that!
   ```

3. **甘特图 (Gantt Chart)**:
   ```mermaid
   gantt
     title 项目开发甘特图
     dateFormat  YYYY-MM-DD
     section 设计
     设计阶段1 :done,    des1, 2023-01-01,2023-01-05
     设计阶段2 :active,  des2, after des1, 5d
     section 开发
     开发阶段1 :         dev1, after des2, 5d
     开发阶段2 :         dev2, after dev1, 5d
   ```

4. **类图 (Class Diagram)**:
   ```mermaid
   classDiagram
     Animal <|-- Duck
     Animal <|-- Fish
     Animal <|-- Zebra
     Animal : +int age()
     Duck : +string swim()
     Fish : -int age()
     Zebra : +bool is_wild()
   ```

5. **状态图 (State Diagram)**:
   ```mermaid
   stateDiagram-v2
     [*] --> Still
     Still --> [*]
     Still --> Moving
     Moving --> Still
     Moving --> Crash
     Crash --> [*]
   ```

6. **实体关系图 (Entity Relationship Diagram)**:
   ```mermaid
   erDiagram
     CAR ||--o{ DRIVER : has
     CAR {
       int CAR_ID
       string CAR_NAME
     }
     DRIVER {
       string DRIVER_NAME
       int LICEENCE_ID
     }
   ```

7. **用户旅程图 (Journey Diagram)**:
   ```mermaid
   journey
     title My Working Day
     section Go to work
       I go from home to my working place : get ready
     section Do work
       I do my work : doing
     section End of day
       I go back to home : going home
   ```


9. **饼图 (Pie Chart)**:
   ```mermaid
   pie
     "A" : 386
     "B" : 386
     "C" : 386
     "D" : 386
     "E" : 386
   ```
