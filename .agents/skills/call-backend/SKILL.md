---
name: call-backend
description: Composite bundler skill activating all backend development skills. Use for API development, async performance, database architecture, query optimization, clean code, and backend refactoring.
---

# 🚀 Composite Skill: Backend Engineering, APIs, Refactoring & DB (`/call-backend`)

This composite skill governs production backend development across FastAPI, Node.js, async systems, REST/GraphQL design, database optimization, and high-reliability APIs.

---

## 📦 Bundled Skills & Deep References

When detailed implementation schemas, framework configurations, or specific sub-workflows are required, read the corresponding skill using `view_file`:

| Skill | Path | Focus & On-Demand Capabilities |
| :--- | :--- | :--- |
| **`/fastapi-pro`** | `.agents/skills/fastapi-pro/SKILL.md` | Async FastAPI, SQLAlchemy 2.0 async sessions, Pydantic V2 |
| **`/fastapi-templates`** | `.agents/skills/fastapi-templates/SKILL.md` | Scaffolding, dependency injection hierarchies, routing setup |
| **`/nodejs-backend-patterns`** | `.agents/skills/nodejs-backend-patterns/SKILL.md` | Express/Fastify architectures, middleware pipelines, error handlers |
| **`/api-design-principles`** | `.agents/skills/api-design-principles/SKILL.md` | RESTful resource design, idempotency keys, pagination standards |
| **`/api-documenter`** | `.agents/skills/api-documenter/SKILL.md` | OpenAPI 3.1, JSON Schema, developer portals |
| **`/api-testing-observability-api-mock`** | `.agents/skills/api-testing-observability-api-mock/SKILL.md` | Realistic API mocking, contract testing, observability hooks |
| **`/async-python-patterns`** | `.agents/skills/async-python-patterns/SKILL.md` | `asyncio` task management, queues, async context managers |
| **`/python-performance-optimization`** | `.agents/skills/python-performance-optimization/SKILL.md` | Query profiling, memory optimization, worker scaling |
| **`/python-pro`** | `.agents/skills/python-pro/SKILL.md` | Python 3.12+ features, strict typing, modern tooling |
| **`/python-testing-patterns`** | `.agents/skills/python-testing-patterns/SKILL.md` | `pytest`, integration test suites, database fixtures |
| **`/database-architect`** | `.agents/skills/database-architect/SKILL.md` | Relational & NoSQL schema design, normalization, sharding |
| **`/database-optimizer`** | `.agents/skills/database-optimizer/SKILL.md` | Indexing strategies, execution plan tuning, cache tiers (Redis) |
| **`/sql-optimization-patterns`** | `.agents/skills/sql-optimization-patterns/SKILL.md` | EXPLAIN ANALYZE, N+1 query elimination, CTE optimization |
| **`/database-migration`** | `.agents/skills/database-migration/SKILL.md` | Zero-downtime expand/contract migrations (Alembic, Prisma) |
| **`/code-refactoring-refactor-clean`** | `.agents/skills/code-refactoring-refactor-clean/SKILL.md` | Clean code, SOLID design, technical debt remediation |
| **`/codebase-design`** | `.agents/skills/codebase-design/SKILL.md` | Deep modules, loose coupling, interface clarity |

---

## ⚡ Core Directives & Playbook (Fast Path)

When `/call-backend` is invoked, strictly adhere to these backend engineering standards:

### 1. API Design & Status Code Standards
- **RESTful Resource URLs**: Plural nouns for collections (`/api/v1/users`, `/api/v1/orders/{id}/items`).
- **Standard Status Codes**:
  - `200 OK` (Standard success), `201 Created` (Resource created with `Location` header)
  - `400 Bad Request` (Validation error), `401 Unauthorized` (Unauthenticated), `403 Forbidden` (Permission denied)
  - `404 Not Found` (Missing resource), `409 Conflict` (State/duplicate conflict), `422 Unprocessable Entity`
- **Standardized Error Envelope**:
  ```json
  {
    "error": {
      "code": "RESOURCE_NOT_FOUND",
      "message": "User with id 123 does not exist",
      "details": []
    }
  }
  ```

### 2. Async I/O & Connection Management
- **Never Block the Event Loop**: Avoid synchronous I/O (`time.sleep`, standard `requests`, sync file reads) in async code.
- **Connection Pools**: Always use shared connection pools for databases, Redis, and HTTP clients with explicit acquire timeouts and keep-alive limits.

### 3. Database Performance & Zero-Downtime Migrations
- **Prevent N+1 Queries**: Always use `joinedload`, `selectinload`, or batch lookups when loading relationships.
- **Expand-and-Contract Migrations**:
  1. *Expand*: Add new column/table as nullable or with defaults. Deploy code writing to both.
  2. *Backfill*: Migrate existing records in background batches.
  3. *Contract*: Point reads to new schema, remove legacy column in subsequent release.

### 4. Testing & Verification
- Unit test business logic with isolated mocks.
- Integration test API endpoints using real/test database containers.
- Verify that all database queries hit appropriate indexes using `EXPLAIN ANALYZE`.

---

## ⚡ Execution Workflow

1. **Schema & Contract Definition**: Define Pydantic/TypeScript models, API routes, and DB models.
2. **Implementation**: Implement controller, service, and repository layers with strict async standards.
3. **Validation & Benchmarking**: Run unit/integration tests, verify error envelopes, and check query performance.
