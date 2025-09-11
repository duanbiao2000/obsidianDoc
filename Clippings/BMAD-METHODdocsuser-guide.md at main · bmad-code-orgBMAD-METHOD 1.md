---
title: BMAD-METHOD/docs/user-guide.md at main · bmad-code-org/BMAD-METHOD
source: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/working-in-the-brownfield.md
author:
  - "[[GitHub]]"
published:
date: 2025-08-17
description: Breakthrough Method for Agile Ai Driven Development - BMAD-METHOD/docs/user-guide.md at main · bmad-code-org/BMAD-METHOD
tags:
  - clippings
---
### 决策树```
Do you have a large codebase or monorepo?
├─ Yes → PRD-First Approach
│   └─ Create PRD → Document only affected areas
└─ No → Is the codebase well-known to you?
    ├─ Yes → PRD-First Approach
    └─ No → Document-First Approach

Is this a major enhancement affecting multiple systems?
├─ Yes → Full Brownfield Workflow
│   └─ ALWAYS run Test Architect *risk + *design first
└─ No → Is this more than a simple bug fix?
    ├─ Yes → *create-brownfield-epic
    │   └─ Run Test Architect *risk for integration points
    └─ No → *create-brownfield-story
        └─ Still run *risk if touching critical paths

Does the change touch legacy code?
├─ Yes → Test Architect is MANDATORY
│   ├─ *risk → Identify regression potential
│   ├─ *design → Plan test coverage
│   └─ *review → Validate no breakage
└─ No → Test Architect is RECOMMENDED
    └─ *review → Ensure quality standards
```