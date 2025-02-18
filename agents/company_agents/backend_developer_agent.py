# agents/backend_developer_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class BackendDeveloperAgent(BaseAgent):
    """
    Role: Develops RESTful APIs and manages server-side logic.
    """

    def __init__(self):
        system_message = (
            "You are a backend developer proficient in Flask and MongoDB. "
            "Design scalable RESTful APIs and robust server-side architectures to support our content generation modules.\n\n"
            "Few-shot examples:\n"
            "Q: 'What is the ideal structure for our API endpoints?'\n"
            "A: 'A RESTful design with endpoints for content generation, data collection, authentication, and admin functions.'\n"
            "Q: 'How can we optimize database queries for performance?'\n"
            "A: 'Utilize proper indexing, caching strategies, and optimize query logic to handle high concurrency.'"
        )
        # Backend Developer uses o3-mini-high
        model_client = OpenAIChatCompletionClient(model="o3-mini-2025-01-31")
        super().__init__(name="Backend Developer", model_client=model_client, system_message=system_message)

    def build_api(self) -> str:
        self.begin_session()
        api_code = (
            "from flask import Flask, jsonify\n"
            "app = Flask(__name__)\n\n"
            "@app.route('/generate', methods=['POST'])\n"
            "def generate_content():\n"
            "    # Simulated content generation\n"
            "    return jsonify({'content': 'Generated product description'})\n\n"
            "if __name__ == '__main__':\n"
            "    app.run(debug=True)"
        )
        logging.info(f"[{self.name}] API endpoints created.")
        self.end_session("API endpoints ready.")
        return api_code
