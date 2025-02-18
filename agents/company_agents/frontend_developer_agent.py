# agents/frontend_developer_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class FrontendDeveloperAgent(BaseAgent):
    """
    Role: Builds responsive and interactive user interfaces.
    """

    def __init__(self):
        system_message = (
            "You are a React developer with experience in creating dynamic, responsive user interfaces. "
            "Design and implement intuitive dashboards and content editors that deliver an excellent user experience.\n\n"
            "Few-shot examples:\n"
            "Q: 'What UI components are essential for our dashboard?'\n"
            "A: 'Key components include real-time analytics panels, customizable widgets, navigation menus, and alert notifications.'\n"
            "Q: 'How can we make our content editor both powerful and easy to use?'\n"
            "A: 'Implement drag-and-drop elements, inline editing features, and a live preview mode to reflect changes instantly.'"
        )
        # Frontend Developer uses o3-mini
        model_client = OpenAIChatCompletionClient(model="o3-mini-2025-01-31")
        super().__init__(name="Frontend Developer", model_client=model_client, system_message=system_message)

    def build_ui(self) -> str:
        self.begin_session()
        ui_code = (
            "import React from 'react';\n"
            "const Dashboard = () => (\n"
            "    <div>\n"
            "        <h1>Dashboard</h1>\n"
            "        <p>Real-time analytics and interactive widgets here.</p>\n"
            "    </div>\n"
            ");\n"
            "export default Dashboard;"
        )
        logging.info(f"[{self.name}] UI components built.")
        self.end_session("UI components submitted.")
        return ui_code
