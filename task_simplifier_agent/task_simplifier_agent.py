from google.adk.agents.llm_agent import Agent

task_simplifier_agent = Agent(
    model="gemini-2.5-flash",
    name="task_simplifier_agent",
    instruction="""

You help users by breaking complex tasks into small, simple steps.

Guidelines:
- Use numbered steps
- Keep each step short and clear
- Avoid overwhelming the user


"""
)
