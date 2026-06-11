"""Orchestration agent - master coordinator for all skill agents."""

from agents.base_agent import BaseAgent
from agents.config.agent_config import AgentRole
from agents.skill_agents.copywriting_agent import CopywritingAgent
from agents.skill_agents.blogging_agent import BloggingAgent
from agents.skill_agents.youtube_agent import YouTubeAgent
from agents.utility_agents.coherence_agent import CoherenceAgent


ORCHESTRATION_SYSTEM_PROMPT = """You are the Orchestration Agent. Your role is to:
1. Understand user requests for marketing campaigns or content
2. Break down requests into focused subtasks
3. Delegate to specialized skill agents
4. Coordinate outputs and ensure brand coherence
5. Compile and present final results

When receiving a request like "Campaign: $50K passive income", you should:
1. Identify the core campaign theme
2. Determine what content is needed (blog, copy, video script, etc.)
3. Create plans for each skill agent
4. Collect outputs from agents
5. Verify coherence across outputs
6. Return compiled campaign materials

Be strategic about which agents to activate based on the request.
"""


class OrchestrationAgent(BaseAgent):
    """Master coordinator for marketing automation agents."""

    def __init__(self):
        super().__init__(
            name=AgentRole.ORCHESTRATION,
            system_prompt=ORCHESTRATION_SYSTEM_PROMPT
        )
        # Initialize skill agents
        self.copywriting_agent = CopywritingAgent()
        self.blogging_agent = BloggingAgent()
        self.youtube_agent = YouTubeAgent()
        self.coherence_agent = CoherenceAgent()

    def handle_request(self, user_request: str, brand_guidelines: dict = None) -> dict:
        """
        Handle user request and coordinate agent responses.

        Args:
            user_request: Natural language request (e.g., "Campaign: $50K passive income")
            brand_guidelines: Optional brand guidelines for coherence check

        Returns:
            Compiled campaign outputs with coherence verification
        """
        print(f"\n{'='*60}")
        print(f"ORCHESTRATION AGENT - Processing Request")
        print(f"{'='*60}")
        print(f"Request: {user_request}\n")

        # Step 1: Parse request and create subplans
        subplans = self._create_subplans(user_request)
        print(f"Created {len(subplans)} subplans")
        for i, plan in enumerate(subplans, 1):
            print(f"  {i}. {plan.get('agent_type')}: {plan.get('description')}")
        print()

        # Step 2: Execute skill agents based on subplans
        outputs = self._execute_skill_agents(subplans)
        print(f"\nCollected outputs from {len(outputs)} agents\n")

        # Step 3: Verify coherence
        print("Running coherence check...")
        coherence_result = self.coherence_agent.execute(outputs, brand_guidelines)
        print(f"Coherence Score: {coherence_result['coherence_check'].get('coherence_score', 'N/A')}/100")
        if coherence_result['coherence_check'].get('issues'):
            print(f"Issues found: {len(coherence_result['coherence_check']['issues'])}")
            for issue in coherence_result['coherence_check']['issues'][:3]:
                print(f"  - {issue}")
        print()

        # Step 4: Compile final output
        final_output = {
            "status": "completed",
            "user_request": user_request,
            "subplans": subplans,
            "agent_outputs": outputs,
            "coherence_check": coherence_result['coherence_check'],
            "summary": self._create_summary(outputs, coherence_result)
        }

        return final_output

    def _create_subplans(self, user_request: str) -> list:
        """
        Parse user request and create execution plans for skill agents.
        """
        # For Phase 1 MVP, default to copywriting + blogging + youtube
        # In future, this would be smarter based on NLP analysis

        # Extract key info from request
        topic = user_request.split(":")[-1].strip() if ":" in user_request else user_request

        subplans = [
            {
                "agent_type": "copywriting",
                "description": f"High-converting copy for '{topic}'",
                "plan": {
                    "topic": topic,
                    "brand_voice": "Professional, confident, benefit-focused",
                    "target_audience": "Busy professionals seeking passive income",
                    "desired_outcome": "High conversion to trial/purchase",
                    "format": "sales_page"
                }
            },
            {
                "agent_type": "blogging",
                "description": f"Authority blog post about '{topic}'",
                "plan": {
                    "topic": topic,
                    "target_keyword": f"passive income from {topic.lower()}",
                    "length": "medium",
                    "target_audience": "Business professionals interested in financial growth",
                    "tone": "Educational and trustworthy",
                    "include_cta": True
                }
            },
            {
                "agent_type": "youtube",
                "description": f"YouTube script for '{topic}' video",
                "plan": {
                    "topic": topic,
                    "hook_type": "benefit",
                    "target_duration": 480,  # 8 minutes
                    "audience": "Business professionals seeking financial education",
                    "content_angle": "Educational with proven strategies",
                    "cta_type": "website"
                }
            }
        ]

        return subplans

    def _execute_skill_agents(self, subplans: list) -> list:
        """Execute skill agents based on subplans."""
        outputs = []

        for subplan in subplans:
            agent_type = subplan.get('agent_type')
            plan = subplan.get('plan', {})

            print(f"Executing {agent_type.capitalize()} Agent...")

            try:
                if agent_type == "copywriting":
                    output = self.copywriting_agent.execute(plan)
                elif agent_type == "blogging":
                    output = self.blogging_agent.execute(plan)
                elif agent_type == "youtube":
                    output = self.youtube_agent.execute(plan)
                else:
                    output = {
                        "agent": agent_type,
                        "status": "error",
                        "error": f"Unknown agent type: {agent_type}"
                    }

                outputs.append(output)
                print(f"  ✓ {agent_type.capitalize()} Agent completed\n")

            except Exception as e:
                print(f"  ✗ {agent_type.capitalize()} Agent failed: {str(e)}\n")
                outputs.append({
                    "agent": agent_type,
                    "status": "error",
                    "error": str(e)
                })

        return outputs

    def _create_summary(self, outputs: list, coherence_result: dict) -> str:
        """Create executive summary of campaign."""
        coherence_score = coherence_result['coherence_check'].get('coherence_score', 0)
        coherence_status = "✓ Coherent" if coherence_score >= 75 else "⚠ Review needed"

        summary = f"""
CAMPAIGN EXECUTION SUMMARY
==========================
Agents Executed: {len(outputs)}
Outputs Generated: {len([o for o in outputs if o.get('status') == 'completed'])}
Brand Coherence: {coherence_status} ({coherence_score}/100)

Output Types:
"""

        for output in outputs:
            if output.get('status') == 'completed':
                summary += f"\n  ✓ {output.get('type', 'unknown').upper()}"

        return summary
