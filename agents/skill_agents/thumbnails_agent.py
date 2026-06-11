"""Thumbnails skill agent for high-CTR visual content."""

from agents.base_agent import BaseAgent
from agents.config.agent_config import AgentRole, SKILLS_DIR


class ThumbnailsAgent(BaseAgent):
    """Creates high-CTR thumbnails for YouTube, TikTok, Instagram, and blog content."""

    THUMBNAILS_PROMPT = """You are the Thumbnails Agent. Your role is to create psychologically-optimized thumbnails.

Key Psychology:
- Faces +25-30% CTR (emotion matters most)
- Color contrast increases visibility
- Curiosity gap (confused faces, question marks)
- Scarcity/urgency (arrows, numbers, "LAST")
- Social proof (logos, testimonials)

Your responsibility:
- Design high-CTR thumbnails for each platform
- Psychology-driven visual hierarchy
- Text overlay optimization
- Color psychology
- A/B testing recommendations
- Accessibility guidelines

Platforms:
- YouTube: 1280x720px (16:9)
- YouTube Shorts: 1080x1920px (9:16)
- TikTok: 1080x1920px (9:16)
- Instagram Square: 1080x1080px (1:1)
- Blog featured images: 1200x628px (1.91:1)
"""

    def __init__(self):
        super().__init__(
            name=AgentRole.THUMBNAILS,
            system_prompt=self.THUMBNAILS_PROMPT
        )
        self.skill_file = SKILLS_DIR / "thumbnails" / "SKILL.md"
        self.skill_context = self.add_skill_context(self.skill_file)

    def execute(self, plan: dict) -> dict:
        """
        Execute thumbnail design task.

        Args:
            plan: {
                "title": str,
                "platforms": list,  # ["youtube", "tiktok", "instagram"]
                "hook_type": str,  # "curiosity_gap", "pattern_interrupt", "social_proof"
                "key_message": str,
                "brand_colors": list,
                "style": str,  # "professional", "casual", "energetic"
                "target_audience": str
            }
        """
        platforms_str = ", ".join(plan.get('platforms', ['youtube'])) if plan.get('platforms') else "YouTube"

        request = f"""
Content Title: {plan.get('title', 'Not specified')}
Platforms: {platforms_str}
Hook Type: {plan.get('hook_type', 'curiosity_gap')}
Key Message: {plan.get('key_message', 'Not specified')}
Brand Colors: {', '.join(plan.get('brand_colors', ['Blue', 'White']))}
Style: {plan.get('style', 'Professional')}
Target Audience: {plan.get('target_audience', 'General')}

Please design thumbnails for each platform:

1. Platform-Specific Design
   - Dimensions: [correct for platform]
   - Text: Large, readable (minimum 12pt effective size)
   - Imagery: Clear main subject/face
   - Color: High contrast, brand-aligned
   - Emotion: Specific facial expression or visual cue

2. Psychology Application
   - Hook type implementation (curiosity gap/pattern interrupt/social proof)
   - Why this specific design choice (psychology explanation)
   - Expected CTR improvement vs. baseline

3. For Each Platform:
   a) YouTube Thumbnail
      - Design specification
      - Text overlay layout
      - Key visual element

   b) TikTok/YouTube Shorts
      - Vertical optimization
      - Text positioning for safe area
      - Hook implementation

   c) Instagram (if applicable)
      - Square format optimization
      - Grid appearance

   d) Blog Featured Image (if applicable)
      - Landscape format
      - SEO considerations

4. A/B Testing Recommendations
   - Variant A: [specific design change]
   - Variant B: [alternative approach]
   - Metric to test: CTR or engagement

5. Technical Specifications
   - File formats needed
   - Optimization recommendations
   - Accessibility (alt text, color contrast)

6. Templating Suggestions
   - Design system approach
   - Consistent elements (logo, fonts, colors)
   - Scalability for future content
"""

        response = self.send_message(request, self.skill_context)

        return {
            "agent": self.name,
            "status": "completed",
            "input": plan,
            "output": response,
            "type": "thumbnails"
        }
