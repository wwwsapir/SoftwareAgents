# api/communication_api.py
class CommunicationAPI:
    """
    A simple communication API to route messages between agents.
    In production, you might use message queues or websockets.
    """

    def __init__(self):
        self.agents = {}

    def register_agent(self, agent):
        self.agents[agent.name] = agent

    def send(self, sender_name, recipient_name, message):
        if recipient_name in self.agents:
            recipient = self.agents[recipient_name]
            recipient.receive_message(sender_name, message)
        else:
            print(f"Agent {recipient_name} not found in CommunicationAPI.")
