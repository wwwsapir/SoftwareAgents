# agents/base_agent.py
import logging
from autogen_agentchat.agents import AssistantAgent


class BaseAgent(AssistantAgent):
    """
    BaseAgent extends AssistantAgent to add session management.
    The provided system_message (combining prompt and few-shot examples) primes the agent.
    """

    def __init__(self, name, model_client, system_message, **kwargs):
        super().__init__(name=name, model_client=model_client, system_message=system_message, **kwargs)
        self.contacts = {}  # For inter-agent communication.
        logging.basicConfig(level=logging.INFO)

    def begin_session(self):
        """
        Resets the conversation history for a new session.
        """
        self.reset()  # Reset the conversation history (AssistantAgent method)
        logging.info(f"[{self.name}] BEGIN SESSION – Conversation reset and primed with system_message.")

    def end_session(self, message=""):
        logging.info(f"[{self.name}] END SESSION – {message}")
