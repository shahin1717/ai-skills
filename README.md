# 🤖 AI Agent Skills Library (`ai-skills`)

[![Skills Catalog](https://img.shields.io/badge/Skills-74%20Available-blueviolet?style=for-the-badge&logo=probot)](.agents/DESCRIPTIONS.md)
[![Agent Protocol](https://img.shields.io/badge/Protocol-Agentic%20Coding-ff69b4?style=for-the-badge)](.agents/skills)

A curated repository of production-grade **AI Agent Skills** designed for autonomous AI agents and pair-programming assistants. This library equips agents with domain-specific patterns, architectural guardrails, best practices, and expert execution routines across AI engineering, full-stack development, data architecture, debugging, and workflow automation.

---

## ⚡ Quick Start: Install All 74+ Skills via CLI

Install all skills directly into your project or globally using the `npx skills` CLI command:

### 📦 Install All Skills to Your Project
Run this command from your project root directory:

```bash
npx skills add shahin1717/ai-skills
```

### 🌐 Install All Skills Globally
To make all skills available across all projects on your machine:

```bash
npx skills add shahin1717/ai-skills -g
```

### 🎯 Install a Specific Skill
To install just a single skill (e.g. `ai-engineer` or `diagnosing-bugs`):

```bash
npx skills add shahin1717/ai-skills --skill=ai-engineer
```

> [!IMPORTANT]
> Always execute `npx skills` commands from your **workspace root** (or pass `-g` for global installation).

---

## 💡 What is an AI Skill?

An **AI Skill** is a structured instruction package (`SKILL.md`) loaded into an AI agent's context when a specific task domain is triggered. Instead of relying on general model improvisation, skills provide:

* **Expert Workflows & Best Practices**: Standardized guidelines and code patterns proven in production.
* **Domain Guardrails**: Clear boundaries on what to do and what *not* to do.
* **Deterministic Quality**: Consistent, high-grade technical output across complex development tasks.

---

## 📂 Repository Structure

```text
ai-skills/
├── .agents/
│   ├── DESCRIPTIONS.md         # Full catalog and usage matrix for all skills
│   └── skills/                 # 74 specialized agent skill directories
│       ├── ai-engineer/
│       ├── diagnosing-bugs/
│       ├── python-pro/
│       ├── database-architect/
│       ├── obsidian-markdown/
│       └── ...
└── README.md                   # Main documentation
```

---

## 🌐 Upstream Skill Sources & Registries

The skills in this repository are curated and compiled from top upstream AI agent skill sources. You can also install skills directly from the original creators using the `npx skills` CLI:

### 1. 📦 Matt Pocock Skills (`mattpocock/skills`)
* **GitHub Repository**: [https://github.com/mattpocock/skills](https://github.com/mattpocock/skills)
* **Install All Skills**:
  ```bash
  npx skills add mattpocock/skills
  ```
* **Install Specific Skill** (e.g., `handoff` or `code-review`):
  ```bash
  npx skills add mattpocock/skills --skill=handoff
  ```

### 2. 📦 Vercel Labs Skills (`vercel-labs/skills`)
* **GitHub Repository**: [https://github.com/vercel-labs/skills](https://github.com/vercel-labs/skills)
* **Install All Skills**:
  ```bash
  npx skills add vercel-labs/skills
  ```
* **Install Specific Skill** (e.g., `find-skills`):
  ```bash
  npx skills add vercel-labs/skills --skill=find-skills
  ```

### 3. 📦 Antigravity Skills (`rmyndharis/antigravity-skills`)
* **GitHub Repository**: [https://github.com/rmyndharis/antigravity-skills](https://github.com/rmyndharis/antigravity-skills)
* **Install All Skills**:
  ```bash
  npx skills add rmyndharis/antigravity-skills
  ```
* **Install Specific Skill** (e.g., `code-documentation-doc-generate`):
  ```bash
  npx skills add rmyndharis/antigravity-skills --skill=code-documentation-doc-generate
  ```

---

## 🛠️ Skill Categories Overview

This repository provides **74 specialized skills** across key engineering domains:

### 🧠 AI & Machine Learning
* **`ai-engineer`**: LLM applications, RAG systems, vector search, and agent orchestration.
* **`ml-engineer`**: Production ML model serving, feature engineering, and inference optimization.
* **`ml-pipeline-workflow`**: End-to-end MLOps pipelines from data prep to production deployment.
* **`embedding-strategies`**: Embeddings model selection, chunking, and semantic search tuning.
* **`langchain-architecture`**: Agentic workflows, tool integration, and memory patterns.
* **`llm-application-dev-prompt-optimize`**: Advanced prompt engineering (CoT, Constitutional AI).
* **`vector-database-engineer`**: Pinecone, Weaviate, Qdrant, Milvus, and pgvector implementations.

### 🐍 Python & Backend Engineering
* **`python-pro`**: Modern Python 3.12+ features, async/await, and production standards.
* **`python-performance-optimization`**: Profiling (`cProfile`, memory profilers) and bottleneck removal.
* **`python-testing-patterns`**: `pytest`, fixtures, mocking, and TDD strategies.
* **`async-python-patterns`**: High-concurrency `asyncio` and non-blocking I/O routines.
* **`fastapi-pro`** & **`fastapi-templates`**: Async REST APIs with FastAPI, SQLAlchemy 2.0, Pydantic V2.
* **`nodejs-backend-patterns`**: Express/Fastify services, middleware, and microservices.
* **`bash-pro`**: Defensive shell scripting, CI/CD automation, and process management.

### 🗄️ Data & Database Engineering
* **`data-engineer`**: Scalable data pipelines using Spark, dbt, Airflow, and cloud platforms.
* **`data-quality-frameworks`**: Data validation with Great Expectations and dbt tests.
* **`database-architect`**: Green-field schema design, SQL/NoSQL selection, and data modeling.
* **`database-optimizer`**: Advanced indexing, EXPLAIN analysis, and N+1 query elimination.
* **`database-migration`**: Zero-downtime database migrations and rollback procedures.
* **`postgresql`**: PostgreSQL schema design, jsonb strategies, and query performance.
* **`spark-optimization`**: Apache Spark memory tuning, partitioning, and shuffle minimization.

### 🏗️ Architecture & Code Quality
* **`architect-review`**: System architecture reviews, microservices, and event-driven designs.
* **`architecture-patterns`**: Clean Architecture, Hexagonal Architecture, and Domain-Driven Design (DDD).
* **`codebase-design`**: Deep module design principles and interface separation.
* **`code-review`**: Automated review against coding standards and specification requirements.
* **`code-refactoring-refactor-clean`**: SOLID refactoring and technical debt reduction.

### 🌐 Web, Frontend & APIs
* **`frontend-developer`**: React 19, Next.js 15, state management, and responsive layouts.
* **`nextjs-app-router-patterns`**: Next.js App Router, Server Components, and streaming.
* **`api-design-principles`**: REST and GraphQL API standards and developer experience.
* **`api-documenter`**: OpenAPI 3.1 specifications, interactive docs, and SDK generation.

### 🔬 Debugging, Research & Workflow
* **`diagnosing-bugs`**: Systematic diagnosis loop for complex bugs and performance regressions.
* **`research`**: In-depth technical research against high-trust primary sources.
* **`grilling`** / **`grill-me`**: Relentless stress-testing of architecture plans and ideas.
* **`defuddle`**: Extracting clean Markdown content from documentation web pages.
* **`handoff`**: Structured context handoff notes for resuming complex multi-step tasks.

### 📓 Obsidian & Knowledge Management
* **`obsidian-markdown`**: Obsidian-flavored markdown syntax (wikilinks, callouts, embeds).
* **`obsidian-bases`**: `.base` database views, card layouts, and formulas.
* **`obsidian-cli`**: Command-line vault manipulation, searching, and note automation.
* **`json-canvas`**: `.canvas` file creation and visual flowchart editing.

*(For the complete list and detailed descriptions of all 74 skills, see [.agents/DESCRIPTIONS.md](file://.agents/DESCRIPTIONS.md)).*

---

## 🚀 How Agents Discover Skills

Agent tools automatically scan customization roots for skills:

1. **Global Customizations**: `~/.gemini/config/skills/`
2. **Workspace Customizations**: `.agents/skills/<skill-name>/SKILL.md`

When a user request matches a skill's `name` or `description`, the agent reads the skill instructions before initiating execution.

You can also explicitly invoke any skill in conversation:
> *"Use the `diagnosing-bugs` skill to investigate this memory leak."*  
> *"Run `architect-review` on the proposed API refactor."*

---

## 🤝 Contributing & Adding New Skills

To add a new custom skill to this library:

1. Create a directory under `.agents/skills/<your-skill-name>/`.
2. Add a `SKILL.md` file with YAML frontmatter:
   ```yaml
   ---
   name: your-skill-name
   description: Concise description of when and why to trigger this skill.
   ---
   ```
3. Add clear, actionable sections:
   - **Use this skill when**: Trigger criteria.
   - **Do not use this skill when**: Out of scope cases.
   - **Instructions**: Step-by-step guidance, patterns, and code rules.
4. Update [.agents/DESCRIPTIONS.md](file://.agents/DESCRIPTIONS.md) to register your skill in the catalog.

---

## 📄 License

This repository is maintained for AI agent workflows and open developer skill catalogs.