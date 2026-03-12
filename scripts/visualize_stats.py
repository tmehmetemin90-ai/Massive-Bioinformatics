from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_dir = Path(__file__).resolve().parent.parent
results_dir = base_dir / "results"

df = pd.read_csv(results_dir / "read_stats.csv", sep=";")

upper = df["read_length"].quantile(0.99)

plt.figure(figsize=(8,5))
sns.histplot(df[df["read_length"] <= upper]["read_length"], bins=50)
plt.title("Read Length Distribution (up to 99th percentile)")
plt.xlabel("Read Length")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(results_dir / "read_length_distribution.png")
plt.close()
#graphic GC content
plt.figure(figsize=(8,5))
sns.histplot(df["gc_content"], bins=50)
plt.title("GC Content Distribution")
plt.xlabel("GC Content (%)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(results_dir / "gc_content_distribution.png")
plt.close()

plt.figure(figsize=(8,5))
sns.histplot(df["mean_quality"], bins=50)
plt.title("Mean Read Quality Distribution")
plt.xlabel("Mean Quality Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(results_dir / "quality_distribution.png")
plt.close()

summary = df[["read_length", "gc_content", "mean_quality"]].describe()

with open(results_dir / "summary_statistics.txt", "w", encoding="utf-8") as f:
    f.write("Summary statistics\n\n")
    f.write(summary.to_string())

print("Visualization completed.")
