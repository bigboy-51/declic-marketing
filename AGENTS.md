# Declic Marketing: Agent SDK Architecture

This document defines the complete Agent SDK system for automating and orchestrating the 8 marketing skills into autonomous workflows.

---

## The Agent Hierarchy

```
┌──────────────────────────────────────┐
│     Orchestration Agent              │
│     (Master Coordinator)             │
│     - Receives user requests         │
│     - Plans workflow                 │
│     - Delegates to skill agents      │
│     - Compiles final output          │
└──────────────┬───────────────────────┘
               │
      ┌────────┴────────┬────────┬──────┬────────┬──────────┬────────┐
      │                 │        │      │        │          │        │
      ▼                 ▼        ▼      ▼        ▼          ▼        ▼
  Branding         Copywriting Blogging SEO/AIO YouTube   Thumbnails Funnel
  Agent            Agent       Agent    Agent    Agent     Agent      Agent
  (Voice,          (Text       (Long-   (Google  (Hooks,   (CTR,      (Conv-
   Identity)       Copy)       form)    +AI)     Scripts)  Psychology) ersion)
      │                 │        │      │        │          │        │
      └────────┬────────┴────────┴──────┴────────┴──────────┴────────┘
               │
      ┌────────▼────────┬─────────────┬──────────────┐
      │                 │             │              │
      ▼                 ▼             ▼              ▼
  Coherence Agent   Design Agent   Metrics Agent   Optimization Agent
  (Verification)    (Visuals)      (Tracking)      (Testing)
```

---

## Agent Definitions

### 1. Orchestration Agent (Master)

**Role:** Receive user requests, plan workflows, delegate to skill agents, compile outputs.

**Capabilities:**
- Understand campaign briefs
- Plan multi-step workflows
- Call other agents in optimal order
- Aggregate outputs into final deliverables
- Handle failures and revisions

**Input:** 
```
"Campaign: Make $50K passive income - target: busy professionals"
```

**Output:**
```
Coordinated campaign package:
- Blog post
- YouTube script
- Thumbnails
- Email sequence
- Design assets
- Funnel setup
- Metrics report
```

**Decision Logic:**
```
IF request type = "Campaign launch":
  1. Call Branding Agent (define voice)
  2. Call Copywriting Agent (headlines)
  3. Call Blogging Agent (content)
  4. Call SEO/AIO Agent (optimization)
  5. Call YouTube Agent (scripts)
  6. Call Thumbnails Agent (images)
  7. Call Funnel Agent (conversion)
  8. Call Design Agent (visuals)
  9. Call Coherence Agent (verify)
  10. Call Metrics Agent (setup tracking)

ELSE IF request type = "Optimize funnel":
  1. Call Metrics Agent (analyze current)
  2. Call Funnel Agent (identify leak)
  3. Call relevant skill agents (fix it)
  4. Call Optimization Agent (A/B test)

ELSE IF request type = "Test hypothesis":
  1. Call Optimization Agent (design test)
  2. Call relevant skill agents (generate variants)
  3. Call Metrics Agent (measure)
```

---

### 2. Branding Agent

**Role:** Define and maintain brand voice, positioning, visual identity.

**Uses Skill:** Branding

**Capabilities:**
- Define voice and tone
- Establish color palette
- Set visual guidelines
- Ensure brand consistency
- Provide style guide to other agents

**Input:** 
```
Campaign brief + Target audience
"50K passive income + busy professionals"
```

**Output:**
```
{
  "voice": "professional, approachable, direct",
  "colors": {
    "primary": "#2563EB (trust)",
    "secondary": "#10B981 (growth)"
  },
  "key_message": "Clear is better than clever",
  "tone": "Expert but accessible"
}
```

**Interacts With:**
- Copywriting Agent (voice consistency)
- YouTube Agent (tone + pace)
- Design Agent (colors + fonts)
- Coherence Agent (verification)

---

### 3. Copywriting Agent

