"""YouTube script skill agent."""

from agents.base_agent import BaseAgent
from agents.config.agent_config import (
    AgentRole,
    YOUTUBE_AGENT_PROMPT,
    YOUTUBE_SKILL,
)


class YouTubeAgent(BaseAgent):
    """Generates viral YouTube scripts optimized for watch time and engagement."""

    def __init__(self):
        super().__init__(
            name=AgentRole.YOUTUBE,
            system_prompt=YOUTUBE_AGENT_PROMPT
        )
        self.skill_context = self.add_skill_context(YOUTUBE_SKILL)

    def execute(self, plan: dict) -> dict:
        """
        Execute YouTube script generation task.

        Args:
            plan: {
                "topic": str,
                "hook_type": "pattern_interrupt" | "curiosity_gap" | "benefit",
                "target_duration": int (in seconds),
                "audience": str,
                "content_angle": str,
                "cta_type": "subscribe" | "website" | "product" | etc
            }
        """
        # Build request message
        hook_descriptions = {
            "pattern_interrupt": "sudden change in pattern to grab attention",
            "curiosity_gap": "reveal gap between what viewers know and want to know",
            "benefit": "promise immediate benefit or transformation"
        }

        hook_type = plan.get('hook_type', 'pattern_interrupt')
        hook_desc = hook_descriptions.get(hook_type, hook_type)

        request = f"""
Topic: {plan.get('topic', 'Not specified')}
Hook Type: {hook_type} ({hook_desc})
Target Duration: {plan.get('target_duration', 480)} seconds
Target Audience: {plan.get('audience', 'General')}
Content Angle: {plan.get('content_angle', 'Educational and entertaining')}
CTA Type: {plan.get('cta_type', 'Subscribe')}

Please generate a YouTube script following AIO (Artificial Intelligence Optimization) principles.
Include:
1. Compelling video title
2. Hook script (word-for-word, first 15 seconds)
3. Main script with timing markers
4. Key moments for cuts/b-roll
5. Strong CTA
6. Thumbnail ideas
7. Tags and description optimization
8. Rewatch moments (points that make people rewatch)
"""

        # Get response from Claude with skill context
        response = self.send_message(request, self.skill_context)

        return {
            "agent": self.name,
            "status": "completed",
            "input": plan,
            "output": response,
            "type": "youtube"
        }
