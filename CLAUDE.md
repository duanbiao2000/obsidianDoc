---
tags:
  - knowledge-base-structure
  - note-taking-system
  - knowledge-management
  - obsidian
  - Type/Reference
  - knowledge-base-structure
  - note-taking-system
  - knowledge-management
  - obsidian
  - knowledge-base-structure
  - note-taking-system
  - knowledge-management
  - obsidian
  - Type/Reference
  - knowledge-base-structure
  - note-taking-system
  - knowledge-management
  - obsidian
  - knowledge-base-structure
  - note-taking-system
  - knowledge-management
  - obsidian
  - Type/Reference
  - knowledge-base-structure
  - note-taking-system
  - knowledge-management
  - obsidian
  - knowledge-base-structure
  - note-taking-system
  - knowledge-management
  - obsidian
  - Type/Reference
  - knowledge-base-structure
  - note-taking-system
  - knowledge-management
  - obsidian
---
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Type

This is an **Obsidian vault** - a personal knowledge management system implementing a modified PARA method combined with Zettelkasten principles. This is not a software development repository, but a structured knowledge base.

## Directory Structure (PARA-based)

```
├── 0.DailyNotes/          # Daily journal entries and temporal records
├── 1.Projects/            # Active projects with clear outcomes
├── 2.Topics/              # Knowledge domains and areas of interest
│   ├── 00.协议与规范/
│   ├── 01.技术栈/
│   ├── 02.认知系统/
│   ├── 03.内容创作/
│   ├── 04.职业发展/
│   ├── 05.生活与健康/
│   └── 06.语言与移民/
├── 3.Resources/           # Learning materials and references
├── 4.Archives/            # Completed projects and historical content
├── 5.Misc/                # Templates and utilities
│   └── Template/          # Standardized templates for various note types
├── 6.Calendar/            # Calendar-related notes
└── Atlas/                 # System documentation and central hub
    ├── BASE/              # Foundational principles and governance
    ├── Cards/             # Knowledge cards (Canvas, Excalidraw, PPT)
    ├── Index/             # System indexes and navigation
    └── kanban/            # Visual workflow management
```

## Core Knowledge Management Principles

### 1. PARA Method Implementation
- **Projects**: Active work with clear outcomes and deliverables
- **Areas (Topics)**: Ongoing responsibilities and knowledge domains
- **Resources**: Reference materials, learning content, assets
- **Archives**: Completed projects and inactive content

### 2. Zettelkasten System
- **Atomic Notes**: Each note contains a single concept or function
- **Molecular Cards**: Groups of related atomic notes
- **Bi-directional Links**: Primary organizational structure (over folders)
- **Connection Density**: Aim for >2 links per note for discoverability

### 3. Tag Taxonomy (Three-tier system)
```
#Domain/<SubDomain>     # e.g., #Domain/AI, #Domain/Psychology
#Status/<State>         # e.g., #Status/TODO, #Status/Review, #Status/Done
#Type/<ContentType>     # e.g., #Type/Note, #Type/Reference, #Type/Keynote
```

See `Atlas/Index/仓库标签管理系统.md` for the complete tag specification and compression rules.

## File Organization Conventions

### Index Files (MOC - Map of Content)
- Every directory should have an `_Index_of_<DirectoryName>.md` file
- Use Zoottelkeeper plugin for automatic index generation
- See `Atlas/MOCs.md` for the master list of all indexes

### Note Quality Standards
All notes should meet these criteria (from archived `claude.md范例.md`):
1. **Clarity**: Precise language, clear definitions, no ambiguity
2. **Structure**: Logical hierarchy, proper sectioning, internal links
3. **Depth**: Appropriate detail level, background context, decision rationale
4. **Maintainability**: Single source of truth, update mechanisms, reusability

### Template System
Templates are stored in `5.Misc/Template/`:
- `Zettelkasten模板.md` - Atomic note structure
- `项目管理模板.md` - Project tracking
- `研究笔记模板.md` - Research documentation
- `每日回顾模板.md` / `每周回顾模板.md` - Periodic reviews
- `Templater/` subdirectory - Templater plugin scripts

