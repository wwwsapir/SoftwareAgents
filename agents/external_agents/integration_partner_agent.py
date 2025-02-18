# external_agents/integration_partner_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class IntegrationPartnerAgent(BaseAgent):
    """
    Role: Shares integration challenges and recommendations for system interoperability.
    """

    def __init__(self):
        system_message = (
            "You are a Third-Party Integration Partner with experience integrating systems like CMS, e-commerce platforms, and marketing tools. "
            "Provide guidance on ensuring our product integrates smoothly and adds value across diverse ecosystems.\n\n"
            "Few-shot examples:\n"
            "Q: 'What challenges do you typically encounter when integrating with new systems?'\n"
            "A: 'Differences in API standards, data format discrepancies, and ensuring real-time data synchronization are common challenges.'\n"
            "Q: 'How can our product be designed to facilitate smooth integrations with external platforms?'\n"
            "A: 'By following industry-standard API protocols, offering detailed documentation, and providing dedicated support for integration efforts.'"
        )
        # Integration Partner uses gpt-4o-mini (external)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini-2024-07-18")
        super().__init__(name="Integration Partner", model_client=model_client, system_message=system_message)

    def advise_integration(self) -> str:
        self.begin_session()
        advice = (
            "Advice: Use industry-standard API protocols, offer detailed documentation, and provide dedicated support to ensure smooth integrations."
        )
        logging.info(f"[{self.name}] {advice}")
        self.end_session("Integration advice delivered.")
        return advice
