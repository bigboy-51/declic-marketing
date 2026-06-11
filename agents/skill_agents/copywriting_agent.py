"""Copywriting skill agent."""

from pathlib import Path
from agents.base_agent import BaseAgent
from agents.config.agent_config import (
    AgentRole,
    COPYWRITING_AGENT_PROMPT,
    COPYWRITING_SKILL,
)


class CopywritingAgent(BaseAgent):
    """Generates high-converting copy, headlines, and CTAs."""

    def __init__(self):
        super().__init__(
            name=AgentRole.COPYWRITING,
            system_prompt=COPYWRITING_AGENT_PROMPT
        )
        self.skill_context = self.add_skill_context(COPYWRITING_SKILL)

    def execute(self, plan: dict) -> dict:
        """
        Execute copywriting task.

        Args:
            plan: {
                "topic": str,
                "brand_voice": str,
                "target_audience": str,
                "desired_outcome": str,
                "format": "sales_page" | "email" | "ad" | etc
            }
        """
        # Build request message
        request = f"""
Topic: {plan.get('topic', 'Not specified')}
Brand Voice: {plan.get('brand_voice', 'Professional')}
Target Audience: {plan.get('target_audience', 'Business professionals')}
Desired Outcome: {plan.get('desired_outcome', 'Increase conversions')}
Format: {plan.get('format', 'General copy')}

Please generate high-converting copy following the AIDA/PASTOR frameworks.
Include multiple variants and explain the psychology behind each approach.
"""

        # Get response from Claude with skill context
        response = self.send_message(request, self.skill_context)

        return {
            "agent": self.name,
            "status": "completed",
            "input": plan,
            "output": response,
            "type": "copywriting"
        }
