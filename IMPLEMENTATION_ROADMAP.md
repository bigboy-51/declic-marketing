# Implementation Roadmap: Declic Marketing Agent SDK

**Status:** Ready to build  
**Last updated:** 2026-06-11  
**Scope:** 10 skills + 12 agents → Complete marketing automation system

---

## Current State: What You Have

### 10 Marketing Skills ✅
```
copywriting, branding, blogging, youtube-script, seo-aio, 
thumbnails, lead-magnets, closer, funnel, design
```

**Documented in:** `.claude/skills/*/SKILL.md`  
**Usable right now:** Yes (manually or via Claude prompts)

### 12 Agents Defined ✅
```
Orchestration Agent (master coordinator)
├─ 8 Skill Agents (copywriting, branding, blogging, youtube, seo-aio, thumbnails, lead-magnets, closer)
├─ Design Agent
└─ 3 Utility Agents (coherence, metrics, optimization)
```

**Documented in:** `AGENTS.md`  
**Status:** Architecture ready, implementation pending

---

## Quick Start: Use Skills TODAY (No Code Required)

You don't need to build agents to get value. Use the skills now:

```
1. Need a sales page?
   → Read: .claude/skills/copywriting/SKILL.md
   → Use: Follow the AIDA/PASTOR framework
   → Apply: Write your copy

2. Need a blog post?
   → Read: .claude/skills/blogging/SKILL.md
   → Use: Structure + EEAT framework
   → Apply: Write and optimize

3. Need a lead magnet?
   → Read: .claude/skills/lead-magnets/SKILL.md
   → Use: Pick type (quiz, ebook, etc)
   → Apply: Create the asset

4. Need to close more deals?
   → Read: .claude/skills/closer/SKILL.md
   → Use: Email sequence + objection handling
   → Apply: Send emails, run calls

(Same pattern for all 10 skills)
```

**Time to value:** Immediate (read skill → apply framework)

---

## Implementation Plan: 3 Phases

### Phase 1: MVP (Proof of Concept) - 2 Weeks

**Goal:** One complete workflow automated end-to-end

**Build:**
```
1. Orchestration Agent (main coordinator)
   - Receives user request: "Campaign: $50K passive income"
   - Plans workflow
   - Delegates to skill agents
   - Compiles output

2. Three Skill Agents (MVP core):
   a) Copywriting Agent
      - Uses: copywriting/SKILL.md framework
      - Input: Topic + brand voice
      - Output: Headlines, CTAs, copy variants
   
   b) Blogging Agent
      - Uses: blogging/SKILL.md framework
      - Input: Topic + keyword + length
      - Output: Blog article (structure + EEAT)
   
   c) YouTube Agent
      - Uses: youtube-script/SKILL.md framework
      - Input: Blog topic + hook type
      - Output: Script with timings + AIO/AEO/GEO

3. Coherence Agent
   - Checks if all three outputs align (voice, message, brand)
   - Flags inconsistencies
```

**Integration Method:** Claude API with tool_use
```
User request → Orchestration Agent → Calls skill agents → Gets outputs → Coherence check → Delivers result
```

**Success Criteria:**
- ✅ User says: "Campaign: Make $50K passive income"
- ✅ System returns: Blog + YouTube script + Copy variants
- ✅ All outputs match brand voice (verified by Coherence Agent)
- ✅ Takes < 5 minutes end-to-end

**Deliverable:** Working proof-of-concept, ready for Phase 2

---

### Phase 2: Full System - 4 Weeks

**Build on Phase 1. Add:**

```
1. Remaining Skill Agents (5 more):
   - Branding Agent
   - SEO/AIO Agent
   - Thumbnails Agent
   - Lead Magnets Agent
   - Closer Agent
   - Funnel Agent
   - Design Agent

2. Utility Agents:
   - Metrics Agent (setup tracking)
   - Optimization Agent (autonomous testing)

3. Full Orchestration Logic:
   - Campaign launch workflow
   - Funnel optimization loop
   - Content distribution workflow
   - Autonomous improvement cycle
```

