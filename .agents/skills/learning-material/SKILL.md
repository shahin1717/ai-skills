---
name: learning-material
description: Write learning materials (lessons, course notes, study guides, chapters, cheat sheets, exercises) in Markdown or LaTeX that are clear, well-structured, and pleasant to read, on any subject. Use when asked to write or improve teaching or self-study content, a course/roadmap topic, lecture notes, or a LaTeX handout. Not for API or code documentation (use call-doc for that).
---

# Learning Material Writing

Write material a learner can read once and come away understanding. The reader is a student, not a maintainer: optimise for understanding and retention, not completeness.

## 1. Before writing

1. **Read the house rules.** Look for `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, design notes, templates, or scaffolding scripts in the target repo, and read two or three existing pages. Their structure, tone, file layout and math conventions override everything below.
2. **Pin down the brief.** Audience and level, prerequisites, format (`.md` or `.tex`), length, and where the file goes. If the repo or request answers these, don't ask. Ask only when a wrong guess would waste the whole piece.
3. **Ground the facts.** Don't trust memory for definitions, numbers, dates, formulas, API names or claims about papers. Check primary sources (official docs, textbooks, original papers) and keep the links for a "Further reading" section.
4. **Outline first.** Write learning objectives (3-5, phrased as things the reader can *do*: "compute", "explain why", "implement"), then a section outline. Each section teaches one idea.

## 2. How to teach on the page

- **Intuition, then formalism, then practice.** Start with a concrete example or picture, name the idea, then give the precise definition or formula, then use it.
- **Concrete before abstract.** Every abstract statement gets an example within a few lines.
- **Worked examples with every step shown**, including the boring arithmetic. Then a near-identical problem for the reader.
- **Explain why, not just what.** Each formula or rule answers "why does this work?" or "why do we need this?".
- **Name the misconceptions.** Add a short "Common mistake" where learners usually go wrong.
- **Connect.** Link back to prerequisites when you use them, and say where this idea is used later or in the real world.
- **One new concept at a time.** If a section needs two new ideas, split it.
- **Check understanding.** End major sections with 1-3 quick questions; put answers in a collapsible block.
- **Recap.** Close with a short summary of the key ideas (not a restatement of the intro) and what comes next.

Recommended page skeleton (adapt to house rules):

```
# Title
One-paragraph hook: what this is and why the reader should care.
## What you'll learn          (objectives)
## Prerequisites              (with links)
## <Concept sections>         (intuition -> definition -> worked example -> check)
## Common mistakes
## Summary
## Exercises                  (answers separate or collapsed)
## Further reading            (primary sources, free links)
```

## 3. Markdown that looks good everywhere

Target GitHub-flavoured Markdown unless told otherwise (it also renders in VS Code, Obsidian, and most viewers).

- **Headings:** one `#` title, then `##`/`###` only. No skipped levels. Headings say what the section teaches ("Why gradients point uphill"), not "Part 2".
- **Paragraphs:** 2-4 sentences. Lists only for genuinely list-shaped content; prose for reasoning.
- **Tables** for comparisons and properties. Keep cells short.
- **Callouts** with GitHub alerts, used sparingly (a few per page):
  `> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`.
- **Collapsible answers:** `<details><summary>Answer</summary> ... </details>` (leave a blank line after `<summary>` so Markdown inside renders).
- **Math:** `$...$` inline, `$$...$$` display. On GitHub, anything containing `\\` (matrices, `aligned`) goes in a ```` ```math ```` block, and inline math with tricky characters uses $`...`$.
- **Diagrams:** Mermaid code blocks (flowchart, sequence, graph) for structure; your own SVG/PNG in an `assets/` folder for anything else. Every figure gets a one-line caption saying what to notice.
- **Code:** always a language tag; runnable top to bottom; show expected output in a separate block; comment only the non-obvious.
- **Emphasis:** bold for a term at the point it is defined, and almost nowhere else. No emoji in headings unless house style uses them.
- **Links:** relative links for pages in the same repo; descriptive link text, never "click here".
- **Long pages** (more than ~6 sections) get a short table of contents after the hook.

## 4. LaTeX

Use when asked for `.tex`, a printable handout, lecture notes, or heavy math.

- `article` for notes/handouts, `book`/`report` for multi-chapter material, `beamer` for slides.
- Core packages: `amsmath, amssymb, amsthm, mathtools, hyperref, cleveref, csquotes, booktabs, graphicx, xcolor, tcolorbox, listings` (or `minted` if `-shell-escape` is available), `microtype`, `geometry`.
- Define and use semantic environments: `definition`, `theorem`, `example`, `remark`, `exercise` (via `amsthm` or `tcolorbox`); use a coloured `tcolorbox` for intuition/warning boxes.
- `description` for term-definition lists, `\enquote{}` for quotes, `\cref{}` for all references, `\label` on every numbered thing.
- Tables with `booktabs` (`\toprule`, `\midrule`, `\bottomrule`), no vertical rules. Every table and figure is a float with a caption.
- Macros for repeated notation (`\newcommand{\R}{\mathbb{R}}`), defined once in the preamble.
- Bibliography with `biblatex` + `biber` when sources are cited.
- **Compile it.** Run `latexmk -pdf` (or `-xelatex`) and fix all errors and overfull-box warnings before declaring done. If no TeX toolchain is installed, say so instead of claiming it compiles.

## 5. Originality and sources

- Write in your own words. Never copy or closely paraphrase textbook or course text; never paste third-party figures.
- Cite where facts and ideas come from in "Further reading", preferring free and legitimate links.

## 6. Finish

1. Run the `humanizer` pass over the prose: cut filler, stock AI phrasing, forced triads, and empty closers. Keep the meaning, formulas and code exactly.
2. Check against the list:
   - [ ] Objectives stated and actually met by the content
   - [ ] Every new term defined before use
   - [ ] Every abstract idea has a concrete example
   - [ ] Math renders (check `\\` rule) / LaTeX compiles cleanly
   - [ ] Code runs; outputs shown
   - [ ] Links work and are relative inside the repo
   - [ ] House rules from `CLAUDE.md` / templates followed
   - [ ] Repo checks run if the project has them (e.g. a `scripts/check_*.py`)
3. Report what you wrote, where, and anything you could not verify.
