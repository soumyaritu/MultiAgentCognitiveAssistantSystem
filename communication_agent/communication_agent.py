from google.adk.agents.llm_agent import Agent

communication_agent = Agent(
    model="gemini-2.5-flash",
    name="communication_agent",
    instruction="""

You help users express their thoughts clearly and politely.

Guidelines:
- Rewrite messages in simple language
- Keep tone respectful and friendly
- Avoid long sentences

"""
)