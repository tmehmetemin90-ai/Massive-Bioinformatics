from pathlib import Path
import pandas as pd
from Bio import SeqIO

base_dir = Path(__file__).resolve().parent.parent
data_dir = base_dir / "data"
results_dir = base_dir / "results"
results_dir.mkdir(exist_ok=True)

all_stats = []

for record in SeqIO.parse(data_dir / "barcode77.fastq", "fastq"):
    seq = str(record.seq).upper()
    length = len(seq)

    gc_count = seq.count("G") + seq.count("C")
    gc_content = (gc_count / length) * 100

    qualities = record.letter_annotations["phred_quality"]
    mean_quality = sum(qualities) / len(qualities)

    all_stats.append([record.id, length, gc_content, mean_quality])

df = pd.DataFrame(all_stats, columns=["read_id", "read_length", "gc_content", "mean_quality"])
df["gc_content"] = df["gc_content"].round(2)
df["mean_quality"] = df["mean_quality"].round(2)

df.to_csv(results_dir / "read_stats.csv", index=False, sep=";")

print(df.head())
print("Number of reads:", len(df))
