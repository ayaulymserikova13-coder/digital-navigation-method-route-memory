import pandas as pd
import yaml

# Load configuration
with open("configs/config.yaml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

# Load paths and metrics from configuration
data_path = config["data"]["sample_path"]
output_path = config["data"]["output_path"]

primary_metric = config["metrics"]["primary"]
secondary_metric = config["metrics"]["secondary"]
rq1_tbt_metric = config["metrics"]["rq1_tbt"]
rq1_map_metric = config["metrics"]["rq1_map"]

# Load sample data
df = pd.read_csv(data_path)

# Validate required columns
required_columns = {
    "participant_id",
    "group",
    primary_metric,
    secondary_metric,
    rq1_tbt_metric,
    rq1_map_metric,
}

missing_columns = required_columns - set(df.columns)

if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

# RQ1: navigation habits
rq1_results = df[[rq1_tbt_metric, rq1_map_metric]].mean()

# RQ2 and RQ3: experimental outcomes
group_results = df.groupby("group")[
    [primary_metric, secondary_metric]
].mean()

print("Digital Navigation Route Memory Benchmark")
print("=" * 42)

print("\nRQ1 Navigation Frequency Means")
print(rq1_results)

print("\nRQ2 and RQ3 Group Accuracy Means")
print(group_results)

# Save group benchmark results
group_results.to_csv(output_path)

print(f"\nResults saved to {output_path}")