# Agent SDK Implementation - Phase 1 MVP

**Status:** ✅ Phase 1 MVP Complete  
**Build Time:** 1 week  
**Agents Implemented:** 4 (1 Orchestration + 3 Skill + 1 Utility)

---

## What's Implemented

### Agents (Phase 1)
1. **Orchestration Agent** — Master coordinator, parses requests, delegates to skill agents
2. **Copywriting Agent** — Generates high-converting copy using AIDA/PASTOR frameworks
3. **Blogging Agent** — Creates EEAT-optimized blog posts with SEO signals
4. **YouTube Agent** — Produces viral video scripts with hooks and AIO optimization
5. **Coherence Agent** — Verifies brand alignment across all outputs

### Architecture
```
User Request
    ↓
Orchestration Agent
    ↓
├─ Copywriting Agent → Copy variants
├─ Blogging Agent → Blog article
├─ YouTube Agent → Video script
    ↓
Coherence Agent → Brand verification
    ↓
Final Campaign Output
```

---

## Quick Start

### 1. Install Dependencies
```bash
cd /home/user/declic-marketing
pip install -r requirements.txt
```

### 2. Set Up API Key
```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

### 3. Run Demo Campaign
```bash
python main.py
```

This will:
- Initialize the Orchestration Agent
- Create a sample campaign: "Build $50K Passive Income..."
- Call Copywriting, Blogging, and YouTube agents
- Run coherence verification
- Save results to `campaign_output.json`

### 4. Interactive Mode
```bash
python main.py interactive
```

This lets you input custom campaign requests like:
- "Campaign: Tax-efficient portfolio management"
- "Campaign: Automated rebalancing for beginners"

---

## Project Structure

```
agents/
├── __init__.py                          # Package initialization
├── base_agent.py                        # Base class for all agents
├── orchestration_agent.py               # Master coordinator
├── skill_agents/
│   ├── __init__.py
│   ├── copywriting_agent.py            # AIDA/PASTOR frameworks
│   ├── blogging_agent.py                # EEAT signals
│   └── youtube_agent.py                 # AIO optimization
├── utility_agents/
│   ├── __init__.py
│   └── coherence_agent.py               # Brand verification
└── config/
    └── agent_config.py                  # Configuration & constants

main.py                                  # Demo and CLI entry point
requirements.txt                         # Python dependencies
.env.example                            # Environment template
AGENTS_IMPLEMENTATION.md                # This file
```

---

## How It Works

### Phase 1 Workflow

1. **User sends request:**
   ```
   "Campaign: Build $50K Passive Income with Automated Portfolio Management"
   ```

2. **Orchestration Agent:**
   - Parses the request
   - Creates subplans for each skill agent
   - Delegates execution

3. **Skill Agents execute in parallel:**
   - **Copywriting Agent**: Creates headlines, CTAs, copy variants
   - **Blogging Agent**: Writes SEO-optimized blog post
   - **YouTube Agent**: Generates video script with hooks

4. **Coherence Agent verifies:**
   - Brand voice consistency
   - Message alignment
   - Target audience understanding
   - Value proposition consistency

5. **Results compiled:**
   - All outputs organized by agent
   - Coherence score (0-100)
   - Issues and suggestions identified
   - Campaign ready for review

---

## Agent Details

### Copywriting Agent
- **Input**: Topic, brand voice, target audience, format
- **Output**: Headlines, body copy, CTAs, psychology breakdown
- **Framework**: AIDA (Attention → Interest → Desire → Action) + PASTOR (Problem → Amplify → Story → Transformation → Offer → Response)

### Blogging Agent
- **Input**: Topic, keyword, length, audience, tone
- **Output**: Full blog outline, first 2-3 sections, SEO metadata, link opportunities
- **Framework**: EEAT (Experience, Expertise, Authoritativeness, Trustworthiness)

### YouTube Agent
- **Input**: Topic, hook type, duration, audience, content angle, CTA type
- **Output**: Video title, hook script, full script with timings, thumbnail ideas, tags
- **Framework**: AIO (Artificial Intelligence Optimization) with hook psychology

### Coherence Agent
- **Input**: List of outputs from skill agents, optional brand guidelines
- **Output**: JSON with coherence score, issues, strengths, suggestions
- **Checks**: Voice, tone, messaging, positioning, audience, value prop, CTAs

---

## Skill Integration

Each agent automatically loads its corresponding SKILL.md file:

- **copywriting_agent** ← `.claude/skills/copywriting/SKILL.md`
- **blogging_agent** ← `.claude/skills/blogging/SKILL.md`
- **youtube_agent** ← `.claude/skills/youtube-script/SKILL.md`

The skill framework is injected into Claude's system prompt, ensuring consistency with documented best practices.

---

## Example Output

When you run `python main.py`, you get:

```
==============================================================================
DECLIC MARKETING AGENT SDK - PHASE 1 MVP DEMO
==============================================================================

