from Bio import SeqIO
import sys

contig_id=sys.argv[1]
input_file='../06_megahit/assembled.contigs.fa'
output_file='phage_contig.fasta'

for r in SeqIO.parse(input_file,'fasta'):
    if contig_id in r.id:
        SeqIO.write(r,output_file,'fasta')
        print('Extracted',r.id)
        break