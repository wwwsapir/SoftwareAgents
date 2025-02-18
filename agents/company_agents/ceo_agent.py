# agents/ceo_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class CEOAgent(BaseAgent):
    """
    Role: Overall strategic leadership and vision.
    """

    def __init__(self):
        system_message = (
            "You are an experienced CEO with a strong track record in scaling tech companies. "
            "Your focus is on long-term vision, strategic planning, and fostering an innovative company culture. "
            "Provide guidance on strategic direction, growth, and overcoming high-level challenges.\n\n"
            "Few-shot examples:\n"
            "Q: 'What should be our strategic focus for market expansion in the next 3 years?'\n"
            "A: 'We should concentrate on expanding into emerging markets, forming strategic partnerships, "
            "and investing in innovative R&D to stay ahead of trends.'\n"
            "Q: 'How can we balance short-term profitability with long-term innovation?'\n"
            "A: 'Implement a dual-track strategy where part of the revenue funds immediate market responsiveness "
            "and part is reinvested into long-term R&D.'"
        )
        # CEO uses o3-mini (nontechnical high reasoning)
        model_client = OpenAIChatCompletionClient(model="o3-mini")
        super().__init__(name="CEO", model_client=model_client, system_message=system_message)

    def process_command(self, command: str) -> str:
        self.begin_session()
        logging.info(f"[{self.name}] Processing command: {command}")
        # Simulated delegation to VP agents.
        logging.info(f"[{self.name}] Delegating tasks to VP agents...")
        vp_product_output = "MVP Requirements defined."
        vp_tech_output = "Technical strategy documented."
        vp_marketing_output = "Marketing plan created."
        vp_ops_output = "Operations plan confirmed."
        final_output = (
            "Final product outputs:\n"
            f"{vp_product_output}\n{vp_tech_output}\n{vp_marketing_output}\n{vp_ops_output}"
        )
        logging.info(f"[{self.name}] {final_output}")
        self.end_session("Process complete; final outputs attached.")
        return final_output
