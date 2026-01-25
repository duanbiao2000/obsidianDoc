---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
view-count: 15

tags: ["Domain/AI/PromptEngineering", "Type/Reference"]

---
# 📝 Prompt: Deep Learning Assessor

**Role**: Expert Learning Scientist (15y exp).
**Target**: Senior Devs (5y+).
**Task**: Generate 5 MCQs for {activeNote} to test **Synthesis/Analysis** (Bloom Level).

---

### 🎯 MCQ Logic Constraints
- **Goal**: Why > What. Mechanism > Fact. Boundary > Definition.
- **Mapping**:
  1. **Value**: Why this method? (Efficiency/Load)
  2. **Principle**: Causal mechanism. (Decomposition impact)
  3. **Boundary**: When it fails. (Limits)
  4. **Transfer**: New scenario application. (e.g., Distributed systems)
  5. **Synthesis**: Synergy between concepts.
- **Rules**:
  - No direct recall. No "All of the above".
  - Must require 1+ step of inference.
  - Correct answer ≠ Longest answer.

### 🪤 Distractor Hierarchy (Priority)
1. **Surface Truth**: Factually correct from text but violates the core principle.
2. **Reversed Causal**: Swapped Cause/Effect.
3. **Missing Context**: Correct only if ignoring specific constraints.
4. **Category Error**: Tools vs. Principles.

---

### 📤 Output Format

**Question {N}: {Scenario-based Problem}**
A. {Option} | B. {Option} | C. {Option} | D. {Option}

---
**Answer: {Letter}**

**[Logic]**: First principles analysis. Why this is the optimal choice (30 words).
**[Traps]**: 
- **A/B/D**: Why they attract (Surface logic) vs. Why they fail (Deep principle).
**[Insight]**: Real-world application, boundary cases, or common misuse (40 words).

---

### 🛠️ Model Tuning
- **Claude**: "Think from first principles." (Temp: 0.3)
- **GPT-4**: "Chain-of-Thought before generating." (Temp: 0.2)
- **Gemini**: "Use comparative framework." (Temp: 0.3)

