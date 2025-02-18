import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent

class ProductManagerAgent(BaseAgent):
    """
    Role: Aggregates external feedback and prioritizes feature development.
    """
    def __init__(self):
        system_message = (
            "You are a Product Manager skilled in collecting and prioritizing customer and market feedback. "
            "Translate stakeholder insights into actionable product features and a coherent roadmap.\n\n"
            "Few-shot examples:\n"
            "Q: 'What are the top three user requests for our upcoming release?'\n"
            "A: 'Enhanced content personalization, an intuitive dashboard, and robust CRM integration.'\n"
            "Q: 'How should we resolve conflicting feedback from different customer segments?'\n"
            "A: 'Analyze usage data and market trends to balance priorities, and consider A/B testing to validate feature choices.'"
        )
        # Product Manager uses o3-mini (nontechnical)
        model_client = OpenAIChatCompletionClient(model="o3-mini-2025-01-31")
        super().__init__(name="Product Manager", model_client=model_client, system_message=system_message)

    def export_output_to_file(self, output: str, filename: str = "product_manager_output.txt"):
        with open(filename, "w") as f:
            f.write(output)
        logging.info(f"[{self.name}] Output exported to {filename}")

    def gather_requirements(self) -> str:
        self.begin_session()
        # Simulate collecting feedback to produce product requirements.
        requirements = (
            "Aggregated Requirements: Enhanced content personalization, intuitive dashboard, and robust CRM integration."
        )
        logging.info(f"[{self.name}] {requirements}")
        self.conversation_history.append({
            "action": "gather_requirements",
            "output": requirements
        })
        self.export_output_to_file(requirements)
        self.end_session("Requirements finalized.")
        return requirements
