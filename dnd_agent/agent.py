from google.adk.agents import LlmAgent
from google.adk.models import LiteLlm

root_agent = LlmAgent(
    model=LiteLlm(model="anthropic/claude-haiku-4-5"),
    name="root_agent",
    instruction="""You are a helpful Dungeons and Dragons Agent
    """,
)
