"""Optimization utility agent for autonomous improvement cycles."""

from agents.base_agent import BaseAgent
from agents.config.agent_config import AgentRole


class OptimizationAgent(BaseAgent):
    """Analyzes performance data and recommends autonomous improvements."""

    OPTIMIZATION_PROMPT = """You are the Optimization Agent. Your role is to drive continuous improvement.

Responsibility:
- Analyze performance data and identify leaks/opportunities
- Recommend specific, testable improvements
- Prioritize tests by expected impact
- Design autonomous optimization loops
- Learn from test results

Think in terms of:
- Conversion funnel optimization (drop-off analysis)
- Copy and creative variations
- Timing and frequency optimization
- Audience segmentation refinement
- Channel mix optimization
- Landing page element testing

Always recommend:
1. Root cause analysis (why the problem exists)
2. Specific hypothesis (what to test)
3. Test design (variant A vs B vs C)
4. Expected lift (% improvement if successful)
5. Success metrics (how to measure)
6. Statistical significance threshold
7. Timeline (how long to run test)

Your output should be:
- Data insights (what the numbers tell us)
- Prioritized test queue (impact × confidence)
- Test designs (ready to implement)
- Learning from past tests (what worked, what didn't)
"""

    def __init__(self):
        super().__init__(
            name=AgentRole.OPTIMIZATION,
            system_prompt=self.OPTIMIZATION_PROMPT
        )

    def execute(self, plan: dict) -> dict:
        """
        Execute optimization analysis and testing recommendations.

        Args:
            plan: {
                "current_performance": dict,  # Key metrics: conversion rate, CTR, etc
                "time_period": str,
                "funnel_stage": str,  # "awareness", "consideration", "conversion"
                "problem_area": str,  # "low signup rate", "high bounce rate", etc
                "constraints": list,  # Budget, time, tech
                "past_tests": list  # What's been tested before
            }
        """
        perf = plan.get('current_performance', {})
        constraints_str = ", ".join(plan.get('constraints', [])) if plan.get('constraints') else "None"
        past_tests_str = ", ".join(plan.get('past_tests', [])) if plan.get('past_tests') else "None yet"

        request = f"""
Current Performance:
- Conversion Rate: {perf.get('conversion_rate', 'Not provided')}
- CTR: {perf.get('ctr', 'Not provided')}
- Email Open Rate: {perf.get('email_open_rate', 'Not provided')}
- Cost Per Acquisition: {perf.get('cpa', 'Not provided')}
- Customer Lifetime Value: {perf.get('ltv', 'Not provided')}
- Churn Rate: {perf.get('churn_rate', 'Not provided')}

Analysis Period: {plan.get('time_period', '30 days')}
Funnel Stage to Optimize: {plan.get('funnel_stage', 'conversion')}
Primary Problem: {plan.get('problem_area', 'Need improvement')}
Constraints: {constraints_str}
Past Tests Conducted: {past_tests_str}

Please analyze and provide:

1. Performance Diagnosis
   - What the data tells us
   - Where the biggest leak/opportunity is
   - Root cause analysis (why is this happening?)
   - How this compares to industry benchmarks

2. Optimization Opportunities (Ranked by Impact × Feasibility)

   Opportunity 1: [Specific improvement]
   - Current state: [Metric: X%]
   - Expected state: [Metric: X% → Y%]
   - Lift: [+Z%]
   - Hypothesis: [Why this will work]
   - Test design:
     * Variant A (Control): [Current approach]
     * Variant B: [Proposed change]
     * Variant C (Optional): [Alternative approach]
   - Sample size needed: [For statistical significance]
   - Test duration: [Days/weeks]
   - Success metric: [How to measure]
   - Confidence level: [High/Medium/Low]

   Opportunity 2: [Next priority]
   [Same structure]

   Opportunity 3: [Follow-up test]
   [Same structure]

3. Test Queue (In Priority Order)
   - Test 1 (Week 1): [Expected lift X%, Confidence: Y%]
   - Test 2 (Week 2): [Expected lift X%, Confidence: Y%]
   - Test 3 (Week 3): [Expected lift X%, Confidence: Y%]

4. Autonomous Optimization Loop
   - Week 1: Run Test 1 (A/B, 50/50 split, daily monitoring)
   - Day 7: Analyze Test 1 results
   - Week 2: Implement winner or new test
   - Weekly: Report lift vs baseline
   - Monthly: Review overall impact, adjust strategy

5. Quick Wins (Can implement immediately)
   - No test needed: [Change recommendation]
   - Expected lift: [X%]
   - Implementation: [Easy/Medium/Hard]

6. Learning from Data
   - What's working well (double down here)
   - What's not working (eliminate or redesign)
   - Unexpected findings (investigate further)

7. Tools & Setup
   - Analytics needed
   - Testing platform setup
   - Audience segmentation
   - Tracking modifications

8. 90-Day Improvement Plan
   - If all tests succeed: [Expected overall lift]
   - Monthly growth targets
   - Revenue impact projection

9. Risk Assessment
   - Downside risk (what could go wrong)
   - Mitigation (how to protect)
   - Rollback strategy (if test fails)
"""

        response = self.send_message(request, include_hooks=False)

        return {
            "agent": self.name,
            "status": "completed",
            "input": plan,
            "output": response,
            "type": "optimization"
        }
