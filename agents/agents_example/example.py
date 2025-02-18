import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient


# Define a tool
async def get_weather(city: str) -> str:
    return f"The weather in {city} is 73 degrees and Sunny."


async def main() -> None:
    with open('../credentials_secret.txt', 'r') as cred_file:
        content = cred_file.read()
        openai_api_key = content.split('\n')[0].split('=')[1]
    # Define an agent
    weather_agent = AssistantAgent(
        name="product_agent",
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-mini-2024-07-18",
            api_key=openai_api_key,
        ),
        system_message="You are a product manager agent. You write and edit requirements and communicate with the programmers when needed.",
        # tools=[get_weather],
    )

    # Define an agent
    programmer_agent = AssistantAgent(
        name="programmer_agent",
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-mini-2024-07-18",
        ),
        system_message="You are a programmer agent. You write great software code in any language asked.",
        # tools=[get_weather],
    )

    # Define termination condition
    termination = TextMentionTermination("TERMINATE")

    # Define a team
    agent_team = RoundRobinGroupChat([weather_agent, programmer_agent], termination_condition=termination)

    # Run the team and stream messages to the console
    stream = agent_team.run_stream(task="Create a small trivia game web app with only two trivia questions.")
    await Console(stream)

asyncio.run(main())
