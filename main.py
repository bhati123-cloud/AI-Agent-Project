import os
import pandas as pd
import numpy as np
import warnings
from datetime import datetime
from kaggle.api.kaggle_api_extended import KaggleApi

# 1. Dataset Discovery & Selection
def discover_datasets(theme="E-Commerce Sales"):
    # Use Kaggle API to search for datasets
    api = KaggleApi()
    api.authenticate()
    search_results = api.dataset_list(search=theme, sort_by='hottest')
    datasets = []
    for ds in search_results:
        datasets.append({
            "ref": ds.ref,
            "title": ds.title,
            "subtitle": ds.subtitle,
            "url": f"https://www.kaggle.com/datasets/{ds.ref}",
            "description": ds.subtitle or ds.title
        })
    if not datasets:
        raise Exception("No datasets found for the theme on Kaggle.")
    # Pick the first dataset (most relevant)
    return datasets[0]

# 2. Data Ingestion & Preprocessing
def ingest_and_preprocess(dataset):
    print(f"Downloading dataset: {dataset['title']}")
    api = KaggleApi()
    api.authenticate()
    download_dir = "kaggle_data"
    os.makedirs(download_dir, exist_ok=True)
    api.dataset_download_files(dataset['ref'], path=download_dir, unzip=True)
    # Find a CSV or Excel file in the downloaded folder
    files = os.listdir(download_dir)
    data_file = None
    for f in files:
        if f.endswith('.csv') or f.endswith('.xlsx'):
            data_file = os.path.join(download_dir, f)
            break
    if not data_file:
        raise Exception("No CSV or Excel file found in the downloaded dataset.")
    if data_file.endswith('.csv'):
        df = pd.read_csv(data_file, low_memory=False)
    else:
        df = pd.read_excel(data_file)
    # Basic preprocessing: drop duplicates, handle missing values
    df = df.drop_duplicates()
    missing = df.isnull().sum()
    # Fill numeric NaNs with median, categorical with mode
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=FutureWarning)
        for col in df.columns:
            if df[col].dtype in [np.float64, np.int64]:
                df[col] = df[col].fillna(df[col].median())
            else:
                df[col] = df[col].fillna(df[col].mode()[0])
    df = df.infer_objects(copy=False)
    return df, missing

# 3. Exploratory Data Analysis (EDA)
def perform_eda(df):
    eda = {}
    eda["shape"] = df.shape
    eda["columns"] = list(df.columns)
    eda["dtypes"] = df.dtypes.astype(str).to_dict()
    eda["describe"] = df.describe(include="all").to_dict()
    eda["missing"] = df.isnull().sum().to_dict()
    return eda

# 4. Insight Generation
def generate_insights(df):
    insights = []
    # 1. Top correlation
    corr = df.select_dtypes(include=[np.number]).corr()
    corr_pairs = corr.unstack().sort_values(ascending=False)
    for (a, b), val in corr_pairs.items():
        if a != b and abs(val) > 0.7:
            insights.append(f"Strong correlation ({val:.2f}) between '{a}' and '{b}'.")
            break
    # 2. Outlier detection (z-score)
    for col in df.select_dtypes(include=[np.number]).columns:
        z = (df[col] - df[col].mean()) / df[col].std()
        outliers = (abs(z) > 3).sum()
        if outliers > 0:
            insights.append(f"Column '{col}' has {outliers} outliers (z-score > 3).")
            break
    # 3. Trend: increasing/decreasing mean by a categorical variable
    for col in df.select_dtypes(include=[object]).columns:
        if df[col].nunique() < 10:
            means = df.groupby(col)[df.select_dtypes(include=[np.number]).columns[0]].mean()
            if means.is_monotonic_increasing:
                insights.append(f"Mean of '{df.select_dtypes(include=[np.number]).columns[0]}' increases with '{col}'.")
                break
            elif means.is_monotonic_decreasing:
                insights.append(f"Mean of '{df.select_dtypes(include=[np.number]).columns[0]}' decreases with '{col}'.")
                break
    # 4. Most common value
    for col in df.columns:
        common = df[col].mode()[0]
        insights.append(f"Most common value in '{col}' is '{common}'.")
        break
    # 5. Unique value count
    for col in df.columns:
        unique = df[col].nunique()
        if unique == df.shape[0]:
            insights.append(f"Column '{col}' has all unique values (possible ID field).")
            break
    return insights[:5]

# 5. Reporting
def generate_report(dataset, eda, insights, output_path="insight_report.md"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# AI Agent Insight Report\n")
        f.write(f"**Dataset:** {dataset['title']}\n\n")
        f.write(f"**Description:** {dataset['description']}\n\n")
        f.write(f"**Generated on:** {now}\n\n")
        f.write("## Dataset Overview\n")
        f.write(f"- Shape: {eda['shape']}\n")
        f.write(f"- Columns: {eda['columns']}\n")
        f.write(f"- Data Types: {eda['dtypes']}\n\n")
        f.write("## Basic Statistics\n")
        for col, stats in eda["describe"].items():
            f.write(f"**{col}**: {stats}\n\n")
        f.write("## Missing Values\n")
        for col, miss in eda["missing"].items():
            if miss > 0:
                f.write(f"- {col}: {miss} missing\n")
        f.write("\n## Key Insights\n")
        for i, insight in enumerate(insights, 1):
            f.write(f"{i}. {insight}\n")
    print(f"Report generated at {output_path}")

# 6. Simulated Output (Email/Gist/Local)
def send_report(output_path):
    print(f"Report available at: {os.path.abspath(output_path)}")

# Main Agent Workflow
def main():
    theme = "E-Commerce Sales"
    dataset = discover_datasets(theme)
    df, missing = ingest_and_preprocess(dataset)
    eda = perform_eda(df)
    insights = generate_insights(df)
    report_path = "insight_report.md"
    generate_report(dataset, eda, insights, report_path)
    send_report(report_path)

if __name__ == "__main__":
    main()

# Agent Design Note:
"""
Agent Design Note:
The agent simulates autonomous decision-making at each step. For dataset selection, it uses Kaggle API to dynamically search for datasets relevant to the theme. Preprocessing is generic: duplicates are dropped, and missing values are filled using median/mode. EDA and insight generation are modular, using basic statistics, correlation, and outlier detection to surface interesting patterns. The report is output as Markdown for easy sharing. 

The following features are not implemented but are possible future improvements: more advanced insight generation (using LLMs or AutoML), richer reporting (HTML/PDF with charts), and real email/GitHub integration.
"""
