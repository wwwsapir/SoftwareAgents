# external_agents/it_data_security_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class ITDataSecurityAgent(BaseAgent):
    """
    Role: Advises on system security, data privacy compliance, and risk management.
    """

    def __init__(self):
        system_message = (
            "You are an IT and Data Security Officer with deep experience in cybersecurity and data privacy. "
            "Provide recommendations on securing our system and ensuring compliance with standards such as GDPR.\n\n"
            "Few-shot examples:\n"
            "Q: 'What security protocols are essential for a system handling sensitive customer data?'\n"
            "A: 'Implement multi-factor authentication, encryption for data at rest and in transit, and regular vulnerability assessments.'\n"
            "Q: 'How can we best ensure our data pipelines comply with GDPR?'\n"
            "A: 'Use data anonymization techniques, enforce strict access controls, and maintain thorough audit logs.'"
        )
        # IT Data Security Officer uses gpt-4o-mini (external)
        model_client = OpenAIChatCompletionClient(model="gpt-4o-mini-2024-07-18")
        super().__init__(name="IT Data Security Officer", model_client=model_client, system_message=system_message)

    def advise_security(self) -> str:
        self.begin_session()
        advice = (
            "Advice: Implement multi-factor authentication, encrypt data in transit and at rest, and conduct regular security audits."
        )
        logging.info(f"[{self.name}] {advice}")
        self.end_session("Security guidelines delivered.")
        return advice
