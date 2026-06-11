"""Metrics utility agent for analytics and performance tracking."""

from agents.base_agent import BaseAgent
from agents.config.agent_config import AgentRole, SKILLS_DIR


class MetricsAgent(BaseAgent):
    """Sets up tracking, defines KPIs, and monitors campaign performance."""

    METRICS_PROMPT = """You are the Metrics Agent. Your role is to establish measurement frameworks.

Responsibility:
- Define success metrics for campaigns
- Setup analytics tracking (GA4, product analytics, conversion tracking)
- Create dashboards for real-time monitoring
- Establish KPI targets and benchmarks
- Identify leading vs lagging indicators
- Recommend attribution models

Think in terms of:
- Acquisition metrics (traffic, clicks, impressions, reach)
- Activation metrics (signups, form completions, onboarding)
- Retention metrics (return rate, engagement, churn)
- Revenue metrics (conversions, AOV, LTV, CAC)
- Referral metrics (viral coefficient, NPS, share rate)

Your output should be:
- Clear metric definitions
- Implementation requirements
- Tracking setup (GA4, events, parameters)
- Dashboard specifications
- Alert thresholds
- Weekly/monthly reporting structure
"""

    def __init__(self):
        super().__init__(
            name=AgentRole.METRICS,
            system_prompt=self.METRICS_PROMPT
        )

    def execute(self, plan: dict) -> dict:
        """
        Execute metrics setup task.

        Args:
            plan: {
                "campaign_type": str,
                "success_goal": str,
                "audience": str,
                "channels": list,  # ["email", "blog", "video", "social"]
                "timeline": str,  # "30 days", "quarterly", etc
                "existing_tools": list,  # GA4, Mixpanel, etc
                "reporting_frequency": str  # "weekly", "daily", etc
            }
        """
        channels_str = ", ".join(plan.get('channels', ['email'])) if plan.get('channels') else "Email"
        tools_str = ", ".join(plan.get('existing_tools', [])) if plan.get('existing_tools') else "None specified"

        request = f"""
Campaign Type: {plan.get('campaign_type', 'Not specified')}
Success Goal: {plan.get('success_goal', 'Not specified')}
Target Audience: {plan.get('audience', 'Not specified')}
Channels: {channels_str}
Timeline: {plan.get('timeline', '30 days')}
Analytics Tools Available: {tools_str}
Reporting Frequency: {plan.get('reporting_frequency', 'weekly')}

Please create a comprehensive metrics framework:

1. Success Metrics Definition
   - Primary metric (the ONE number that matters)
   - Secondary metrics (3-5 supporting metrics)
   - How each is calculated
   - Target values (realistic benchmarks)

2. Analytics Setup
   - GA4 events to track (names, parameters)
   - Conversion tracking (goals, micro conversions)
   - User property definitions
   - Custom dimensions/metrics
   - Audience segments

3. Tracking Implementation
   - Event names standardization
   - Parameter structure
   - Cross-domain tracking (if applicable)
   - Attribution window setting

4. Dashboard Specifications
   a) Real-time Dashboard
      - Top-level KPIs (what to check first thing)
      - Live conversion funnel
      - Channel performance
      - Refresh frequency

   b) Weekly Summary
      - Week-over-week trends
      - Channel attribution breakdown
      - Top performers (content, offers, creatives)
      - Issues/anomalies

   c) Monthly Deep-Dive
      - Campaign ROI analysis
      - Cohort analysis
      - Retention curves
      - LTV calculations
      - CAC by channel

5. Alerts & Monitoring
   - Alert threshold 1: [metric drops X%]
   - Alert threshold 2: [conversion rate below X%]
   - Alert threshold 3: [unusual traffic pattern]
   - Response protocol (when alerts fire)

6. Reporting Template
   - {plan.get('reporting_frequency', 'Weekly')} report structure
   - Key sections (what to highlight)
   - Stakeholder communication (execs vs teams)
   - Action items section

7. A/B Testing Framework
   - Statistical significance required
   - Minimum sample size
   - Test duration
   - Metric to optimize
   - Reporting cadence

8. Attribution Model
   - Recommended model (first-touch, last-touch, linear, time-decay, data-driven)
   - Why this model for this campaign
   - How to implement

9. Benchmarks & Targets
   - Industry benchmarks (for comparison)
   - Current baseline (if existing campaign)
   - Realistic targets (30 days, 90 days, 1 year)
   - Stretch goals
"""

        response = self.send_message(request, include_hooks=False)

        return {
            "agent": self.name,
            "status": "completed",
            "input": plan,
            "output": response,
            "type": "metrics"
        }
