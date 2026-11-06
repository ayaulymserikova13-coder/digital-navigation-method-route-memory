
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# Project paths
ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "processed" / "bootstrap_ci.csv"
FIGURES_DIR = ROOT / "reports" / "figures"

FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Load calculated statistics
df = pd.read_csv(DATA_FILE)

# Select primary research metric
metric = "direction_recall_accuracy"

plot_data = (
    df[df["metric"] == metric]
    .set_index("group")
    .loc[["TBT", "MAP"]]
)

means = plot_data["mean"].to_numpy()
lower_errors = means - plot_data["ci_lower"].to_numpy()
upper_errors = plot_data["ci_upper"].to_numpy() - means

# Create scientific figure
fig, ax = plt.subplots(figsize=(7, 5))

positions = [0, 1]
colors = ["#0072B2", "#E69F00"]

ax.bar(
    positions,
    means,
    color=colors,
    width=0.55,
    alpha=0.85
)

ax.errorbar(
    positions,
    means,
    yerr=[lower_errors, upper_errors],
    fmt="o",
    color="black",
    capsize=6,
    linewidth=1.8,
    markersize=5
)

ax.set_xticks(positions)
ax.set_xticklabels(["TBT (baseline)", "MAP"])
ax.set_ylabel("Direction recall accuracy (%)")
ax.set_xlabel("Navigation method")
ax.set_title("Direction Recall by Navigation Method")

ax.set_ylim(0, 105)
ax.grid(axis="y", alpha=0.25)
ax.set_axisbelow(True)

fig.tight_layout()

# Save publication-ready figures
png_path = FIGURES_DIR / "direction_recall.png"
pdf_path = FIGURES_DIR / "direction_recall.pdf"

fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(pdf_path, bbox_inches="tight")

plt.close(fig)

print("Direction recall figure created successfully")
print("PNG:", png_path)
print("PDF:", pdf_path)


# Second figure: Landmark Recognition Accuracy
metric = "landmark_recognition_accuracy"

plot_data = (
    df[df["metric"] == metric]
    .set_index("group")
    .loc[["TBT", "MAP"]]
)

means = plot_data["mean"].to_numpy()
lower_errors = means - plot_data["ci_lower"].to_numpy()
upper_errors = plot_data["ci_upper"].to_numpy() - means

fig, ax = plt.subplots(figsize=(7, 5))

ax.bar(
    positions,
    means,
    color=colors,
    width=0.55,
    alpha=0.85
)

ax.errorbar(
    positions,
    means,
    yerr=[lower_errors, upper_errors],
    fmt="o",
    color="black",
    capsize=6,
    linewidth=1.8,
    markersize=5
)

ax.set_xticks(positions)
ax.set_xticklabels(["TBT (baseline)", "MAP"])
ax.set_ylabel("Landmark recognition accuracy (%)")
ax.set_xlabel("Navigation method")
ax.set_title("Landmark Recognition by Navigation Method")

ax.set_ylim(0, 105)
ax.grid(axis="y", alpha=0.25)
ax.set_axisbelow(True)

fig.tight_layout()

png_path = FIGURES_DIR / "landmark_recognition.png"
pdf_path = FIGURES_DIR / "landmark_recognition.pdf"

fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(pdf_path, bbox_inches="tight")

plt.close(fig)

print("\nLandmark recognition figure created successfully")
print("PNG:", png_path)
print("PDF:", pdf_path)


# Third figure: MAP minus TBT group differences
comparison_file = ROOT / "data" / "processed" / "group_comparison.csv"
comparison = pd.read_csv(comparison_file)

metric_order = [
    "direction_recall_accuracy",
    "landmark_recognition_accuracy"
]

comparison = (
    comparison.set_index("metric")
    .loc[metric_order]
)

differences = comparison["difference_pp"].to_numpy()
lower = comparison["ci_lower"].to_numpy()
upper = comparison["ci_upper"].to_numpy()

# Asymmetric 95% confidence intervals
errors = [
    differences - lower,
    upper - differences
]

labels = [
    "Direction recall",
    "Landmark recognition"
]

fig, ax = plt.subplots(figsize=(8, 4.8))

y_positions = [1, 0]

ax.errorbar(
    differences,
    y_positions,
    xerr=errors,
    fmt="o",
    color="#0072B2",
    ecolor="#0072B2",
    markersize=9,
    capsize=6,
    linewidth=2
)

# Zero means no difference between groups
ax.axvline(
    x=0,
    color="gray",
    linestyle="--",
    linewidth=1.5
)

ax.set_yticks(y_positions)
ax.set_yticklabels(labels)

ax.set_xlabel("Mean difference: MAP - TBT (percentage points)")
ax.set_title("Navigation Method Effects on Route Memory")

ax.set_xlim(-15, 35)
ax.set_ylim(-0.5, 1.5)
ax.grid(axis="x", alpha=0.25)
ax.set_axisbelow(True)

fig.tight_layout()

png_path = FIGURES_DIR / "group_differences.png"
pdf_path = FIGURES_DIR / "group_differences.pdf"

fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(pdf_path, bbox_inches="tight")

plt.close(fig)

print("\nGroup differences figure created successfully")
print("PNG:", png_path)
print("PDF:", pdf_path)


# Fourth figure: Self-Reported Navigation Habits (RQ1)
import numpy as np

participant_file = ROOT / "data" / "processed" / "participant_scores.csv"
participants = pd.read_csv(participant_file)

# Paired differences for each participant
paired_differences = (
    participants["tbt_trips_30d"] -
    participants["map_study_trips_30d"]
).to_numpy()

mean_difference = paired_differences.mean()

# Bootstrap 95% confidence interval
rng = np.random.default_rng(42)
n_bootstrap = 10000

bootstrap_means = np.array([
    rng.choice(
        paired_differences,
        size=len(paired_differences),
        replace=True
    ).mean()
    for _ in range(n_bootstrap)
])

ci_lower, ci_upper = np.percentile(
    bootstrap_means,
    [2.5, 97.5]
)

# Create scientific figure
fig, ax = plt.subplots(figsize=(9, 5))

participant_indices = np.arange(len(paired_differences))

ax.scatter(
    paired_differences,
    participant_indices,
    color="#0072B2",
    s=45,
    alpha=0.85,
    label="Individual participants"
)

# Mean difference with bootstrap confidence interval
ax.errorbar(
    mean_difference,
    9.5,
    xerr=[
        [mean_difference - ci_lower],
        [ci_upper - mean_difference]
    ],
    fmt="D",
    color="#D55E00",
    markersize=9,
    capsize=6,
    linewidth=2.5,
    label="Mean difference (95% CI)"
)

ax.axvline(
    x=0,
    color="gray",
    linestyle="--",
    linewidth=1.5
)

ax.set_xlabel("TBT - MAP study (trips per 30 days)")
ax.set_ylabel("Participant index")
ax.set_title("Self-Reported Navigation Habits: Paired Differences")

ax.grid(axis="x", alpha=0.2)
ax.set_axisbelow(True)

fig.tight_layout()

png_path = FIGURES_DIR / "navigation_habits.png"
pdf_path = FIGURES_DIR / "navigation_habits.pdf"

fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(pdf_path, bbox_inches="tight")

plt.close(fig)

print("\nNavigation habits figure created successfully")
print("Mean difference:", round(mean_difference, 2))
print("95% CI:", round(ci_lower, 2), round(ci_upper, 2))
print("PNG:", png_path)
print("PDF:", pdf_path)
