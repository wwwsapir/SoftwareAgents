# agents/ai_ml_engineer_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class AIMLEngineerAgent(BaseAgent):
    """
    Role: Develops, trains, and fine-tunes AI models for content generation.
    """

    def __init__(self):
        system_message = (
            "You are an AI/ML Engineer with expertise in training and fine-tuning language models. "
            "Advise on best practices for developing high-quality, contextually relevant AI models for content generation.\n\n"
            "Few-shot examples:\n"
            "Q: 'What steps can we take to improve the accuracy of our product descriptions?'\n"
            "A: 'Fine-tune the model on industry-specific data, implement quality checks, and iterate using real user feedback.'\n"
            "Q: 'How should we fine-tune our model using retail-specific data?'\n"
            "A: 'Incorporate domain-specific vocabulary during training and use a curated dataset covering various retail scenarios.'"
        )
        # AI/ML Engineer uses o3-mini-high
        model_client = OpenAIChatCompletionClient(model="o3-mini-2025-01-31")
        super().__init__(name="AI/ML Engineer", model_client=model_client, system_message=system_message)

    def train_model(self) -> str:
        self.begin_session()
        training_info = (
            "AI Model Training: Fine-tuned GPT-based model using LangChain on retail-specific data."
        )
        logging.info(f"[{self.name}] {training_info}")
        self.end_session("Model training complete.")
        return training_info
