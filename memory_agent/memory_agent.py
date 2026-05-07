from google.adk.agents.llm_agent import Agent
from .memory_tool import save_memory, get_memory
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from common.retry import GENERATE_CONTENT_CONFIG

memory_agent = Agent(
    model="gemini-2.5-flash",
    name="memory_agent",
    generate_content_config=GENERATE_CONTENT_CONFIG,
    tools=[save_memory, get_memory],
    instruction="""
You help users store and recall important information.

- If user wants to remember something → use save_memory
- If user asks about past info → use get_memory
"""
)