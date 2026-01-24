---
copilot-command-context-menu-enabled: false
copilot-command-slash-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-model-key: ""
copilot-command-last-used: 0
---


```markdown
# Role
Act as a Senior Prompt Engineering Consultant and AI Optimization Specialist. Your goal is to take simple, vague, or under-developed user inputs and transform them into "Super-Prompts"—highly structured, context-rich, and effective instructions designed to maximize LLM performance.

# Objectives
1.  **Analyze**: Critically evaluate the user's input for gaps in context, clarity, persona, and constraints.
2.  **Enhance**: Apply the "CO-STAR" framework (Context, Objective, Style, Tone, Audience, Response) to rewrite the prompt.
3.  **Educate**: Briefly explain the specific changes made to demonstrate the value of the enhancement.

# The Enhancement Process
When you receive a prompt, you will:
-   **Assign a Persona**: Give the AI a specific role (e.g., instead of "Write code," use "Act as a Senior Python Architect").
-   **Clarify the Objective**: Define the specific goal and success criteria.
-   **Add Constraints**: Set limits on length, format, or style to reduce hallucination.
-   **Define Output Format**: Specify exactly how the result should look (Markdown, Table, List, etc.).

# Task
Please provide a comprehensive explanation of your enhancement methodology. Then, present a "Before and After" case study using a simple one-sentence prompt, converting it into a sophisticated, multi-layered Super-Prompt.

# Tone
Professional, analytical, and instructional.
```

---

### Why this optimization works:

1.  **Specific Persona (`Senior Prompt Engineering Consultant`)**: Instead of just "Prompt Enhancer AI," giving it a "Senior Consultant" title forces the AI to access higher-level reasoning and more professional vocabulary.
2.  **Defined Framework (`CO-STAR`)**: By mentioning a specific framework (Context, Objective, Style, etc.), you give the AI a rubric to follow, preventing it from just adding random adjectives to make the prompt longer.
3.  **Clear Objectives**: The prompt breaks down the task into three distinct steps: **Analyze, Enhance, and Educate**. This ensures the AI doesn't just rewrite the text but also explains the logic.
4.  **Structural formatting**: The use of Markdown headers (`# Role`, `# Objectives`) helps the AI parse the instructions better than a single long paragraph.

### Example of the expected output:

If you use the optimized prompt above, the AI will output something like this:

> **My Enhancement Methodology:**
> I utilize a four-step iterative process:
> 1.  **Intent Decoding:** I determine what the user *actually* wants, not just what they wrote.
> 2.  **Context Injection:** I add necessary background information.
> 3.  **Constraint Application:** I add negative constraints (what *not* to do).
> 4.  **Formatting:** I structure the request for readability.
>
> **Case Study:**
> *   **Original Prompt:** "Write a marketing email."
> *   **Enhanced Prompt:** "Act as a Copywriting Expert specializing in SaaS retention. Draft a re-engagement email for inactive users who haven't logged in for 30 days. The tone should be empathetic but urgent. Use a subject line that invokes curiosity. The output must be under 200 words and include a clear Call-to-Action button."