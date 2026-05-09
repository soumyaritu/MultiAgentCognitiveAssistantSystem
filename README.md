MultiAgent Cognitive Assistant Architecture

Overview
The MultiAgent Cognitive Assistant System is built using the Google Agent Development Kit (ADK) and operates through a hierarchical multi-agent architecture. The system uses a primary router agent to orchestrate and delegate specific tasks to specialized sub-agents. All agents currently utilize the gemini-2.5-flash model.

Core Structure
1. Root Agent (Orchestrator)
Path: cognitive_assistant/agent.py
Name: cognitive_root_agent
Role: Acts as the main entry point and Cognitive Support Assistant. It interprets user requests and routes them to the appropriate specialised sub-agent.

Routing Logic:
Task help → task_simplifier_agent
Reminders or schedule → reminder_agent
Learning/explanations → learning_agent
Memory recall → memory_agent
Writing messages → communication_agent
Sending emails → email_agent

Sub-Agents
2. Task Simplifier Agent
Path: task_simplifier_agent/task_simplifier_agent.py
Role: Helps users by breaking down complex tasks into small, manageable, and clear numbered steps to avoid overwhelming the user.

3. Reminder Agent
Path: reminder_agent/reminder_agent.py
Role: Assists in creating realistic, simple daily routines and schedules while encouraging consistency and breaks.

4. Learning Agent
Path: learning_agent/learning_agent.py
Role: Explains concepts simply using short sentences, real-life examples, and simple terminology.

5. Memory Agent
Path: memory_agent/memory_agent.py
Role: Helps users store and recall important information.
Tools Used:
save_memory
get_memory

6. Communication Agent
Path: communication_agent/communication_agent.py
Role: Rewrites user messages to be simple, clear, polite, and respectful.

7. Email Agent
Path: email_agent/email_sending_agent.py
Role: Collects necessary information (recipient, subject, body) and sends emails using Gmail.
Tools Used:
send_email

Supporting Components
Common Configurations (common/retry.py): Contains the GENERATE_CONTENT_CONFIG which manages retry logic and reliability settings for LLM API calls.
Credentials & Environment Variables:
credentials.json & token.json for Gmail/Google API integrations.
.env for securing API keys and environment variables.
