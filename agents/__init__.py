"""Declic Marketing Agent SDK - Phase 1 MVP"""

from agents.orchestration_agent import OrchestrationAgent
from agents.skill_agents.copywriting_agent import CopywritingAgent
from agents.skill_agents.blogging_agent import BloggingAgent
from agents.skill_agents.youtube_agent import YouTubeAgent
from agents.utility_agents.coherence_agent import CoherenceAgent

__version__ = "0.1.0"
__all__ = [
    "OrchestrationAgent",
    "CopywritingAgent",
    "BloggingAgent",
    "YouTubeAgent",
    "CoherenceAgent",
]
