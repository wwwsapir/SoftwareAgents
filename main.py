# main.py
import asyncio
import os

from api.communication_api import CommunicationAPI
from agents.company_agents.ceo_agent import CEOAgent
from agents.company_agents.vp_product_agent import VPProductAgent
from agents.company_agents.vp_technology_agent import VPTechnologyAgent
from agents.company_agents.vp_marketing_agent import VPMarketingAgent
from agents.company_agents.vp_operations_agent import VPOperationsAgent
from agents.company_agents.product_manager_agent import ProductManagerAgent
from agents.company_agents.ai_ml_engineer_agent import AIMLEngineerAgent
from agents.company_agents.frontend_developer_agent import FrontendDeveloperAgent
from agents.company_agents.backend_developer_agent import BackendDeveloperAgent
from agents.company_agents.data_engineer_agent import DataEngineerAgent
from agents.company_agents.devops_engineer_agent import DevOpsEngineerAgent
from agents.company_agents.ux_ui_designer_agent import UXUIDesignerAgent
from agents.company_agents.qa_engineer_agent import QAEngineerAgent
from agents.company_agents.compliance_legal_agent import ComplianceLegalAgent
from agents.company_agents.marketing_specialist_agent import MarketingSpecialistAgent

from agents.external_agents.retail_business_owner_agent import RetailBusinessOwnerAgent
from agents.external_agents.ecommerce_manager_agent import EcommerceManagerAgent
from agents.external_agents.digital_marketer_agent import DigitalMarketerAgent
from agents.external_agents.content_creator_agent import ContentCreatorAgent
from agents.external_agents.merchandiser_agent import MerchandiserAgent
from agents.external_agents.customer_experience_agent import CustomerExperienceAgent
from agents.external_agents.crm_manager_agent import CRMManagerAgent
from agents.external_agents.it_data_security_agent import ITDataSecurityAgent
from agents.external_agents.industry_analyst_agent import IndustryAnalystAgent
from agents.external_agents.integration_partner_agent import IntegrationPartnerAgent


with open('./credentials_secret.txt', 'r') as cred_file:
    content = cred_file.read()
    os.environ["OPENAI_API_KEY"] = content.split('\n')[0].split('=')[1]  # automatically used by the agents


async def main():
    # Initialize Communication API
    comms = CommunicationAPI()

    # Initialize internal agents
    ceo = CEOAgent()
    vp_product = VPProductAgent()
    vp_technology = VPTechnologyAgent()
    vp_marketing = VPMarketingAgent()
    vp_operations = VPOperationsAgent()
    product_manager = ProductManagerAgent()
    ai_ml_engineer = AIMLEngineerAgent()
    frontend_developer = FrontendDeveloperAgent()
    backend_developer = BackendDeveloperAgent()
    data_engineer = DataEngineerAgent()
    devops_engineer = DevOpsEngineerAgent()
    ux_ui_designer = UXUIDesignerAgent()
    qa_engineer = QAEngineerAgent()
    compliance_legal = ComplianceLegalAgent()
    marketing_specialist = MarketingSpecialistAgent()

    # Initialize external agents
    retail_owner = RetailBusinessOwnerAgent()
    ecommerce_manager = EcommerceManagerAgent()
    digital_marketer = DigitalMarketerAgent()
    content_creator = ContentCreatorAgent()
    merchandiser = MerchandiserAgent()
    cx_specialist = CustomerExperienceAgent()
    crm_manager = CRMManagerAgent()
    it_security = ITDataSecurityAgent()
    industry_analyst = IndustryAnalystAgent()
    integration_partner = IntegrationPartnerAgent()

    # Register all agents with Communication API
    all_agents = [
        ceo, vp_product, vp_technology, vp_marketing, vp_operations, product_manager,
        ai_ml_engineer, frontend_developer, backend_developer, data_engineer, devops_engineer,
        ux_ui_designer, qa_engineer, compliance_legal, marketing_specialist,
        retail_owner, ecommerce_manager, digital_marketer, content_creator,
        merchandiser, cx_specialist, crm_manager, it_security, industry_analyst, integration_partner
    ]
    for agent in all_agents:
        comms.register_agent(agent)

    # Optionally, set up inter-agent contacts (e.g., CEO communicates with VP agents)
    ceo.contacts = {
        "VP Product": vp_product,
        "VP Technology": vp_technology,
        "VP Marketing": vp_marketing,
        "VP Operations/Compliance": vp_operations
    }

    # Simulate process: CEO receives a command to build the MVP.
    final_output = ceo.process_command("Build the MVP version of the product")
    print("\n=== Final Output ===")
    print(final_output)


if __name__ == '__main__':
    asyncio.run(main())
