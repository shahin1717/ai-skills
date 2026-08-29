---
name: claude-hub
description: Bridge AI agents with GitHub repositories, issues, pull requests, and automated release workflows. Use when creating PRs, managing issues, reviewing git history, or automating GitHub CI/CD actions.
---

# 🐙 Claude Hub: GitHub Repository & Issue Management (`/claude-hub`)

This skill equips agents with expert capabilities to interact with GitHub repositories, draft structured pull requests, manage issue backlogs, and automate CI/CD workflows.

---

## ⚡ Directives & Workflows

### 1. Pull Request (PR) Crafting
- Generate clean, standardized PR descriptions containing:
  - **Summary**: Concise explanation of changes.
  - **Motivation / Context**: Why the change was made and which issue it addresses.
  - **Key Changes**: Bulleted list of architectural and implementation diffs.
  - **Testing & Verification**: Exact commands run and test verification results.

### 2. Issue Triage & Management
- Parse and classify GitHub issues by priority and component.
- Reproduce reported bugs before attempting fixes.
- Generate reproduction steps and root-cause analysis in comments.

### 3. Git Worktree & Branch Management
- Create isolated development branches using conventional naming:
  - `feat/<feature-name>`
  - `fix/<bug-description>`
  - `refactor/<module-name>`
- Maintain a clean commit history with atomic, descriptive messages.
