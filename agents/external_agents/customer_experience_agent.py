# external_agents/customer_experience_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class CustomerExperienceAgent(BaseAgent):
    """
    Role: Provides usability and interaction design feedback from a customer's perspective.
    """

    def __init__(self):
        system_message = (
            "You are a Customer Experience Specialist focused on enhancing digital interactions. "
            "Provide detailed feedback on interface design, usability, and how our product can better meet customer needs.\n\n"
            "Few-shot examples:\n"
            "Q: 'Which features in an online dashboard most improve user satisfaction?'\n"
            "A: 'Real-time analytics, an intuitive layout, and customizable widgets are key.'\n"
            "Q: 'How can we make our interface more intuitive for everyday users?'\n"
            "A: 'Implement clear navigation, interactive guides, and immediate feedback on user actions.'"
        )
        # Customer Experience Specialist uses GPT-4o (external)
        model_client = OpenAIChatCompletionClient(model="gpt-4o")
        super().__init__(name="Customer Experience Specialist", model_client=model_client,
                         system_message=system_message)

    def provide_usability_feedback(self) -> str:
        self.begin_session()
        feedback = (
            "Feedback: Intuitive navigation, real-time analytics, and interactive guides greatly enhance user satisfaction."
        )
        logging.info(f"[{self.name}] {feedback}")
        self.end_session("Usability feedback delivered.")
        return feedback