**New Capabilities:**
```
"Launch complete campaign" → Blog + YouTube + Thumbnails + Email + Funnel + Design + Metrics

vs.

"Optimize my funnel" → Metrics Agent analyzes → Identifies leak → Optimization Agent tests fix → Reports results
```

**Success Criteria:**
- ✅ One request = 8+ skill agents in coordinated action
- ✅ Complete campaigns generated in 30 min
- ✅ Funnel optimization running autonomously
- ✅ Brand coherence guaranteed across all outputs

**Deliverable:** Production-ready system, all 10 skills integrated

---

### Phase 3: Optimization & Scale - Ongoing

**Enhance:**
```
1. Agent Intelligence
   - Learn from past campaigns
   - Improve prompts based on results
   - A/B test different approaches

2. User Experience
   - Natural language requests ("Build campaign around $50K")
   - Conversational back-and-forth
   - Progress tracking

3. Integration
   - Connect to Canva (for design export)
   - Connect to email platform (for sending)
   - Connect to analytics (for tracking)
   - Connect to ThumbnailCreator (for AI thumbnails)

4. Performance
   - Cache common frameworks
   - Parallel agent execution
   - Faster response times
```

---

## Architecture: How Agents Call Skills

### The Integration Pattern

```
┌─────────────────────────────────────┐
│     User Request                    │
│  "Campaign: $50K passive income"    │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│   Orchestration Agent (Claude)      │
│   - Parse request                   │
│   - Plan workflow                   │
│   - Delegate to skill agents        │
└────────────────┬────────────────────┘
                 │
    ┌────────────┴────────────┬──────────────┐
    │                         │              │
┌───▼───────┐    ┌───────────▼──┐   ┌──────▼──────┐
│ Copywriting │   │   Blogging    │   │   YouTube   │
│   Agent     │   │    Agent      │   │    Agent    │
└───┬───────┘    └───────────┬──┘   └──────┬──────┘
    │                        │             │
    │ Uses:                  │ Uses:       │ Uses:
    │ copywriting/SKILL.md   │ blogging/   │ youtube-script/
    │ framework              │ SKILL.md    │ SKILL.md
    │ (AIDA/PASTOR)          │ (EEAT)      │ (Hooks + AIO/AEO/GEO)
    │                        │             │
    └────────────┬───────────┴─────────────┘
                 │
         ┌───────▼─────────┐
         │  Coherence Agent│
         │  (Verification) │
         └───────┬─────────┘
                 │
         ┌───────▼─────────┐
         │  Final Output   │
         │ (Blog + Script  │
         │  + Copy)        │
         └─────────────────┘
```

### Implementation (Pseudo-code)

```python
# Phase 1 MVP Structure

class OrchestrationAgent:
    def handle_request(self, user_request):
        # Step 1: Understand request
        plan = self.parse_request(user_request)
        
        # Step 2: Call skill agents in sequence
        copywriting_output = CopywritingAgent().execute(plan)
        blogging_output = BloggingAgent().execute(plan)
        youtube_output = YouTubeAgent().execute(plan)
        
        # Step 3: Verify coherence
        verification = CoherenceAgent().verify([
            copywriting_output,
            blogging_output,
            youtube_output
        ])
        
        # Step 4: Return result or request revisions
        if verification.is_coherent:
            return self.compile_output([...])
        else:
            return self.request_revisions(verification.issues)

class CopywritingAgent:
    def execute(self, plan):
        # Input: plan with topic, target audience, brand voice
        # Process: Apply copywriting/SKILL.md framework (AIDA/PASTOR)
        # Output: Headlines, CTAs, copy variants
        return {
            "headlines": [...],
            "ctas": [...],
            "copy_variants": [...]
        }

class BloggingAgent:
    def execute(self, plan):
        # Input: plan with topic, keyword, length
        # Process: Apply blogging/SKILL.md framework (EEAT)
        # Output: Blog article with structure
        return {
            "article": "...",
            "seo_metadata": {...},
            "internal_links": [...]
        }

# ... similar for YouTubeAgent, CoherenceAgent
```

---

## Build Order & Dependencies

