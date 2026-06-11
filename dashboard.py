#!/usr/bin/env python3
"""
Declic Marketing Agent SDK - Dashboard
Simple visual interface for agent orchestration
"""

import streamlit as st
import json
from datetime import datetime
from agents import OrchestrationAgent

# Page configuration
st.set_page_config(
    page_title="Declic Marketing Agent SDK",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .agent-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #1f77b4;
    }
    .agent-success {
        background-color: #d4edda;
        border-left-color: #28a745;
    }
    .agent-processing {
        background-color: #fff3cd;
        border-left-color: #ffc107;
    }
    .agent-error {
        background-color: #f8d7da;
        border-left-color: #dc3545;
    }
    .coherence-high {
        color: #28a745;
        font-weight: bold;
    }
    .coherence-medium {
        color: #ffc107;
        font-weight: bold;
    }
    .coherence-low {
        color: #dc3545;
        font-weight: bold;
    }
    .metric-card {
        padding: 15px;
        border-radius: 8px;
        background-color: #f0f2f6;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🚀 Declic Marketing Agent SDK")
st.markdown("**Real-time orchestration dashboard for coordinated marketing campaigns**")
st.divider()

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Configuration")

    brand_guidelines = {
        "voice": st.text_input(
            "Brand Voice",
            "Confident, knowledgeable, accessible"
        ),
        "tone": st.text_input(
            "Brand Tone",
            "Professional yet conversational"
        ),
        "positioning": st.text_input(
            "Positioning",
            "Making investing accessible"
        ),
        "target_audience": st.text_input(
            "Target Audience",
            "Busy professionals seeking passive income"
        ),
        "value_proposition": st.text_input(
            "Value Proposition",
            "Automated portfolio management"
        )
    }

    st.divider()
    st.markdown("## 📊 About")
    st.info("""
    **Phase 1 MVP Features:**
    - Orchestration Agent
    - Copywriting Agent
    - Blogging Agent
    - YouTube Agent
    - Coherence Verification

    **Response time:** 30-60 sec
    """)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## 📝 Campaign Request")
    user_request = st.text_area(
        "Enter your campaign brief:",
        "Campaign: Build $50K Passive Income with Automated Portfolio Management",
        height=100,
        label_visibility="collapsed"
    )

with col2:
    st.markdown("## 🎯 Quick Templates")
    if st.button("📈 Passive Income", use_container_width=True):
        st.session_state.request = "Campaign: Build $50K Passive Income with Automated Portfolio Management"
    if st.button("🛡️ Risk Management", use_container_width=True):
        st.session_state.request = "Campaign: Protect Your Portfolio with Intelligent Risk Management"
    if st.button("💰 Tax Efficiency", use_container_width=True):
        st.session_state.request = "Campaign: Maximize Returns with Tax-Efficient Portfolio Strategies"
    if st.button("🎓 Beginner Guide", use_container_width=True):
        st.session_state.request = "Campaign: Start Investing: A Complete Beginner's Guide"

st.divider()

# Execute button
if st.button("🚀 Launch Campaign", use_container_width=True, type="primary"):

    if not user_request.strip():
        st.error("❌ Please enter a campaign request")
    else:
        st.session_state.executing = True

        # Create placeholder for progress
        progress_placeholder = st.empty()
        status_placeholder = st.empty()

        with progress_placeholder.container():
            st.markdown("### 📊 Execution Progress")
            progress_bar = st.progress(0)

        try:
            # Initialize orchestrator
            with status_placeholder.container():
                st.info("🔄 Initializing Orchestration Agent...")
            progress_bar.progress(10)

            orchestrator = OrchestrationAgent()

            # Step 1: Parse request
            with status_placeholder.container():
                st.info("📋 Parsing campaign request...")
            progress_bar.progress(20)

            # Step 2: Execute campaign
            with status_placeholder.container():
                st.info("⚡ Executing skill agents...")

            result = orchestrator.handle_request(user_request, brand_guidelines)

            progress_bar.progress(90)

            # Step 3: Display results
            progress_placeholder.empty()
            status_placeholder.empty()

            st.success("✅ Campaign execution completed!")
            progress_bar.progress(100)

            st.divider()

            # Results section
            st.markdown("## 📊 Campaign Results")

            # Coherence metrics
            coherence = result.get('coherence_check', {})
            coherence_score = coherence.get('coherence_score', 0)

            metric_col1, metric_col2, metric_col3 = st.columns(3)

            with metric_col1:
                st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                st.markdown("**Agents Executed**")
                st.markdown(f"<h2>{len(result.get('agent_outputs', []))}/3</h2>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

            with metric_col2:
                st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                st.markdown("**Coherence Score**")
                if coherence_score >= 75:
                    color_class = "coherence-high"
                elif coherence_score >= 50:
                    color_class = "coherence-medium"
                else:
                    color_class = "coherence-low"
                st.markdown(f"<h2><span class='{color_class}'>{coherence_score}/100</span></h2>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

            with metric_col3:
                st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
                st.markdown("**Status**")
                status = "✅ Coherent" if coherence.get('is_coherent') else "⚠️ Review"
                st.markdown(f"<h2>{status}</h2>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

            st.divider()

            # Agent outputs
            st.markdown("## 🤖 Agent Outputs")

            for i, output in enumerate(result.get('agent_outputs', []), 1):
                if output.get('status') == 'completed':
                    agent_name = output.get('agent', 'Unknown').upper()
                    output_type = output.get('type', 'unknown')

                    with st.expander(f"✅ {agent_name} — {output_type}", expanded=(i==1)):
                        # Show output preview
                        full_output = output.get('output', '')

                        # Create tabs for different views
                        tab1, tab2 = st.tabs(["📄 Full Output", "📊 Summary"])

                        with tab1:
                            st.markdown(full_output)

                        with tab2:
                            # Show first 500 chars as summary
                            summary = full_output[:500] + "..." if len(full_output) > 500 else full_output
                            st.text(summary)
                            st.caption(f"Total length: {len(full_output)} characters")

                elif output.get('status') == 'error':
                    agent_name = output.get('agent', 'Unknown').upper()
                    error_msg = output.get('error', 'Unknown error')
                    st.error(f"❌ {agent_name} failed: {error_msg}")

            st.divider()

            # Coherence analysis
            st.markdown("## 🔍 Brand Coherence Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### Issues Found")
                if coherence.get('issues'):
                    for issue in coherence.get('issues', []):
                        st.warning(f"⚠️ {issue}")
                else:
                    st.success("✅ No brand coherence issues detected")

            with col2:
                st.markdown("### Suggestions")
                if coherence.get('suggestions'):
                    for suggestion in coherence.get('suggestions', []):
                        st.info(f"💡 {suggestion}")
                else:
                    st.success("✅ All aspects optimized")

            st.divider()

            # Strengths
            st.markdown("### ✨ Identified Strengths")
            if coherence.get('strengths'):
                for strength in coherence.get('strengths', []):
                    st.success(f"✓ {strength}")

            st.divider()

            # Download option
            st.markdown("## 💾 Export Results")

            export_col1, export_col2 = st.columns(2)

            with export_col1:
                # JSON export
                json_data = {
                    "timestamp": datetime.now().isoformat(),
                    "request": user_request,
                    "coherence_score": coherence_score,
                    "agent_count": len(result.get('agent_outputs', [])),
                    "coherence_issues": coherence.get('issues', []),
                    "coherence_suggestions": coherence.get('suggestions', [])
                }

                st.download_button(
                    label="📥 Download JSON",
                    data=json.dumps(json_data, indent=2),
                    file_name=f"campaign_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json",
                    use_container_width=True
                )

            with export_col2:
                # Markdown export
                markdown_content = f"""# Campaign Report
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Request
{user_request}

## Metrics
- Coherence Score: {coherence_score}/100
- Status: {'✅ Coherent' if coherence.get('is_coherent') else '⚠️ Review Needed'}

## Issues
{chr(10).join([f'- {issue}' for issue in coherence.get('issues', [])])}

## Suggestions
{chr(10).join([f'- {suggestion}' for suggestion in coherence.get('suggestions', [])])}
"""
                st.download_button(
                    label="📋 Download Markdown",
                    data=markdown_content,
                    file_name=f"campaign_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown",
                    use_container_width=True
                )

        except Exception as e:
            st.error(f"❌ Error during campaign execution: {str(e)}")
            st.exception(e)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #888; padding: 20px;'>
<small>Declic Marketing Agent SDK — Phase 1 MVP | Orchestration • Copywriting • Blogging • YouTube • Coherence</small>
</div>
""", unsafe_allow_html=True)