**Role:** Generate persuasive, high-converting copy.

**Uses Skill:** Copywriting (AIDA/PASTOR frameworks)

**Capabilities:**
- Write headlines
- Create email copy
- Craft CTAs
- Apply psychology principles
- A/B test variants

**Input:**
```
{
  "format": "sales_page_headline",
  "topic": "50K passive income portfolio",
  "brand_voice": "professional, direct",
  "target_emotion": "hope + clarity"
}
```

**Output:**
```
"How Busy Professionals Make $50K Passive Income (Without Daily Monitoring)"
```

**Interacts With:**
- Branding Agent (voice consistency)
- Blogging Agent (consistent messaging)
- YouTube Agent (hook alignment)
- Funnel Agent (message matches journey)

---

### 4. Blogging Agent

**Role:** Write SEO-optimized, long-form content.

**Uses Skill:** Blogging (EEAT + topical authority)

**Capabilities:**
- Structure articles (headers, bullets, summaries)
- Optimize for EEAT signals
- Create featured snippet-ready content
- Internal linking strategy
- Call-to-action integration

**Input:**
```
{
  "headline": "How Busy Professionals Make $50K Passive Income",
  "keyword": "passive income strategy",
  "length": 2000,
  "audience": "busy professionals",
  "brand_voice": "professional, direct"
}
```

**Output:**
```
2000-word article with:
- Clear H1-H3 hierarchy
- EEAT signals (credentials, data)
- Featured snippet-ready answers
- 3-5 internal links
- Brand-consistent CTA
```

**Interacts With:**
- SEO/AIO Agent (optimization)
- Copywriting Agent (headlines + CTAs)
- Design Agent (header image)
- Funnel Agent (email sequence)
- Metrics Agent (track views, time, engagement)

---

### 5. SEO/AIO Agent

**Role:** Optimize for Google + AI systems (Google, ChatGPT, Claude, Perplexity).

**Uses Skill:** SEO/AIO (AIO + AEO + GEO)

**Capabilities:**
- Add schema markup
- Optimize for AEO (answer engines)
- Ensure GEO (generative engine optimization)
- Structure for AI extraction
- Improve Core Web Vitals signals

**Input:**
```
{
  "content": "Blog article (2000 words)",
  "topic": "passive income strategy",
  "optimize_for": ["google", "chatgpt", "claude"]
}
```

**Output:**
```
{
  "schema_markup": "article + author + credentials",
  "aeo_optimized": "direct answer in first 100 words",
  "geo_optimized": "unique data + citable insights",
  "core_web_vitals": "LCP < 2.5s, CLS < 0.1"
}
```

**Interacts With:**
- Blogging Agent (content structure)
- YouTube Agent (transcript optimization)
- Metrics Agent (track AI visibility)

---

### 6. YouTube Agent

**Role:** Create video scripts optimized for retention and AI discovery.

**Uses Skill:** YouTube Script (hooks + AIO/AEO/GEO)

**Capabilities:**
- Write video scripts (with timings)
- Create attention-grabbing hooks
- Add AIO/AEO/GEO directives
- Generate thumbnail visual cues
- Structure for AI systems

**Input:**
```
{
  "blog_article": "How Busy Professionals Make $50K",
  "duration": "3-5 minutes",
  "hook_type": "curiosity_gap",
  "target_emotion": "shock + excitement",
  "aio_aeo_geo": true
}
```

**Output:**
```
Script with:
- 3-second hook (shock/excitement)
- Timestamps for every section
- Camera directions (if Higgsfield ready)
- Answer in first 30 seconds (AEO)
- Rewatch moments
- Clear CTAs
- Transcript-ready structure
```

**Interacts With:**
- Blogging Agent (content source)
- Thumbnails Agent (visual cues for frames)
- Copywriting Agent (hook messaging)
- Branding Agent (tone + pace)
- Metrics Agent (track retention, CTR, rewatches)

---

