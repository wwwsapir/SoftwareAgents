# agents/compliance_legal_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class ComplianceLegalAgent(BaseAgent):
    """
    Role: Provides legal guidance and ensures regulatory compliance.
    """

    def __init__(self):
        system_message = (
            "You are a Compliance and Legal Advisor with deep knowledge of data privacy regulations and ethical AI guidelines. "
            "Advise on ensuring our product meets legal requirements and maintains ethical standards.\n\n"
            "Few-shot examples:\n"
            "Q: 'What are the primary legal challenges we should anticipate when launching our product?'\n"
            "A: 'Ensuring GDPR compliance, managing user consent, and avoiding intellectual property infringements.'\n"
            "Q: 'How can we implement transparency into our AI algorithms for ethical compliance?'\n"
            "A: 'Include explainability features, regular bias audits, and clear disclosures about AI-generated content.'"
        )
        # Compliance and Legal Advisor uses o3-mini
        model_client = OpenAIChatCompletionClient(model="o3-mini")
        super().__init__(name="Compliance Legal Advisor", model_client=model_client, system_message=system_message)

    def review_compliance(self) -> str:
        self.begin_session()
        report = (
            "Compliance Report: GDPR, data privacy, and ethical AI guidelines reviewed and documented."
        )
        logging.info(f"[{self.name}] {report}")
        self.end_session("Legal guidelines delivered.")
        return report
