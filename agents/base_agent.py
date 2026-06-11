"""Base agent class for all agents."""

import json
from abc import ABC, abstractmethod
from pathlib import Path
from anthropic import Anthropic

from config.agent_config import MODEL_NAME, MAX_TOKENS, TEMPERATURE


class BaseAgent(ABC):
    """Base class for all agents."""

    def __init__(self, name: str, system_prompt: str):
        self.name = name
        self.system_prompt = system_prompt
        self.client = Anthropic()
        self.conversation_history = []

    def add_skill_context(self, skill_file: Path) -> str:
        """Load skill framework from SKILL.md file."""
        if skill_file.exists():
            with open(skill_file, "r") as f:
                return f.read()
        return ""

    def send_message(self, user_message: str, skill_context: str = "") -> str:
        """Send message to Claude and get response."""
        # Combine system prompt with skill context
        full_system = self.system_prompt
        if skill_context:
            full_system += f"\n\nSKILL FRAMEWORK:\n{skill_context}"

        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Get response from Claude
        response = self.client.messages.create(
            model=MODEL_NAME,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            system=full_system,
            messages=self.conversation_history
        )

        # Extract response text
        assistant_message = response.content[0].text

        # Add to history
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        return assistant_message

    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []

    def get_history(self) -> list:
        """Get conversation history."""
        return self.conversation_history.copy()

    @abstractmethod
    def execute(self, plan: dict) -> dict:
        """Execute the agent's task. Implemented by subclasses."""
        pass
