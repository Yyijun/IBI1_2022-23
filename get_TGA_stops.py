#extract all the genes whose sequence ends with the 'TGA' stop codon from the file
#import the module
import re
#open the file
fa_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
TGA_genes = open('TGA_genes.fa','w')
sequence = ''
gene_name = ''
for line in fa_file:
    line = line.strip()
    if line.startswith('>'):
       if sequence.endswith('TGA'): #filter for required genes
         TGA_genes.write(f'>{gene_name}\n{sequence}\n') #write down into the TGA_genes
       gene_name = re.findall(r'gene:(.+) gene_biotype:.+', line) #read out the gene name
       gene_name = ''.join(gene_name) #convert the list to string
       sequence = '' #empty the sequence
    else:
       sequence = sequence + line #collect the sequences

if sequence.endswith('TGA'):
    TGA_genes.write(f'>{gene_name}\n{sequence}\n') #write down the last required gene name and its sequence which are not writen down in the loop

#close the files
TGA_genes.close()
fa_file.close()