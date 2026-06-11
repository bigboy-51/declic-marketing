"""Declic Marketing Agent SDK - Complete (Phase 1 + 2 + 3)"""

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
    DesignAgent,
    FunnelAgent,
)
from agents.utility_agents.coherence_agent import CoherenceAgent
from agents.utility_agents.metrics_agent import MetricsAgent
from agents.utility_agents.optimization_agent import OptimizationAgent

__version__ = "0.3.0"  # Phase 3 Complete
__all__ = [
    "OrchestrationAgent",
    # Phase 1 Skill Agents
    "CopywritingAgent",
    "BloggingAgent",
    "YouTubeAgent",
    # Phase 2 Skill Agents
    "BrandingAgent",
    "SEOAIOAgent",
    "ThumbnailsAgent",
    "LeadMagnetsAgent",
    "CloserAgent",
    # Phase 3 Skill Agents
    "DesignAgent",
    "FunnelAgent",
    # Utility Agents
    "CoherenceAgent",
    "MetricsAgent",
    "OptimizationAgent",
]
