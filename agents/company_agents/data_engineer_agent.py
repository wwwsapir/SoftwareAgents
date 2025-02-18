# agents/data_engineer_agent.py
import logging
from autogen_ext.models.openai import OpenAIChatCompletionClient
from agents.base_agent import BaseAgent


class DataEngineerAgent(BaseAgent):
    """
    Role: Designs and implements data pipelines for secure and compliant data handling.
    """

    def __init__(self):
        system_message = (
            "You are a Data Engineer experienced in building scalable data pipelines and ensuring data security. "
            "Advise on designing efficient, compliant data flows that support personalization.\n\n"
            "Few-shot examples:\n"
            "Q: 'How can we design a real-time data pipeline for user personalization?'\n"
            "A: 'Build a pipeline that ingests data from various sources, processes it in real time using stream processing tools, and stores it in a NoSQL database.'\n"
            "Q: 'What best practices ensure our data handling meets compliance standards?'\n"
            "A: 'Implement encryption, anonymization, and strict access controls while following GDPR guidelines.'"
        )
        # Data Engineer uses o3-mini-high
        model_client = OpenAIChatCompletionClient(model="o3-mini-2025-01-31")
        super().__init__(name="Data Engineer", model_client=model_client, system_message=system_message)

    def build_data_pipeline(self) -> str:
        self.begin_session()
        pipeline_code = (
            "import pymongo\n"
            "client = pymongo.MongoClient('mongodb://localhost:27017/')\n"
            "db = client['retail_data']\n\n"
            "def ingest_data(data):\n"
            "    db.data.insert_one(data)\n"
            "    return 'Data ingested'\n"
        )
        logging.info(f"[{self.name}] Data pipeline implemented.")
        self.end_session("Data pipeline implemented.")
        return pipeline_code