## Key Plugins and Their Uses

This vault heavily relies on Obsidian plugins:
- **dataview**: Query and index notes (see `Atlas/Index/Dataviewer.md`)
- **zoottelkeeper-obsidian-plugin**: Auto-generate index files
- **obsidian-tasks-plugin**: Task management with TODO status
- **templater-obsidian**: Advanced template scripting
- **obsidian-kanban**: Kanban boards in `Atlas/kanban/`
- **obsidian-excalidraw-plugin**: Diagrams in `Atlas/Cards/Excalidraw/`
- **obsidian-spaced-repetition**: Flashcard creation for memorization
- **smart-connections**: AI-powered note connections
- **obsidian-git**: Version control integration

## Working with This Vault

### When Creating New Notes:
1. **Determine location** based on PARA (Projects/Topics/Resources/Archives)
2. **Use appropriate template** from `5.Misc/Template/`
3. **Apply tags** following the three-tier taxonomy
4. **Add bi-directional links** to related notes (minimum 2-3)
5. **Include metadata** in YAML frontmatter (tags, related, update, rating, view-count)

### When Modifying Existing Notes:
1. **Preserve YAML frontmatter** structure
2. **Update the `update` field** with current date
3. **Maintain link integrity** - broken links reduce knowledge graph value
4. **Check for orphaned notes** when deleting content

### When Organizing Content:
- **Projects > 3 months inactive** → Move to `4.Archives/`
- **Superseded content** → Move to `4.Archives/Outdates/`
- **Always update parent index files** when moving content
- **Use `status: TODO/Review/Done` tags** to track content lifecycle

## Knowledge Processing Pipeline

The vault follows this content transformation:
```
Raw Information → Question Focus → Key Info Extraction → Atomic Notes → Triangulation → Structured Output
```

When helping process information:
1. Extract core concepts from raw content
2. Create atomic notes with clear titles
3. Link to existing related notes
4. Tag appropriately with Domain/Status/Type
5. Add to relevant directory index

## Important Governance Documents

- **Development Philosophy**: `4.Archives/Tools/claude.md范例.md` - Engineering standards for agent-driven work
- **Tag Management**: `Atlas/Index/仓库标签管理系统.md` - Tag taxonomy and compression rules
- **Task Management**: `Atlas/BASE/Whole Vault任务管理.md` - TODO tracking via tasks plugin
- **System Overview**: `Atlas/MOCs.md` - Master index of all MOC files

## Development Standards (from `claude.md范例.md`)

When working on code or automation within this vault:

1. **Reality over Ritual**: Use real data only, no mocking core logic
2. **Verification First**: Can it run → verify output → then test → then lint
3. **Failure Accounting**: Always count total tests, failures, and specific reasons
4. **Agent as Executor**: Follow user/system instructions precisely, don't freelance
5. **Continuity**: All work must be handoff-able to another agent/human
6. **Constraint to Reduce Implicit Complexity**: Avoid hidden async/try-except-import patterns

## Common Tasks

### Viewing all incomplete tasks:
The vault uses the tasks plugin. See all TODOs in `Atlas/Index/Whole Vault任务管理.md` or use:
```
```tasks
not done
sort by priority
sort by due
limit 50
```
```

### Finding related content:
- Use **bi-directional links** in note headers
- Check **Dataview queries** in `Atlas/Index/`
- Search by **Domain tags** to find topical content
- Use **smart-connections** plugin for AI-similar notes

### Updating index files:
- Most indexes are auto-generated by Zoottelkeeper
- Manual index updates: follow the existing pattern in `Atlas/Index/_Index_of_Index.md`
- Include direct links with descriptive prefixes (📄 for notes, 🗂️ for indexes)

## Important Constraints

1. **Never delete content** - move to Archives instead
2. **Maintain link coherence** - update backlinks when renaming/moving
3. **Preserve YAML structure** - frontmatter is used by many plugins
4. **Chinese language** - This is primarily a Chinese-language vault, respect existing naming conventions
5. **Obsidian-specific syntax** - Preserve `[[wiki-links]]`, `![[embeds]]`, and `%% comments %%`
