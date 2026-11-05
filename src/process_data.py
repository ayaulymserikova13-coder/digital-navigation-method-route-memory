import numpy as np
from pathlib import Path
import pandas as pd

# Project paths
ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = ROOT / "data" / "raw" / "Route_Memory_Google_Forms_Results.xlsx"
OUTPUT_FILE = ROOT / "data" / "processed" / "participant_scores.csv"

# Load real experiment data
responses = pd.read_excel(INPUT_FILE, sheet_name="Form Responses")
answer_key = pd.read_excel(INPUT_FILE, sheet_name="Answer Key")

print("Digital Navigation Route Memory - Data Processing")
print("Total participants:", len(responses))


# Validate raw experiment data
print("\nRAW DATA VALIDATION")

# Check participant count
if len(responses) != 20:
    raise ValueError("Expected 20 participants")

# Check unique participant IDs
if responses["Participant ID"].isna().any():
    raise ValueError("Missing participant IDs")

if responses["Participant ID"].duplicated().any():
    raise ValueError("Duplicate participant IDs")

# Check assigned groups
group_counts_raw = responses[
    "Assigned navigation group"
].value_counts()

if group_counts_raw.to_dict() != {"TBT": 10, "MAP": 10}:
    raise ValueError(
        f"Unexpected group distribution: {group_counts_raw.to_dict()}"
    )

print("Participant IDs: valid")
print("Group distribution: valid")


# Check required columns
required_columns = [
    "Participant ID",
    "Assigned navigation group",
    "Was this route unfamiliar?",
    "TBT trips (last 30 days)",
    "MAP trips (last 30 days)",
] + [
    f"D{i} — Direction Recall" for i in range(1, 6)
] + [
    f"L{i} — Landmark Recognition" for i in range(1, 11)
]

missing_columns = [
    column for column in required_columns
    if column not in responses.columns
]

if missing_columns:
    raise ValueError(f"Missing columns: {missing_columns}")

# Read correct answers from the Answer Key sheet
key = dict(zip(
    answer_key.iloc[:, 0].astype(str).str.strip(),
    answer_key.iloc[:, 1].astype(str).str.strip()
))


# Validate original direction and landmark answers
direction_options = {"Turn left", "Turn right", "Go straight"}
landmark_options = {"Yes", "No"}

for i in range(1, 6):
    column = f"D{i} — Direction Recall"

    if f"D{i}" not in key:
        raise ValueError(f"Missing answer key for D{i}")

    if key[f"D{i}"] not in direction_options:
        raise ValueError(f"Invalid answer key for D{i}")

    answers = responses[column].dropna().astype(str).str.strip()
    invalid = ~answers.isin(direction_options)

    if invalid.any():
        raise ValueError(f"Invalid answers in {column}")

for i in range(1, 11):
    column = f"L{i} — Landmark Recognition"

    if f"L{i}" not in key:
        raise ValueError(f"Missing answer key for L{i}")

    if key[f"L{i}"] not in landmark_options:
        raise ValueError(f"Invalid answer key for L{i}")

    answers = responses[column].dropna().astype(str).str.strip()
    invalid = ~answers.isin(landmark_options)

    if invalid.any():
        raise ValueError(f"Invalid answers in {column}")

print("\nAnswer validation: OK")


# Calculate participant-level accuracy
results = []

for _, participant in responses.iterrows():
    direction_correct = 0
    landmark_correct = 0

    for i in range(1, 6):
        column = f"D{i} — Direction Recall"
        answer = str(participant[column]).strip()
        correct_answer = key[f"D{i}"]

        if answer == correct_answer:
            direction_correct += 1

    for i in range(1, 11):
        column = f"L{i} — Landmark Recognition"
        answer = str(participant[column]).strip()
        correct_answer = key[f"L{i}"]

        if answer == correct_answer:
            landmark_correct += 1

    results.append({
        "participant_id": participant["Participant ID"],
        "group": participant["Assigned navigation group"],
        "tbt_trips_30d": participant["TBT trips (last 30 days)"],
        "map_study_trips_30d": participant["MAP trips (last 30 days)"],
        "direction_correct": direction_correct,
        "landmark_correct": landmark_correct,
        "direction_recall_accuracy": direction_correct / 5 * 100,
        "landmark_recognition_accuracy": landmark_correct / 10 * 100,
    })

df = pd.DataFrame(results)

# Save processed data
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

# Show group-level results
summary = df.groupby("group")[
    ["direction_recall_accuracy", "landmark_recognition_accuracy"]
].mean()

print("\nGroup summary (%):")
print(summary.round(2))

print("\nProcessed data saved to:")
print(OUTPUT_FILE)

