# 🤖 Agent Skills Catalog

This file documents all available AI agent **skills** for the project workspace and developer environment.

A **skill** is a set of precise instructions loaded into the AI agent's context when a relevant task is triggered. Instead of the agent improvising, the skill tells it *exactly* how to perform a specialized task — with known patterns, best practices, and guardrails. This keeps outputs consistent and production-quality without you having to re-explain context every time.

---

## 🌐 Skill Repositories & Installation Commands

Our workspace skills are sourced and installed using the `npx skills` CLI.

> [!IMPORTANT]
> **Installation Rule**: Always execute `npx skills` commands from your **workspace root**, NOT inside `.agents/skills`.

### 1. 📦 Matt Pocock Skills (`mattpocock/skills`)
* **GitHub Repository**: [https://github.com/mattpocock/skills](https://github.com/mattpocock/skills)
* **Installation Command (All Skills)**:
  ```bash
  npx skills add mattpocock/skills
  ```

### 2. 📦 Vercel Labs Skills (`vercel-labs/skills`)
* **GitHub Repository**: [https://github.com/vercel-labs/skills](https://github.com/vercel-labs/skills)
* **Installation Command (All Skills)**:
  ```bash
  npx skills add vercel-labs/skills
  ```

### 3. 📦 Antigravity Skills (`rmyndharis/antigravity-skills`)
* **GitHub Repository**: [https://github.com/rmyndharis/antigravity-skills](https://github.com/rmyndharis/antigravity-skills)
* **Installation Command (All Skills)**:
  ```bash
  npx skills add rmyndharis/antigravity-skills
  ```

### 4. 📦 Deep Research Skills (`Weizhena/Deep-Research-skills`)
* **GitHub Repository**: [https://github.com/Weizhena/Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills)
* **Installation Command (All Skills)**:
  ```bash
  npx skills add Weizhena/Deep-Research-skills
  ```

---

## 🔍 How Skills Are Triggered

Skills are matched automatically by name/description when you ask the agent to do something relevant. You can also mention the skill name directly (e.g. *"use the `diagnosing-bugs` skill"* or *"use `cloudflare`"*).

---

## 📂 Complete Skills Reference (92 Available Skills)

### 🧠 AI & Machine Learning
| Skill | Description / Usage |
| :--- | :--- |
| `ai-engineer` | Build LLM applications, RAG systems, vector search, and agent orchestration. |
| `ml-engineer` | Production ML model serving, feature engineering, and inference optimization. |
| `ml-pipeline-workflow` | End-to-end MLOps pipelines from data prep to production deployment. |
| `embedding-strategies` | Embeddings model selection, chunking, and semantic search tuning. |
| `langchain-architecture` | Agentic workflows, tool integration, and memory patterns. |
| `llm-application-dev-prompt-optimize` | Advanced prompt engineering (CoT, Constitutional AI). |
| `vector-database-engineer` | Pinecone, Weaviate, Qdrant, Milvus, and pgvector implementations. |
| `quant-analyst` | Financial modeling, backtesting, and statistical arbitrage. |
| `data-scientist` | Advanced analytics, ML modeling, and statistical insights. |
| `composio` | 1000+ external app integrations via CLI or SDK for AI agents. |

---

### ☁️ Cloudflare Ecosystem & Serverless Edge
| Skill | Description / Usage |
| :--- | :--- |
| `agents-sdk` | Stateful AI agents on Cloudflare Workers, Durable Objects, and WebSockets. |
| `cloudflare` | Comprehensive Cloudflare platform (Workers, Pages, KV, D1, R2, Vectorize). |
| `cloudflare-email-service` | Transactional email sending and routing integration. |
| `cloudflare-one` | Cloudflare One Zero Trust, Access, Gateway, WARP, and SASE security. |
| `cloudflare-one-migrations` | Migration planning from legacy VPN/SASE to Cloudflare One. |
| `durable-objects` | Cloudflare Durable Objects for stateful coordination, RPC, and SQLite storage. |
| `sandbox-sdk` | Sandboxed applications for secure code execution and live previews. |
| `turnstile-spin` | End-to-end Cloudflare Turnstile bot verification and CAPTCHA setup. |
| `workers-best-practices` | Cloudflare Workers production code reviews and architectural patterns. |
| `wrangler` | Cloudflare Workers CLI for deploying and managing Workers, KV, R2, D1, Queues. |

---

### 🐍 Python & Backend Engineering
| Skill | Description / Usage |
| :--- | :--- |
| `python-pro` | Modern Python 3.12+ features, async/await, and production standards. |
| `python-performance-optimization` | Profiling (`cProfile`, memory profilers) and bottleneck removal. |
| `python-testing-patterns` | `pytest`, fixtures, mocking, and TDD strategies. |
| `async-python-patterns` | High-concurrency `asyncio` and non-blocking I/O routines. |
| `fastapi-pro` | High-performance async APIs with FastAPI, SQLAlchemy 2.0, Pydantic V2. |
| `fastapi-templates` | Production-ready FastAPI project scaffolding. |
| `nodejs-backend-patterns` | Express/Fastify services, middleware, and microservices. |
| `bash-pro` | Defensive shell scripting, CI/CD automation, and process management. |
| `php-pro` | Writing idiomatic PHP code with modern OOP features. |
| `scala-pro` | Master enterprise Scala functional programming and distributed systems. |

---

### 🗄️ Data & Database Engineering
| Skill | Description / Usage |
| :--- | :--- |
| `data-engineer` | Build scalable data pipelines (Spark, dbt, Airflow, cloud platforms). |
| `data-engineering-data-pipeline` | Architecture for scalable batch and streaming pipelines. |
| `data-engineering-data-driven-feature` | Feature engineering guided by data insights and A/B testing. |
| `data-quality-frameworks` | Data validation with Great Expectations and dbt tests. |
| `data-storytelling` | Transform data into compelling narratives and stakeholder visuals. |
| `database-architect` | Greenfield schema design, SQL/NoSQL selection, and data modeling. |
| `database-admin` | Cloud database operations, high availability, and disaster recovery. |
| `database-optimizer` | Advanced indexing, EXPLAIN analysis, and query performance tuning. |
| `sql-optimization-patterns` | Master SQL query optimization and EXPLAIN analysis. |
| `database-migration` | Zero-downtime database schema migrations and rollback procedures. |
| `database-migrations-sql-migrations` | SQL database migrations for PostgreSQL, MySQL, SQL Server. |
| `database-migrations-migration-observability` | Migration monitoring, CDC, and observability infrastructure. |
| `database-cloud-optimization-cost-optimize` | Cloud cost reduction strategies for cloud databases. |
| `postgresql` | PostgreSQL schema design, jsonb strategies, and performance patterns. |
| `sql-pro` | Master modern SQL with cloud-native OLTP/OLAP databases. |
| `dbt-transformation-patterns` | dbt analytics engineering, models, tests, and documentation. |
| `spark-optimization` | Apache Spark memory tuning, partitioning, and shuffle minimization. |

---

### 🏗️ Architecture & Code Quality
| Skill | Description / Usage |
| :--- | :--- |
| `architect-review` | Review code changes for architectural integrity and scalability. |
| `architecture-patterns` | Clean Architecture, Hexagonal Architecture, and Domain-Driven Design (DDD). |
| `codebase-design` | Shared vocabulary for deep module design and interface separation. |
| `code-review` | Structured code review against repo standards and spec requirements. |
| `code-refactoring-refactor-clean` | Refactor code to SOLID principles and clean code patterns. |
| `codebase-cleanup-refactor-clean` | Full codebase refactoring, technical debt reduction, and cleanup. |
| `improve-codebase-architecture` | Deepening opportunities visual HTML analysis and architectural refactoring. |
| `domain-modeling` | Build and maintain a project domain model and ubiquitous language. |
| `design-an-interface` | Generate multiple interface designs using parallel sub-agents. |

---

### 🌐 Web, Frontend & Performance
| Skill | Description / Usage |
| :--- | :--- |
| `frontend-developer` | React 19, Next.js 15, state management, and responsive layouts. |
| `nextjs-app-router-patterns` | Next.js 14+ App Router, Server Components, streaming, and parallel routes. |
| `web-perf` | Core Web Vitals analysis (LCP, INP, CLS) and Chrome DevTools MCP optimization. |
| `api-design-principles` | REST and GraphQL API design best practices. |
| `api-documenter` | OpenAPI 3.1 specifications, interactive docs, and SDK generation. |
| `api-testing-observability-api-mock` | Mock services for API development, testing, and demos. |

---

### 🔬 Debugging, Observability & Workflow
| Skill | Description / Usage |
| :--- | :--- |
| `diagnosing-bugs` | Systematic diagnosis loop for hard bugs and performance regressions. |
| `sentry-fix-issues` | Automated Sentry issue investigation and bug fixing via MCP. |
| `research` | Preliminary research framework generator (`outline.yaml`, `fields.yaml`) & `validate_json.py`. |
| `research-add-fields` | Add/supplement field definitions into research `fields.yaml`. |
| `research-add-items` | Add/supplement research objects/items into research `outline.yaml`. |
| `research-deep` | Parallel batch deep research execution per item with validation. |
| `research-report` | Synthesize deep research JSON results into markdown reports. |
| `grilling` | Stress-test architecture plans and ideas with challenging questions. |
| `grill-me` | Interactive interview to resolve design decisions. |
| `grill-with-docs` | Grill ideas grounded in specific documentation (creates ADRs & glossary). |
| `defuddle` | Extract clean Markdown content from web pages (removes nav/ads). |
| `handoff` | Structured context handoff notes for resuming complex multi-step tasks. |
| `teach` | Teach concepts clearly with code examples within the workspace. |
| `skill-creator` | Guide for creating and maintaining effective AI agent skills. |

---

### 📓 Obsidian & Knowledge Management
| Skill | Description / Usage |
| :--- | :--- |
| `obsidian-markdown` | Obsidian-flavored markdown syntax (wikilinks, callouts, embeds). |
| `obsidian-bases` | Create Obsidian Bases (`.base` files) for database-like note views. |
| `obsidian-cli` | Query, search, and manage Obsidian vaults from terminal. |
| `obsidian-workspace-sync` | Sync `.code-workspace` settings with Obsidian vault profiles. |
| `json-canvas` | Create and edit `.canvas` files for visual flowcharts in Obsidian. |

---

### 🛠️ Specialized Engineering & Compliance
| Skill | Description / Usage |
| :--- | :--- |
| `airflow-dag-patterns` | Build production Apache Airflow DAGs with best practices. |
| `code-documentation-doc-generate` | Generate comprehensive API docs and architecture diagrams from code. |
| `content-marketer` | AI-powered content strategy, SEO, and omnichannel marketing. |
| `legal-advisor` | Privacy policies, ToS, disclaimers, and GDPR compliance texts. |
| `gdpr-data-handling` | GDPR-compliant data handling, consent management, and privacy. |
| `pci-compliance` | PCI DSS compliance requirements for payment systems. |
| `business-analyst` | KPI frameworks, dashboards, and strategic business intelligence. |
| `kpi-dashboard-design` | Metrics selection, visualization, and real-time monitoring. |
| `hybrid-cloud-networking` | VPN and secure hybrid connectivity between cloud and on-prem. |
| `ios-developer` | Develop native iOS applications with Swift, SwiftUI, and iOS 18. |
| `unity-ecs-patterns` | Unity ECS and DOTS for high-performance game development. |

---

> [!TIP]
> Mentioning any skill name explicitly in your prompt (e.g. *"use `diagnosing-bugs`"* or *"run `cloudflare`"*) immediately loads the skill instructions into the agent context.
