# Step 8: Polishing

```bash
samtools view -bS -F4 mapped.sam | samtools sort -o mapped_sorted.bam
samtools index mapped_sorted.bam
pilon --genome phage_contig.fasta --frags mapped_sorted.bam --output polished --changes
```