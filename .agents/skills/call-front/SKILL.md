---
name: call-front
description: Composite bundler skill activating all frontend and design skills. Use when building React/Next.js UI, crafting high-end visual aesthetics, designing responsive layouts, or implementing web motion and animations.
---

# 🚀 Composite Skill: Frontend, UI/UX Design, Motion & Aesthetics (`/call-front`)

This composite skill drives world-class frontend engineering, Next.js 15/React 19 architecture, anti-slop visual design systems, fluid physics-based motion, and responsive component libraries.

---

## 📦 Bundled Skills & Deep References

When specialized design systems, motion physics formulas, or specific UI frameworks are required, read the corresponding skill using `view_file`:

| Skill | Path | Focus & On-Demand Capabilities |
| :--- | :--- | :--- |
| **`/frontend-developer`** | `.agents/skills/frontend-developer/SKILL.md` | React 19, client state management, responsive UI |
| **`/nextjs-app-router-patterns`** | `.agents/skills/nextjs-app-router-patterns/SKILL.md` | Next.js 15 App Router, Server Components, Streaming |
| **`/impeccable`** | `.agents/skills/impeccable/SKILL.md` | Visual hierarchy, cognitive load, typography & design polish |
| **`/emil-design-eng`** | `.agents/skills/emil-design-eng/SKILL.md` | Emil Kowalski motion details, micro-interactions |
| **`/apple-design`** | `.agents/skills/apple-design/SKILL.md` | Apple fluid motion, spring curves, materials & depth |
| **`/design-taste-frontend`** | `.agents/skills/design-taste-frontend/SKILL.md` | Anti-slop frontend design, non-templated interfaces |
| **`/gpt-taste`** | `.agents/skills/gpt-taste/SKILL.md` | GSAP scroll triggers, bento grids, editorial typography |
| **`/high-end-visual-design`** | `.agents/skills/high-end-visual-design/SKILL.md` | Agency-grade shadows, spacing, glassmorphism |
| **`/industrial-brutalist-ui`**| `.agents/skills/industrial-brutalist-ui/SKILL.md` | Swiss typography, terminal aesthetics, rigid data grids |
| **`/minimalist-ui`** | `.agents/skills/minimalist-ui/SKILL.md` | Warm monochrome palettes, flat bento grids |
| **`/stitch-design-taste`** | `.agents/skills/stitch-design-taste/SKILL.md` | Semantic Design System tokens & layout variance |
| **`/brandkit`** | `.agents/skills/brandkit/SKILL.md` | Visual identity boards, logos, dark-tech palettes |
| **`/image-to-code`** | `.agents/skills/image-to-code/SKILL.md` | Pixel-accurate reproduction of visual design mockups |
| **`/animate`** | `.agents/skills/animate/SKILL.md` | Motion implementation, exit transitions, spring physics |
| **`/animation-vocabulary`** | `.agents/skills/animation-vocabulary/SKILL.md` | Motion lexicon (pop-in, rubber-banding, layout morph) |
| **`/web-perf`** | `.agents/skills/web-perf/SKILL.md` | Core Web Vitals (LCP, INP, CLS), render optimization |

---

## ⚡ Core Directives & Playbook (Fast Path)

When `/call-front` is invoked, strictly adhere to these design and engineering standards:

### 1. Anti-Slop Visual Hierarchy & Aesthetics
- **Banned**: Generic pure primaries (e.g. `#FF0000`, `#0000FF`), generic unstyled cards, bootstrap-like defaults.
- **Enforced**:
  - Curated, rich palettes (e.g. deep slate `#0B0F19`, zinc `#18181B`, emerald/indigo/violet accents).
  - Modern typography hierarchy (e.g. `Outfit`, `Inter`, `Plus Jakarta Sans`) with tight tracking on headings (`tracking-tight`).
  - Subtle depth via multi-layered shadows and subtle borders (`border border-white/10`).

### 2. Next.js 15 & React 19 Architecture
- **Server Components by Default**: Fetch data and render on the server. Add `'use client'` only where user interactivity, browser hooks, or animations require it.
- **Suspense & Streaming**: Wrap async component boundaries in `<Suspense fallback={<Skeleton />}>` to avoid blocking initial render.

### 3. Motion & Micro-Interactions
- **Natural Springs & Curves**: Use fluid cubic-bezier curves (e.g. `cubic-bezier(0.16, 1, 0.3, 1)`) for UI transitions.
- **Zero Layout Shift (CLS = 0)**: Animate only composite properties (`transform`, `opacity`, `filter`). Never animate `width`, `height`, `margin`, or `top` directly.

### 4. Zero Placeholders
- Build working, interactive UI states (empty states, active states, loading skeletons, error states). Never leave `[TODO: Insert Image Here]`.

---

## ⚡ Execution Workflow

1. **Design Foundation**: Establish color tokens, typography, layout grid, and component hierarchy.
2. **Component Implementation**: Build accessible, type-safe React/Next.js components with fluid hover and transition states.
3. **Motion Polish & Performance**: Add micro-interactions, verify responsiveness on mobile/desktop, and check Core Web Vitals.
