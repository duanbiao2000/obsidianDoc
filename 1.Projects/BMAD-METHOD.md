---
aliases: BMAD-METHOD/docs/enhanced-ide-development-workflow.md at main · bmad-code-org/BMAD-METHOD
source: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/enhanced-ide-development-workflow.md
author:
  - "[[GitHub]]"
published:
date: 2025-08-17
description: Breakthrough Method for Agile Ai Driven Development - BMAD-METHOD/docs/enhanced-ide-development-workflow.md at main · bmad-code-org/BMAD-METHOD
tags:
  - clippings
view-count: 2
---
## BMAD-METHOD：語義壓縮版

### **核心工作流**
- ★ SM創建故事→Dev實現→QA審查→質量門檢
- ★ 測試架構師全程嵌入開發生命週期

### **關鍵階段**
- △ 故事創作：SM代理→草稿→批准
- ★ 開發實現：Dev代理→執行清單→報告
- △ QA集成：風險→設計→追溯→NFR→審查

### **測試架構師命令**
- ★ `*risk`：識別集成/回歸風險→優先級高
- ★ `*design`：創建測試策略→新功能必需
- △ `*trace`：驗證測試覆蓋→中等優先級
- ★ `*nfr`：驗證質量屬性→關鍵功能必需
- ❗ `*review`：綜合評估→**必填項**
- △ `*gate`：更新質量決策→按需執行

### **質量門狀態**
- PASS：所有要求滿足→可通過
- CONCERNS：非關鍵問題→建議審查
- ❗ FAIL：關鍵問題→必須修復
- △ WAIVED：問題已知接受→需文檔化

### **風險評分矩陣**
- ❗ 分數9：高概率×高影響→P0測試→未測試則FAIL
- 分數6：中高組合→P1測試→缺口則CONCERNS
- △ 分數4：中等組合→P1測試→顯著缺口則CONCERNS
- 分數2-3：低中組合→P2測試
- 分數1：最小風險→P2測試

### **測試質量標準**
- ★ 無不穩定測試：異步處理+顯式等待
- ❗ 無硬等待：僅動態策略（輪詢/事件）
- △ 無狀態：測試獨立並行運行
- 自清理：測試管理自身數據
- ★ 適當級別：單元(邏輯)/集成(交互)/E2E(旅程)

### **任務類型核心**
- △ advanced-elicitation：進階需求引導→挖掘隱性需求
- △ facilitate-brainstorming：結構化頭腦風暴→激發創意
- ★ brownfield-create-epic/story：遺留系統改造→兼容性優先
- △ correct-course：項目偏離→調整回歸正軌
- ★ create-deep-research-prompt：結構化提示→深度調研
- △ shard-doc+index-docs：文檔拆分+索引→提升處理效率

### **文檔模板類型**
- ★ architecture-tmpl：通用架構設計
- ❗ brownfield-*-tmpl：遺留系統專用→改造/迭代
- △ prd-tmpl：產品需求文檔
- competitor-analysis-tmpl：競品分析
- △ front-end-*-tmpl：前端架構/規格
- story-tmpl：用戶故事標準格式

### **成功指標**
- ★ 零回歸缺陷到生產環境
- ★ 100%需求測試覆蓋
- △ 清晰質量門→Go/No-Go決策
- 文檔化風險接受→技術債務管理
- ❗ 左移測試→早期風險識別

### **可遷移原則**
- ★ 質量嵌入全流程→非事後檢查
- △ 風險驅動測試→優先級明確
- ★ 文檔化決策→可追溯性保證
- △ 自助質量檢查→開發者賦能</Assistant>