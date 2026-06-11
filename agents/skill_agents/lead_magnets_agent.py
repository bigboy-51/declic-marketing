"""Lead Magnets skill agent for high-converting offers."""

from agents.base_agent import BaseAgent
from agents.config.agent_config import AgentRole, SKILLS_DIR


class LeadMagnetsAgent(BaseAgent):
    """Creates high-converting lead magnets across 8 formats."""

    LEAD_MAGNETS_PROMPT = """You are the Lead Magnets Agent. Your role is to create high-converting lead captures.

Conversion Benchmarks (2026):
- Quizzes: 40.1% (highest converting)
- Giveaways: 29.37%
- Webinars: 27.4%
- Interactive Tools: 26.44%
- Reports: 24.61%
- Checklists: 20-28%
- Templates: 18-25%
- Ebooks (specific): 15-22%

Key principle: Specificity > Generality
- "Ultimate Guide" = 4-8% conversion (BAD)
- "5 Mistakes Costing $50K/Year" = 15-22% conversion (GOOD)

Your responsibility:
- Choose optimal magnet type for audience
- Create compelling headline/CTA
- Design signup form (3-5 fields max)
- Write email sequence (welcome + bonus + nurture)
- Ensure mobile optimization
- Provide A/B testing recommendations
"""

    def __init__(self):
        super().__init__(
            name=AgentRole.LEAD_MAGNETS,
            system_prompt=self.LEAD_MAGNETS_PROMPT
        )
        self.skill_file = SKILLS_DIR / "lead-magnets" / "SKILL.md"
        self.skill_context = self.add_skill_context(self.skill_file)

    def execute(self, plan: dict) -> dict:
        """
        Execute lead magnet creation task.

        Args:
            plan: {
                "target_audience": str,
                "main_pain_point": str,
                "desired_magnet_type": str (optional, will recommend if not provided),
                "offer_value": str,
                "company_name": str,
                "existing_asset": str (optional, asset to repurpose)
            }
        """
        magnet_type = plan.get('desired_magnet_type', 'Let me recommend based on audience')

        request = f"""
Target Audience: {plan.get('target_audience', 'Not specified')}
Main Pain Point: {plan.get('main_pain_point', 'Not specified')}
What We Offer: {plan.get('offer_value', 'Not specified')}
Company: {plan.get('company_name', 'Our company')}
Magnet Type Preference: {magnet_type}
Existing Asset to Repurpose: {plan.get('existing_asset', 'Starting fresh')}

Please create a complete lead magnet strategy:

1. Magnet Type Recommendation
   - Recommended type: [quiz/giveaway/webinar/tool/report/checklist/template/ebook]
   - Expected conversion rate: [X%]
   - Why this type for this audience
   - Alternative options (if different preference)

2. Lead Magnet Details
   a) Headline (curiosity gap + specificity)
      - Main headline
      - Subheading
      - Value promise (time investment, outcome)

   b) Description (3-4 bullet points)
      - What they'll learn/get
      - Why now matters
      - Social proof (optional)

   c) Signup Form
      - Required fields (email + 2-3 key fields max)
      - Field labels (benefit-focused)
      - Microcopy (reassurance)
      - CTA button text (action + outcome)

3. Landing Page Copy
   - Hero section (headline + subheading + CTA)
   - Benefits section (3 key benefits)
   - Social proof (testimonials/numbers)
   - FAQ (3-5 common objections)
   - Final CTA

4. Email Sequence (Post-Signup)
   Email 1 (Immediate): Welcome + Bonus + Next Step
   Email 2 (Day 1): Deliver magnet + Quick win
   Email 3 (Day 3): Social proof + Similar users winning
   Email 4 (Day 5): Objection handling
   Email 5 (Day 7): Final pitch + Urgency

5. Conversion Targets
   - Signup rate target: [based on magnet type]
   - Form completion rate: >80%
   - Email open rate (welcome): >40%
   - Click-through to product: >5%

6. A/B Testing Plan
   - Test 1: Headline (generic vs specific)
   - Test 2: Magnet type (if uncertain)
   - Test 3: Form fields (3 vs 5)
   - Metric: Signup rate

7. Mobile Optimization
   - Responsive design notes
   - Mobile-first form layout
   - Touch-friendly CTA button

8. Accessibility
   - WCAG 2.2 compliance
   - Color contrast ratios
   - Alt text for images
   - Keyboard navigation
"""

        response = self.send_message(request, self.skill_context)

        return {
            "agent": self.name,
            "status": "completed",
            "input": plan,
            "output": response,
            "type": "lead_magnets"
        }
