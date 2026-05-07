from google.adk.agents.llm_agent import Agent

learning_agent = Agent(
    model="gemini-2.5-flash",
    name="learning_agent",
    instruction="""

You explain concepts in a simple way.

Guidelines:
- Use short sentences
- Give real-life examples
- Avoid complex terminology
- Repeat key ideas if needed

"""
)