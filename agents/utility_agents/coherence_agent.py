"""Coherence utility agent for output verification."""

import json
from agents.base_agent import BaseAgent
from agents.config.agent_config import AgentRole, COHERENCE_AGENT_PROMPT


class CoherenceAgent(BaseAgent):
    """Verifies that marketing outputs are coherent and brand-aligned."""

    def __init__(self):
        super().__init__(
            name=AgentRole.COHERENCE,
            system_prompt=COHERENCE_AGENT_PROMPT
        )

    def execute(self, outputs: list, brand_guidelines: dict = None) -> dict:
        """
        Verify coherence across multiple outputs.

        Args:
            outputs: List of outputs from skill agents
            brand_guidelines: Optional brand guidelines dict with:
                - voice: str
                - tone: str
                - positioning: str
                - target_audience: str
                - value_proposition: str
        """
        # Prepare brand context
        brand_info = ""
        if brand_guidelines:
            brand_info = f"""
Brand Guidelines for Coherence Check:
- Voice: {brand_guidelines.get('voice', 'Not specified')}
- Tone: {brand_guidelines.get('tone', 'Not specified')}
- Positioning: {brand_guidelines.get('positioning', 'Not specified')}
- Target Audience: {brand_guidelines.get('target_audience', 'Not specified')}
- Value Proposition: {brand_guidelines.get('value_proposition', 'Not specified')}
"""

        # Prepare outputs summary
        outputs_summary = ""
        for i, output in enumerate(outputs, 1):
            agent_type = output.get('type', 'unknown')
            agent_name = output.get('agent', 'Unknown Agent')
            content = output.get('output', '')[:500]  # First 500 chars
            outputs_summary += f"\n--- Output {i} ({agent_type} from {agent_name}) ---\n{content}...\n"

        # Build verification request
        request = f"""
{brand_info}

Please analyze the following marketing outputs for coherence:
{outputs_summary}

Check for:
1. Consistent brand voice and tone
2. Aligned messaging and positioning
3. Consistent target audience understanding
4. Aligned value proposition
5. Consistent call-to-action strategy
6. Overall brand coherence

Respond with JSON containing:
{{
    "is_coherent": true/false,
    "coherence_score": 0-100,
    "issues": ["issue1", "issue2"],
    "strengths": ["strength1", "strength2"],
    "suggestions": ["suggestion1", "suggestion2"]
}}
"""

        # Get response
        response = self.send_message(request)

        # Parse JSON response
        try:
            # Extract JSON from response
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            if json_start >= 0 and json_end > json_start:
                json_str = response[json_start:json_end]
                coherence_result = json.loads(json_str)
            else:
                coherence_result = {
                    "is_coherent": False,
                    "coherence_score": 0,
                    "issues": ["Could not parse coherence analysis"],
                    "strengths": [],
                    "suggestions": []
                }
        except json.JSONDecodeError:
            coherence_result = {
                "is_coherent": False,
                "coherence_score": 0,
                "issues": ["JSON parse error in coherence check"],
                "strengths": [],
                "suggestions": [],
                "raw_response": response
            }

        return {
            "agent": self.name,
            "status": "completed",
            "output_count": len(outputs),
            "coherence_check": coherence_result,
            "type": "verification"
        }
