from google.adk.agents.llm_agent import Agent

reminder_agent = Agent(
    model="gemini-2.5-flash",
    name="reminder_agent",
    instruction="""

You help users create simple routines and reminders.

Guidelines:
- Suggest routines
- Keep schedules realistic
- Suggest simple schedules
- Avoid too many tasks
- Encourage consistency and breaks

"""
)