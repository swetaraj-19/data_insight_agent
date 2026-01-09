import os
import requests
from google.cloud import bigquery
from google.adk.tools.bigquery import BigQueryToolset, BigQueryCredentialsConfig
import google.auth
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv

load_dotenv()
GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
BQ_DATASET_ID = os.getenv("BQ_DATASET_ID")


# Tool 1: BigQuery Toolset (Standard Google Tool)
def get_bq_tools():
    """"Initializes official BigQuery tools with ADC."""

    # Use Application Default Credentials (ADC) for secure GCP access
    credentials, _ = google.auth.default()
    config = BigQueryCredentialsConfig(credentials=credentials)
    return BigQueryToolset(credentials_config=config)

def generate_visual(data: list, chart_type: str, title: str, x_label: str = None, y_label: str = None) -> str:
    """
    Generates a professional visualization chart based on query results.
    Args:
        data: List of dictionaries from SQL results.
        chart_type: 'bar', 'line', 'pie', or 'scatter'.
        title: Chart title.
    """
    if not data:
        return "No data available to visualize."
        
    df = pd.DataFrame(data)
    plt.figure(figsize=(12, 7))
    sns.set_context("talk")
    sns.set_style("whitegrid")

    # Identify numeric and categorical columns automatically if labels aren't provided
    cols = df.columns.tolist()
    x_col = x_label if x_label in cols else cols[0]
    y_col = y_label if y_label in cols else (cols[1] if len(cols) > 1 else cols[0])

    try:
        if chart_type == "line":
            sns.lineplot(data=df, x=x_col, y=y_col, marker='o', color='#004a99')
        elif chart_type == "bar":
            sns.barplot(data=df, x=x_col, y=y_col, palette="Blues_d")
        elif chart_type == "pie":
            plt.pie(df[y_col], labels=df[x_col], autopct='%1.1f%%', colors=sns.color_palette("pastel"))
        elif chart_type == "scatter":
            sns.scatterplot(data=df, x=x_col, y=y_col, s=100, color='#e63946')
        
        plt.title(title, pad=20)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save for UI persistence
        output_path = "output_chart.png"
        plt.savefig(output_path)
        plt.close()
        
        return f"Chart '{title}' generated successfully and saved as {output_path}."
    except Exception as e:
        return f"Error during visualization: {str(e)}"