# 🤖 AI Agent Skills Library (`ai-skills`)

[![Skills Catalog](https://img.shields.io/badge/Skills-123%20Available-blueviolet?style=for-the-badge&logo=probot)](.agents/DESCRIPTIONS.md)
[![Composite Skills](https://img.shields.io/badge/Calling--Skills-8%20Bundles-brightgreen?style=for-the-badge)](call-doc.md)
[![Agent Protocol](https://img.shields.io/badge/Protocol-Agentic%20Coding-ff69b4?style=for-the-badge)](.agents/skills)

A curated repository of production-grade **AI Agent Skills** designed for autonomous AI agents and pair-programming assistants. This library equips agents with domain-specific patterns, architectural guardrails, best practices, and expert execution routines across composite meta-skills, AI engineering, UI/UX design & motion, Cloudflare serverless edge, full-stack development, data architecture, debugging, and workflow automation.

---

## ⚡ Quick Start: Install All 123+ Skills via CLI

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

### 🎯 Install a Specific Skill or Composite Bundle
To install a specific skill (e.g. `call-front`, `call-backend`, `impeccable`, or `ai-engineer`):

```bash
npx skills add shahin1717/ai-skills --skill=call-front
```

> [!IMPORTANT]
> Always execute `npx skills` commands from your **workspace root** (or pass `-g` for global installation).

---

## 🚀 Composite Calling Skills (`call-doc.md`)

Avoid invoking multiple individual skills one by one! Use **Composite Calling Skills** to trigger a complete suite of specialized skills in a single prompt:

| Shortcut Command | Composite Skill Name | Total Bundled Skills | Primary Domain |
| :--- | :--- | :---: | :--- |
| **`/call-ai-ml`** | `call-ai-ml` | 22 skills | Full-Stack AI/ML, RAG, Vectors, LLM & Pipelines |
| **`/call-backend`** | `call-backend` | 22 skills | Backend APIs, FastAPI, Node.js, DB & Performance |
| **`/call-arch`** | `call-arch` | 14 skills | Architecture Design, Domain Modeling & Refactoring |
| **`/call-front`** | `call-front` | 25 skills | Frontend, UI/UX Aesthetics, Next.js & Motion |
| **`/call-cloudflare`** | `call-cloudflare` | 11 skills | Cloudflare Edge, Workers, DO & Infrastructure |
| **`/call-data`** | `call-data` | 13 skills | Big Data, Data Pipelines, SQL & DB Tuning |
| **`/call-debug`** | `call-debug` | 7 skills | Deep Bug Diagnosis, Sentry & Performance |
| **`/call-research`** | `call-research` | 8 skills | Deep Research, Web Scraping & Synthesis |

*(See [call-doc.md](file://call-doc.md) for full reference).*

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
├── call-doc.md                 # Complete reference for 8 Composite Calling Skills
├── .agents/
│   ├── DESCRIPTIONS.md         # Full catalog and usage matrix for all 123 skills
│   └── skills/                 # 123 specialized agent skill directories
│       ├── call-ai-ml/
│       ├── call-backend/
│       ├── call-arch/
│       ├── call-front/
│       ├── impeccable/
│       ├── ai-engineer/
│       ├── cloudflare/
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

### 2. 📦 Vercel Labs Skills (`vercel-labs/skills`)
* **GitHub Repository**: [https://github.com/vercel-labs/skills](https://github.com/vercel-labs/skills)
* **Install All Skills**:
  ```bash
  npx skills add vercel-labs/skills
  ```

### 3. 📦 Antigravity Skills (`rmyndharis/antigravity-skills`)
* **GitHub Repository**: [https://github.com/rmyndharis/antigravity-skills](https://github.com/rmyndharis/antigravity-skills)
* **Install All Skills**:
  ```bash
  npx skills add rmyndharis/antigravity-skills
  ```

### 4. 📦 Deep Research Skills (`Weizhena/Deep-Research-skills`)
* **GitHub Repository**: [https://github.com/Weizhena/Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills)
* **Install All Skills**:
  ```bash
  npx skills add Weizhena/Deep-Research-skills
  ```

### 5. 📦 Impeccable Design Skill (`pbakaus/impeccable`)
* **GitHub Repository**: [https://github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable)
* **Install Skill**:
  ```bash
  npx skills add pbakaus/impeccable
  ```

### 6. 📦 Taste Skill Engine (`Leonxlnx/taste-skill`)
* **GitHub Repository**: [https://github.com/Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
* **Install All Skills**:
  ```bash
  npx skills add Leonxlnx/taste-skill
  ```

### 7. 📦 Emil Kowalski Skills (`emilkowalski/skills`)
* **GitHub Repository**: [https://github.com/emilkowalski/skills](https://github.com/emilkowalski/skills)
* **Install All Skills**:
  ```bash
  npx skills add emilkowalski/skills
  ```

### 8. 📦 Cloudflare Agent Skills (`cloudflare/skills`)
* **GitHub Repository**: [https://github.com/cloudflare/skills](https://github.com/cloudflare/skills)
* **Install All Skills**:
  ```bash
  npx skills add cloudflare/skills
  ```

### 9. 📦 Sentry AI Skills (`getsentry/sentry-for-ai`)
* **GitHub Repository**: [https://github.com/getsentry/sentry-for-ai](https://github.com/getsentry/sentry-for-ai)
* **Install Skill**:
  ```bash
  npx skills add getsentry/sentry-for-ai
  ```

### 10. 📦 Composio Skills (`composiohq/skills`)
* **GitHub Repository**: [https://github.com/composiohq/skills](https://github.com/composiohq/skills)
* **Install Skill**:
  ```bash
  npx skills add composiohq/skills
  ```

---

## 🛠️ Skill Categories Overview

This repository provides **123 specialized skills** across key engineering domains:

### 🚀 Composite Calling Skills (Meta Bundles)
* **`call-ai-ml`**: Composite bundler skill: activates 22 AI/ML, RAG, vector database, prompt optimization, and FastAPI pipeline skills at once.
* **`call-backend`**: Composite bundler skill: activates 22 backend development, FastAPI/Node.js, DB architecture, performance, and clean code skills.
* **`call-arch`**: Composite bundler skill: activates 14 architecture design, deep module refactoring, domain modeling, and system review skills.
* **`call-front`**: Composite bundler skill: activates 25 frontend, UI/UX visual aesthetics, Next.js, and web motion/animation skills.
* **`call-cloudflare`**: Composite bundler skill: activates 11 Cloudflare edge, Workers, Durable Objects, Zero Trust, and Wrangler CLI skills.
* **`call-data`**: Composite bundler skill: activates 13 big data pipeline, SQL query tuning, PostgreSQL, dbt, and database migration skills.
* **`call-debug`**: Composite bundler skill: activates 7 deep bug diagnosis, Sentry error fixing, Web Vitals performance, and mock testing skills.
* **`call-research`**: Composite bundler skill: activates 8 deep research execution, web page markdown extraction, and synthesis skills.

### 🧠 AI & Machine Learning
* **`ai-engineer`**: Build production-ready LLM applications, advanced RAG systems, and intelligent agents.
* **`ml-engineer`**: Build production ML systems with PyTorch 2.x, TensorFlow, and modern ML frameworks.
* **`ml-pipeline-workflow`**: Build end-to-end MLOps pipelines from data preparation through model training, validation, and production deployment.
* **`embedding-strategies`**: Select and optimize embedding models for semantic search and RAG applications.
* **`langchain-architecture`**: Design LLM applications using the LangChain framework with agents, memory, and tool integration patterns.
* **`llm-application-dev-prompt-optimize`**: You are an expert prompt engineer specializing in crafting effective prompts for LLMs through advanced techniques inc...
* **`vector-database-engineer`**: Expert in vector databases, embedding strategies, and semantic search implementation.
* **`quant-analyst`**: Build financial models, backtest trading strategies, and analyze market data.
* **`data-scientist`**: Expert data scientist for advanced analytics, machine learning, and statistical modeling.
* **`composio`**: Integrate 1000+ external apps via Composio CLI or SDK for AI agents.

### ☁️ Cloudflare Ecosystem & Serverless Edge
* **`agents-sdk`**: Build AI agents on Cloudflare Workers using the Agents SDK.
* **`cloudflare`**: Comprehensive Cloudflare platform skill covering Workers, Pages, storage (KV, D1, R2), AI (Workers AI, Vectorize, Age...
* **`cloudflare-email-service`**: Send and receive transactional emails with Cloudflare Email Service (Email Sending + Email Routing).
* **`cloudflare-one`**: Guides Cloudflare One Zero Trust and SASE work across Access, Gateway, WARP, Tunnel, Cloudflare WAN, DLP, CASB, devic...
* **`cloudflare-one-migrations`**: Plans migrations from Zscaler ZIA/ZPA, Palo Alto, legacy VPN, SWG, or SASE stacks to Cloudflare One.
* **`durable-objects`**: Create and review Cloudflare Durable Objects.
* **`sandbox-sdk`**: Build sandboxed applications for secure code execution.
* **`turnstile-spin`**: Set up Cloudflare Turnstile end-to-end in a project.
* **`web-perf`**: Analyzes web performance using Chrome DevTools MCP.
* **`workers-best-practices`**: Reviews and authors Cloudflare Workers code against production best practices.
* **`wrangler`**: Cloudflare Workers CLI for deploying, developing, and managing Workers, KV, R2, D1, Vectorize, Hyperdrive, Workers AI...

### 🎨 UI/UX Design, Motion & Frontend Engineering
* **`impeccable`**: Frontend design, polish, typography, spacing, color, motion, micro-interactions, and visual hardening.
* **`emil-design-eng`**: Emil Kowalski's philosophy on UI polish, component design, animation decisions, and micro-interactions.
* **`apple-design`**: Apple-style interface design, fluid physical motion, spring animations, depth materials, and typography.
* **`design-taste-frontend`**: Anti-slop frontend skill for landing pages, portfolios, and redesigns with real design systems.
* **`design-taste-frontend-v1`**: Original v1 taste-skill for landing pages, portfolios, and UI refactoring.
* **`gpt-taste`**: Elite UX/UI & GSAP motion engineering with layout variance, AIDA structure, wide typography, gapless bento.
* **`high-end-visual-design`**: High-end agency design guidance for fonts, spacing, shadows, card structures, and subtle motion.
* **`industrial-brutalist-ui`**: Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics.
* **`minimalist-ui`**: Clean editorial-style interfaces with warm monochrome palettes, flat bento grids, and muted pastels.
* **`stitch-design-taste`**: Semantic Design System Skill for Google Stitch enforcing DESIGN.md standards.
* **`brandkit`**: Premium brand-kit image generation for logo systems, identity decks, and visual-world presentations.
* **`image-to-code`**: Generate section design images first, analyze deeply, then build matching web interface layout.
* **`imagegen-frontend-web`**: Section-by-section website image reference generation for landing pages and web apps.
* **`imagegen-frontend-mobile`**: Mobile app image-generation skill for creating premium iOS/Android screen concepts and flows.
* **`animate`**: Build web animations from scratch with intentional curves, duration, interruption handling, and exits.
* **`animation-vocabulary`**: Reverse-lookup glossary converting vague motion descriptions into precise terms (e.g. Pop in, Rubber-banding).
* **`find-animation-opportunities`**: Search codebase/UI for static elements that should animate, proposing exact motion parameters.
* **`improve-animations`**: Survey codebase animation code as a senior motion advisor and produce prioritized audits/plans.
* **`review-animations`**: Review existing animation and motion code diffs against Emil Kowalski's high craft bar.
* **`pick-ui-library`**: Curated selection guide for picking UI libraries (OTP, charts, command menus, virtualization, toasts).
* **`prototype`**: Build multiple UI variants behind a visual picker for live comparison and selection.
* **`redesign-existing-projects`**: Upgrade existing websites and apps to premium quality without breaking functionality.
* **`frontend-developer`**: Build React components, implement responsive layouts, and handle client-side state management.
* **`nextjs-app-router-patterns`**: Master Next.js 14+ App Router with Server Components, streaming, parallel routes, and advanced data fetching.
* **`design-an-interface`**: Generate multiple radically different interface designs for a module using parallel sub-agents.

### 🐍 Python & Backend Engineering
* **`python-pro`**: Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices.
* **`python-performance-optimization`**: Profile and optimize Python code using cProfile, memory profilers, and performance best practices.
* **`python-testing-patterns`**: Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development.
* **`async-python-patterns`**: Master Python asyncio, concurrent programming, and async/await patterns for high-performance applications.
* **`fastapi-pro`**: Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2.
* **`fastapi-templates`**: Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling.
* **`nodejs-backend-patterns`**: Build production-ready Node.js backend services with Express/Fastify, implementing middleware patterns, error handlin...
* **`bash-pro`**: Master of defensive Bash scripting for production automation, CI/CD pipelines, and system utilities.
* **`php-pro`**: Write idiomatic PHP code with generators, iterators, SPL data structures, and modern OOP features.
* **`scala-pro`**: Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing.

### 🗄️ Data & Database Engineering
* **`data-engineer`**: Build scalable data pipelines, modern data warehouses, and real-time streaming architectures.
* **`data-engineering-data-pipeline`**: You are a data pipeline architecture expert specializing in scalable, reliable, and cost-effective data pipelines for...
* **`data-engineering-data-driven-feature`**: Build features guided by data insights, A/B testing, and continuous measurement using specialized agents for analysis...
* **`data-quality-frameworks`**: Implement data quality validation with Great Expectations, dbt tests, and data contracts.
* **`data-storytelling`**: Transform data into compelling narratives using visualization, context, and persuasive structure.
* **`database-architect`**: Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and ...
* **`database-admin`**: Expert database administrator specializing in modern cloud databases, automation, and reliability engineering.
* **`database-optimizer`**: Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures.
* **`sql-optimization-patterns`**: Master SQL query optimization, indexing strategies, and EXPLAIN analysis to dramatically improve database performance...
* **`database-migration`**: Execute database migrations across ORMs and platforms with zero-downtime strategies, data transformation, and rollbac...
* **`database-migrations-sql-migrations`**: SQL database migrations with zero-downtime strategies for PostgreSQL, MySQL, SQL Server.
* **`database-migrations-migration-observability`**: Migration monitoring, CDC, and observability infrastructure.
* **`database-cloud-optimization-cost-optimize`**: You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performan...
* **`postgresql`**: Design a PostgreSQL-specific schema.
* **`sql-pro`**: Master modern SQL with cloud-native databases, OLTP/OLAP optimization, and advanced query techniques.
* **`dbt-transformation-patterns`**: Master dbt (data build tool) for analytics engineering with model organization, testing, documentation, and increment...
* **`spark-optimization`**: Optimize Apache Spark jobs with partitioning, caching, shuffle optimization, and memory tuning.

### 🏗️ Architecture, Code Quality & Output
* **`architect-review`**: Master software architect specializing in modern architecture patterns, clean architecture, microservices, event-driv...
* **`architecture-patterns`**: Implement proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Drive...
* **`codebase-design`**: Shared vocabulary for designing deep modules.
* **`code-review`**: Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code...
* **`code-refactoring-refactor-clean`**: You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software e...
* **`codebase-cleanup-refactor-clean`**: You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software e...
* **`improve-codebase-architecture`**: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one y...
* **`domain-modeling`**: Build and sharpen a project's domain model.
* **`full-output-enforcement`**: Overrides default LLM truncation behavior, enforcing complete unabridged code generation.

### 🔬 Research, Debugging, Observability & Workflow
* **`diagnosing-bugs`**: Diagnosis loop for hard bugs and performance regressions.
* **`sentry-fix-issues`**: Automated Sentry issue investigation and bug fixing via MCP.
* **`research`**: Conduct preliminary research on a topic and generate research outline.
* **`research-add-fields`**: Add field definitions to existing research outline.
* **`research-add-items`**: Add items (research objects) to existing research outline.
* **`research-deep`**: Read research outline, launch independent agent for each item for deep research.
* **`research-report`**: Summarize deep research results into markdown report, cover all fields, skip uncertain values.
* **`grilling`**: Grill the user relentlessly about a plan, decision, or idea.
* **`grill-me`**: A relentless interview to sharpen a plan or design.
* **`grill-with-docs`**: A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go.
* **`defuddle`**: Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens.
* **`handoff`**: Compact the current conversation into a handoff document for another agent to pick up.
* **`teach`**: Teach the user a new skill or concept, within this workspace.
* **`skill-creator`**: Guide for creating effective skills.
* **`api-design-principles`**: Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight develo...
* **`api-documenter`**: Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices.
* **`api-testing-observability-api-mock`**: You are an API mocking expert specializing in realistic mock services for development, testing, and demos.

### 📓 Obsidian & Knowledge Management
* **`obsidian-markdown`**: Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific ...
* **`obsidian-bases`**: Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries.
* **`obsidian-cli`**: Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, tasks, properties, an...
* **`obsidian-workspace-sync`**: Detects the existence of .code-workspace files in the project root, maps the developer workspace to the corresponding...
* **`json-canvas`**: Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections.

### 🛠️ Specialized Engineering & Compliance
* **`airflow-dag-patterns`**: Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment.
* **`code-documentation-doc-generate`**: You are a documentation expert specializing in creating comprehensive, maintainable documentation from code.
* **`content-marketer`**: Elite content marketing strategist specializing in AI-powered content creation, omnichannel distribution, SEO optimiz...
* **`legal-advisor`**: Draft privacy policies, terms of service, disclaimers, and legal notices.
* **`gdpr-data-handling`**: Implement GDPR-compliant data handling with consent management, data subject rights, and privacy by design.
* **`pci-compliance`**: Implement PCI DSS compliance requirements for secure handling of payment card data and payment systems.
* **`business-analyst`**: Master modern business analysis with AI-powered analytics, real-time dashboards, and data-driven insights.
* **`kpi-dashboard-design`**: Design effective KPI dashboards with metrics selection, visualization best practices, and real-time monitoring patterns.
* **`hybrid-cloud-networking`**: Configure secure, high-performance connectivity between on-premises infrastructure and cloud platforms using VPN and ...
* **`ios-developer`**: Develop native iOS applications with Swift/SwiftUI.
* **`unity-ecs-patterns`**: Master Unity ECS (Entity Component System) with DOTS, Jobs, and Burst for high-performance game development.

*(For the complete catalog and detailed usage matrix of all 123 skills, see [.agents/DESCRIPTIONS.md](file://.agents/DESCRIPTIONS.md)).*

---

## 🚀 How Agents Discover Skills

Agent tools automatically scan customization roots for skills:

1. **Global Customizations**: `~/.gemini/config/skills/` or `~/.agents/skills/`
2. **Workspace Customizations**: `.agents/skills/<skill-name>/SKILL.md`

When a user request matches a skill's `name` or `description`, the agent reads the skill instructions before initiating execution.

You can also explicitly invoke any skill or composite bundle in conversation:
> *"Use `/call-front` to build this dark mode dashboard UI."*  
> *"Run `/call-backend` on this user authentication service."*

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
