# agents/vp_technology_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class VPTechnologyAgent(BaseAgent):
    """
    Role: Manages technical strategy, AI/ML, system design, and infrastructure.
    """

    def __init__(self):
        system_message = (
            "You are a VP of Technology with expertise in AI/ML, scalable system architecture, and cloud infrastructure. "
            "Advise on technical strategy, integration of advanced AI models, and ensuring the robustness of our technology stack.\n\n"
            "Few-shot examples:\n"
            "Q: 'What are the key technical challenges in deploying an AI-driven content system?'\n"
            "A: 'Key challenges include ensuring low-latency processing, scalable microservices, and robust data privacy.'\n"
            "Q: 'Which technologies will best support our scalability requirements?'\n"
            "A: 'Use cloud services like AWS, containerization with Docker, orchestration via Kubernetes, and a modular microservices design.'"
        )
        # VP Technology uses o3-mini-high (technical)
        model_client = OpenAIChatCompletionClient(model="o3-mini-high")
        super().__init__(name="VP Technology", model_client=model_client, system_message=system_message)

    def define_technical_strategy(self) -> str:
        self.begin_session()
        strategy = (
            "Technical Strategy: Use Flask and MongoDB for backend, React for frontend, "
            "integrate AI models via LangChain, and deploy on AWS using Docker and Kubernetes."
        )
        logging.info(f"[{self.name}] {strategy}")
        self.end_session("Technical plan ready.")
        return strategy
