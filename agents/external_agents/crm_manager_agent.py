# external_agents/crm_manager_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class CRMManagerAgent(BaseAgent):
    """
    Role: Provides feedback on integration efficiency and data flow between systems.
    """

    def __init__(self):
        system_message = (
            "You are a CRM and Marketing Automation Manager with expertise in system integrations. "
            "Provide feedback on how our product can integrate smoothly with existing systems to improve data flow and operational efficiency.\n\n"
            "Few-shot examples:\n"
            "Q: 'What integration features are most critical for your current systems?'\n"
            "A: 'Seamless API connectivity, real-time data synchronization, and robust error handling are essential.'\n"
            "Q: 'How do you ensure seamless data exchange between platforms?'\n"
            "A: 'Standardizing data formats and implementing secure, well-documented APIs are key.'"
        )
        # CRM Manager uses GPT-4o (external)
        model_client = OpenAIChatCompletionClient(model="gpt-4o")
        super().__init__(name="CRM Manager", model_client=model_client, system_message=system_message)

    def provide_integration_feedback(self) -> str:
        self.begin_session()
        feedback = (
            "Feedback: Seamless API connectivity and standardized data formats are crucial for efficient integration."
        )
        logging.info(f"[{self.name}] {feedback}")
        self.end_session("Integration feedback provided.")
        return feedback
