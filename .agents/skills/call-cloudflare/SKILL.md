---
name: call-cloudflare
description: Composite bundler skill activating Cloudflare ecosystem skills. Use when developing Workers, Durable Objects, Pages, Zero Trust security, Turnstile verification, or Wrangler configurations.
---

# 🚀 Composite Skill: Cloudflare Serverless Edge & Infrastructure (`/call-cloudflare`)

This composite skill commands the full Cloudflare edge ecosystem: Workers, Durable Objects, Agents SDK, Sandbox SDK, Storage (D1, KV, R2, Vectorize), Zero Trust security, and Wrangler configuration.

---

## 📦 Bundled Skills & Deep References

When detailed implementation schemas, Wrangler bindings, or specialized APIs are required, read the corresponding skill using `view_file`:

| Skill | Path | Focus & On-Demand Capabilities |
| :--- | :--- | :--- |
| **`/cloudflare`** | `.agents/skills/cloudflare/SKILL.md` | Workers, Pages, D1, KV, R2, Vectorize, Hyperdrive |
| **`/agents-sdk`** | `.agents/skills/agents-sdk/SKILL.md` | Cloudflare Agents SDK, stateful agents, WebSocket chat |
| **`/durable-objects`** | `.agents/skills/durable-objects/SKILL.md` | State coordination, SQLite in DO, alarms, RPC methods |
| **`/sandbox-sdk`** | `.agents/skills/sandbox-sdk/SKILL.md` | Sandboxed untrusted code execution & container environments |
| **`/cloudflare-email-service`** | `.agents/skills/cloudflare-email-service/SKILL.md` | Transactional email sending, routing, SPF/DKIM/DMARC |
| **`/cloudflare-one`** | `.agents/skills/cloudflare-one/SKILL.md` | Zero Trust Access, Gateway, WARP, Tunnel & SASE |
| **`/cloudflare-one-migrations`**| `.agents/skills/cloudflare-one-migrations/SKILL.md`| Migrations from Zscaler, Palo Alto, legacy VPN |
| **`/turnstile-spin`** | `.agents/skills/turnstile-spin/SKILL.md` | Bot verification widget & server-side siteverify |
| **`/workers-best-practices`** | `.agents/skills/workers-best-practices/SKILL.md` | Async handlers, streaming, execution context invariants |
| **`/wrangler`** | `.agents/skills/wrangler/SKILL.md` | Wrangler CLI commands, `wrangler.jsonc`, secret management |
| **`/web-perf`** | `.agents/skills/web-perf/SKILL.md` | Edge latency, Core Web Vitals, caching headers |

---

## ⚡ Core Directives & Playbook (Fast Path)

When `/call-cloudflare` is invoked, strictly adhere to these edge development standards:

### 1. Worker Lifecycle & Binding Rules
- **No Global Mutable State**: Never store request-specific state in global variables. Worker instances are reused across requests.
- **Exported Handler Pattern**: Always use ESM module syntax (`export default { async fetch(request, env, ctx) { ... } }`).
- **Background Tasks**: Use `ctx.waitUntil(promise)` for non-blocking side-effects (e.g. logging, analytics) to return responses immediately.

### 2. Durable Objects & Agents SDK
- **Durable Object SQLite Storage**: Use the embedded SQLite database (`this.ctx.storage.sql.exec(...)`) for structured state within DOs.
- **RPC Communication**: Use direct RPC method calls on Durable Object stubs rather than serializing manual HTTP request payloads.
- **Alarms**: Use `this.ctx.storage.setAlarm(timestamp)` for scheduled self-wakeups and durable queues.

### 3. Edge Storage Selection
- **KV**: Read-heavy, globally cached key-value data with eventual consistency.
- **D1**: Relational transactional SQL at the edge.
- **R2**: Large asset/blob storage without egress fees.
- **Vectorize**: High-speed vector similarity indexing for edge RAG pipelines.

### 4. Wrangler Configuration Best Practices
- Prefer modern `wrangler.jsonc` (JSON with comments) over legacy `wrangler.toml`.
- Keep environment bindings, compatibility flags, and migration tags clearly declared.

---

## ⚡ Execution Workflow

1. **Architecture & Bindings**: Identify required Cloudflare primitives (Workers, DO, D1, KV, Vectorize).
2. **Implementation**: Write ESM Worker code, implement DO RPC methods, or configure Turnstile/Access policies.
3. **Local Dev & Testing**: Validate locally with `wrangler dev` and automated tests using `@cloudflare/vitest-pool-workers`.
