# test_product_department.py
import asyncio
import os
import unittest

from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console

from agents.company_agents.vp_product_agent import VPProductAgent
from agents.company_agents.product_manager_agent import ProductManagerAgent
from unittest.mock import patch


class TestProductDepartmentComms(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with open('../credentials_secret.txt', 'r') as cred_file:
            content = cred_file.read()
            os.environ["OPENAI_API_KEY"] = content.split('\n')[0].split('=')[1]  # automatically used by the agents

    def test_vp_product_agent_requirements(self):
        vp_product = VPProductAgent()
        output = vp_product.define_requirements()

        # Check that conversation history is updated
        self.assertGreater(len(vp_product.conversation_history), 0,
                           "Conversation history should have at least one entry.")
        self.assertIn("MVP Requirements", vp_product.conversation_history[-1]["output"],
                      "The conversation history should contain the MVP requirements.")
        expected_output = (
            "MVP Requirements: Core content generation, basic data collection, simple dashboard, and privacy compliance.")
        self.assertEqual(output, expected_output,
                         "The VP Product Agent output should match the expected requirements.")

        # Verify file output
        filename = "vp_product_output.txt"
        self.assertTrue(os.path.exists(filename), "Output file should exist.")
        with open(filename, "r") as f:
            file_content = f.read()
        self.assertEqual(file_content, expected_output,
                         "The file content should match the agent's output.")
        os.remove(filename)  # Clean up the file

    def test_product_manager_agent_requirements(self):
        product_manager = ProductManagerAgent()
        output = product_manager.gather_requirements()

        # Check that conversation history is updated
        self.assertGreater(len(product_manager.conversation_history), 0,
                           "Conversation history should have at least one entry.")
        self.assertIn("Aggregated Requirements", product_manager.conversation_history[-1]["output"],
                      "The conversation history should contain the aggregated requirements.")
        expected_output = (
            "Aggregated Requirements: Enhanced content personalization, intuitive dashboard, and robust CRM integration.")
        self.assertEqual(output, expected_output,
                         "The Product Manager Agent output should match the expected aggregated requirements.")

        # Verify file output
        filename = "product_manager_output.txt"
        self.assertTrue(os.path.exists(filename), "Output file should exist.")
        with open(filename, "r") as f:
            file_content = f.read()
        self.assertEqual(file_content, expected_output,
                         "The file content should match the agent's output.")
        os.remove(filename)  # Clean up the file

    # @patch("builtins.input", return_value="yes")
    def test_internal_communication_between_vp_product_and_product_manager(self):
        """
        Test that VP Product can send a message to Product Manager and that
        Product Manager can process the message to generate a draft requirement.
        """
        vp_product = VPProductAgent()
        product_manager = ProductManagerAgent()

        # Set up contacts between VP Product and Product Manager.
        vp_product.contacts["Product Manager"] = product_manager
        product_manager.contacts["VP Product"] = vp_product

        # VP Product sends a message to Product Manager.
        test_message = "Please provide additional insights for the product requirements."
        try:
            # Define termination condition
            termination = TextMentionTermination("TERMINATE")
            # Define a team
            agent_team = RoundRobinGroupChat(
                [vp_product.contacts["Product Manager"], product_manager.contacts["VP Product"]],
                termination_condition=termination)
            # Run the team and stream messages to the console
            test_message = "Please provide basic requirements for a simple trivia questions game."
            stream = agent_team.run_stream(task=test_message)
            asyncio.run(Console(stream))
        except Exception as e:
            self.fail(f"Console(stream) raised an exception: {e}")

        # self.assertEqual(pm_output, expected_pm_output,
        #                  "Product Manager output should match the expected aggregated requirements.")

        # Ensure the conversation history of Product Manager includes the message received.
        # self.assertGreater(len(product_manager.conversation_history), 0,
        #                    "Product Manager conversation history should not be empty.")
        # last_entry = product_manager.conversation_history[-1]
        # self.assertIn("Aggregated Requirements", last_entry["output"],
        #               "The conversation history should reflect the aggregation action.")

        # Clean up output file.
        # filename = "product_manager_output.txt"
        # if os.path.exists(filename):
        #     os.remove(filename)


if __name__ == "__main__":
    unittest.main()
