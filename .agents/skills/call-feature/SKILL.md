---
name: call-feature
description: Master multi-agent feature delivery orchestrator. Automates end-to-end feature development across research, architecture design, backend & AI pipelines, high-end frontend UI, and test/doc verification using parallel subagents. Use when implementing any complete feature from scratch.
---

# 🚀 Master Composite Skill: Multi-Agent Feature Delivery (`/call-feature`)

This master skill orchestrates complete, production-ready feature implementation by executing a structured multi-agent lifecycle across research, architecture, core engineering build, frontend UI/UX, and test verification.

---

## 📦 Bundled Calling Skills & Direct References

When orchestrating subagents or executing specific phases, read the corresponding composite skills:

| Phase | Skill Command | Path | Key Skills & Capabilities |
| :--- | :--- | :--- | :--- |
| **0. Research & Trends** | **`/call-research`** | `.agents/skills/call-research/SKILL.md` | `last30days`, `graphify`, `defuddle`, `research-deep`, `agent-browser` |
| **1. Architecture & Specs** | **`/call-arch`** | `.agents/skills/call-arch/SKILL.md` | `architect-review`, `domain-modeling`, `database-architect`, `design-an-interface` |
| **2. Core Engineering & Build** | **`/call-build`** / **`/call-backend`** | `.agents/skills/call-build/SKILL.md`<br/>`.agents/skills/call-backend/SKILL.md` | `using-superpowers` (TDD), `ponytail` (YAGNI), `fastapi-pro`, `python-pro`, `nodejs` |
| **3. AI & Data Intelligence** | **`/call-ai-ml`** | `.agents/skills/call-ai-ml/SKILL.md` | `ai-engineer`, `vector-database-engineer`, `embedding-strategies`, `langchain` |
| **4. High-End UI & Motion** | **`/call-front`** | `.agents/skills/call-front/SKILL.md` | `ui-ux-pro-max`, `impeccable`, `design-taste-frontend`, `hyperframes`, `animate` |
| **5. QA, Tests & Docs** | **`/call-debug`** / **`/call-doc`** | `.agents/skills/call-debug/SKILL.md`<br/>`.agents/skills/call-doc/SKILL.md` | `diagnosing-bugs`, `python-testing-patterns`, `api-documenter`, `i-have-adhd` |

### Direct Skills (used alongside the composites)

| Skill | Path | Focus |
| :--- | :--- | :--- |
| **`/ponytail`** | `.agents/skills/ponytail/SKILL.md` | Lazy/minimal solution ladder: YAGNI, stdlib first, no needless deps. Apply in Phase 2 before writing code |
| **`/ponytail-review`** | `.agents/skills/ponytail-review/SKILL.md` | Review the diff for over-engineering. Run in Phase 4 |
| **`/ponytail-audit`** | `.agents/skills/ponytail-audit/SKILL.md` | Whole-repo bloat audit. Run before final delivery on large features |
| **`/using-superpowers`** | `.agents/skills/using-superpowers/SKILL.md` | TDD discipline, planning and verification |
| **`/i-have-adhd`** | `.agents/skills/i-have-adhd/SKILL.md` | Action-first final summary |

---

## 🤖 Multi-Agent Orchestration Playbook

When `/call-feature <feature_description>` is triggered, execute the following 5-phase pipeline:

```
[ User Feature Request ]
           │
           ▼
[ Phase 0: Research & Trend Discovery ] ──► (Subagent 0: /call-research)
           │
           ▼
[ Phase 1: Architecture & API Specs ]   ──► (Subagent 1: /call-arch)
           │
           ▼
[ Phase 2: Core Engineering & Build ]   ──► (Subagent 2: /call-build + /call-backend + /call-ai-ml)
           │
           ▼
[ Phase 3: Frontend UI & Motion ]       ──► (Subagent 3: /call-front)
           │
           ▼
[ Phase 4: QA & Documentation ]         ──► (Subagent 4: /call-debug + /call-doc)
           │
           ▼
[ Final Verification & Action-First Summary ]
```

### Phase 0: Research & Grounding (`/call-research`)
- If technical unknowns, external SDKs, or competitor benchmarks are involved, scan primary documentation and recent community practices via `last30days` and `defuddle`.
- Synthesize findings into key technical constraints before writing architecture.

### Phase 1: Architecture & Data Contracts (`/call-arch`)
- Map domain entities, aggregates, and domain invariants (DDD).
- Specify database schemas, migrations, and clean OpenAPI / TypeScript interface contracts.
- Enforce the Dependency Rule (Domain logic never imports transport or ORM layers).

### Phase 2: Core Engineering & Build (`/call-build` + `/call-backend` + `/call-ai-ml`)
- **Backend Architecture & APIs (`/call-backend`)**: Implement repository adapters, database schemas, async REST/GraphQL endpoints, and connection pooling.
- **Engineering Discipline & TDD (`/call-build`)**: Enforce strict Test-Driven Development (`test-driven-development`) by writing tests first, and apply `/ponytail` (decision ladder: YAGNI, stdlib first, no needless dependencies) before writing any code.
- **AI/ML Pipelines (`/call-ai-ml`)**: When applicable, configure vector store embeddings, retrieval schemas, prompt templates, and streaming handlers.

### Phase 3: Frontend UI & Motion (`/call-front`)
- Build React 19 / Next.js 15 components utilizing `ui-ux-pro-max` design intelligence and `impeccable` visual craft.
- Enforce anti-slop visual hierarchy: intentional typography, rich dark-mode tokens, subtle borders.
- Implement physics-based micro-interactions without causing layout shifts (`CLS = 0`).

### Phase 4: Quality, Testing & Documentation (`/call-debug` + `/call-doc`)
- Write comprehensive unit and integration test suites covering edge cases and error branches.
- Run `/ponytail-review` on the diff and remove over-engineering it flags.
- Generate top-level file docstrings and OpenAPI 3.1 specifications.

### Phase 5: Action-First Delivery & Verification
- Run test suites to verify passing status.
- Present a concise, ADHD-friendly, action-first summary (`i-have-adhd`) of files modified, endpoints created, and verification results.

---

## ⚡ Execution Directives

- **Clean Contracts First**: Never write frontend UI before API schemas and domain models are specified.
- **Context Isolation**: When spawning subagents for independent tasks, pass only relevant specs to maintain token efficiency.
- **Zero Regression**: Preserve existing workspace functionality and adhere strictly to project conventions.
