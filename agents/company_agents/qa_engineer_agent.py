# agents/qa_engineer_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class QAEngineerAgent(BaseAgent):
    """
    Role: Develops test plans and executes comprehensive testing strategies.
    """

    def __init__(self):
        system_message = (
            "You are a QA Engineer with expertise in both automated and manual testing. "
            "Create comprehensive testing strategies that ensure our product is reliable, secure, and meets user expectations.\n\n"
            "Few-shot examples:\n"
            "Q: 'What key test cases should we prioritize for our content generation module?'\n"
            "A: 'Focus on API reliability, UI responsiveness, data integrity during personalization, and security compliance.'\n"
            "Q: 'How can we integrate automated testing into our CI/CD pipeline?'\n"
            "A: 'Implement unit, integration, and regression tests that run automatically on each code push using tools like Jenkins or GitHub Actions.'"
        )
        # QA Engineer uses o3-mini-high
        model_client = OpenAIChatCompletionClient(model="o3-mini-2025-01-31")
        super().__init__(name="QA Engineer", model_client=model_client, system_message=system_message)

    def run_tests(self) -> str:
        self.begin_session()
        test_plan = (
            "Test Plan: API reliability, UI responsiveness, data integrity, and security compliance tests defined."
        )
        logging.info(f"[{self.name}] {test_plan}")
        self.end_session("Testing completed.")
        return test_plan
