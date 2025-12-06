# Step 0: Environment Setup

```bash
conda create -n phage_assembly python=3.9 -y
conda activate phage_assembly
conda install -c bioconda fastqc bbmap megahit samtools pilon biopython -y
conda install -c conda-forge seqtk -y
brew install bandage
```