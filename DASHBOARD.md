# 📊 Agent Dashboard

Simple visual interface for the Declic Marketing Agent SDK.

## Quick Start

### 1. Install Streamlit
```bash
pip install -r requirements.txt
```

### 2. Set Your API Key
```bash
export ANTHROPIC_API_KEY=your_key_here
```

Or create `.env` file:
```bash
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
```

### 3. Launch Dashboard
```bash
streamlit run dashboard.py
```

Opens at: `http://localhost:8501`

---

## Interface Overview

### 📝 Top Section: Campaign Request
- **Text area**: Enter your campaign brief
- **Quick templates**: 4 pre-loaded campaign templates (Passive Income, Risk Management, Tax Efficiency, Beginner Guide)
- **Launch button**: Execute the full workflow

### ⚙️ Sidebar: Configuration
- **Brand Voice**: How your brand speaks
- **Brand Tone**: Emotional quality of communication
- **Positioning**: Market position statement
- **Target Audience**: Who you're talking to
- **Value Proposition**: What you promise

### 📊 Results Section (after execution)

#### Metrics Cards
- **Agents Executed**: How many agents ran successfully
- **Coherence Score**: 0-100 brand alignment score
- **Status**: Coherent ✅ or Review Needed ⚠️

#### Agent Outputs
Each agent (Copywriting, Blogging, YouTube) shows:
- **Full Output tab**: Complete response from Claude
- **Summary tab**: First 500 characters preview

Expandable panels show agent name, type, and full content.

#### Brand Coherence Analysis
Shows:
- **Issues Found**: Brand inconsistencies detected
- **Suggestions**: Improvement recommendations
- **Identified Strengths**: What's working well

#### Export Options
- **JSON**: Machine-readable results
- **Markdown**: Human-readable report

---

## Example Workflow

1. **Load dashboard**: `streamlit run dashboard.py`
2. **Enter request**: "Campaign: Tax-efficient portfolio strategies"
3. **Customize brand** (sidebar):
   - Voice: "Expert, accessible, friendly"
   - Tone: "Confident and educational"
4. **Click "Launch Campaign"**
5. **Watch progress**: Real-time status updates
6. **Review results**: See all agent outputs with coherence score
7. **Export report**: Download as JSON or Markdown

---

## Quick Templates

Press any button to auto-fill the campaign request:

```
📈 Passive Income
→ "Campaign: Build $50K Passive Income with Automated Portfolio Management"

🛡️ Risk Management
→ "Campaign: Protect Your Portfolio with Intelligent Risk Management"

💰 Tax Efficiency
→ "Campaign: Maximize Returns with Tax-Efficient Portfolio Strategies"

🎓 Beginner Guide
→ "Campaign: Start Investing: A Complete Beginner's Guide"
```

---

## Understanding Coherence Scores

**75-100:** ✅ **Excellent** — All outputs perfectly aligned
**50-74:** ⚠️ **Good** — Minor inconsistencies, review recommended
**0-49:** ❌ **Review** — Significant brand misalignment

The coherence check verifies:
- Voice consistency (professional, technical, etc.)
- Tone alignment (friendly, formal, etc.)
- Messaging consistency (same talking points)
- Audience understanding (targeting the same person)
- Value proposition clarity (same benefits promised)
- CTA alignment (same next steps)

---

## Performance

**Typical execution:**
- Parse request: <1 second
- Copywriting agent: 10-20 seconds
- Blogging agent: 15-30 seconds
- YouTube agent: 15-30 seconds
- Coherence check: 5-10 seconds
- **Total: 45-90 seconds**

Response time depends on Claude API latency.

---

## Customization

Edit `dashboard.py` to:
- Change colors (CSS section at top)
- Add new quick templates
- Modify sidebar configuration
- Add new export formats

---

## Troubleshooting

**Issue:** `ModuleNotFoundError: No module named 'streamlit'`
- **Fix**: `pip install streamlit`

**Issue:** Port 8501 already in use
- **Fix**: `streamlit run dashboard.py --server.port 8502`

**Issue:** API key not recognized
- **Fix**: Ensure `.env` file has `ANTHROPIC_API_KEY` or environment variable is set

**Issue:** Agents not executing
- **Fix**: Check that skill files exist at `.claude/skills/*/SKILL.md`

---

## Browser Compatibility

Works best on:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)

---

## Next Steps

- Test different campaign requests
- Evaluate coherence scores
- Gather feedback on output quality
- Plan Phase 2 agent integration
- Consider custom branding for dashboard

---

## Tips

1. **Brand guidelines matter**: Specific voice/tone improves coherence
2. **Clear requests work best**: "Build $50K passive income" → better outputs than vague requests
3. **Review issues first**: Start with the "Issues Found" section
4. **Export reports**: Save JSON for tracking, Markdown for sharing
5. **Iterate**: Refine brand guidelines based on coherence scores
