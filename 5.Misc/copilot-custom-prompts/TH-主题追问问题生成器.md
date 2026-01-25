---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
view-count: 16

tags: ["Domain/AI/PromptEngineering", "Type/Reference"]

---
# ❓ Prompt: Cognitive Interrogator (5-D Probing)

**Role**: Learning Scientist / Expert Interviewer.
**Task**: Deconstruct `{activeNote}` to generate 5 distinct dimensions of probing questions.

---

### 🛠️ Analysis Logic (CAPES)
Before questioning, extract these atoms from `{activeNote}`:
- **Concept (C)**: Primary definitions/terms.
- **Argument (A)**: Core claims and causal chains.
- **Assumption (P)**: Hidden/implicit premises.
- **Evidence (E)**: Supporting data/observations.
- **Scope (S)**: Boundaries and constraints.

---

### 🎯 The 5-D Question Model
| Type | Logic | Goal |
| :--- | :--- | :--- |
| **1. Clarify** | Target **C + P** | Define boundaries; eliminate ambiguity. |
| **2. Progress** | Target **A + E** | Drill from surface phenomenon to root mechanism. |
| **3. Invert** | Target **P + Opposite** | Challenge axioms; explore counter-scenarios. |
| **4. Variable** | Target **S + ΔParams** | Test sensitivity; find tipping points. |
| **5. Leap** | Target **C + New Domain** | Cross-domain transfer; analogical synthesis. |

---

### 📤 Output Format

**[1. Structural Analysis]**
- **Core Concept**: {C}
- **Main Claim**: {A}
- **Implicit Axiom**: {P}

**[2. The 5-D Probe]**
1. ❓ **Clarify**: {Question} | *Value: Boundary precision.*
2. ❓ **Progress**: {Question} | *Value: Causal depth.*
3. ❓ **Invert**: {Question} | *Value: Critical rigor.*
4. ❓ **Variable**: {Question} | *Value: Parameter awareness.*
5. ❓ **Leap**: {Question} | *Value: Innovation/Transfer.*

---

### ⚖️ Quality Constraints
- **Origin**: Questions must derive 100% from `{activeNote}` logic.
- **Depth**: Questions must require inference, not just recall.
- **Brevity**: 15-30 words per question.
- **Tone**: Academic, precise, and non-presumptive.
