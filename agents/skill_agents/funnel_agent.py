"""Funnel skill agent for multi-step conversion optimization."""

from agents.base_agent import BaseAgent
from agents.config.agent_config import AgentRole, SKILLS_DIR


class FunnelAgent(BaseAgent):
    """Creates and optimizes multi-step marketing funnels."""

    FUNNEL_PROMPT = """You are the Funnel Agent. Your role is to design high-converting funnels.

Responsibility:
- Define funnel stages (awareness → consideration → conversion → retention)
- Optimize each stage for conversion
- Identify and fix drop-off points
- Design funnel variations for different segments
- Setup funnel tracking and analytics
- A/B test funnel elements

Benchmarks (2026):
- Average conversion rate: 3.1%
- Top quartile: 6.8%
- Elite performers: 9.2%

Think in terms of:
- Awareness funnel (attract qualified traffic)
- Consideration funnel (build interest)
- Conversion funnel (close deals)
- Retention funnel (customer success, upsell)
- Referral funnel (viral growth)

Your output should be:
- Funnel stage breakdown
- Traffic and conversion targets
- Copy and creative for each stage
- Technology stack needed
- Testing priorities
- Optimization roadmap
"""

    def __init__(self):
        super().__init__(
            name=AgentRole.FUNNEL,
            system_prompt=self.FUNNEL_PROMPT
        )
        self.skill_file = SKILLS_DIR / "funnel" / "SKILL.md"
        self.skill_context = self.add_skill_context(self.skill_file)

    def execute(self, plan: dict) -> dict:
        """
        Execute funnel design task.

        Args:
            plan: {
                "product_name": str,
                "target_audience": str,
                "ideal_customer_profile": str,
                "current_cac": float,  # Cost per acquisition
                "current_ltv": float,  # Lifetime value
                "conversion_goal": float,  # Target conversion rate
                "traffic_channels": list,  # ["content", "ads", "referral", etc]
                "sales_cycle": str,  # "1 day", "30 days", "6 months"
                "key_objections": list
            }
        """
        channels_str = ", ".join(plan.get('traffic_channels', ['organic'])) if plan.get('traffic_channels') else "Organic"
        objections_str = ", ".join(plan.get('key_objections', [])) if plan.get('key_objections') else "To be identified"

        request = f"""
Product: {plan.get('product_name', 'Your Product')}
Target Audience: {plan.get('target_audience', 'Not specified')}
Ideal Customer Profile: {plan.get('ideal_customer_profile', 'To be defined')}
Current CAC: ${plan.get('current_cac', 'Not tracked')}
Current LTV: ${plan.get('current_ltv', 'Not tracked')}
Target Conversion Rate: {plan.get('conversion_goal', '5')}%
Traffic Channels: {channels_str}
Sales Cycle: {plan.get('sales_cycle', '30 days')}
Key Objections: {objections_str}

Please design a complete funnel:

1. Funnel Architecture
   - Stage 1: AWARENESS (attract prospects)
     * Goal: Reach 10,000 qualified visitors
     * Channel 1: [Channel with messaging]
     * Channel 2: [Channel with messaging]
     * Expected CTR to next stage: X%

   - Stage 2: CONSIDERATION (build interest)
     * Goal: Get 1,000 signups
     * Content: Lead magnet, comparison, social proof
     * Nurture: 3-5 email sequence
     * Time to next stage: X days
     * Expected conversion to stage 3: X%

   - Stage 3: CONVERSION (close)
     * Goal: 50-100 paying customers
     * Sales process: Demo, trial, call, etc
     * Pricing presentation: [Strategy]
     * Objection handling: [For key objections]
     * Close rate target: X%
     * Sales cycle: X days

   - Stage 4: RETENTION (customer success)
     * Goal: 90%+ retention
     * Onboarding: X days
     * Support model: [Tier 1, 2, 3]
     * Expansion playbook: Upsell, cross-sell

   - Stage 5: REFERRAL (viral loop)
     * Goal: X% of customers refer others
     * Incentive: [What do they get?]
     * Ease of sharing: [Method]
     * Tracking: How to measure

2. Traffic & Conversion Model
   ```
   Awareness:     10,000 visitors
   ↓ X% CTR
   Consideration: 1,000 signups
   ↓ Y% conversion
   Conversion:    100 customers
   ↓ Z% retention
   Retained:      90 customers
   ↓ A% referral
   Referred:      10 new customers
   ```

   Monthly projection:
   - New customers: X
   - Revenue: $Y
   - CAC: $Z
   - LTV: $A
   - CLTV (payback): X months

3. Channel-Specific Funnels
   For each traffic channel:
   - [Channel name]: Funnel variant
     * Audience segment
     * Message angle
     * Conversion targets
     * Cost per stage

4. Content & Copy by Stage

   Awareness Stage:
   - Blog post: [Topic]
   - Video: [Hook for YouTube/TikTok]
   - Ad copy: [Platform-specific]
   - CTA: [Soft (awareness)]

   Consideration Stage:
   - Lead magnet: [Type + benefit]
   - Email sequence: [5-email outline]
   - Case study: [Customer success story]
   - Testimonial: [Specific benefit highlighted]
   - CTA: [Medium (consideration)]

   Conversion Stage:
   - Demo script: [Discovery-first]
   - Objection responses: [For key objections]
   - Pricing page: [Positioning]
   - Contract/Terms: [Risk reduction]
   - CTA: [Hard (action)]

5. Optimization Priorities

   Quick Wins (Week 1):
   - [High-impact, low-effort change]
   - [Faster wins first]

   Phase 1 (Weeks 1-4):
   - Test 1: [Awareness message variant]
   - Test 2: [Lead magnet type]
   - Test 3: [Email subject line]

   Phase 2 (Weeks 5-8):
   - Test 4: [Landing page variant]
   - Test 5: [Pricing presentation]
   - Test 6: [Call script variant]

   Phase 3 (Weeks 9-12):
   - Scaling what works
   - Advanced personalization
   - Retention optimization

6. Technology Stack
   - Landing page: [Tool]
   - Email marketing: [Platform]
   - CRM: [System]
   - Analytics: [GA4, custom tracking]
   - Automation: [Zapier, Make, etc]
   - Payment: [Stripe, etc]

7. Metrics & Tracking
   - Awareness stage metric: [Traffic quality, engagement]
   - Consideration metric: [Signup rate, email open rate]
   - Conversion metric: [Trial signup, demo booking, deal closed]
   - Retention metric: [Month 1 + 3 + 6 retention]
   - Referral metric: [NPS, viral coefficient]

8. Benchmark Comparison
   - Industry average conversion: 3.1%
   - Your target: {plan.get('conversion_goal', '5')}%
   - Path to top quartile: 6.8%
   - Path to elite: 9.2%

9. 90-Day Roadmap
   - Weeks 1-4: Funnel setup + quick wins
   - Weeks 5-8: Optimization + testing
   - Weeks 9-12: Scaling + refinement
   - Expected improvement: [X% conversion lift]

10. Risk & Mitigation
    - Risk 1: [Low conversion stage]
      * Solution: [Specific test]
    - Risk 2: [High CAC]
      * Solution: [Channel optimization]
"""

        response = self.send_message(request, self.skill_context)

        return {
            "agent": self.name,
            "status": "completed",
            "input": plan,
            "output": response,
            "type": "funnel"
        }
