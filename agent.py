import os
from google.adk.agents import Agent
from .tools import get_bq_tools

# 1. Specialist Sub-agent: Focused on Aggregation and Trend Analysis 
insights_specialist = Agent(
    name="insights_specialist",
    model="gemini-2.5-flash", 
    description="Specialist in data aggregation, trend analysis, and visualization.",
    instruction="""
    Analyze raw data results from BigQuery to:
    1. Perform Data Aggregation: Provide summaries, averages, and totals.
    2. Conduct Trend Analysis: Identify month-over-month growth or anomalies.
    3. Reporting: Summarize findings in structured tables.
    4. Visualization: Recommend chart types for the data (e.g., line charts for trends).
    """
)

# 2. Root Orchestrator: Coordinator for Agent Engine deployment 
root_agent = Agent(
    name="corner_banca_orchestrator",
    model="gemini-2.5-flash",
    description="Primary Data Insight Agent for Cornèr Banca.",
    instruction="""
    You are the Cornèr Banca Data Insight Agent.
    - Use the BigQueryToolset to query the 20 tables in scope[cite: 341].
    - For any complex trend analysis or reporting, delegate to the 'insights_specialist'.
    - Ensure all responses are in English[cite: 374].
    """,
    tools=[get_bq_tools()],
    sub_agents=[insights_specialist] 
)