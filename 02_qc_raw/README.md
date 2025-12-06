# Step 1: Raw Read QC

```bash
mkdir 01_fastqc_raw
fastqc -o 01_fastqc_raw -t 4 SAMPLE_1.fq SAMPLE_2.fq
```