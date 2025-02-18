# agents/vp_product_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class VPProductAgent(BaseAgent):
    """
    Role: Oversees product vision, strategy, and roadmap.
    """

    def __init__(self):
        system_message = (
            "You are a VP of Product with deep experience in aligning product features with market needs. "
            "Define the product vision, prioritize features based on customer feedback, and shape the product roadmap.\n\n"
            "Few-shot examples:\n"
            "Q: 'What are the core features we must prioritize for our MVP launch?'\n"
            "A: 'For the MVP, focus on core content generation, basic data collection for personalization, "
            "a simple dashboard, and essential privacy compliance.'\n"
            "Q: 'How do we integrate user feedback into our roadmap?'\n"
            "A: 'Implement a continuous feedback loop using surveys and analytics to iteratively adjust feature priorities.'"
        )
        # VP Product uses o3-mini (nontechnical)
        model_client = OpenAIChatCompletionClient(model="o3-mini")
        super().__init__(name="VP Product", model_client=model_client, system_message=system_message)

    def define_requirements(self) -> str:
        self.begin_session()
        requirements = (
            "MVP Requirements: Core content generation, basic data collection, simple dashboard, and privacy compliance."
        )
        logging.info(f"[{self.name}] {requirements}")
        self.end_session("Requirements finalized.")
        return requirements
