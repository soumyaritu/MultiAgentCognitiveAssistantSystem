from google.adk.agents.llm_agent import Agent
from .gmail_tool import send_email

email_agent = Agent(
    model="gemini-2.5-flash",
    name="email_agent",
    tools=[send_email],
    instruction="""
You help users send emails using Gmail.

Collect:
- recipient email
- subject
- message body

Then send the email using the tool.
"""
)