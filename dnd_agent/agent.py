from google.adk.agents import LlmAgent
from google.adk.models import LiteLlm

from dnd_agent.prompt import AGENT_SYSTEM_PROMPT

root_agent = LlmAgent(
    model=LiteLlm(model="anthropic/claude-haiku-4-5"),
    name="root_agent",
    instruction=AGENT_SYSTEM_PROMPT,
)
