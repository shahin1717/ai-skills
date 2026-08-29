# 🤖 Agent Skills Catalog

This file documents all available AI agent **skills** for the project workspace and developer environment.

A **skill** is a set of precise instructions loaded into the AI agent's context when a relevant task is triggered. Instead of the agent improvising, the skill tells it *exactly* how to perform a specialized task — with known patterns, best practices, and guardrails. This keeps outputs consistent and production-quality without you having to re-explain context every time.

---

## 🚀 Composite Calling Skills (`call-doc.md`)

Save time in conversation by invoking **Composite Calling Skills** (`/call-feature`, `/call-build`, `/call-doc`, `/call-front`, `/call-backend`, `/call-ai-ml`, `/call-arch`, `/call-cloudflare`, `/call-data`, `/call-debug`, `/call-research`) to activate an entire bundle of specialized skills in a single command. See [call-doc.md](file://call-doc.md) for full details.

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

### 5. 📦 Impeccable Design Skill (`pbakaus/impeccable`)
* **GitHub Repository**: [https://github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable)
* **Installation Command**:
  ```bash
  npx skills add pbakaus/impeccable
  ```

### 6. 📦 Taste Skill Engine (`Leonxlnx/taste-skill`)
* **GitHub Repository**: [https://github.com/Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
* **Installation Command (All Skills)**:
  ```bash
  npx skills add Leonxlnx/taste-skill
  ```

### 7. 📦 Emil Kowalski Skills (`emilkowalski/skills`)
* **GitHub Repository**: [https://github.com/emilkowalski/skills](https://github.com/emilkowalski/skills)
* **Installation Command (All Skills)**:
  ```bash
  npx skills add emilkowalski/skills
  ```

### 8. 📦 Cloudflare Agent Skills (`cloudflare/skills`)
* **GitHub Repository**: [https://github.com/cloudflare/skills](https://github.com/cloudflare/skills)
* **Installation Command (All Skills)**:
  ```bash
  npx skills add cloudflare/skills
  ```

### 9. 📦 Sentry AI Skills (`getsentry/sentry-for-ai`)
* **GitHub Repository**: [https://github.com/getsentry/sentry-for-ai](https://github.com/getsentry/sentry-for-ai)
* **Installation Command**:
  ```bash
  npx skills add getsentry/sentry-for-ai
  ```

### 10. 📦 Composio Skills (`composiohq/skills`)
* **GitHub Repository**: [https://github.com/composiohq/skills](https://github.com/composiohq/skills)
* **Installation Command**:
  ```bash
  npx skills add composiohq/skills
  ```

---

## 🔍 How Skills Are Triggered

Skills are matched automatically by name/description when you ask the agent to do something relevant. You can also mention any skill or composite calling skill directly (e.g. `"/call-front"`, `"/call-backend"`, or `"use cloudflare"`).

---

## 📂 Complete Skills Reference (200+ Available Skills)

### 🚀 Composite Calling Skills (Meta Bundles)
| Skill | Description / Usage |
| :--- | :--- |
| `call-feature` | Master composite skill: orchestrates full-lifecycle multi-agent feature delivery across research, architecture, core engineering build, frontend UI, testing, and docs using parallel subagents. |
| `call-build` | Composite bundler skill: activates 15 software engineering discipline, TDD, virtual team roles, anti-overengineering (ponytail), and high-density token execution skills. |
| `call-ai-ml` | Composite bundler skill: activates 22 AI/ML, RAG, vector database, prompt optimization, and FastAPI pipeline skills at once. |
| `call-backend` | Composite bundler skill: activates 22 backend development, FastAPI/Node.js, DB architecture, performance, and clean code skills. |
| `call-arch` | Composite bundler skill: activates 14 architecture design, deep module refactoring, domain modeling, and system review skills. |
| `call-front` | Composite bundler skill: activates 27 frontend, UI/UX visual aesthetics, Next.js, and web motion/animation skills. |
| `call-cloudflare` | Composite bundler skill: activates 11 Cloudflare edge, Workers, Durable Objects, Zero Trust, and Wrangler CLI skills. |
| `call-data` | Composite bundler skill: activates 13 big data pipeline, SQL query tuning, PostgreSQL, dbt, and database migration skills. |
| `call-debug` | Composite bundler skill: activates 7 deep bug diagnosis, Sentry error fixing, Web Vitals performance, and mock testing skills. |
| `call-research` | Composite bundler skill: activates 14 deep research execution, web page markdown extraction, graph parsing, trends, and synthesis skills. |
| `call-doc` | Composite bundler skill: activates 12 code annotation, header docstring, OpenAPI, architecture review, and documentation skills. |

---

### 🧠 AI & Machine Learning
| Skill | Description / Usage |
| :--- | :--- |
| `ai-engineer` | Build production-ready LLM applications, advanced RAG systems, and intelligent agents. |
| `ml-engineer` | Build production ML systems with PyTorch 2.x, TensorFlow, and modern ML frameworks. |
| `ml-pipeline-workflow` | Build end-to-end MLOps pipelines from data preparation through model training, validation, and production deployment. |
| `embedding-strategies` | Select and optimize embedding models for semantic search and RAG applications. |
| `langchain-architecture` | Design LLM applications using the LangChain framework with agents, memory, and tool integration patterns. |
| `llm-application-dev-prompt-optimize` | You are an expert prompt engineer specializing in crafting effective prompts for LLMs through advanced techniques inc... |
| `vector-database-engineer` | Expert in vector databases, embedding strategies, and semantic search implementation. |
| `quant-analyst` | Build financial models, backtest trading strategies, and analyze market data. |
| `data-scientist` | Expert data scientist for advanced analytics, machine learning, and statistical modeling. |
| `composio` | Integrate 1000+ external apps via Composio CLI or SDK for AI agents. |

---

### ☁️ Cloudflare Ecosystem & Serverless Edge
| Skill | Description / Usage |
| :--- | :--- |
| `agents-sdk` | Build AI agents on Cloudflare Workers using the Agents SDK. |
| `cloudflare` | Comprehensive Cloudflare platform skill covering Workers, Pages, storage (KV, D1, R2), AI (Workers AI, Vectorize, Age... |
| `cloudflare-email-service` | Send and receive transactional emails with Cloudflare Email Service (Email Sending + Email Routing). |
| `cloudflare-one` | Guides Cloudflare One Zero Trust and SASE work across Access, Gateway, WARP, Tunnel, Cloudflare WAN, DLP, CASB, devic... |
| `cloudflare-one-migrations` | Plans migrations from Zscaler ZIA/ZPA, Palo Alto, legacy VPN, SWG, or SASE stacks to Cloudflare One. |
| `durable-objects` | Create and review Cloudflare Durable Objects. |
| `sandbox-sdk` | Build sandboxed applications for secure code execution. |
| `turnstile-spin` | Set up Cloudflare Turnstile end-to-end in a project. |
| `web-perf` | Analyzes web performance using Chrome DevTools MCP. |
| `workers-best-practices` | Reviews and authors Cloudflare Workers code against production best practices. |
| `wrangler` | Cloudflare Workers CLI for deploying, developing, and managing Workers, KV, R2, D1, Vectorize, Hyperdrive, Workers AI... |

---

### 🎨 UI/UX Design, Motion & Frontend Engineering
| Skill | Description / Usage |
| :--- | :--- |
| `ui-ux-pro-max` | Design intelligence, multi-platform UI generation, design systems, and responsive layout styling. |
| `hyperframes` | Code-to-video engine: renders HTML/CSS into deterministic MP4 videos, product tours, and motion graphics. |
| `impeccable` | Frontend design, polish, typography, spacing, color, motion, micro-interactions, and visual hardening. |
| `emil-design-eng` | Emil Kowalski's philosophy on UI polish, component design, animation decisions, and micro-interactions. |
| `apple-design` | Apple-style interface design, fluid physical motion, spring animations, depth materials, and typography. |
| `design-taste-frontend` | Anti-slop frontend skill for landing pages, portfolios, and redesigns with real design systems. |
| `design-taste-frontend-v1` | Original v1 taste-skill for landing pages, portfolios, and UI refactoring. |
| `gpt-taste` | Elite UX/UI & GSAP motion engineering with layout variance, AIDA structure, wide typography, gapless bento. |
| `high-end-visual-design` | High-end agency design guidance for fonts, spacing, shadows, card structures, and subtle motion. |
| `industrial-brutalist-ui` | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. |
| `minimalist-ui` | Clean editorial-style interfaces with warm monochrome palettes, flat bento grids, and muted pastels. |
| `stitch-design-taste` | Semantic Design System Skill for Google Stitch enforcing DESIGN.md standards. |
| `brandkit` | Premium brand-kit image generation for logo systems, identity decks, and visual-world presentations. |
| `image-to-code` | Generate section design images first, analyze deeply, then build matching web interface layout. |
| `imagegen-frontend-web` | Section-by-section website image reference generation for landing pages and web apps. |
| `imagegen-frontend-mobile` | Mobile app image-generation skill for creating premium iOS/Android screen concepts and flows. |
| `animate` | Build web animations from scratch with intentional curves, duration, interruption handling, and exits. |
| `animation-vocabulary` | Reverse-lookup glossary converting vague motion descriptions into precise terms (e.g. Pop in, Rubber-banding). |
| `find-animation-opportunities` | Search codebase/UI for static elements that should animate, proposing exact motion parameters. |
| `improve-animations` | Survey codebase animation code as a senior motion advisor and produce prioritized audits/plans. |
| `review-animations` | Review existing animation and motion code diffs against Emil Kowalski's high craft bar. |
| `pick-ui-library` | Curated selection guide for picking UI libraries (OTP, charts, command menus, virtualization, toasts). |
| `prototype` | Build multiple UI variants behind a visual picker for live comparison and selection. |
| `redesign-existing-projects` | Upgrade existing websites and apps to premium quality without breaking functionality. |
| `frontend-developer` | Build React components, implement responsive layouts, and handle client-side state management. |
| `nextjs-app-router-patterns` | Master Next.js 14+ App Router with Server Components, streaming, parallel routes, and advanced data fetching. |
| `design-an-interface` | Generate multiple radically different interface designs for a module using parallel sub-agents. |

---

### 🏗️ Build Methodology, Python & Backend Engineering
| Skill | Description / Usage |
| :--- | :--- |
| `using-superpowers` | Comprehensive software development methodology enforcing TDD discipline and structured engineering. |
| `subagent-driven-development` | Orchestrating and dispatching parallel specialized subagents with isolated context boundaries. |
| `test-driven-development` | Strict Red-Green-Refactor testing discipline for robust, zero-regression software delivery. |
| `gstack` | Virtual engineering team roles (CEO, Eng Manager, Architect, QA Lead, Release Eng) by Garry Tan. |
| `ponytail` | Anti-overengineering decision ladder (YAGNI, code reuse, native features before adding dependencies). |
| `caveman` | Ultra-concise, high-density token-efficient responses eliminating filler words and fluff. |
| `i-have-adhd` | Action-first, bounded, scannable steps without buried conclusions or rambling explanations. |
| `python-pro` | Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices. |
| `python-performance-optimization` | Profile and optimize Python code using cProfile, memory profilers, and performance best practices. |
| `python-testing-patterns` | Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. |
| `async-python-patterns` | Master Python asyncio, concurrent programming, and async/await patterns for high-performance applications. |
| `fastapi-pro` | Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. |
| `fastapi-templates` | Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling. |
| `nodejs-backend-patterns` | Build production-ready Node.js backend services with Express/Fastify, implementing middleware patterns, error handlin... |
| `bash-pro` | Master of defensive Bash scripting for production automation, CI/CD pipelines, and system utilities. |
| `php-pro` | Write idiomatic PHP code with generators, iterators, SPL data structures, and modern OOP features. |
| `scala-pro` | Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing. |

---

### 🗄️ Data & Database Engineering
| Skill | Description / Usage |
| :--- | :--- |
| `data-engineer` | Build scalable data pipelines, modern data warehouses, and real-time streaming architectures. |
| `data-engineering-data-pipeline` | You are a data pipeline architecture expert specializing in scalable, reliable, and cost-effective data pipelines for... |
| `data-engineering-data-driven-feature` | Build features guided by data insights, A/B testing, and continuous measurement using specialized agents for analysis... |
| `data-quality-frameworks` | Implement data quality validation with Great Expectations, dbt tests, and data contracts. |
| `data-storytelling` | Transform data into compelling narratives using visualization, context, and persuasive structure. |
| `database-architect` | Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and ... |
| `database-admin` | Expert database administrator specializing in modern cloud databases, automation, and reliability engineering. |
| `database-optimizer` | Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. |
| `sql-optimization-patterns` | Master SQL query optimization, indexing strategies, and EXPLAIN analysis to dramatically improve database performance... |
| `database-migration` | Execute database migrations across ORMs and platforms with zero-downtime strategies, data transformation, and rollbac... |
| `database-migrations-sql-migrations` | SQL database migrations with zero-downtime strategies for PostgreSQL, MySQL, SQL Server. |
| `database-migrations-migration-observability` | Migration monitoring, CDC, and observability infrastructure. |
| `database-cloud-optimization-cost-optimize` | You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performan... |
| `postgresql` | Design a PostgreSQL-specific schema. |
| `sql-pro` | Master modern SQL with cloud-native databases, OLTP/OLAP optimization, and advanced query techniques. |
| `dbt-transformation-patterns` | Master dbt (data build tool) for analytics engineering with model organization, testing, documentation, and increment... |
| `spark-optimization` | Optimize Apache Spark jobs with partitioning, caching, shuffle optimization, and memory tuning. |

---

### 🏗️ Architecture, Code Quality & Output
| Skill | Description / Usage |
| :--- | :--- |
| `architect-review` | Master software architect specializing in modern architecture patterns, clean architecture, microservices, event-driv... |
| `architecture-patterns` | Implement proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Drive... |
| `codebase-design` | Shared vocabulary for designing deep modules. |
| `code-review` | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes — Standards (does the code... |
| `code-refactoring-refactor-clean` | You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software e... |
| `codebase-cleanup-refactor-clean` | You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software e... |
| `improve-codebase-architecture` | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one y... |
| `domain-modeling` | Build and sharpen a project's domain model. |
| `full-output-enforcement` | Overrides default LLM truncation behavior, enforcing complete unabridged code generation. |

---

### 🔬 Research, Debugging, Observability & Workflow
| Skill | Description / Usage |
| :--- | :--- |
| `last30days` | Grounded multi-source research aggregating Reddit, X, YouTube, TikTok, and Hacker News trends. |
| `graphify` | Local AST parser converting codebases, docs, and schemas into queryable knowledge graphs. |
| `agent-browser` | Browser automation CLI for live website interaction, form filling, automated testing, and web data extraction. |
| `find-skills` | Meta-skill to discover, search, and install new skills across the ecosystem. |
| `claude-hub` | Bridge AI agents with GitHub repositories, issues, pull requests, and automated release workflows. |
| `diagnosing-bugs` | Diagnosis loop for hard bugs and performance regressions. |
| `sentry-fix-issues` | Automated Sentry issue investigation and bug fixing via MCP. |
| `research` | Conduct preliminary research on a topic and generate research outline. |
| `research-add-fields` | Add field definitions to existing research outline. |
| `research-add-items` | Add items (research objects) to existing research outline. |
| `research-deep` | Read research outline, launch independent agent for each item for deep research. |
| `research-report` | Summarize deep research results into markdown report, cover all fields, skip uncertain values. |
| `grilling` | Grill the user relentlessly about a plan, decision, or idea. |
| `grill-me` | A relentless interview to sharpen a plan or design. |
| `grill-with-docs` | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| `defuddle` | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. |
| `handoff` | Compact the current conversation into a handoff document for another agent to pick up. |
| `teach` | Teach the user a new skill or concept, within this workspace. |
| `skill-creator` | Guide for creating effective skills. |
| `api-design-principles` | Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight develo... |
| `api-documenter` | Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. |
| `api-testing-observability-api-mock` | You are an API mocking expert specializing in realistic mock services for development, testing, and demos. |

---

### 📓 Obsidian & Knowledge Management
| Skill | Description / Usage |
| :--- | :--- |
| `obsidian-markdown` | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific ... |
| `obsidian-bases` | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. |
| `obsidian-cli` | Interact with Obsidian vaults using the Obsidian CLI to read, create, search, and manage notes, tasks, properties, an... |
| `obsidian-workspace-sync` | Detects the existence of .code-workspace files in the project root, maps the developer workspace to the corresponding... |
| `json-canvas` | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. |

---

### 🛠️ Specialized Engineering & Compliance
| Skill | Description / Usage |
| :--- | :--- |
| `airflow-dag-patterns` | Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment. |
| `code-documentation-doc-generate` | You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. |
| `content-marketer` | Elite content marketing strategist specializing in AI-powered content creation, omnichannel distribution, SEO optimiz... |
| `legal-advisor` | Draft privacy policies, terms of service, disclaimers, and legal notices. |
| `gdpr-data-handling` | Implement GDPR-compliant data handling with consent management, data subject rights, and privacy by design. |
| `pci-compliance` | Implement PCI DSS compliance requirements for secure handling of payment card data and payment systems. |
| `business-analyst` | Master modern business analysis with AI-powered analytics, real-time dashboards, and data-driven insights. |
| `kpi-dashboard-design` | Design effective KPI dashboards with metrics selection, visualization best practices, and real-time monitoring patterns. |
| `hybrid-cloud-networking` | Configure secure, high-performance connectivity between on-premises infrastructure and cloud platforms using VPN and ... |
| `ios-developer` | Develop native iOS applications with Swift/SwiftUI. |
| `unity-ecs-patterns` | Master Unity ECS (Entity Component System) with DOTS, Jobs, and Burst for high-performance game development. |

---

### 🤖 Dedicated Subagents (`.agents/agents/`)
| Agent Profile | Focus & Specialization |
| :--- | :--- |
| `architect-agent` | Domain-Driven Design (DDD), Clean Architecture, DB schemas, and OpenAPI contracts. |
| `backend-agent` | Async APIs (FastAPI/Node.js), database repositories, connection pooling, and AI/ML pipelines. |
| `frontend-agent` | React 19 / Next.js 15, anti-slop visual styling, design tokens, and physics-based motion. |
| `qa-docs-agent` | Test suite generation, edge case validation, OpenAPI docs, and top-level docstrings. |
| `web-search-agent` | Creative query generation, multi-source exploration (GitHub Issues, Reddit, arXiv, Tech forums). |

---

> [!TIP]
> Use composite calling commands like `"/call-feature"`, `"/call-front"`, `"/call-backend"`, `"/call-ai-ml"`, or `"/call-arch"` to load an entire suite of skills in a single prompt!
