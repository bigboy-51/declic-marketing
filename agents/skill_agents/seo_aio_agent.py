"""SEO/AIO skill agent for AI-era visibility."""

from agents.base_agent import BaseAgent
from agents.config.agent_config import AgentRole, SKILLS_DIR


class SEOAIOAgent(BaseAgent):
    """Optimizes content for AI-era discovery (Google + ChatGPT + Perplexity + Claude)."""

    SEO_AIO_PROMPT = """You are the SEO/AIO Agent. Your role is to optimize content for discovery in the AI era.

Frameworks:
- AIO (Artificial Intelligence Optimization): Make content understandable and citable by AI
- AEO (Answer Engine Optimization): Get extracted as direct answers by LLMs
- GEO (Generative Engine Optimization): Get referenced in AI-generated summaries
- Traditional SEO: Still matter (Google, featured snippets)

Your responsibility:
- Keyword research (search intent, volume, competition)
- Content structure for AI parsing
- Schema markup and rich snippets
- Answer engine optimization
- AI citation-friendly formatting
- Performance monitoring (rankings, featured snippet positions)
"""

    def __init__(self):
        super().__init__(
            name=AgentRole.SEO_AIO,
            system_prompt=self.SEO_AIO_PROMPT
        )
        self.skill_file = SKILLS_DIR / "seo-aio" / "SKILL.md"
        self.skill_context = self.add_skill_context(self.skill_file)

    def execute(self, plan: dict) -> dict:
        """
        Execute SEO/AIO optimization task.

        Args:
            plan: {
                "content_type": "blog" | "video" | "product_page" | "landing_page",
                "topic": str,
                "target_keywords": list,
                "current_content": str (optional),
                "competitors": list,
                "content_goal": str
            }
        """
        keywords_str = ", ".join(plan.get('target_keywords', [''])) if plan.get('target_keywords') else "Not specified"
        competitors_str = ", ".join(plan.get('competitors', [])) if plan.get('competitors') else "Not specified"

        request = f"""
Content Type: {plan.get('content_type', 'blog')}
Topic: {plan.get('topic', 'Not specified')}
Target Keywords: {keywords_str}
Key Competitors: {competitors_str}
Goal: {plan.get('content_goal', 'Increase organic visibility')}

Current Content (if optimizing existing):
{plan.get('current_content', 'Creating new content')}

Please provide:
1. Keyword Research & Strategy
   - Primary keyword + search intent
   - Related keywords and semantic variations
   - Long-tail keyword opportunities
   - Volume, difficulty, competition analysis

2. AIO Optimization
   - Clear structure for AI understanding
   - Schema markup recommendations
   - Citation-friendly formatting

3. AEO Optimization
   - Answer engine positioning (first 100 words)
   - Direct answer format for LLM extraction
   - Structured data for AI understanding

4. GEO Optimization
   - Unique insights/data AI should cite
   - Claim-backed assertions
   - Credibility signals

5. Traditional SEO
   - Title tag optimization
   - Meta description
   - H1-H6 structure
   - Featured snippet optimization
   - Internal linking strategy

6. Performance Targets
   - Realistic ranking timeline
   - Featured snippet opportunity
   - Expected organic traffic
"""

        response = self.send_message(request, self.skill_context)

        return {
            "agent": self.name,
            "status": "completed",
            "input": plan,
            "output": response,
            "type": "seo_aio"
        }
