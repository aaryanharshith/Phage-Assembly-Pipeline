# Step 2: Trimming

```bash
cat > adapters.fa << 'EOF'
>Adapter
AATGATACGG...
EOF

bbduk.sh in1=SAMPLE_1.fq in2=SAMPLE_2.fq out1=SAMPLE_1_trimmed.fq out2=SAMPLE_2_trimmed.fq ref=adapters.fa qtrim=rl trimq=20 minlen=100
```