---
name: call-arch
description: Composite bundler skill activating system architecture skills. Use when proposing major architectural changes, deep module refactoring, domain boundary modeling, and technical debt reviews.
---

# 🚀 Composite Skill: Architecture Design, Refactoring & System Review (`/call-arch`)

This composite skill drives clean system architecture, Domain-Driven Design (DDD), deep module boundaries, and high-impact structural refactoring.

---

## 📦 Bundled Skills & Deep References

When detailed architectural specs, deep design principles, or specific review workflows are required, read the corresponding skill by reading its `SKILL.md` file:

| Skill | Path | Focus & On-Demand Capabilities |
| :--- | :--- | :--- |
| **`/architect-review`** | `.agents/skills/architect-review/SKILL.md` | Clean architecture review, microservices, event systems |
| **`/architecture-patterns`** | `.agents/skills/architecture-patterns/SKILL.md` | Clean Architecture, Hexagonal (Ports & Adapters), DDD |
| **`/codebase-design`** | `.agents/skills/codebase-design/SKILL.md` | Deep module interfaces, cognitive load reduction |
| **`/improve-codebase-architecture`**| `.agents/skills/improve-codebase-architecture/SKILL.md`| Codebase modernization, layer decoupling & seam identification |
| **`/database-architect`** | `.agents/skills/database-architect/SKILL.md` | Data layer architecture, storage engine selection, normalization |
| **`/domain-modeling`** | `.agents/skills/domain-modeling/SKILL.md` | Ubiquitous language, bounded contexts & aggregate roots |
| **`/design-an-interface`** | `.agents/skills/design-an-interface/SKILL.md` | Multi-option API exploration ("design it twice") |
| **`/grill-with-docs`** | `.agents/skills/grill-with-docs/SKILL.md` | Stress-testing architectural plans against constraints |
| **`/code-refactoring-refactor-clean`**| `.agents/skills/code-refactoring-refactor-clean/SKILL.md`| SOLID principles, dead code pruning, clean code practices |
| **`/codebase-cleanup-refactor-clean`**| `.agents/skills/codebase-cleanup-refactor-clean/SKILL.md`| Structural refactoring, DRY consolidation, complexity reduction |
| **`/code-review`** | `.agents/skills/code-review/SKILL.md` | Standards vs Specification dual-axis review |
| **`/code-documentation-doc-generate`**| `.agents/skills/code-documentation-doc-generate/SKILL.md`| System overview docs, architecture flowcharts, component diagrams |
| **`/langchain-architecture`** | `.agents/skills/langchain-architecture/SKILL.md` | Design LLM applications using the LangChain framework with agents, memory, and tool… |
| **`/fastapi-templates`** | `.agents/skills/fastapi-templates/SKILL.md` | Create production-ready FastAPI projects with async patterns, dependency injection, and… |

---

## ⚡ Core Directives & Playbook (Fast Path)

When `/call-arch` is invoked, strictly enforce the following architectural rules:

### 1. Hexagonal & Clean Layering
Organize system boundaries into distinct, decoupled tiers:
```
  [ Entry Points / Controllers / CLI ]
                   │
                   ▼
  [ Application Services / Use Cases ]
                   │
                   ▼
       [ Core Domain Entities ]
                   ▲
                   │
  [ Adapters / Repositories / External APIs ]
```
- **Dependency Rule**: Dependencies always point inward toward the Domain. The core domain never imports database drivers, framework-specific code, or transport layers.

### 2. Deep Modules vs Shallow Wrappers
- **Maximize Depth**: Modules should have small, intuitive interfaces that hide substantial internal complexity.
- **Eliminate Pass-Throughs**: Avoid shallow classes or functions that merely forward calls to another layer without adding domain logic.
- **Information Hiding**: Keep internal data structures private. Expose only intention-revealing operations.

### 3. Interface Design & Ergonomics
- **Explore Alternatives**: For critical interfaces, compare two radically different API styles (e.g. fluent builder vs config object) before committing.
- **Explicit Invariants**: Validate inputs at boundary boundaries and enforce domain invariants in entity constructors.

### 4. Zero-Regression Refactoring
- Refactor in incremental steps (seams, parallel implementation, switchover, cleanup).
- Never mix structural refactoring with functional behavior changes in the same step.
- Preserve existing public API contracts and verified behavior.

---

## ⚡ Execution Workflow

1. **Domain & Boundary Analysis**: Map domain entities, identify bounded contexts, and locate coupling hotspots.
2. **Architectural Proposal**: Define target architecture, component interfaces, and migration steps.
3. **Execution & Refactor**: Implement clean boundaries, inject dependencies via interfaces, and verify zero functional regressions.
