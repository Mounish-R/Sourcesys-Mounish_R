def get_eda_prompt(sample_data: str) -> str:
    return f"""
Please act as an expert Data Scientist and analyze the following dataset sample to produce a concise, professional Exploratory Data Analysis (EDA) report.

Format your response exactly using this Markdown structure:

# Exploratory Data Analysis Report

**Dataset Overview:**
[Provide a clear, 1-2 sentence description of what the data represents.]

**Data Quality Assessment:**
- **Missing Values:** [Mention any noticeable missing data]
- **Anomalies & Outliers:** [Highlight apparent errors or outliers]

**Critical Issues Identified:**
[State the single most significant data quality problem.]

**Recommended Actions:**
[Provide a clear, actionable step to resolve the main issue.]

Ensure the tone is highly professional and the response relies purely on the provided sample. Do not include any conversational filler.

Data Sample:
{sample_data}
"""
