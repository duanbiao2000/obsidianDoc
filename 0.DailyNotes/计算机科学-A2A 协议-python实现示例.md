---
date: 2025-04-17 00:58
update: 2025-04-23 18:50
tags:
  - DG/Seedling
---

`samples/python/` 目錄包含使用 Python 語言實現 A2A (Agent to Agent) 協議的範例程式碼。
### 主要組成部分 (Main Components)

此 `samples/python/` 目錄中的主要組成部分及其作用說明如下：

- `agents/`: 這個子目錄收集了多種 Agent 的實現範例。為了方便管理與理解，這些範例根據所使用的開發框架進一步劃分到不同的子目錄中：
- `crewai/`: 提供了使用 CrewAI 框架構建的 Agent 範例。CrewAI 是一個專門用於協調和管理多個 Agent 協同工作的框架。
- `google_adk/`: 包含了利用 Google ADK (Agent Development Kit) 開發的 Agent 範例。
- `langgraph/`: 展示了如何使用 LangGraph 框架來實現 Agent 範例。LangGraph 是一個適用於構建基於圖結構的 Agent 工作流程的框架。
- `types.py`: 這個關鍵檔案定義了在 A2A 協議實現中使用的核心數據模型類別，例如用於表示工作項目的 `Task`、Agent 間溝通內容的 `Message`，以及 Agent 產出結果的 `Artifact` 等。

### A2A 協議核心數據模型 (A2A Protocol Core Data Models)

深入理解 A2A 協議的核心數據模型對於使用和開發相關應用至關重要。這些模型在 `types.py` 檔案中被明確定義：

- **Task (任務)**: 作為 A2A 協議中的核心概念，`Task` 表示一個 Agent 需要執行或完成的一項具體工作。一個 `Task` 對象通常包含任務的詳細描述、任何必要的輸入數據，以及可能的截止日期等資訊。Agent 通過接收和處理 `Task` 來執行其功能並推動工作流程。
- **Message (消息)**: `Message` 是 Agent 之間進行資訊交換和協作的載體。`Message` 對象可以攜帶多種類型的內容，包括純文字、結構化數據或特定的指令。Agent 依賴 `Message` 來進行溝通和協同完成複雜任務。
- **Artifact (工件)**: `Artifact` 代表了 Agent 完成一個或多個 `Task` 後所產生的成果或輸出。這些工件的形式多樣，可以是檔案、數據集、報告或任何其他有價值的產出。Agent 通過生成 `Artifact` 來向系統或其他 Agent 提供其工作的價值。

#A2A #Python #Tech/Agent #CrewAI #GoogleADK #LangGraph
