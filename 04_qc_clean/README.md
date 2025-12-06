# Step 3: Post-Trimming QC

```bash
mkdir 03_fastqc_clean
fastqc -o 03_fastqc_clean -t 4 SAMPLE_*_trimmed.fq
```