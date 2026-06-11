"""Skill agents for marketing automation."""

from agents.skill_agents.copywriting_agent import CopywritingAgent
from agents.skill_agents.blogging_agent import BloggingAgent
from agents.skill_agents.youtube_agent import YouTubeAgent
from agents.skill_agents.branding_agent import BrandingAgent
from agents.skill_agents.seo_aio_agent import SEOAIOAgent
from agents.skill_agents.thumbnails_agent import ThumbnailsAgent
from agents.skill_agents.lead_magnets_agent import LeadMagnetsAgent
from agents.skill_agents.closer_agent import CloserAgent
from agents.skill_agents.design_agent import DesignAgent
from agents.skill_agents.funnel_agent import FunnelAgent

__all__ = [
    # Phase 1
    "CopywritingAgent",
    "BloggingAgent",
    "YouTubeAgent",
    # Phase 2
    "BrandingAgent",
    "SEOAIOAgent",
    "ThumbnailsAgent",
    "LeadMagnetsAgent",
    "CloserAgent",
    # Phase 3
    "DesignAgent",
    "FunnelAgent",
]
