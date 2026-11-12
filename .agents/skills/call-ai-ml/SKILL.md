---
name: call-ai-ml
description: Composite bundler skill activating all AI/ML engineering skills at once. Use when building ML models, RAG vector systems, LLM workflows, async data pipelines, or AI-powered FastAPI services.
---

# 🚀 Composite Skill: Full-Stack AI/ML, RAG & Data Pipelines (`/call-ai-ml`)

This composite skill unifies machine learning engineering, LLM application architecture, vector databases, and high-performance async Python backend systems.

---

## 📦 Bundled Skills & Deep References

When detailed implementation schemas, framework configurations, or specific sub-workflows are required, read the corresponding skill by reading its `SKILL.md` file:

| Skill | Path | Focus & On-Demand Capabilities |
| :--- | :--- | :--- |
| **`/ai-engineer`** | `.agents/skills/ai-engineer/SKILL.md` | Production LLM apps, advanced RAG, agent orchestration |
| **`/ml-engineer`** | `.agents/skills/ml-engineer/SKILL.md` | PyTorch/TensorFlow, model serving, inference optimization |
| **`/ml-pipeline-workflow`** | `.agents/skills/ml-pipeline-workflow/SKILL.md` | End-to-end MLOps, automated training & deployment pipelines |
| **`/vector-database-engineer`** | `.agents/skills/vector-database-engineer/SKILL.md` | Qdrant, Pinecone, Milvus, pgvector indexing & query design |
| **`/embedding-strategies`** | `.agents/skills/embedding-strategies/SKILL.md` | Chunking strategies, model selection, reranking & embedding tuning |
| **`/langchain-architecture`** | `.agents/skills/langchain-architecture/SKILL.md` | LangGraph/LangChain agents, memory systems & tool binding |
| **`/llm-application-dev-prompt-optimize`** | `.agents/skills/llm-application-dev-prompt-optimize/SKILL.md` | Constitutional AI, CoT reasoning, few-shot prompt optimization |
| **`/composio`** | `.agents/skills/composio/SKILL.md` | 1000+ external tool integrations & agent tool calling |
| **`/fastapi-pro`** | `.agents/skills/fastapi-pro/SKILL.md` | High-throughput async FastAPI, Pydantic V2, WebSockets |
| **`/fastapi-templates`** | `.agents/skills/fastapi-templates/SKILL.md` | Clean architecture project scaffolding and dependency injection |
| **`/async-python-patterns`** | `.agents/skills/async-python-patterns/SKILL.md` | `asyncio` concurrency, connection pooling, non-blocking I/O |
| **`/python-pro`** | `.agents/skills/python-pro/SKILL.md` | Python 3.12+ typing, modern patterns, uv, ruff, performance |
| **`/python-performance-optimization`** | `.agents/skills/python-performance-optimization/SKILL.md` | Profiling (cProfile, memory), bottleneck resolution |
| **`/python-testing-patterns`** | `.agents/skills/python-testing-patterns/SKILL.md` | `pytest`, `pytest-asyncio`, fixtures, mocking & TDD |
| **`/architect-review`** | `.agents/skills/architect-review/SKILL.md` | Architectural integrity, domain boundaries & scalability review |
| **`/api-documenter`** | `.agents/skills/api-documenter/SKILL.md` | OpenAPI 3.1 specs, interactive documentation |
| **`/api-testing-observability-api-mock`** | `.agents/skills/api-testing-observability-api-mock/SKILL.md` | Mocking API services and realistic sandbox testing |
| **`/code-review`** | `.agents/skills/code-review/SKILL.md` | Dual-axis code review (Standards + Specification) |
| **`/architecture-patterns`** | `.agents/skills/architecture-patterns/SKILL.md` | Implement proven backend architecture patterns including Clean Architecture, Hexagonal… |
| **`/codebase-design`** | `.agents/skills/codebase-design/SKILL.md` | Shared vocabulary for designing deep modules. Use when the user wants to design or… |
| **`/improve-codebase-architecture`** | `.agents/skills/improve-codebase-architecture/SKILL.md` | Scan a codebase for deepening opportunities, present them as a visual HTML report, then… |
| **`/code-documentation-doc-generate`** | `.agents/skills/code-documentation-doc-generate/SKILL.md` | You are a documentation expert specializing in creating comprehensive, maintainable… |

---

## ⚡ Core Directives & Playbook (Fast Path)

When `/call-ai-ml` is invoked, strictly adhere to these engineering standards:

### 1. Vector Search & RAG Architecture
- **Chunking Strategy**: Use semantic/document-aware chunking with token overlap (e.g. 512 tokens with 64-token overlap).
- **Hybrid Retrieval**: Combine dense semantic embeddings (cosine similarity) with sparse keyword search (BM25) and apply cross-encoder reranking.
- **Metadata Filtering**: Always enforce tenant isolation and structured metadata indexing (e.g. user_id, document_type, timestamp).

### 2. Modern Python 3.12+ & Async API Standards
- **Pydantic V2 & Type Safety**: Use strict type hints and Pydantic V2 models for all request/response schemas and LLM structured outputs.
- **Non-blocking Async**:
  ```python
  # Always use async client sessions with explicit timeouts
  async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
      response = await client.post(...)
  ```
- **FastAPI Architecture**: Structure by feature/domain with dedicated routers, service layers, repositories, and dependency injection (`Depends()`).

### 3. LLM Pipeline & Prompt Guardrails
- **Structured Outputs**: Force LLM outputs into strict JSON schemas or Pydantic models.
- **Fail-Safe & Retries**: Wrap external model calls in exponential backoff retries with graceful fallbacks.
- **Observability**: Log token counts, latency, and prompt/response metadata for all model interactions.

### 4. Testing & Verification
- Unit test all transformations with `pytest`.
- Use `pytest-asyncio` for asynchronous endpoints and worker loops.
- Mock all external LLM and database calls in automated suites.

---

## ⚡ Execution Workflow

1. **Architecture & Scope**: Define data flow, model choice, embedding dimensions, and API contracts.
2. **Implementation**: Build type-safe async services, vectorized retrieval, or pipeline components.
3. **Validation**: Test with realistic payloads, verify memory/latency characteristics, and ensure full test coverage.
