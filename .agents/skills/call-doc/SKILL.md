---
name: call-doc
description: Composite bundler skill activating all documentation, API specification, code annotation, and architectural review skills. Use when reading project files to insert top-level file header docstrings, inline code documentation, API reference guides, and technical architecture specs.
---

# 🚀 Composite Skill: Comprehensive Documentation, API Spec & Code Annotation (`/call-doc`)

This composite skill drives comprehensive codebase documentation, strict module docstrings, OpenAPI/GraphQL specifications, and architectural documentation.

---

## 📦 Bundled Skills & Deep References

When detailed API schemas, documentation generators, or specific review workflows are required, read the corresponding skill using `view_file`:

| Skill | Path | Focus & On-Demand Capabilities |
| :--- | :--- | :--- |
| **`/code-documentation-doc-generate`** | `.agents/skills/code-documentation-doc-generate/SKILL.md` | Automated API docs, system overview diagrams, user guides |
| **`/api-documenter`** | `.agents/skills/api-documenter/SKILL.md` | OpenAPI 3.1 specifications, interactive developer docs |
| **`/api-design-principles`** | `.agents/skills/api-design-principles/SKILL.md` | REST/GraphQL design principles, contract guidelines |
| **`/grill-with-docs`** | `.agents/skills/grill-with-docs/SKILL.md` | Stress-testing documentation against real architectural constraints |
| **`/architect-review`** | `.agents/skills/architect-review/SKILL.md` | Architecture validation, clean interface review |
| **`/code-review`** | `.agents/skills/code-review/SKILL.md` | Standards vs spec code review & doc completeness check |
| **`/codebase-design`** | `.agents/skills/codebase-design/SKILL.md` | Deep module interfaces, cognitive clarity |
| **`/domain-modeling`** | `.agents/skills/domain-modeling/SKILL.md` | Ubiquitous language, domain definitions & invariants |
| **`/defuddle`** | `.agents/skills/defuddle/SKILL.md` | Clean markdown extraction from web docs |
| **`/data-storytelling`** | `.agents/skills/data-storytelling/SKILL.md` | Clear technical narratives, tables, and visual explanations |
| **`/obsidian-markdown`** | `.agents/skills/obsidian-markdown/SKILL.md` | Obsidian-flavored markdown, wikilinks, callouts, frontmatter |
| **`/code-refactoring-refactor-clean`** | `.agents/skills/code-refactoring-refactor-clean/SKILL.md` | Clean code standards, readability enhancements |

---

## ⚡ Core System Prompt & File Annotation Directives

> **"Read project files. At the beginning of each file write a docstring explaining this file and then document the code."**

When executing code documentation across project files, strictly enforce the following rules:

### 1. Mandatory File Header Docstrings
At the very top of every project file (immediately following any language-required shebang `#!/usr/bin/env ...` or pragmas such as `"use strict";`), insert a comprehensive file-level header docstring that details:

1. **File & Module Purpose**: Clear summary of the file's primary responsibility and scope.
2. **Architecture & System Context**: How this file fits into the broader application architecture (e.g., API route, controller, service layer, data access, component, utility).
3. **Public Interface & Exports**: Enumeration of main exported functions, classes, interfaces, types, and constants.
4. **Dependencies & Side Effects**: Key external libraries, database interactions, network requests, file I/O, or state mutations.
5. **Usage & Maintenance Invariants**: Thread-safety notes, performance bounds, security implications, and guidelines for future maintainers.

### 2. In-Code & Symbol Level Documentation
Annotate all structural elements within each file:
- **Classes / Structs / Interfaces**: Purpose, responsibilities, domain alignment, invariants, and generic type parameters.
- **Functions & Methods**:
  - `@param` / `:param`: Purpose, expected data types, constraints, and default/nullability behavior for every parameter.
  - `@returns` / `:return`: Description of return values, output data structures, and edge-case returns.
  - `@throws` / `:raises`: Complete list of raised exceptions, custom error types, or status codes.
- **Fields, Properties & Constants**: Explanation of constant values, configuration keys, and internal state fields.
- **Complex Logic & Algorithms**: Inline explanatory comments for complex branching, mathematical formulas, state machine transitions, and performance-critical loops.

### 3. Language-Specific Docstring Standards

| Language | Header Docstring Style | Symbol / Function Docstring Style | Primary Convention |
| :--- | :--- | :--- | :--- |
| **Python** | Top-of-file `"""..."""` | `"""..."""` inside block | PEP 257 / Google Docstrings |
| **TypeScript / JavaScript** | Top-of-file `/** ... */` | `/** ... */` above symbol | JSDoc / TSDoc |
| **Rust** | Top-of-file `//! ...` | `/// ...` above symbol | Rustdoc |
| **Go** | Top-of-file `// Package ...` | `// Function ...` comment | Godoc |
| **C / C++ / Java** | Top-of-file `/** ... */` | `/** ... */` above symbol | Javadoc / Doxygen |
| **Markdown / Technical Docs** | Frontmatter YAML / Header | Section explanations | GitHub Flavored Markdown |

---

## ⚡ Execution Workflow

When `/call-doc` is invoked:

1. **Integrated Analysis**:
   - Scan workspace project files to understand codebase structure and domain models.
   - Evaluate public interfaces, API contracts, and structural relationships.
2. **File Header & In-Code Annotation**:
   - Read each source file.
   - Add/update top-level file header docstrings outlining file purpose, system role, exports, and invariants.
   - Document functions, methods, classes, types, and complex internal code logic.
3. **API & Technical Documentation Synthesis**:
   - Generate OpenAPI/GraphQL specifications using `/api-documenter`.
   - Create automated technical docs, architecture diagrams, and user guides using `/code-documentation-doc-generate`.
   - Validate doc consistency against requirements and architecture.
4. **Quality & Integrity Verification**:
   - Ensure 100% functional equivalence and zero code regression.
   - Run syntax validators, type checkers, and test suites to verify docstrings and code integrity.
