---
name: call-feature
description: Master multi-agent feature delivery orchestrator. Automates end-to-end feature development across research, architecture design, backend & AI pipelines, high-end frontend UI, and test/doc verification using parallel subagents. Use when implementing any complete feature from scratch.
---

# 🚀 Master Composite Skill: Multi-Agent Feature Delivery (`/call-feature`)

This master skill orchestrates complete, production-ready feature implementation by executing a structured multi-agent lifecycle across architecture, backend, frontend, testing, and documentation.

---

## 📦 Bundled Calling Skills & Direct References

When orchestrating subagents or executing specific phases, read the corresponding composite skills:

| Phase | Skill Command | Path | Scope & Responsibilities |
| :--- | :--- | :--- | :--- |
| **0. Research** | **`/call-research`** | `.agents/skills/call-research/SKILL.md` | Tech stack vetting, benchmarks, API/lib documentation |
| **1. Architecture** | **`/call-arch`** | `.agents/skills/call-arch/SKILL.md` | Domain models, Hexagonal layers, DB schemas, API specs |
| **2. Core & Backend** | **`/call-backend`** | `.agents/skills/call-backend/SKILL.md` | Async APIs, DB queries, migrations, business logic |
| **3. AI & Data** | **`/call-ai-ml`** | `.agents/skills/call-ai-ml/SKILL.md` | RAG pipelines, vector indexes, LLM agent workflows |
| **4. High-End UI** | **`/call-front`** | `.agents/skills/call-front/SKILL.md` | Anti-slop UI, Next.js 15/React 19, motion & design tokens |
| **5. Testing & Docs** | **`/call-debug`** / **`/call-doc`** | `.agents/skills/call-debug/SKILL.md`<br/>`.agents/skills/call-doc/SKILL.md` | Test suites, edge-case checks, OpenAPI & docstrings |

---

## 🤖 Multi-Agent Orchestration Playbook

When `/call-feature <feature_description>` is triggered, execute the following 5-phase pipeline:

```
[ User Feature Request ]
           │
           ▼
[ Phase 1: Architecture & API Specs ] ──► (Subagent 1: /call-arch)
           │
           ▼
[ Phase 2: Backend & AI Pipelines ]   ──► (Subagent 2: /call-backend + /call-ai-ml)
           │
           ▼
[ Phase 3: Frontend UI & Motion ]     ──► (Subagent 3: /call-front)
           │
           ▼
[ Phase 4: QA & Documentation ]       ──► (Subagent 4: /call-debug + /call-doc)
           │
           ▼
[ Final Verification & Walkthrough ]
```

### Phase 1: Architecture & Data Contracts (`/call-arch`)
1. Analyze the feature requirements and identify domain invariants.
2. Define data transfer objects (DTOs), database schemas/models, and API contract specifications (`OpenAPI`/types).
3. Ensure strict Hexagonal / Clean Architecture boundaries (Domain does not import transport or ORM layers).

### Phase 2: Backend Implementation (`/call-backend` + `/call-ai-ml`)
1. Implement the repository adapters, service logic, and API endpoints.
2. If AI/ML is required: configure vector store embeddings, retrieval schemas, prompt templates, and streaming handlers.
3. Optimize queries to prevent N+1 issues and add database migrations.

### Phase 3: Frontend Interface & Aesthetics (`/call-front`)
1. Build interactive React 19 / Next.js 15 components consuming the Phase 1 API contracts.
2. Enforce anti-slop visual standards: rich typography, intentional color tokens, subtle depth, responsive layout.
3. Add fluid spring micro-interactions without layout shifts (`CLS = 0`).

### Phase 4: Quality, Testing & Documentation (`/call-debug` + `/call-doc`)
1. Write unit and integration tests covering positive paths and critical edge cases.
2. Validate against runtime bugs or error states.
3. Add top-level file header docstrings and complete API documentation.

### Phase 5: Synthesis & Walkthrough
1. Run local test validation.
2. Present a clear summary of implemented components, API endpoints, and verification steps.

---

## ⚡ Execution Directives

- **Clean Contracts First**: Never write frontend UI before API schemas and domain models are specified.
- **Context Isolation**: When spawning subagents for independent tasks, pass only relevant specs to maintain token efficiency and clean context.
- **Zero Regression**: Preserve existing workspace functionality and adhere strictly to project conventions.
