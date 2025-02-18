# external_agents/merchandiser_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class MerchandiserAgent(BaseAgent):
    """
    Role: Shares insights on product presentation, categorization, and visual appeal.
    """

    def __init__(self):
        system_message = (
            "You are a Merchandiser with expertise in product presentation and category management. "
            "Advise on how AI-generated content can enhance product layouts, categorization, and overall visual appeal.\n\n"
            "Few-shot examples:\n"
            "Q: 'What aspects of product presentation impact sales the most?'\n"
            "A: 'Clear, engaging descriptions combined with high-quality images and dynamic categorization drive sales.'\n"
            "Q: 'How can our system help optimize product categorization?'\n"
            "A: 'By analyzing sales trends and customer behavior, the system can suggest optimized categorization that aligns with market trends.'"
        )
        # Merchandiser uses gpt-4o-mini (external)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini-2024-07-18")
        super().__init__(name="Merchandiser", model_client=model_client, system_message=system_message)

    def offer_insights(self) -> str:
        self.begin_session()
        insights = (
            "Insights: Clear product presentation and optimized categorization are crucial for increasing sales."
        )
        logging.info(f"[{self.name}] {insights}")
        self.end_session("Insights provided.")
        return insights
