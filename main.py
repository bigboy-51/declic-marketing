#!/usr/bin/env python3
"""
Phase 1 MVP: Declic Marketing Agent SDK Demo

This demonstrates the complete orchestration workflow:
User Request → Orchestration Agent → Skill Agents → Coherence Check → Campaign Output
"""

import os
import json
from pathlib import Path
from agents import OrchestrationAgent


def load_brand_guidelines() -> dict:
    """Load brand guidelines for Declic Financier."""
    return {
        "voice": "Confident, knowledgeable, accessible",
        "tone": "Professional yet conversational",
        "positioning": "Making investing accessible to busy professionals",
        "target_audience": "Busy professionals seeking passive income",
        "value_proposition": "Automated portfolio management with 2-3x returns vs. traditional approaches"
    }


def demo_campaign() -> None:
    """Run a demo campaign to showcase the agent system."""
    print("\n" + "="*80)
    print("DECLIC MARKETING AGENT SDK - PHASE 1 MVP DEMO")
    print("="*80)

    # Initialize orchestration agent
    print("\nInitializing Orchestration Agent...")
    orchestrator = OrchestrationAgent()
    print("✓ Orchestration Agent ready\n")

    # Brand guidelines
    brand_guidelines = load_brand_guidelines()

    # Demo request
    user_request = "Campaign: Build $50K Passive Income with Automated Portfolio Management"

    # Execute the full workflow
    result = orchestrator.handle_request(user_request, brand_guidelines)

    # Display results
    print("="*80)
    print("CAMPAIGN RESULTS")
    print("="*80)
    print(result.get('summary', ''))

    # Detailed output
    print("\n" + "="*80)
    print("DETAILED OUTPUTS BY AGENT")
    print("="*80)

    for output in result.get('agent_outputs', []):
        if output.get('status') == 'completed':
            agent = output.get('agent', 'Unknown')
            output_type = output.get('type', 'unknown')

            print(f"\n{'─'*80}")
            print(f"Agent: {agent.upper()}")
            print(f"Type: {output_type}")
            print(f"{'─'*80}")

            # Show first 1000 chars of output
            full_output = output.get('output', '')
            preview = full_output[:1000] + "..." if len(full_output) > 1000 else full_output
            print(preview)

    # Coherence analysis
    print("\n" + "="*80)
    print("BRAND COHERENCE ANALYSIS")
    print("="*80)

    coherence = result.get('coherence_check', {})
    print(f"\nCoherence Score: {coherence.get('coherence_score', 'N/A')}/100")
    print(f"Status: {'✓ COHERENT' if coherence.get('is_coherent') else '⚠ REVIEW NEEDED'}")

    if coherence.get('issues'):
        print("\nIssues Identified:")
        for issue in coherence.get('issues', []):
            print(f"  • {issue}")

    if coherence.get('suggestions'):
        print("\nSuggestions:")
        for suggestion in coherence.get('suggestions', []):
            print(f"  • {suggestion}")

    if coherence.get('strengths'):
        print("\nStrengths:")
        for strength in coherence.get('strengths', []):
            print(f"  ✓ {strength}")

    # Save results to file
    output_file = Path(__file__).parent / "campaign_output.json"
    with open(output_file, 'w') as f:
        # Convert to JSON-serializable format
        json_result = {
            "request": result.get('user_request'),
            "status": result.get('status'),
            "agents_executed": len(result.get('agent_outputs', [])),
            "coherence_score": coherence.get('coherence_score'),
            "coherence_issues": coherence.get('issues', []),
            "summary": result.get('summary', '')
        }
        json.dump(json_result, f, indent=2)

    print(f"\n✓ Full results saved to: {output_file}")
    print("\n" + "="*80)


def interactive_mode() -> None:
    """Run in interactive mode for custom requests."""
    print("\n" + "="*80)
    print("DECLIC MARKETING AGENT SDK - INTERACTIVE MODE")
    print("="*80)

    orchestrator = OrchestrationAgent()
    brand_guidelines = load_brand_guidelines()

    print("\nEnter your campaign request (or 'quit' to exit):")
    print("Examples:")
    print("  - Campaign: Help busy professionals build $100K passive income")
    print("  - Campaign: Tax-efficient portfolio management strategies")
    print("  - Campaign: Automated rebalancing for millennial investors\n")

    while True:
        user_input = input("\n> ").strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break

        if not user_input:
            continue

        try:
            result = orchestrator.handle_request(user_input, brand_guidelines)
            print(result.get('summary', ''))

            # Show brief coherence result
            coherence = result.get('coherence_check', {})
            print(f"\nCoherence Score: {coherence.get('coherence_score', 'N/A')}/100")

        except Exception as e:
            print(f"Error processing request: {str(e)}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        interactive_mode()
    else:
        demo_campaign()
