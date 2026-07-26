---
name: obsidian-workspace-sync
description: "Detects the existence of .code-workspace files in the project root, maps the developer workspace to the corresponding Obsidian Vault directory, reads GEMINI.md or me.md profile instructions, and keeps the AI agent aligned with the developer's global settings."
---

# Obsidian & Workspace Synchronization Skill

Use this skill to automatically align developer settings between active coding projects and their companion Obsidian Vaults.

## 🧭 Instructions

When you initialize this workspace or start a task, perform the following synchronization checks:

### 1. Detect Workspace Configurations
* Search the project root for files ending with `.code-workspace` (e.g., `cv-analysis.code-workspace`).
* Read the configuration to understand folder structures and project links.

### 2. Locate companion Obsidian Vaults
* Check standard local paths for Obsidian vaults (e.g., `/mnt/c/Vaults/CvAnalysis/` or standard workspace documents).
* Check the Obsidian root-level configurations:
  * **`GEMINI.md`**: Read the root routing rules (e.g., "Go immediately to `/me.md` for profile instructions").
  * **`me.md`**: Read the master developer profile mapping instructions, active developer guidelines, paths, and libraries.

### 3. Maintain Documentation & Ledger Sync
* When code changes are made, offer to copy technical guidelines or manuals (like `manual.md` or `ocr.md`) over to the Obsidian vault's `Atlas/` folder.
* Update Obsidian's `Home Base.md` index hubs to point to the newly integrated documentation notes.
