LangChain 是用於構建具有特定能力的 AI 代理 (Agent) 的框架，例如能夠操作瀏覽器或執行程式碼。
而 LangGraph 則是一個圖框架，專門用於將這些由 LangChain 或其他方式創建的獨立代理及其他組件，編排成複雜、狀態化的對話或工作流程 (Workflow)。
例如，GPT Researcher 便是利用 LangChain 構建執行不同任務的代理，再由 LangGraph 將這些代理協調起來，形成一個自動化的研究系統。