Initializing Orchestration Agent...
✓ Orchestration Agent ready

============================================================================
ORCHESTRATION AGENT - Processing Request
============================================================================
Request: Campaign: Build $50K Passive Income...

Created 3 subplans
  1. copywriting: High-converting copy for 'Build $50K Passive Income...'
  2. blogging: Authority blog post about 'Build $50K Passive Income...'
  3. youtube: YouTube script for 'Build $50K Passive Income...' video

Executing Copywriting Agent...
  ✓ Copywriting Agent completed

Executing Blogging Agent...
  ✓ Blogging Agent completed

Executing YouTube Agent...
  ✓ YouTube Agent completed

Running coherence check...
Coherence Score: 87/100

============================================================================
CAMPAIGN RESULTS
...
```

Results are also saved to `campaign_output.json`.

---

## What's Next (Phase 2)

Phase 2 adds 4 more skill agents:
- **Branding Agent** — Visual identity, color systems, voice guidelines
- **SEO/AIO Agent** — Answer engine optimization for AI era
- **Thumbnails Agent** — High-CTR thumbnail generation
- **Lead Magnets Agent** — Quizzes, calculators, giveaways, ebooks

Plus 3 utility agents:
- **Design Agent** — Component systems, accessibility
- **Metrics Agent** — Tracking and analytics setup
- **Optimization Agent** — Autonomous A/B testing

---

## Testing

### Unit Tests (Future)
```bash
pytest tests/
```

### Integration Tests (Future)
```bash
pytest tests/integration/
```

### Manual Testing
1. Run demo: `python main.py`
2. Try interactive: `python main.py interactive`
3. Modify `main.py` to test different requests

---

## Troubleshooting

**Issue:** `ModuleNotFoundError: No module named 'anthropic'`
- **Fix**: `pip install -r requirements.txt`

**Issue:** `ANTHROPIC_API_KEY not set`
- **Fix**: Create `.env` file with your API key (copy from `.env.example`)

**Issue:** Coherence agent returns null/empty
- **Fix**: Ensure all skill agents completed successfully (check agent output status)

**Issue:** Skill files not found
- **Fix**: Ensure you're running from project root directory, skill files should be at `.claude/skills/*/SKILL.md`

---

## Performance

**Phase 1 MVP Metrics:**
- **Response time**: ~30-60 seconds (depending on Claude API latency)
- **Token usage**: ~6,000-8,000 tokens per request
- **Coherence check**: Additional ~2,000 tokens

**Optimization opportunities (Phase 3):**
- Cache skill frameworks to reduce context
- Parallel agent execution (agents can run simultaneously)
- Response streaming for real-time feedback
- Prompt optimization to reduce token usage

---

## API Reference

### OrchestrationAgent
```python
from agents import OrchestrationAgent

orchestrator = OrchestrationAgent()

# Execute with brand guidelines
result = orchestrator.handle_request(
    user_request="Campaign: Your request here",
    brand_guidelines={
        "voice": "...",
        "tone": "...",
        "positioning": "...",
        "target_audience": "...",
        "value_proposition": "..."
    }
)

# Access results
print(result['coherence_check']['coherence_score'])
print(result['agent_outputs'])
```

### Individual Skill Agents
```python
from agents import CopywritingAgent

agent = CopywritingAgent()
output = agent.execute({
    "topic": "Your topic",
    "brand_voice": "Professional",
    "target_audience": "Busy professionals",
    "desired_outcome": "Increase conversions",
    "format": "sales_page"
})

print(output['output'])  # Full response from Claude
```

---

## Configuration

Edit `agents/config/agent_config.py` to customize:
- **MODEL_NAME**: Switch Claude version
- **MAX_TOKENS**: Adjust output length
- **TEMPERATURE**: Change creativity level
- **AGENT_TIMEOUT**: Timeout for agent execution
- **Skill file paths**: Update if skill locations change

---

## Next Steps

1. **Test Phase 1**: Run demos, verify outputs quality
2. **Gather feedback**: Which outputs most valuable?
3. **Plan Phase 2**: Add remaining skill agents
4. **Integrate external tools**: Canva, email platforms, analytics
5. **Optimize prompts**: A/B test different frameworks

---

## Questions?

Refer to:
- `AGENTS.md` — Full Agent SDK architecture
- `IMPLEMENTATION_ROADMAP.md` — Phased implementation strategy
- `.claude/skills/*/SKILL.md` — Individual skill frameworks
- `CLAUDE.md` — Operating principles (Karpathy-style)
