# 🤖 Agent Skills Catalog

This file documents all available AI agent **skills** for the **Crack-Distill** project workspace.

A **skill** is a set of precise instructions loaded into the AI agent's context when a relevant task is triggered. Instead of the agent improvising, the skill tells it *exactly* how to perform a specialized task — with known patterns, best practices, and guardrails. This keeps outputs consistent and production-quality without you having to re-explain context every time.

---

## 🌐 Skill Repositories & Installation Commands

Our workspace skills are sourced and installed from these 3 primary repositories using the `npx skills` CLI.

> [!IMPORTANT]
> **Installation Rule**: Always execute `npx skills` commands from your **workspace root** (e.g. `cd ~/distill`), NOT inside `.agents/skills`.

### 1. 📦 Matt Pocock Skills (`mattpocock/skills`)
* **GitHub Repository**: [https://github.com/mattpocock/skills](https://github.com/mattpocock/skills)
* **Skills Registry**: [https://skills.sh/mattpocock/skills](https://skills.sh/mattpocock/skills)
* **Installation Command (All Skills)**:
  ```bash
  npx skills add mattpocock/skills
  ```
* **Install Single Skill (e.g. `handoff`)**:
  ```bash
  npx skills add mattpocock/skills --skill=handoff
  ```

### 2. 📦 Vercel Labs Skills (`vercel-labs/skills`)
* **GitHub Repository**: [https://github.com/vercel-labs/skills](https://github.com/vercel-labs/skills)
* **Skills Registry**: [https://skills.sh/vercel-labs/skills](https://skills.sh/vercel-labs/skills)
* **Installation Command (All Skills)**:
  ```bash
  npx skills add vercel-labs/skills
  ```
* **Install Single Skill (e.g. `find-skills`)**:
  ```bash
  npx skills add vercel-labs/skills --skill=find-skills
  ```

### 3. 📦 Antigravity Skills (`rmyndharis/antigravity-skills`)
* **GitHub Repository**: [https://github.com/rmyndharis/antigravity-skills](https://github.com/rmyndharis/antigravity-skills)
* **Skills Registry**: [https://skills.sh/rmyndharis/antigravity-skills](https://skills.sh/rmyndharis/antigravity-skills)
* **Installation Command (All Skills)**:
  ```bash
  npx skills add rmyndharis/antigravity-skills
  ```
* **Install Single Skill (e.g. `code-documentation-doc-generate`)**:
  ```bash
  npx skills add rmyndharis/antigravity-skills --skill=code-documentation-doc-generate
  ```

---

## 🔍 How Skills Are Triggered

Skills are matched automatically by name/description when you ask the agent to do something relevant. You can also mention the skill name directly (e.g. *"use the `diagnosing-bugs` skill"*).

---

## 📂 Skills Reference

### 🧠 AI & Machine Learning
| Skill | Why We Use It |
| :--- | :--- |
| `ai-engineer` | Build LLM pipelines, RAG systems, and AI agents. Useful for any SAM 2 / embedding integration work. |
| `ml-engineer` | Production ML model serving, feature engineering, A/B testing. Used for KD pipeline optimization. |
| `ml-pipeline-workflow` | End-to-end MLOps — training, validation, and deployment automation. Handles our Kaggle → prod pipeline. |
| `embedding-strategies` | Select and tune embedding models for semantic search. Relevant if we add similarity-based crack retrieval. |
| `langchain-architecture` | Design LLM applications with agents, memory, and tools. Useful for any AI-powered tooling around the project. |
| `llm-application-dev-prompt-optimize` | Craft optimized prompts for LLMs (CoT, constitutional AI). Improves SAM 2 prompting strategies. |
| `quant-analyst` | Financial modeling and statistical analysis. Use for rigorous metric significance testing. |
| `data-scientist` | Advanced analytics, ML modeling, and statistical insights. Primary skill for experiment analysis. |

---

### 🐍 Python & Backend
| Skill | Why We Use It |
| :--- | :--- |
| `python-pro` | Modern Python 3.12+, async, performance, and best practices. Core language for our training scripts. |
| `python-performance-optimization` | Profile and optimize Python code. Use when training loops or data loaders are slow. |
| `python-testing-patterns` | pytest, fixtures, mocking, TDD. Ensures our trainer and loss functions are tested correctly. |
| `async-python-patterns` | asyncio and concurrent programming. Relevant for parallel teacher logit generation. |
| `fastapi-pro` | High-performance async APIs with FastAPI. Use if we expose model inference as a REST API. |
| `fastapi-templates` | Production-ready FastAPI project scaffolding. Kickstart any API layer around the model. |
| `bash-pro` | Defensive Bash scripting for automation and CI/CD. Handles Kaggle submission scripts and shell pipelines. |
| `php-pro` | PHP development patterns. Not directly used — low priority for this project. |
| `scala-pro` | Scala and distributed systems. Not directly used — low priority for this project. |

---

### 🗄️ Data & Databases
| Skill | Why We Use It |
| :--- | :--- |
| `data-engineer` | Build scalable data pipelines (Spark, dbt, Airflow). Use for dataset preprocessing pipelines. |
| `data-engineering-data-pipeline` | Architecture for batch/streaming pipelines. Guides design of teacher logit generation at scale. |
| `data-engineering-data-driven-feature` | Feature engineering guided by data insights and A/B testing. |
| `data-quality-frameworks` | Data validation with Great Expectations and dbt tests. Validate converted YOLO datasets. |
| `data-storytelling` | Transform data into compelling narratives. Use when preparing paper tables and visualizations. |
| `database-architect` | Schema modeling and database technology selection. |
| `database-admin` | Cloud database operations and reliability engineering. |
| `database-optimizer` | Query optimization, indexing, and performance tuning. |
| `database-migration` | Zero-downtime schema migrations and data transforms. |
| `database-migrations-sql-migrations` | SQL-specific migration patterns. |
| `database-migrations-migration-observability` | Migration monitoring and CDC. |
| `database-cloud-optimization-cost-optimize` | Cloud cost reduction strategies. |
| `sql-pro` | Advanced SQL with cloud-native databases. |
| `sql-optimization-patterns` | Query optimization and EXPLAIN analysis. |
| `postgresql` | PostgreSQL-specific schema design and performance. |
| `dbt-transformation-patterns` | dbt analytics engineering. |
| `spark-optimization` | Optimize Apache Spark jobs. Useful if we scale logit generation to a cluster. |

---

### 🏗️ Architecture & Code Quality
| Skill | Why We Use It |
| :--- | :--- |
| `architect-review` | Review code changes for architectural integrity and scalability. Use before merging major refactors. |
| `architecture-patterns` | Clean/Hexagonal Architecture and DDD. Guides the trainer/distillation module design. |
| `codebase-design` | Shared vocabulary for deep module design. Use when designing interfaces for the KD pipeline. |
| `code-review` | Structured code review against repo standards. Run this on PRs before merging. |
| `code-refactoring-refactor-clean` | Refactor code to SOLID principles and clean code. Use to clean up training scripts after experiments. |
| `codebase-cleanup-refactor-clean` | Full codebase refactoring and cleanup. |
| `improve-codebase-architecture` | Improve module architecture holistically. |
| `domain-modeling` | Build and maintain a project domain model and ubiquitous language. |
| `design-an-interface` | Generate multiple interface designs using parallel sub-agents. |

---

### 🌐 Web & APIs
| Skill | Why We Use It |
| :--- | :--- |
| `api-design-principles` | REST and GraphQL API design best practices. |
| `api-documenter` | OpenAPI 3.1 docs and developer portals. Use if we publish a model inference API. |
| `api-testing-observability-api-mock` | Mock services for API development and testing. |
| `frontend-developer` | React components and responsive layouts. Use for any dashboard or demo UI. |
| `nextjs-app-router-patterns` | Next.js 14+ App Router and Server Components. |
| `nodejs-backend-patterns` | Node.js backend services and REST APIs. |
| `hybrid-cloud-networking` | VPN and secure cloud connectivity. |

---

### 📝 Documentation & Content
| Skill | Why We Use It |
| :--- | :--- |
| `code-documentation-doc-generate` | Generate API docs and architecture diagrams from code. Use to document the KD pipeline for the paper. |
| `content-marketer` | Content strategy, SEO, and social media automation. |
| `legal-advisor` | Privacy policies, ToS, and GDPR compliance texts. |
| `gdpr-data-handling` | GDPR-compliant data handling and consent management. |
| `pci-compliance` | PCI DSS compliance for payment systems. |
| `business-analyst` | KPI frameworks, dashboards, and business intelligence. |
| `kpi-dashboard-design` | Metrics selection and data visualization layouts. Use for experiment dashboards. |
| `airflow-dag-patterns` | Apache Airflow DAGs for data pipelines and scheduling. |

---

### 🔬 Debugging & Research
| Skill | Why We Use It |
| :--- | :--- |
| `diagnosing-bugs` | **Core skill.** Structured diagnosis loop for hard bugs and performance regressions. Used to debug KD NaN crashes, DDP hook issues, and AMP overflow. |
| `research` | Investigate questions against high-trust primary sources and capture findings as Markdown. Use for literature review and API fact-gathering. |
| `grilling` | Relentlessly stress-test a plan or idea with challenging questions. Use before committing to an experiment design. |
| `grill-me` | Interactive interview to resolve design decisions. |
| `grill-with-docs` | Grill ideas grounded in specific documentation. |
| `handoff` | Structured handoff notes for pausing and resuming complex tasks. |
| `teach` | Explain concepts clearly with examples. Use to generate explanations for the paper's related work section. |

---

### 🔧 Platform-Specific
| Skill | Why We Use It |
| :--- | :--- |
| `obsidian-markdown` | Create and edit Obsidian Flavored Markdown (wikilinks, callouts, embeds). **Used heavily** for DistillVault notes. |
| `obsidian-bases` | Create Obsidian Bases (`.base` files) for database-like note views. Used for the Experimental Results table. |
| `obsidian-cli` | Query, search, and manage Obsidian vaults from terminal. |
| `obsidian-workspace-sync` | Sync `.code-workspace` settings with the Obsidian vault. |
| `json-canvas` | Create and edit `.canvas` files for visual workflows in Obsidian. |
| `defuddle` | Extract clean Markdown from web pages (removes nav/ads). **Use instead of WebFetch** for any documentation URL. |
| `ios-developer` | Native iOS development with Swift/SwiftUI. |
| `unity-ecs-patterns` | Unity ECS and DOTS for high-performance game development. |
| `vector-database-engineer` | Vector databases and semantic search (Pinecone, pgvector, etc.). |

---

> [!TIP]
> When asking the agent to do a task, mentioning the skill name explicitly (e.g. *"use `diagnosing-bugs`"* or *"run a `code-review`"*) immediately loads the right instructions without any guesswork.
