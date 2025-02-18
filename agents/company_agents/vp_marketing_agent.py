# agents/vp_marketing_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class VPMarketingAgent(BaseAgent):
    """
    Role: Directs market positioning, messaging, and growth strategies.
    """

    def __init__(self):
        system_message = (
            "You are a VP of Marketing specializing in digital marketing, brand positioning, and customer acquisition. "
            "Develop messaging strategies and campaigns that resonate with our target audience.\n\n"
            "Few-shot examples:\n"
            "Q: 'What is the optimal marketing strategy to launch our AI content generation tool?'\n"
            "A: 'Leverage social media, targeted email campaigns, and strategic partnerships to drive early adoption.'\n"
            "Q: 'How can we tailor our messaging for different retail sectors?'\n"
            "A: 'Customize messaging to highlight industry-specific benefits such as trend-driven content for fashion and technical reliability for electronics.'"
        )
        # VP Marketing uses o3-mini
        model_client = OpenAIChatCompletionClient(model="o3-mini")
        super().__init__(name="VP Marketing", model_client=model_client, system_message=system_message)

    def create_marketing_plan(self) -> str:
        self.begin_session()
        plan = (
            "Marketing Plan: Leverage social media, targeted email campaigns, and influencer partnerships to drive early adoption."
        )
        logging.info(f"[{self.name}] {plan}")
        self.end_session("Marketing strategy finalized.")
        return plan
