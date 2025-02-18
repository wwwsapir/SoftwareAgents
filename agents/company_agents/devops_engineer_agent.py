# agents/devops_engineer_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class DevOpsEngineerAgent(BaseAgent):
    """
    Role: Sets up cloud infrastructure, containerization, and deployment pipelines.
    """

    def __init__(self):
        system_message = (
            "You are a DevOps/Infrastructure Engineer with expertise in cloud technologies, containerization, and CI/CD. "
            "Design a scalable, reliable infrastructure and optimize deployment pipelines for the product.\n\n"
            "Few-shot examples:\n"
            "Q: 'What cloud infrastructure setup best supports our application scalability?'\n"
            "A: 'Use AWS or Google Cloud with auto-scaling groups, Docker container orchestration via Kubernetes, and robust load balancing.'\n"
            "Q: 'How can we implement effective CI/CD practices?'\n"
            "A: 'Integrate automated testing into your CI/CD pipeline, use Docker for consistent deployments, and leverage orchestration tools for environment consistency.'"
        )
        # DevOps Engineer uses o3-mini-high
        model_client = OpenAIChatCompletionClient(model="o3-mini-high")
        super().__init__(name="DevOps Engineer", model_client=model_client, system_message=system_message)

    def deploy_infrastructure(self) -> str:
        self.begin_session()
        infra_setup = (
            "Deployment Strategy: Use Docker for containerization and Kubernetes for orchestration on AWS."
        )
        logging.info(f"[{self.name}] {infra_setup}")
        self.end_session("Infrastructure ready.")
        return infra_setup
