# external_agents/ecommerce_manager_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class EcommerceManagerAgent(BaseAgent):
    """
    Role: Provides feedback on managing online operations, product listings, and content curation.
    """

    def __init__(self):
        system_message = (
            "You are an E-commerce Manager with extensive experience running online retail platforms. "
            "Provide feedback on how an AI content generation tool can streamline product listing management and improve online customer experiences.\n\n"
            "Few-shot examples:\n"
            "Q: 'What are the biggest pain points in managing your online storefront?'\n"
            "A: 'Keeping product descriptions updated, ensuring SEO optimization, and managing seamless content updates are key challenges.'\n"
            "Q: 'How could an AI content tool improve your workflow?'\n"
            "A: 'Automated updates and personalized content generation would significantly reduce manual work and improve conversion rates.'"
        )
        # E-commerce Manager uses gpt-4o-mini (external)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini-2024-07-18")
        super().__init__(name="Ecommerce Manager", model_client=model_client, system_message=system_message)

    def provide_feedback(self) -> str:
        self.begin_session()
        feedback = (
            "Feedback: Streamlined product listings and automated content updates are critical for operational efficiency."
        )
        logging.info(f"[{self.name}] {feedback}")
        self.end_session("Feedback delivered.")
        return feedback
