# test_communication_flow.py
import os
import unittest
from unittest.mock import patch

from agents.company_agents.ceo_agent import CEOAgent
from agents.company_agents.vp_product_agent import VPProductAgent


class TestCeoComms(unittest.TestCase):

    @patch("builtins.input", return_value="yes")
    def test_ceo_user_communication(self, mock_input):
        """
        Test that the CEO agent processes a product creation command,
        updates its conversation history, exports its output to a file,
        and returns the aggregated output after user approval.
        """
        ceo = CEOAgent()
        command = "Build the MVP version of the product with a complete description."
        output = ceo.process_command(command)

        # Check conversation history is updated.
        self.assertGreater(len(ceo.conversation_history), 0,
                           "CEO conversation history should contain at least one entry.")
        self.assertIn(command, ceo.conversation_history[-1]["command"],
                      "The CEO conversation history should contain the input command.")

        # Verify that the aggregated output contains expected content.
        self.assertIn("MVP Requirements defined", output,
                      "Aggregated output should include product requirements defined by VP Product.")

        # Verify that the output file is created.
        filename = "final_product.txt"
        self.assertTrue(os.path.exists(filename), "Final output file should exist.")
        with open(filename, "r") as f:
            file_content = f.read()
        self.assertEqual(file_content, output,
                         "The final output file content should match the aggregated output.")
        os.remove(filename)  # Clean up the file

    @patch("builtins.input", return_value="yes")
    def test_ceo_product_team_communication(self, mock_input):
        """
        Test that the CEO agent can send a message to VP Product and that the VP Product agent
        produces its requirements output correctly.
        """
        ceo = CEOAgent()
        vp_product = VPProductAgent()
        # Register VP Product as a contact of CEO.
        ceo.contacts["VP Product"] = vp_product

        # Simulate CEO sending a message to VP Product.
        test_message = "Please confirm product requirements."
        try:
            ceo.send_message("VP Product", test_message)
        except Exception as e:
            self.fail(f"CEO.send_message raised an exception: {e}")

        # Now, simulate VP Product generating requirements.
        vp_output = vp_product.define_requirements()
        expected_vp_output = (
            "MVP Requirements: Core content generation, basic data collection, simple dashboard, and privacy compliance."
        )
        self.assertEqual(vp_output, expected_vp_output,
                         "VP Product output should match the expected requirements.")

        # Verify VP Product's conversation history is updated.
        self.assertGreater(len(vp_product.conversation_history), 0,
                           "VP Product conversation history should not be empty.")
        self.assertIn("MVP Requirements", vp_product.conversation_history[-1]["output"],
                      "VP Product conversation history should include the requirements.")

        # Verify VP Product output file is created.
        filename = "vp_product_output.txt"
        self.assertTrue(os.path.exists(filename), "VP Product output file should exist.")
        with open(filename, "r") as f:
            file_content = f.read()
        self.assertEqual(file_content, expected_vp_output,
                         "The VP Product output file content should match the expected output.")
        os.remove(filename)  # Clean up the file


if __name__ == "__main__":
    unittest.main()
