# external_agents/industry_analyst_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class IndustryAnalystAgent(BaseAgent):
    """
    Role: Provides broader market insights, competitive analysis, and trend forecasting.
    """

    def __init__(self):
        system_message = (
            "You are an Industry Analyst with expertise in market trends and competitive strategy. "
            "Provide strategic insights on emerging trends in AI content generation and how our product can be positioned for long-term success.\n\n"
            "Few-shot examples:\n"
            "Q: 'What trends do you see emerging in AI content generation?'\n"
            "A: 'There is a growing demand for personalized content and increased transparency in AI decision-making.'\n"
            "Q: 'How can our product differentiate itself in a competitive market?'\n"
            "A: 'By focusing on deep personalization, seamless integrations, and robust ethical safeguards.'"
        )
        # Industry Analyst uses GPT-4o (external)
        model_client = OpenAIChatCompletionClient(model="gpt-4o")
        super().__init__(name="Industry Analyst", model_client=model_client, system_message=system_message)

    def analyze_market(self) -> str:
        self.begin_session()
        analysis = (
            "Market Analysis: The trend is toward highly personalized and transparent AI content solutions."
        )
        logging.info(f"[{self.name}] {analysis}")
        self.end_session("Market analysis complete.")
        return analysis
