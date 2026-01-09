import os
from google.adk.agents import Agent
from .tools import get_bq_tools, generate_visual
from .prompts import instructions, v_instructions
from dotenv import load_dotenv
from google.adk.code_executors import VertexAiCodeExecutor

load_dotenv()
GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
BQ_DATASET_ID = os.getenv("BQ_DATASET_ID")

# 1. Specialist Sub-agent: Focused on Aggregation and Trend Analysis 
insights_specialist = Agent(
    name="insights_specialist",
    model="gemini-2.5-flash", 
    description="Specialist in data aggregation, trend analysis, and visualization.",
    code_executor=VertexAiCodeExecutor(),
    instruction=v_instructions
)

# 2. Root Orchestrator: Coordinator for Agent Engine deployment 
root_agent = Agent(
    name="corner_banca_orchestrator",
    model="gemini-2.5-flash",
    description="Data Insight Agent for Cornèr Banca.",
    instruction=instructions,
    tools=[get_bq_tools(), generate_visual],
    sub_agents=[insights_specialist] 
)