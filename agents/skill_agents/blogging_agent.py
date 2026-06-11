"""Blogging skill agent."""

from agents.base_agent import BaseAgent
from agents.config.agent_config import (
    AgentRole,
    BLOGGING_AGENT_PROMPT,
    BLOGGING_SKILL,
)


class BloggingAgent(BaseAgent):
    """Generates long-form, authoritative blog content with EEAT signals."""

    def __init__(self):
        super().__init__(
            name=AgentRole.BLOGGING,
            system_prompt=BLOGGING_AGENT_PROMPT
        )
        self.skill_context = self.add_skill_context(BLOGGING_SKILL)

    def execute(self, plan: dict) -> dict:
        """
        Execute blogging task.

        Args:
            plan: {
                "topic": str,
                "target_keyword": str,
                "length": "short" | "medium" | "long",
                "target_audience": str,
                "tone": str,
                "include_cta": bool
            }
        """
        # Build request message
        length_range = {
            "short": "800-1200 words",
            "medium": "1200-2000 words",
            "long": "2000-3000 words"
        }

        request = f"""
Topic: {plan.get('topic', 'Not specified')}
Target Keyword: {plan.get('target_keyword', 'Not specified')}
Content Length: {length_range.get(plan.get('length', 'medium'), '1200-2000 words')}
Target Audience: {plan.get('target_audience', 'Business professionals')}
Tone: {plan.get('tone', 'Professional and authoritative')}
Include CTA: {plan.get('include_cta', True)}

Please generate a blog post following the EEAT framework (Experience, Expertise, Authoritativeness, Trustworthiness).
Include:
1. Optimized title with keyword
2. Meta description
3. Full outline
4. First 2-3 sections (complete text)
5. SEO recommendations
6. Internal link opportunities
"""

        # Get response from Claude with skill context
        response = self.send_message(request, self.skill_context)

        return {
            "agent": self.name,
            "status": "completed",
            "input": plan,
            "output": response,
            "type": "blogging"
        }
