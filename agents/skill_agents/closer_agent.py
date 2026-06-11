"""Closer skill agent for sales sequences and objection handling."""

from agents.base_agent import BaseAgent
from agents.config.agent_config import AgentRole, SKILLS_DIR


class CloserAgent(BaseAgent):
    """Creates email sequences, call scripts, and objection handling strategies."""

    CLOSER_PROMPT = """You are the Closer Agent. Your role is to close deals through strategic sequences and handling objections.

Frameworks:
- Email sequences: 5-email nurture → trial → conversion
- Call scripts: Discovery-first approach (listen 70%, talk 30%)
- Objection handling: 5 psychological frameworks

Key Principles:
1. Listen more than you talk
2. Objections = Legitimate concerns (not brush-offs)
3. Pause 3+ seconds before responding (thoughtful, not reactive)
4. One ask per conversation/email
5. Data-backed responses (specific numbers, not vague)

Behavioral Economics:
- Loss aversion: "Waiting costs you $X"
- Scarcity: Limited spots/deadline
- Social proof: "Others like you are doing this"
- Reciprocity: Give free assessment, they feel obligated
- Anchoring: "Alternative costs $5K, ours is $2K"
"""

    def __init__(self):
        super().__init__(
            name=AgentRole.CLOSER,
            system_prompt=self.CLOSER_PROMPT
        )
        self.skill_file = SKILLS_DIR / "closer" / "SKILL.md"
        self.skill_context = self.add_skill_context(self.skill_file)

    def execute(self, plan: dict) -> dict:
        """
        Execute closer/sales strategy task.

        Args:
            plan: {
                "sales_stage": str,  # "lead_nurture", "trial_conversion", "objection_handling"
                "audience": str,
                "product_benefit": str,
                "pricing": str,
                "common_objections": list,  # ["too expensive", "want to think about it", etc]
                "call_type": str  # "discovery", "demo", "closing"
            }
        """
        objections_str = ", ".join(plan.get('common_objections', [])) if plan.get('common_objections') else "To be identified"
        sales_stage = plan.get('sales_stage', 'lead_nurture')

        request = f"""
Sales Stage: {sales_stage}
Target Audience: {plan.get('audience', 'Not specified')}
Product Benefit: {plan.get('product_benefit', 'Not specified')}
Pricing: {plan.get('pricing', 'Not specified')}
Common Objections: {objections_str}
Call Type: {plan.get('call_type', 'discovery')}

Please create:

1. Email Sequence (5-email nurture to conversion)

   Email 1 (Immediate): Welcome + Quick Win
   - Subject line (emotional trigger)
   - Hook: [curiosity gap or pattern interrupt]
   - Quick win they can do today
   - Light CTA (not pushy)

   Email 2 (Day 1): First Result
   - Subject: Specific benefit achieved
   - Social proof: Their quick win validated
   - Offer next step
   - Psychological trigger: Proof it works

   Email 3 (Day 3): Social Proof + Urgency
   - Success story similar to them
   - Scarcity element (limited spots)
   - Benefits of moving fast
   - Clear CTA

   Email 4 (Day 5): Objection Pre-Handling
   - Address main concern proactively
   - Risk reversal (guarantee, trial, etc)
   - Data-backed promise
   - CTA

   Email 5 (Day 7): Last Chance + Direct Ask
   - Specific deadline (hard stop)
   - Price anchor (what they'd pay for alternative)
   - Direct ask for decision
   - Consequence of waiting

2. Call Script (15-20 minute discovery call)

   [0:00-1:00] OPENING (Rapport + Agenda)
   - Build trust
   - Set time boundary
   - Clear promise: "We'll figure out if this is a fit"

   [1:00-7:00] DISCOVERY (Listen 80%)
   - Open-ended question about frustration
   - Follow-ups to understand THEIR situation
   - Listen for emotional intensity
   - Take notes

   [7:00-10:00] BUILD CREDIBILITY
   - Show you've solved this before
   - Specific example (not generic)
   - Data point they can relate to

   [10:00-12:00] CURIOSITY (Make them want it)
   - Counterintuitive insight
   - What this means for their situation
   - Pause, let it sink in

   [12:00-15:00] BRIDGE (Connect pain to solution)
   - "If we could do [their goal], would that be worth exploring?"
   - Listen for commitment level
   - Don't oversell

   [15:00-18:00] CLOSE (Ask for next step, not sale)
   - Suggest low-friction next step
   - Assessment, trial, short call
   - Schedule firmly (not "I'll reach out")

   [18:00-20:00] CONFIRM (Recap + Lock in)
   - Repeat all details
   - Confirm everything
   - End on positive note

3. Objection Handling (For each common objection)

   Pattern: PAUSE → EMPATHIZE → CLARIFY → REFRAME → MOVE FORWARD

   For each objection:
   - Pause (3+ seconds, think don't react)
   - Empathize ("I get why you'd feel that way")
   - Clarify ("Help me understand...")
   - Reframe (Use 1 of 5 frameworks: Cognitive Reframing, Tactical Empathy, Solution Bridging, Social Proof, Curiosity)
   - Move Forward ("Given that, does this make sense?")

4. Success Metrics
   - Email sequence CTR target: >5%
   - Call-to-close rate: >30% (1 in 3 calls convert)
   - Objection resolution rate: >60%
   - Sales cycle length: 7-14 days

5. Behavioral Economics Application
   - Loss aversion trigger: [specific application]
   - Scarcity trigger: [specific application]
   - Social proof trigger: [specific application]
   - Reciprocity trigger: [specific application]
   - Anchoring: [price comparison example]

6. Quality Checklist
   - ✓ Genuine (not manipulative)
   - ✓ Specific to their situation (not generic)
   - ✓ Empathetic (acknowledge concern first)
   - ✓ Data-backed (real numbers)
   - ✓ One ask per conversation
   - ✓ Patient (doesn't rush)
   - ✓ Followable (repeatable consistently)
"""

        response = self.send_message(request, self.skill_context)

        return {
            "agent": self.name,
            "status": "completed",
            "input": plan,
            "output": response,
            "type": "closer"
        }