# Descriptive statistics
metrics = [
    "direction_recall_accuracy",
    "landmark_recognition_accuracy"
]

statistics = []

for group, group_data in df.groupby("group"):
    for metric in metrics:
        values = group_data[metric]

        statistics.append({
            "group": group,
            "metric": metric,
            "n": len(values),
            "mean": values.mean(),
            "median": values.median(),
            "std": values.std(),
            "p25": values.quantile(0.25),
            "p75": values.quantile(0.75),
            "p95": values.quantile(0.95)
        })

stats_df = pd.DataFrame(statistics)

stats_file = ROOT / "data" / "processed" / "descriptive_statistics.csv"
stats_df.to_csv(stats_file, index=False)

print("\nDescriptive statistics:")
print(stats_df.round(2).to_string(index=False))

print("\nStatistics saved to:", stats_file)


# Bootstrap 95% confidence intervals
RANDOM_SEED = 42
N_BOOTSTRAP = 10000

rng = np.random.default_rng(RANDOM_SEED)

bootstrap_results = []

for group, group_data in df.groupby("group"):
    for metric in metrics:
        values = group_data[metric].to_numpy(dtype=float)

        bootstrap_means = []

        for _ in range(N_BOOTSTRAP):
            sample = rng.choice(
                values,
                size=len(values),
                replace=True
            )
            bootstrap_means.append(sample.mean())

        ci_lower = np.percentile(bootstrap_means, 2.5)
        ci_upper = np.percentile(bootstrap_means, 97.5)

        bootstrap_results.append({
            "group": group,
            "metric": metric,
            "mean": values.mean(),
            "ci_lower": ci_lower,
            "ci_upper": ci_upper,
            "n_bootstrap": N_BOOTSTRAP
        })

bootstrap_df = pd.DataFrame(bootstrap_results)

bootstrap_file = (
    ROOT / "data" / "processed" / "bootstrap_ci.csv"
)

bootstrap_df.to_csv(bootstrap_file, index=False)

print("\nBootstrap 95% Confidence Intervals:")
print(bootstrap_df.round(2).to_string(index=False))

print("\nBootstrap results saved to:", bootstrap_file)


# Bootstrap comparison: MAP minus TBT
comparison_results = []

for metric in metrics:
    map_values = df.loc[
        df["group"] == "MAP", metric
    ].to_numpy(dtype=float)

    tbt_values = df.loc[
        df["group"] == "TBT", metric
    ].to_numpy(dtype=float)

    observed_difference = map_values.mean() - tbt_values.mean()

    bootstrap_differences = []

    for _ in range(N_BOOTSTRAP):
        map_sample = rng.choice(
            map_values, size=len(map_values), replace=True
        )
        tbt_sample = rng.choice(
            tbt_values, size=len(tbt_values), replace=True
        )

        difference = map_sample.mean() - tbt_sample.mean()
        bootstrap_differences.append(difference)

    ci_lower, ci_upper = np.percentile(
        bootstrap_differences, [2.5, 97.5]
    )

    comparison_results.append({
        "metric": metric,
        "map_mean": map_values.mean(),
        "tbt_mean": tbt_values.mean(),
        "difference_pp": observed_difference,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper,
        "n_map": len(map_values),
        "n_tbt": len(tbt_values)
    })

comparison_df = pd.DataFrame(comparison_results)

comparison_file = (
    ROOT / "data" / "processed" / "group_comparison.csv"
)

comparison_df.to_csv(comparison_file, index=False)

print("\nMAP vs TBT comparison (percentage points):")
print(comparison_df.round(2).to_string(index=False))

print("\nComparison saved to:", comparison_file)


# Data quality checks
print("\nDATA QUALITY CHECKS")

# Check participant IDs
duplicate_ids = df["participant_id"].duplicated().sum()
print("Duplicate participant IDs:", duplicate_ids)

# Check group sizes
group_counts = df["group"].value_counts()
print("\nParticipants per group:")
print(group_counts.to_string())

# Check missing values in processed data
missing_values = df.isna().sum().sum()
print("\nMissing values:", missing_values)

# Check accuracy boundaries
for metric in metrics:
    invalid = (~df[metric].between(0, 100)).sum()
    print(f"Invalid values in {metric}:", invalid)

# Save data quality summary
quality_df = pd.DataFrame([{
    "total_participants": len(df),
    "duplicate_ids": int(duplicate_ids),
    "missing_values": int(missing_values),
    "map_participants": int(group_counts.get("MAP", 0)),
    "tbt_participants": int(group_counts.get("TBT", 0))
}])

quality_file = ROOT / "data" / "processed" / "data_quality.csv"
quality_df.to_csv(quality_file, index=False)

print("\nData quality report saved to:", quality_file)
