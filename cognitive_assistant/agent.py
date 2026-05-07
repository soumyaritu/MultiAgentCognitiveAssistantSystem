from task_simplifier_agent.task_simplifier_agent import task_simplifier_agent
from google.adk.agents.llm_agent import Agent
from reminder_agent.reminder_agent import reminder_agent
from learning_agent.learning_agent import learning_agent
from memory_agent.memory_agent import memory_agent
from communication_agent.communication_agent import communication_agent
from email_agent.email_sending_agent import email_agent
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from common.retry import GENERATE_CONTENT_CONFIG

root_agent = Agent(
    model="gemini-2.5-flash",
    name="cognitive_root_agent",
    generate_content_config=GENERATE_CONTENT_CONFIG,
    instruction="""
You are a Cognitive Support Assistant.

Route user requests:

- Task help → task_simplifier_agent
- Reminders or schedule → reminder_agent
- Learning/explanations → learning_agent
- Memory recall → memory_agent
- Writing messages → communication_agent
- Sending emails → email_agent

If unclear, respond simply and politely.
""",
    sub_agents=[
        task_simplifier_agent,
        reminder_agent,
        learning_agent,
        memory_agent,
        communication_agent,
        email_agent,
    ]
)
