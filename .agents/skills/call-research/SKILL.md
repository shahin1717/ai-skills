---
name: call-research
description: Composite bundler skill activating research, web extraction, and synthesis skills. Use when performing deep technical research, extracting markdown documentation, or generating research outlines and reports.
---

# 🚀 Composite Skill: Deep Research, Web Extraction & Technical Synthesis (`/call-research`)

This composite skill executes end-to-end research pipelines by pairing high-speed inlined directives with on-demand access to specialized research skills.

---

## 📦 Bundled Skills & Deep References

When deep schemas, batch configs, or specific sub-workflows are required, read the corresponding skill using `view_file`:

| Skill | Path | Focus & On-Demand Capabilities |
| :--- | :--- | :--- |
| **`/last30days`** | `.agents/skills/last30days/SKILL.md` | Grounded multi-source research aggregating Reddit, X, YouTube, HN trends |
| **`/graphify`** | `.agents/skills/graphify/SKILL.md` | Local AST parser converting codebases, docs, and schemas into knowledge graphs |
| **`/agent-browser`** | `.agents/skills/agent-browser/SKILL.md` | Browser automation CLI for live site testing and data extraction |
| **`/find-skills`** | `.agents/skills/find-skills/SKILL.md` | Meta-skill to discover and install new skills across the ecosystem |
| **`/claude-hub`** | `.agents/skills/claude-hub/SKILL.md` | Bridge AI agents with GitHub repositories, issues, PRs, and actions |
| **`/skill-creator`** | `.agents/skills/skill-creator/SKILL.md` | Procedural framework for creating, validating, and packaging agent skills |
| **`/grill-me`** | `.agents/skills/grill-me/SKILL.md` | Relentless interview to sharpen plans, stress-test ideas, and eliminate blindspots |
| **`/research`** | `.agents/skills/research/SKILL.md` | 5-step research lifecycle, `outline.yaml` & `fields.yaml` schemas |
| **`/defuddle`** | `.agents/skills/defuddle/SKILL.md` | Token-efficient web extraction CLI (`defuddle parse <url> --md`) |
| **`/research-add-fields`** | `.agents/skills/research-add-fields/SKILL.md` | Expanding taxonomy and multi-tier field definitions |
| **`/research-add-items`** | `.agents/skills/research-add-items/SKILL.md` | Supplementing research objects, vendors, or technology targets |
| **`/research-deep`** | `.agents/skills/research-deep/SKILL.md` | Parallelized deep research execution per item |
| **`/research-report`** | `.agents/skills/research-report/SKILL.md` | Synthesis into structured markdown reports without unverified claims |
| **`/grill-with-docs`** | `.agents/skills/grill-with-docs/SKILL.md` | Interrogating architectural assumptions against documentation |
| **`/data-storytelling`** | `.agents/skills/data-storytelling/SKILL.md` | Executive synthesis, visual comparisons, and data narratives |

---

## ⚡ Core Directives & Playbook (Fast Path)

When `/call-research` is invoked, execute the following standardized workflow:

### 1. Research Scope & Taxonomy Setup
1. **Identify Entities**: Brainstorm domain entities/technologies/benchmarks.
2. **Define Field Dimensions**: Group dimensions by detail level:
   - `brief`: High-level summary, origin, license, primary use-case.
   - `moderate`: Key architecture, performance benchmarks, feature matrices.
   - `detailed`: Internal implementation mechanics, edge cases, pricing/operational caveats.

### 2. High-Efficiency Web Extraction
- For URL analysis, strip ads and boilerplate to maximize token efficiency:
  ```bash
  defuddle parse <url> --md -o content.md
  ```
- Use `search_web` for real-time queries and recent technical documentation.
- Maintain source attribution with explicit links.

### 3. File Artifacts Generation
Generate the structured research framework in the working directory:
- **`outline.yaml`**:
  ```yaml
  topic: "Topic Name"
  items:
    - name: "Item 1"
      description: "Summary and justification"
  execution:
    batch_size: 3
    items_per_agent: 1
    output_dir: "./results"
  ```
- **`fields.yaml`**:
  ```yaml
  fields:
    - name: "Architecture"
      description: "Underlying engine and design patterns"
      detail_level: "detailed"
    - name: "Performance"
      description: "Latency and throughput characteristics"
      detail_level: "moderate"
  uncertain: []
  ```

### 4. Synthesis & Executive Reporting
- Consolidate deep findings into an executive markdown report (`research_report.md`).
- Use side-by-side markdown comparison tables.
- Clearly omit or flag unverified claims (`uncertain` status).

---

## ⚡ Execution Workflow

1. **Integrated Analysis**: Parse user topic, establish research goals, and determine depth level.
2. **Schema & Extraction**: Populate `outline.yaml` and `fields.yaml`, then extract web documentation via `defuddle` / search tools.
3. **Synthesis & Verification**: Compile findings, check claims against primary sources, and output executive findings.
