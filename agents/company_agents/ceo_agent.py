# agents/ceo_agent.py
import logging
import os

from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class CEOAgent(BaseAgent):
    """
    Role: Overall strategic leadership and vision.

    Design Rules:
    - Save conversation history for each session.
    - Before closing sessions, export final plans/code to files.
    - Sessions can run in parallel only if all contacted agents are not busy.
    - The CEO periodically presents aggregated outputs to the external user for approval.
    """

    def __init__(self):
        system_message = (
            "You are an experienced CEO with a strong track record in scaling tech companies. "
            "Your focus is on long-term vision, strategic planning, and fostering an innovative company culture. "
            "Provide guidance on strategic direction, growth, and overcoming high-level challenges.\n\n"
            "Few-shot examples:\n"
            "Q: 'What should be our strategic focus for market expansion in the next 3 years?'\n"
            "A: 'We should concentrate on expanding into emerging markets, forming strategic partnerships, "
            "and investing in innovative R&D to stay ahead of trends.'\n"
            "Q: 'How can we balance short-term profitability with long-term innovation?'\n"
            "A: 'Implement a dual-track strategy where part of the revenue funds immediate market responsiveness "
            "and part is reinvested into long-term R&D.'"
        )
        # CEO uses o3-mini (nontechnical high reasoning)
        model_client = OpenAIChatCompletionClient(model="o3-mini-2025-01-31", reasoning_effort='high')
        super().__init__(name="CEO", model_client=model_client, system_message=system_message)

    def can_start_parallel_session(self) -> bool:
        """
        Check if all contact agents are free (i.e. not in the middle of a session).
        """
        for name, agent in self.contacts.items():
            if agent.session_active:
                logging.info(f"[{self.name}] Cannot start parallel session: {name} is busy.")
                return False
        return True

    def export_output_to_file(self, output: str, filename: str = "final_product.txt"):
        """
        Export the aggregated output to a file.
        """
        with open(filename, "w") as f:
            f.write(output)
        logging.info(f"[{self.name}] Final output exported to {filename}")

    def get_user_approval(self) -> bool:
        """
        Simulate waiting for user approval.
        In a production system, this might be an asynchronous callback.
        """
        approval = input("Approve the final product? (yes/no): ")
        return approval.lower() == "yes"

    def process_command(self, command: str) -> str:
        """
        Process a new product command:
        1. Start a session.
        2. Check if contacts are free for parallel sessions.
        3. Delegate tasks to VP agents (simulated).
        4. Aggregate outputs.
        5. Save conversation history.
        6. Export outputs to a file.
        7. Present the output to the user for approval.
        8. Close sessions.
        """
        self.begin_session()
        logging.info(f"[{self.name}] Received command: {command}")

        # Check if parallel sessions can be started
        if not self.can_start_parallel_session():
            logging.info(f"[{self.name}] Waiting for all contacts to be free before delegating tasks.")
            # In production, implement waiting mechanism here.

        # Simulate delegation to VP agents and gathering their outputs:
        logging.info(f"[{self.name}] Delegating tasks to VP agents...")
        vp_product_output = "MVP Requirements defined."
        vp_tech_output = "Technical strategy documented."
        vp_marketing_output = "Marketing plan created."
        vp_ops_output = "Operations plan confirmed."

        aggregated_output = (
            "Final product outputs:\n"
            f"{vp_product_output}\n{vp_tech_output}\n{vp_marketing_output}\n{vp_ops_output}"
        )
        logging.info(f"[{self.name}] Aggregated output:\n{aggregated_output}")

        # Save conversation entry
        self.conversation_history.append({
            "command": command,
            "output": aggregated_output
        })

        # Export aggregated output to file
        self.export_output_to_file(aggregated_output)

        # Present output to user for approval
        logging.info(f"[{self.name}] Awaiting user approval.")
        if not self.get_user_approval():
            logging.info(f"[{self.name}] User did not approve. Requesting changes.")
            final_response = "User requested changes. Please modify the product plan."
        else:
            final_response = aggregated_output

        # End session and instruct contacts to end sessions if active.
        self.end_session("Final output delivered.")
        for name, agent in self.contacts.items():
            if agent.session_active:
                agent.end_session("Session closed by CEO after final approval.")

        return final_response


# For testing purposes, you can run:
if __name__ == '__main__':
    # Create a CEO agent instance and simulate a command.
    ceo = CEOAgent()
    response = ceo.process_command("Build the MVP version of the product with a complete description.")
    print("\n=== Final Output ===")
    print(response)
