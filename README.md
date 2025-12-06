# 🧬 Phage Genome Assembly Pipeline
A lightweight, beginner-friendly, Mac-optimized pipeline for assembling bacteriophage genomes from paired-end Illumina reads.  
This workflow was inspired by Millard *et al.* (2021) and has been used to assemble Pseudomonas phages *Vanta* and *Luminis*.

---

## 📂 Repository Layout

Each folder contains:
- A **README.md** describing the step
- Example commands using generic filenames
- Scripts where applicable

**Pipeline Overview**
1. **Environment Setup** – Install required software  
2. **Raw Read QC** – FASTQC  
3. **Trimming** – BBDUK  
4. **Post-Trim QC** – FASTQC  
5. **Subsampling** – Reduce read depth to ~80×  
6. **Assembly** – MEGAHit  
7. **Coverage Mapping** – BBMap  
8. **Extract Contig** – Identify & isolate dominant phage contig  
9. **Polish** – Pilon  
10. **Final QC + Stats** – Validate assembly  
11. **(Optional) Structure Determination** – Run PhageTerm on Galaxy

---

## 🔧 Requirements
- macOS (Linux also works; commands easily adaptable)
- Conda (Miniconda or Anaconda)
- Homebrew (for Bandage visualization)

---

## ▶️ Quickstart

```bash
git clone https://github.com/<your-lab>/phage-genome-assembly-pipeline.git
cd phage-genome-assembly-pipeline
