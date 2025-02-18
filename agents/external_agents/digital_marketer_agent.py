# external_agents/digital_marketer_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class DigitalMarketerAgent(BaseAgent):
    """
    Role: Evaluates content performance, SEO outcomes, and campaign effectiveness.
    """

    def __init__(self):
        system_message = (
            "You are a Digital Marketer with a strong background in SEO and content strategy. "
            "Evaluate how our product can drive better content performance and improved ROI for marketing campaigns.\n\n"
            "Few-shot examples:\n"
            "Q: 'What content elements drive the best SEO results?'\n"
            "A: 'Targeted keywords, engaging meta descriptions, and well-structured content are essential.'\n"
            "Q: 'How do you measure the success of a digital campaign?'\n"
            "A: 'Metrics such as click-through rates, conversion rates, and overall ROI are key indicators.'"
        )
        # Digital Marketer uses GPT-4o (external)
        model_client = OpenAIChatCompletionClient(model="gpt-4o")
        super().__init__(name="Digital Marketer", model_client=model_client, system_message=system_message)

    def analyze_campaign(self) -> str:
        self.begin_session()
        analysis = (
            "Analysis: Effective SEO requires targeted keywords, engaging meta descriptions, and structured content."
        )
        logging.info(f"[{self.name}] {analysis}")
        self.end_session("Analysis complete.")
        return analysis
