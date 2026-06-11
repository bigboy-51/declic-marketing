"""Declic Marketing Agent SDK - Phase 1 MVP + Phase 2 Expansion"""

from agents.orchestration_agent import OrchestrationAgent
from agents.skill_agents import (
    CopywritingAgent,
    BloggingAgent,
    YouTubeAgent,
    BrandingAgent,
    SEOAIOAgent,
    ThumbnailsAgent,
    LeadMagnetsAgent,
    CloserAgent,
)
from agents.utility_agents.coherence_agent import CoherenceAgent

__version__ = "0.2.0"  # Phase 2
__all__ = [
    "OrchestrationAgent",
    # Phase 1 Agents
    "CopywritingAgent",
    "BloggingAgent",
    "YouTubeAgent",
    # Phase 2 Agents
    "BrandingAgent",
    "SEOAIOAgent",
    "ThumbnailsAgent",
    "LeadMagnetsAgent",
    "CloserAgent",
    # Utility
    "CoherenceAgent",
]
