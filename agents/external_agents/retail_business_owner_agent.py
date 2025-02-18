# external_agents/retail_business_owner_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class RetailBusinessOwnerAgent(BaseAgent):
    """
    Role: Provides insights on ROI, budget constraints, and strategic needs from a retail perspective.
    """

    def __init__(self):
        system_message = (
            "You are a Retail Business Owner with extensive experience managing retail operations. "
            "Provide insights on which features drive ROI and how technology can improve operational efficiency.\n\n"
            "Few-shot examples:\n"
            "Q: 'Which features in an AI content generation tool would directly boost your sales?'\n"
            "A: 'Features like personalized content, dynamic recommendations, and seamless POS integration would boost sales.'\n"
            "Q: 'How do budget constraints affect your adoption of new technologies?'\n"
            "A: 'I require solutions with clear ROI and scalable pricing models that minimize upfront costs.'"
        )
        # Retail Business Owner uses o3-mini
        model_client = OpenAIChatCompletionClient(model="o3-mini")
        super().__init__(name="Retail Business Owner", model_client=model_client, system_message=system_message)

    def provide_feedback(self) -> str:
        self.begin_session()
        feedback = (
            "Feedback: Personalized content and dynamic recommendations would boost sales. Scalable pricing is a must."
        )
        logging.info(f"[{self.name}] {feedback}")
        self.end_session("Feedback provided.")
        return feedback
