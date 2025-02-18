# agents/ux_ui_designer_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class UXUIDesignerAgent(BaseAgent):
    """
    Role: Crafts intuitive interfaces and design assets.
    """

    def __init__(self):
        system_message = (
            "You are a UX/UI Designer specializing in creating clean, engaging, and user-friendly interfaces. "
            "Provide design recommendations that enhance usability for our dashboards and content editors while aligning with our brand identity.\n\n"
            "Few-shot examples:\n"
            "Q: 'Which design elements can improve the usability of our dashboard?'\n"
            "A: 'Clear visual hierarchy, consistent color schemes, interactive tooltips, and intuitive navigation.'\n"
            "Q: 'How do we ensure our content editor is both aesthetically pleasing and functional?'\n"
            "A: 'Incorporate responsive layouts, interactive previews, and continuous user testing feedback.'"
        )
        # UX/UI Designer uses o3-mini (nontechnical)
        model_client = OpenAIChatCompletionClient(model="o3-mini-2025-01-31")
        super().__init__(name="UX/UI Designer", model_client=model_client, system_message=system_message)

    def design_interface(self) -> str:
        self.begin_session()
        design_docs = (
            "UX/UI Design: Wireframes and mockups for dashboard and content editor created using Figma."
        )
        logging.info(f"[{self.name}] {design_docs}")
        self.end_session("Design assets delivered.")
        return design_docs