### Phase 1 Dependencies
```
1. Orchestration Agent ← No dependencies (start here)
2. CopywritingAgent ← Needs: copywriting/SKILL.md ✅ (exists)
3. BloggingAgent ← Needs: blogging/SKILL.md ✅ (exists)
4. YouTubeAgent ← Needs: youtube-script/SKILL.md ✅ (exists)
5. CoherenceAgent ← Needs: All of above
```

### Phase 2 Dependencies
```
6. BrandingAgent ← Needs: branding/SKILL.md ✅ (exists)
7. SEO/AIOAgent ← Needs: seo-aio/SKILL.md ✅ (exists)
8. ThumbnailsAgent ← Needs: thumbnails/SKILL.md ✅ (exists)
9. LeadMagnetsAgent ← Needs: lead-magnets/SKILL.md ✅ (exists)
10. CloserAgent ← Needs: closer/SKILL.md ✅ (exists)
11. FunnelAgent ← Needs: funnel/SKILL.md ✅ (exists)
12. DesignAgent ← Needs: design/SKILL.md ✅ (exists)
13. MetricsAgent ← No skill dependency (own logic)
14. OptimizationAgent ← Needs: All skill agents
```

**Note:** All skills exist. Zero external dependencies. Ready to build.

---

## Tech Stack (Recommended)

### Phase 1 (MVP)
```
Language: Python 3.11+
AI: Claude API (Claude 3.5 Sonnet or Opus)
Framework: Custom (simple script-based orchestration)
Storage: JSON files (for simplicity)
```

### Phase 2+
```
Add: Redis (caching)
Add: PostgreSQL (metrics, history)
Add: FastAPI (if you want API endpoints)
```

---

## Success Metrics by Phase

### Phase 1
- ✅ One request generates 3+ coordinated outputs
- ✅ Coherence check catches inconsistencies
- ✅ < 5 minutes end-to-end
- ✅ Output quality > 80% (vs manual)

### Phase 2
- ✅ Complex campaigns (8+ agents) in 30 min
- ✅ Brand coherence 100% (verified)
- ✅ Funnel optimization loop running
- ✅ Metrics tracking automated

### Phase 3
- ✅ AI improving its own prompts
- ✅ Response time < 2 minutes
- ✅ Full integration with external tools
- ✅ Can run without human intervention

---

## Decision: What's Next?

### Option 1: Start Build Now
- You or someone on your team builds Phase 1
- 2 weeks to proof-of-concept
- Then evaluate Phase 2+

### Option 2: Assign to Developer
- Hand over AGENTS.md + this roadmap
- They follow the Phase 1 plan
- You review in 2 weeks

### Option 3: Use Skills Manually First
- Test all 10 skills manually
- See value immediately
- Build agents when clear need exists

### Option 4: I Build Phase 1
- I create MVP agents (Python)
- Takes ~1 week
- You test and evaluate

---

## File Structure (After Implementation)

```
declic-marketing/
├── CLAUDE.md
├── AGENTS.md
├── IMPLEMENTATION_ROADMAP.md (this file)
├── README.md
├── .claude/
│   └── skills/
│       ├── copywriting/SKILL.md
│       ├── branding/SKILL.md
│       ├── ... (all 10 skills)
│
├── agents/ (NEW - after Phase 1)
│   ├── __init__.py
│   ├── orchestration_agent.py
│   ├── skill_agents/
│   │   ├── copywriting_agent.py
│   │   ├── blogging_agent.py
│   │   └── ... (others in Phase 2)
│   ├── utility_agents/
│   │   ├── coherence_agent.py
│   │   └── ... (metrics, optimization)
│   └── config/
│       ├── agent_config.yaml
│       └── skill_mappings.yaml
│
└── tests/ (NEW - after Phase 1)
    ├── test_orchestration_agent.py
    └── ... (integration tests)
```

---

## Next Step: Your Call

**Choose one:**

A) **Start building Phase 1** (Python, Claude API)
B) **Test skills manually first** (immediate value)
C) **I build Phase 1 MVP** (you review in ~1 week)
D) **Pause and plan more** (if needed)

**What's your preference?** 🚀
