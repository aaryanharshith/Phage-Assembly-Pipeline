# Step 4: Subsampling

```bash
R1_READS=$(grep -c '^@' SAMPLE_1_trimmed.fq)
GENOME_SIZE=60000
READ_LENGTH=150
CURRENT_COV=$(echo "scale=2; ($R1_READS*2*$READ_LENGTH)/$GENOME_SIZE" | bc)
READS_NEEDED=$(echo "scale=0; (80*$GENOME_SIZE)/(2*$READ_LENGTH)" | bc)
seqtk sample -s100 SAMPLE_1_trimmed.fq $READS_NEEDED > SAMPLE_1_sub80x.fq
seqtk sample -s100 SAMPLE_2_trimmed.fq $READS_NEEDED > SAMPLE_2_sub80x.fq
gzip SAMPLE_1_sub80x.fq SAMPLE_2_sub80x.fq
```