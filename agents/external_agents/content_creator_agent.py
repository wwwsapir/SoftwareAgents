# external_agents/content_creator_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class ContentCreatorAgent(BaseAgent):
    """
    Role: Advises on tone, brand consistency, and creative content strategies.
    """

    def __init__(self):
        system_message = (
            "You are a Content Creator and Copywriter with extensive experience crafting engaging narratives. "
            "Advise on how AI-generated content can maintain a consistent brand voice and effectively engage audiences.\n\n"
            "Few-shot examples:\n"
            "Q: 'What tone resonates best with your target audience?'\n"
            "A: 'A friendly, conversational tone with clear calls-to-action usually works best.'\n"
            "Q: 'How can AI assist in maintaining brand consistency while being creative?'\n"
            "A: 'By training on brand guidelines and incorporating continuous feedback, AI can generate content that is both consistent and innovative.'"
        )
        # Content Creator uses GPT-4o (external)
        model_client = OpenAIChatCompletionClient(model="gpt-4o")
        super().__init__(name="Content Creator", model_client=model_client, system_message=system_message)

    def advise_on_copy(self) -> str:
        self.begin_session()
        advice = (
            "Advice: Use a friendly, conversational tone with clear calls-to-action to maintain brand consistency."
        )
        logging.info(f"[{self.name}] {advice}")
        self.end_session("Copy guidelines provided.")
        return advice