### 7. Thumbnails Agent

**Role:** Generate high-CTR thumbnails across platforms.

**Uses Skill:** Thumbnails & Visual Assets

**Capabilities:**
- Design custom thumbnails
- Generate AI variations (ThumbnailCreator)
- Platform-specific optimization
- Hybrid workflows (AI + design refinement)
- A/B test variants

**Input:**
```
{
  "platform": "youtube",
  "message": "50K passive income revealed",
  "emotion": "shock",
  "brand_colors": ["#2563EB", "#10B981"],
  "ai_generation": true
}
```

**Output:**
```
3 thumbnail variants (1280x720 PNG):
1. AI-generated (ThumbnailCreator)
2. Design-refined variation
3. Alternative message test

+ Platform variants:
- Instagram 1080x1350
- TikTok 1080x1920
- LinkedIn 1200x627
```

**Interacts With:**
- YouTube Agent (visual from script cues)
- Branding Agent (color compliance)
- Design Agent (style consistency)
- Metrics Agent (track CTR per variant)

---

### 8. Funnel Agent

**Role:** Design and optimize marketing funnels.

**Uses Skill:** Funnel (benchmarks, optimization loops)

**Capabilities:**
- Map customer journey (awareness → conversion)
- Set conversion targets
- Identify leaks
- Create optimization hypotheses
- A/B test variants

**Input:**
```
{
  "campaign": "50K passive income",
  "awareness_content": "blog + youtube",
  "consideration_content": "case studies + webinar",
  "decision_tactic": "free trial",
  "metrics_target": "3% overall conversion"
}
```

**Output:**
```
{
  "funnel_map": "Blog (500/mo) → YouTube (65% retention) → Email (8% signup) → Trial (12% conversion)",
  "leak_analysis": "Biggest leak: YouTube → Email (30%)",
  "optimization_priority": "Improve YouTube CTA messaging",
  "tracking_setup": "Pixels + UTM + email integrations"
}
```

**Interacts With:**
- All skill agents (content feeds funnel)
- Optimization Agent (test hypotheses)
- Metrics Agent (track conversions)

---

### 9. Design Agent

**Role:** Apply visual design system consistency.

**Uses Skill:** Design (WCAG + scalable systems)

**Capabilities:**
- Apply brand colors + fonts
- Create design assets
- Ensure WCAG compliance
- Maintain visual hierarchy
- Support all platforms

**Input:**
```
{
  "asset_type": "blog_header_image",
  "topic": "50K passive income",
  "brand_colors": ["#2563EB", "#10B981"],
  "text": "50K Passive Income Strategy"
}
```

**Output:**
```
Blog header image (1200x628 px):
- Brand colors (#2563EB + #10B981)
- Clear typography
- WCAG 4.5:1 contrast
- Mobile optimized
+ Email template
+ Social share variants
```

**Interacts With:**
- Branding Agent (design system)
- Blogging Agent (header images)
- YouTube Agent (thumbnail compatibility)
- Funnel Agent (landing page design)

---

### 10. Coherence Agent

**Role:** Verify all outputs are brand-consistent.

**Uses Skill:** All (cross-skill validation)

**Capabilities:**
- Check voice consistency
- Verify color usage
- Validate messaging alignment
- Flag inconsistencies
- Request revisions

**Input:**
```
All agent outputs (blog, script, thumbnails, email, design)
```

**Output:**
```
COHERENCE REPORT:
✅ Voice consistent (professional, direct) across all assets
✅ Colors match system (#2563EB primary, #10B981 secondary)
✅ Message aligned ("50K passive income" + "no daily monitoring")
✅ Audience targeted consistently (busy professionals)

OR

🔴 REVISION NEEDED:
- YouTube script tone too casual (should be professional)
- Email CTA color doesn't match design system
- Blog headline doesn't match YouTube hook
```

**Interacts With:**
- All skill agents (verification)

---

### 11. Metrics Agent

