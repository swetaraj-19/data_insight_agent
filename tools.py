import os
import requests
from google.cloud import bigquery
from google.adk.tools.bigquery import BigQueryToolset, BigQueryCredentialsConfig
import google.auth

# Tool 1: BigQuery Toolset (Standard Google Tool)
def get_bq_tools():
    """Initializes official BigQuery tools for conversational analytics."""

    # Use Application Default Credentials (ADC) for secure GCP access
    credentials, _ = google.auth.default()
    config = BigQueryCredentialsConfig(
        credentials=credentials
    )
    return BigQueryToolset(
        credentials_config=config
    )