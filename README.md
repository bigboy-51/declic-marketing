# Declic Marketing

Marketing, branding, copywriting, and content skills for Declic Financier.

Built with **Karpathy-style pedagogy**: Think deeply, simplify ruthlessly, make surgical changes, measure results, verify before responding.

## Skills (12 Total)

**Core Marketing:**
1. **Copywriting** — High-converting sales copy, emails, ads
2. **Branding** — Brand identity, tone, visual guidelines
3. **Blogging** — Long-form content, SEO, authority
4. **YouTube Script** — Video scripts, editing, AIO/AEO/GEO optimization
5. **SEO/AIO** — AI-era visibility: Google + ChatGPT + Perplexity + Claude
6. **Design** — Visual systems, design principles, assets

**Growth & Conversion:**
7. **Thumbnails & Visual Assets** — High-CTR thumbnails (YouTube, social, blog), psychology-driven
8. **Hooks** — Psychological openings across all formats (video, copy, email, blog) 🆕
9. **Lead Magnets** — Quizzes, giveaways, webinars, calculators, ebooks (+40% conversion)
10. **Closer** — Email sequences, call scripts, objection handling
11. **Funnel** — Marketing funnel strategy, conversion optimization

**Strategy:**
12. **Product Emergence** — Ikigai + JTBD validation, MVP definition, go-to-market (5-phase)

## Getting Started

Each skill is a directory with a `SKILL.md` file containing:
- **Purpose**: What the skill does
- **Framework**: The approach (before/during/after)
- **Quality checklist**: How to validate work
- **Common mistakes**: What to avoid
- **Success metrics**: How to measure

## Using These Skills

Invoke a skill when its domain matches your task:

```
"I need copywriting for our landing page"
→ Uses: /copywriting skill
→ Returns: Copy framework, examples, metrics

"Design our new dashboard"
→ Uses: /design skill
→ Returns: Design system, components, specs
```

## Agent SDK (Phase 1 MVP ✅)

**Status:** Fully implemented and tested  
**Agents:** 5 (Orchestration + 3 Skill Agents + Coherence)  
**Execution time:** ~60 seconds per campaign

**Architecture:**
```
User Request → Orchestration Agent → Skill Agents → Coherence Check → Output
```

**Get started:**
- **Visual Dashboard** (Recommended): `streamlit run dashboard.py` → http://localhost:8501
- **CLI Demo**: `python main.py`
- **Interactive Mode**: `python main.py interactive`

See `AGENTS.md` for architecture, `AGENTS_IMPLEMENTATION.md` for Phase 1 details, `DASHBOARD.md` for UI guide.

## Principles

These skills follow **5 pillars**:

1. **Think Before Coding** — Analyze deeply before proposing
2. **Simplicity First** — Reject over-engineering
3. **Surgical Changes** — Precise, intentional modifications
4. **Goal-Driven Execution** — Measurable success criteria
5. **Verification/Challenge** — Question every proposal

See `CLAUDE.md` for full details.

## Structure

```
declic-marketing/
├── CLAUDE.md (5 pillars, operating principles)
├── AGENTS.md (Agent SDK architecture)
├── AGENTS_IMPLEMENTATION.md (Phase 1 MVP details)
├── DASHBOARD.md (Visual interface guide)
├── README.md (this file)
├── main.py (CLI demo + interactive mode)
├── dashboard.py (Streamlit visual interface)
├── agents/ (Agent SDK implementation)
│   ├── orchestration_agent.py
│   ├── skill_agents/ (copywriting, blogging, youtube)
│   └── utility_agents/ (coherence verification)
└── .claude/skills/ (12 comprehensive frameworks)
    ├── copywriting/SKILL.md
    ├── branding/SKILL.md
    ├── blogging/SKILL.md
    ├── youtube-script/SKILL.md
    ├── seo-aio/SKILL.md
    ├── design/SKILL.md
    ├── thumbnails/SKILL.md
    ├── hooks/SKILL.md 🆕
    ├── lead-magnets/SKILL.md
    ├── closer/SKILL.md
    ├── funnel/SKILL.md
    └── product-emergence/SKILL.md
```

## Next: Agent SDK

Once these skills are validated, they'll be wrapped into **Agent SDK** for:
- Autonomous marketing campaigns
- Multi-step content production
- Funnel optimization loops
- Team coordination

## Reference

- [Karpathy on software engineering](https://github.com/multica-ai/andrej-karpathy-skills)
- [Claude Code skills documentation](https://code.claude.com/docs/en/skills)
- [Declic Financier](https://github.com/bigboy-51/declic-financier)