**Role:** Setup tracking, measure performance, report results.

**Capabilities:**
- Define success metrics
- Setup tracking (pixels, UTM, GA4)
- Measure funnel performance
- Alert on anomalies
- Provide optimization recommendations

**Input:**
```
Campaign outputs + success criteria
"Blog CTR > 3%, YouTube retention > 50%, Trial conversion > 12%"
```

**Output:**
```
METRICS SETUP:
- Blog: Track organic traffic, engagement time, conversions
- YouTube: Track CTR, watch time, retention %, rewatches
- Email: Track open rate, click rate, conversion rate
- Funnel: Track stages, drop-off points, overall conversion

WEEKLY REPORT:
Blog: 520 visits, 2:45 avg time, 4.2% CTR to YouTube
YouTube: 6.8% CTR, 58% retention at 60s, 8% rewatch rate
Email: 32% open, 4.2% click, 1.8% conversion to trial
Funnel: 0.8% → 0.35% → 0.042% (overall: 0.042%)

RECOMMENDATIONS:
"YouTube retention strong, but email → trial conversion low. Test new CTA wording."
```

**Interacts With:**
- All agents (tracking setup)
- Optimization Agent (data for testing)

---

### 12. Optimization Agent

**Role:** Autonomously test, measure, and improve (Karpathy-style).

**Uses Skill:** All (testing framework)

**Capabilities:**
- Design A/B tests (one variable only)
- Generate variants (using skill agents)
- Measure statistical significance
- Document learnings
- Iterate automatically

**Input:**
```
Current metrics + hypothesis
"YouTube CTR is 6.8%, target is 8%. Hypothesis: more shocked faces = higher CTR"
```

**Workflow:**
```
1. THINK: "Why is CTR below target? What could work?"
   → Hypothesis: Shocked faces drive higher CTR

2. SIMPLIFY: "Change one thing only"
   → Test: Current thumbnails vs. more shocked expressions

3. TEST: "Run for 100+ impressions minimum"
   → Call Thumbnails Agent to generate variant
   → Measure CTR for 2 weeks
   → Requires 100+ views for significance

4. VERIFY: "Did hypothesis prove true?"
   → Current CTR: 6.8%
   → Variant CTR: 7.9%
   → Result: +1.6% (statistically significant)

5. IMPLEMENT: "Roll out winner, document learning"
   → New thumbnail approach becomes standard
   → Document: "Shocked > Neutral expressions. Effect: +16% CTR"
   → Test next variable (color contrast)
```

**Interacts With:**
- All agents (generate test variants)
- Metrics Agent (measure results)

---

## Workflow Examples

### Example 1: Campaign Launch (One Request)

```
USER REQUEST:
"Launch campaign: How to build $50K portfolio - target: busy professionals"

ORCHESTRATION AGENT WORKFLOW:

Step 1: Plan
  - Type: Campaign launch
  - Duration: ~30 minutes
  - Agents needed: All 8 skill agents + Design + Coherence

Step 2: Execute
  - T+0: Call Branding Agent
    → Voice: "professional, direct", Colors: "#2563EB + #10B981"
  
  - T+2: Call Copywriting Agent
    → Headline: "How Busy Professionals Make $50K (Without Daily Monitoring)"
  
  - T+5: Call Blogging Agent
    → 2000-word article, EEAT signals, featured snippet ready
  
  - T+10: Call SEO/AIO Agent
    → Schema markup, AEO answers, GEO citations
  
  - T+12: Call YouTube Agent
    → 3-min script, 3-sec hook, AIO/AEO/GEO ready
  
  - T+15: Call Thumbnails Agent
    → 3 YouTube variants + platform variants (Instagram, TikTok, LinkedIn)
  
  - T+18: Call Funnel Agent
    → Blog → YouTube → Email → Trial (3% conversion target)
  
  - T+22: Call Design Agent
    → Blog header, email template, social share images
  
  - T+25: Call Coherence Agent
    → ✅ All aligned (voice, colors, message)
  
  - T+28: Call Metrics Agent
    → Tracking setup complete

Step 3: Deliver
  - Blog post (with SEO optimization + design assets)
  - YouTube script (with hook + timing + AIO directives)
  - 3 thumbnail variants + platform versions
  - Email sequence (5 emails)
  - Design assets (header, email template, social)
  - Funnel metrics (targets, tracking)
  - Coherence report (✅ verified)
  - Metrics dashboard setup

TOTAL TIME: 30 minutes vs. 1-2 days manual
QUALITY: 100% coherence guaranteed
```

