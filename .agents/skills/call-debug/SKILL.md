---
name: call-debug
description: Composite bundler skill activating debugging and observability skills. Use when investigating hard runtime bugs, fixing Sentry errors, diagnosing performance bottlenecks, or reviewing broken tests.
---

# 🚀 Composite Skill: Deep Bug Diagnosis, Performance & Triage (`/call-debug`)

This composite skill executes systematic root-cause diagnosis, error stack trace analysis (Sentry), web performance debugging, and regression testing.

---

## 📦 Bundled Skills & Deep References

When detailed triage methodologies, observability recipes, or specific testing frameworks are required, read the corresponding skill using `view_file`:

| Skill | Path | Focus & On-Demand Capabilities |
| :--- | :--- | :--- |
| **`/diagnosing-bugs`** | `.agents/skills/diagnosing-bugs/SKILL.md` | Scientific bug diagnosis loop, hypothesis testing |
| **`/sentry-fix-issues`** | `.agents/skills/sentry-fix-issues/SKILL.md` | Sentry stack trace parsing, breadcrumbs & release context |
| **`/web-perf`** | `.agents/skills/web-perf/SKILL.md` | Chrome DevTools profiling, Core Web Vitals, render bottlenecks |
| **`/python-testing-patterns`** | `.agents/skills/python-testing-patterns/SKILL.md` | `pytest` reproduction test cases, fixture isolation |
| **`/api-testing-observability-api-mock`** | `.agents/skills/api-testing-observability-api-mock/SKILL.md` | Mocking flaky dependencies to isolate deterministic bugs |
| **`/grilling`** | `.agents/skills/grilling/SKILL.md` | Rigorous interrogation of assumptions and edge cases |
| **`/code-review`** | `.agents/skills/code-review/SKILL.md` | Dual-axis review to check spec conformance and standards |

---

## ⚡ Core Directives & Playbook (Fast Path)

When `/call-debug` is invoked, execute the following 4-phase diagnosis loop:

### 1. Phase 1: Deterministic Reproduction
- **Never guess or patch blind**: Before writing any fix, write a minimal failing test case or reproducible script that reliably reproduces the exact bug.
- **Trace Boundaries**: Inspect request payloads, inputs, database state, and environment variables leading up to the failure.

### 2. Phase 2: Root-Cause Isolation
- **Inspect Stack Traces & Breadcrumbs**:
  - Distinguish root exceptions from wrapped/cascading errors.
  - Check asynchronous context propagation, unhandled promise rejections, and silent exception swallowing.
- **Inspect State Mutations**: Identify race conditions, shared mutable state across requests/threads, or unindexed database queries timing out.

### 3. Phase 3: Surgical Fix & Defensive Hardening
- **Target the Root Cause**: Fix the actual defect at its source rather than adding superficial null-checks or blanket `try...catch` blocks.
- **Enforce Invariants**: Add assertions, type guards, or input validation to make the invalid state impossible to enter again.

### 4. Phase 4: Verification & Anti-Regression
- Run the previously failing test to prove it now passes.
- Run the full test suite to guarantee zero regressions.
- Verify that performance, memory usage, and latency remain within acceptable thresholds.

---

## ⚡ Execution Workflow

1. **Information Gathering**: Collect logs, stack traces, reproduction steps, and system context.
2. **Reproduction & Root Cause**: Create a minimal reproducing test case and isolate the underlying mechanism.
3. **Surgical Fix & Proof**: Apply the targeted fix, run all test suites, and provide an explanation of the root cause and resolution.
