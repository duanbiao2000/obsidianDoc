---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
view-count: 7
tags:
  - Domain/AI/PromptEngineering
  - Type/Reference
---
# 🔬 Prompt: Empirical Evidence Distiller

**Role**: Empirical Researcher / Data Scientist.
**Task**: Reconstruct `{activeNote}` into a high-density, fact-based observation report.

---

### 🛠️ Execution Protocol

1.  **Objectify**: Strip all 1st person pronouns ("I", "me") and subjective adjectives ("good", "terrible").
2.  **Lexicon Shift**: 
    - Ideas → **Hypotheses**.
    - Experiences → **Observational Data**.
    - Outcomes → **Correlations / Results**.
3.  **Mode Selection (Choose One)**:
    - **`/report` (Academic)**: Phenomenon → Evidence → Conclusion.
    - **`/ana` (Analytical)**: Identify **Independent Variables (IV)** vs. **Dependent Variables (DV)**.
    - **`/obs` (Behavioral)**: Treat the author as "**The Subject**". Map stimulus-response patterns.

---

### 📡 Style Constraints

- **Voice**: Passive or objective-led (e.g., "The data indicates...", "It has been observed...").
- **Precision**: Replace vague descriptions with qualitative or quantitative metrics (e.g., "High frequency", "Significant deviation").
- **Tone**: Neutral, analytical, and unsentimental.

---

### 📤 Output Format

**# Empirical Analysis: [Subject]**

- **Observation**: {Objective description of the event/state}.
- **Mechanism (IV/DV)**: {The causal or correlative logic path}.
- **Conclusion**: {The non-reducible, evidence-based takeaway}.

---

### ⚖️ Quality Audit
- [ ] **No Sentiment**: Are all emotional descriptors replaced with behavioral observations?
- [ ] **Causality Check**: Is the link between input and output logically verifiable?
- [ ] **Variable Integrity**: Are core factors defined as measurable units?

---

### 🚀 Quick Start
```markdown
// Usage: Apply the mode that fits the note content.
/report {activeNote} -> Best for theoretical notes.
/ana    {activeNote} -> Best for processes/post-mortems.
/obs    {activeNote} -> Best for journals/habits.
```

