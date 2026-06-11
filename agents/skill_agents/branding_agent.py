"""Branding skill agent."""

from agents.base_agent import BaseAgent
from agents.config.agent_config import AgentRole, SKILLS_DIR


class BrandingAgent(BaseAgent):
    """Creates and validates brand identity, voice, and visual guidelines."""

    BRANDING_PROMPT = """You are the Branding Agent. Your role is to create cohesive brand identity.

Your responsibility:
- Define brand voice (how we speak)
- Define brand tone (emotional quality)
- Visual principles (color, typography, imagery)
- Brand positioning and differentiation
- Audience persona clarity
- Value proposition articulation

Output a comprehensive brand guideline document."""

    def __init__(self):
        super().__init__(
            name=AgentRole.BRANDING,
            system_prompt=self.BRANDING_PROMPT
        )
        self.skill_file = SKILLS_DIR / "branding" / "SKILL.md"
        self.skill_context = self.add_skill_context(self.skill_file)

    def execute(self, plan: dict) -> dict:
        """
        Execute branding task.

        Args:
            plan: {
                "company_name": str,
                "industry": str,
                "target_audience": str,
                "current_brand": str (optional, existing brand description),
                "brand_personality": str (e.g., "bold, innovative, accessible"),
                "competition": str (optional, key competitors)
            }
        """
        request = f"""
Company: {plan.get('company_name', 'Not specified')}
Industry: {plan.get('industry', 'Not specified')}
Target Audience: {plan.get('target_audience', 'Not specified')}
Desired Personality: {plan.get('brand_personality', 'Professional')}

Current Brand (if any): {plan.get('current_brand', 'Starting fresh')}
Key Competitors: {plan.get('competition', 'Not specified')}

Please create a comprehensive brand identity guide including:
1. Brand Voice & Tone (with examples)
2. Visual Identity (color palette, typography, imagery style)
3. Brand Positioning Statement
4. Key Differentiators
5. Audience Persona Deep-Dive
6. Value Proposition (clear, specific, believable)
7. Brand Messaging Framework
8. Do's and Don'ts
"""

        response = self.send_message(request, self.skill_context)

        return {
            "agent": self.name,
            "status": "completed",
            "input": plan,
            "output": response,
            "type": "branding"
        }
