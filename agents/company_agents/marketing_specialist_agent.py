# agents/marketing_specialist_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class MarketingSpecialistAgent(BaseAgent):
    """
    Role: Develops marketing strategies and campaign plans.
    """

    def __init__(self):
        system_message = (
            "You are a Marketing and Customer Experience Specialist with expertise in digital marketing and customer engagement. "
            "Provide strategies for launching our product, optimizing campaigns, and improving customer satisfaction using feedback-driven insights.\n\n"
            "Few-shot examples:\n"
            "Q: 'Which digital channels should we focus on for our product launch?'\n"
            "A: 'Focus on social media, targeted email campaigns, and influencer partnerships.'\n"
            "Q: 'What metrics are most important to measure customer satisfaction post-launch?'\n"
            "A: 'Key metrics include NPS scores, engagement rates, churn rates, and direct survey feedback.'"
        )
        # Marketing Specialist uses o3-mini
        model_client = OpenAIChatCompletionClient(model="o3-mini")
        super().__init__(name="Marketing Specialist", model_client=model_client, system_message=system_message)

    def develop_campaign(self) -> str:
        self.begin_session()
        campaign = (
            "Campaign Plan: Detailed digital marketing strategy focusing on social media, email, and influencer outreach developed."
        )
        logging.info(f"[{self.name}] {campaign}")
        self.end_session("Campaign strategy finalized.")
        return campaign
