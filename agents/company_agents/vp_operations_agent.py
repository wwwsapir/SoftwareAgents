# agents/vp_operations_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class VPOperationsAgent(BaseAgent):
    """
    Role: Ensures operational efficiency, legal compliance, and secure integrations.
    """

    def __init__(self):
        system_message = (
            "You are a VP of Operations/Compliance with expertise in operational management and regulatory requirements. "
            "Advise on streamlining operations, ensuring legal compliance, and managing risk.\n\n"
            "Few-shot examples:\n"
            "Q: 'How can we design our operations to support rapid scaling while remaining compliant?'\n"
            "A: 'Implement automated workflows, scalable cloud infrastructure, and continuous compliance monitoring.'\n"
            "Q: 'What are the key data security measures we must implement from the start?'\n"
            "A: 'Essential measures include encryption, token-based authentication, regular security audits, and strict access control.'"
        )
        # VP Operations uses o3-mini
        model_client = OpenAIChatCompletionClient(model="o3-mini-2025-01-31")
        super().__init__(name="VP Operations/Compliance", model_client=model_client, system_message=system_message)

    def define_operations(self) -> str:
        self.begin_session()
        ops = (
            "Operations Plan: Implement automated workflows, scalable cloud infrastructure, and robust data security measures per GDPR."
        )
        logging.info(f"[{self.name}] {ops}")
        self.end_session("Operations plan confirmed.")
        return ops
