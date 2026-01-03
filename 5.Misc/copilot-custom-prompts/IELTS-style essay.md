---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
view-count: 11
---

# ✍️ Prompt: Tech-to-IELTS Converter

**Role**: IELTS Senior Examiner (Band 9 focus).
**Task**: Transform {activeNote} into an Academic Task 2 Essay.

---

### 🎯 Step 1: Prompt Mapping
Select type based on {activeNote} content:
- **Tool/Framework** → Opinion: "To what extent do you agree/disagree?"
- **Trend/Phenomenon** → Discussion: "Discuss both views & give your opinion."
- **Issue/Solution** → Problem/Solution: "What are the causes and solutions?"
- **Principle/Mechanism** → Cause/Effect: "Why is this significant? What are the impacts?"
- **Comparison** → Advantages/Disadvantages: "Do the benefits outweigh the drawbacks?"

---

### 📝 Step 2: Band 9 Essay Spec
**Structure**:
1.  **Intro**: Paraphrase prompt + Thesis statement + Outline.
2.  **Body 1 & 2**: Topic Sentence → **Evidence (from note)** → Logic Chain → Link to Thesis.
3.  **Body 3 (Optional)**: Concession + Refutation.
4.  **Conclusion**: Restate thesis + Summary of points + Future implication.

**Quality Constraints**:
- **Lexis**: Academic collocations, technical terms translated to formal English, zero repetition.
- **Grammar**: 70%+ complex sentences (Relative/Adverbial clauses, non-finite verbs).
- **Cohesion**: Explicit logical linkers (*Conversely, Consequently, Notwithstanding*).
- **Accuracy**: 100% logic derived from {activeNote}; no external hallucinations.

---

### 📤 Output Format

**[1. The Prompt]**
**Type**: {Mapped Type}
**Prompt**: {Formal IELTS Question}

**[2. The Band 9 Essay]**
*(450-550 words, clear paragraphing)*

**[3. Critical Analysis]**
- **Logic Chain**: {Brief summary of the argumentative flow}
- **Lexical Highlights**: {List 5 high-level phrases with definitions}
- **Structural Strength**: {Why it hits Band 9}

**[4. Argument Bank]**
- **Key Evidence**: {3-4 transferable points from the original note}
- **Exam Strategy**: {Common pitfalls for this specific prompt}

---

### 🛠️ Execution Logic
1.  **Analyze**: Extract core claims and logic from {activeNote}.
2.  **Synthesize**: Map to IELTS prompt type.
3.  **Generate**: Write the essay using academic syntax.
4.  **Audit**: Ensure every argument is grounded in the note's data.