### Example 2: Autonomous Optimization (Runs Weekly)

```
OPTIMIZATION AGENT WORKFLOW:

Monitor: Funnel metrics (YouTube CTR = 6.8%, target = 8%)

Week 1: Identify Leak
  - YouTube CTR below target
  - Email → Trial conversion also low
  - Decision: Fix YouTube CTR first (biggest impact)

Week 2: Form Hypothesis
  - "Shocked faces drive higher CTR"
  - Call Thumbnails Agent to generate variant
  - Generate 3 new thumbnails with shocked expressions
  - A/B test: Current (6.8%) vs. Variant (shocked)

Week 3: Measure
  - Current: 6.8% CTR
  - Variant: 7.9% CTR
  - Result: +1.6% (statistically significant ✅)

Week 4: Implement
  - Roll out shocked face approach
  - Document: "Shocked expressions +16% CTR"
  - Set new baseline: 7.9% CTR
  - Next hypothesis: "Test color contrast (red vs. blue CTA)"

Ongoing:
  - Each week: 1% compound improvement potential
  - 1% × 52 weeks = 67% annual improvement
```

---

## Agent Communication Protocol

### Agent-to-Agent Messages

```
Format:
{
  "from_agent": "Orchestration",
  "to_agent": "Copywriting",
  "request": "Generate headline",
  "context": {
    "topic": "50K passive income",
    "brand_voice": "professional, direct",
    "target_emotion": "hope + clarity"
  },
  "constraints": {
    "length": "50-80 characters",
    "format": "benefit-focused"
  }
}

Response:
{
  "status": "complete",
  "output": "How Busy Professionals Make $50K Passive Income",
  "reasoning": "Benefits (50K) + audience (busy professionals) + clarity (no daily work)",
  "confidence": 0.95
}
```

### Error Handling

```
IF agent output fails coherence check:
  → Coherence Agent flags issue
  → Requests revision from relevant agent
  → Agent regenerates with feedback
  → Coherence Agent re-verifies
  → If still fails → Escalate to user

IF metric falls below threshold:
  → Metrics Agent alerts Optimization Agent
  → Optimization Agent designs test
  → Calls relevant agents to generate variants
  → Measures + reports results
  → Auto-implements if positive
```

---

## SDK Initialization

### Setup Code Structure

```
agents/
├── AGENTS.md (this file)
├── orchestration_agent.py
├── skill_agents/
│   ├── branding_agent.py
│   ├── copywriting_agent.py
│   ├── blogging_agent.py
│   ├── seo_aio_agent.py
│   ├── youtube_agent.py
│   ├── thumbnails_agent.py
│   ├── funnel_agent.py
│   └── design_agent.py
├── utility_agents/
│   ├── coherence_agent.py
│   ├── metrics_agent.py
│   └── optimization_agent.py
└── config/
    ├── agent_config.yaml
    ├── skill_mappings.yaml
    └── workflow_definitions.yaml
```

---

## Next Steps

1. ✅ **Architecture Defined** (this document)
2. **Implement Orchestration Agent** (master coordinator)
3. **Connect to Skills** (bridge agent calls to existing skills)
4. **Build Agent Communication** (message protocol)
5. **Test Workflows** (campaign launch, optimization loops)
6. **Deploy to GitHub** (version control)

---

**Ready to build? 🚀**
