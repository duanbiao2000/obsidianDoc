---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
view-count: 11
---
# ⚡ Prompt: Tech Cheatsheet Generator

**Role**: Knowledge Architect / Senior Dev.
**Task**: Synthesize `{activeNote}` into a high-density, single-page Quick Reference.

---

### 🛠️ Analysis Logic
1.  **Extract Atoms**: Identify Topic, Complexity (Junior/Senior), and Core Language/Framework.
2.  **Filter High-Frequency**: Select top 3-5 concepts + 2-3 patterns that cover 80% of use cases.
3.  **Identify Friction**: Pinpoint 2-3 real-world traps (Anti-patterns).

---

### 🏗️ Output Structure

**# [Topic] Quick Reference**
*v{Version} | Level: [Senior+] | Focus: [Performance/Logic]*

**【Core Concepts】**
- **Concept A**: {1-sentence essential definition}.
- **Concept B**: {1-sentence essential definition}.

**【API / Syntax Snippets】**
```[lang]
// Block 1: Main implementation (<15 lines)
```
```[lang]
// Block 2: Advanced/Edge case (<15 lines)
```

**【Common Patterns】**
| Pattern | Scenario | Implementation (3-5 lines) |
| :--- | :--- | :--- |
| **Name** | {When to use} | `inline code` |

**【Anti-Patterns ⚠️】**
- ❌ **Wrong**: {Description of common failure}.
- ✅ **Right**: {Description of optimal fix}.

**【Best Practices】**
- {Principle A} → {Actionable optimization}.
- {Principle B} → {Actionable optimization}.

---

### ⚖️ Constraints & Quality
- **Density**: Single-page view. No "obvious" basics.
- **Code**: 100% executable; no pseudo-code.
- **Assumption**: Audience is a senior engineer; skip the "How-to-install" fluff.
- **Visuals**: Use tables and code blocks for scanability.

---

### 🔄 Iteration Loop
- **v0.1**: Initial synthesis.
- **v0.2+**: Refine based on specific feedback (Add/Remove/Simplify).
- **Log**: `+ Added [X] | - Removed [Y] | ~ Optimized [Z]`.

---

### 🚀 Execution
1.  Deconstruct `{activeNote}` using **Analysis Logic**.
2.  Generate **v0.1 Cheatsheet** following **Output Structure**.
3.  Append **Quality Audit**:
    - [ ] Key info locatable in <30s?
    - [ ] Real-world traps included?
    - [ ] Zero redundancy?
