rule all:
    input:
        "results/read_stats.csv",
        "results/read_length_distribution.png",
        "results/gc_content_distribution.png",
        "results/quality_distribution.png",
        "results/summary_statistics.txt"


rule stats:
    input:
        "data/barcode77.fastq"
    output:
        "results/read_stats.csv"
    shell:
        "python scripts/read_stats.py"


rule plots:
    input:
        "results/read_stats.csv"
    output:
        "results/read_length_distribution.png",
        "results/gc_content_distribution.png",
        "results/quality_distribution.png",
        "results/summary_statistics.txt"
    shell:
        "python scripts/visualize_stats.py"
