#Count the number of coding sequences contained within each gene
#import the module
import re
#open the file
fa_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
stop_codon = input("Choose a stop codon from 'TAA', 'TAG' and 'TGA':") #set a place to input the stop codon
#create a filename as the new fasta file to be written to
genes = open(f'{stop_codon}_stop_genes.fa','w')
#Stores the sequences of genes whose sequences end with the given stop codon in fasta form
sequence = '' #create sequence to store sequences of required genes
gene_name = '' #create gene_name to store the names of genes
count = 0 #used to count the number of required coding sequences	
for line in fa_file:
    line = line.strip() #put the entire sequence on one line
    if line.startswith('>'):
       if sequence.endswith(f'{stop_codon}'): #filter for required genes
         count = count + 1
         genes.write(f'>{gene_name} {count}\n{sequence}\n') #write down into the genes
       gene_name = re.findall(r'gene:(.+) gene_biotype:.+', line) #read out the gene name
       gene_name = ''.join(gene_name) #convert the list to string
       sequence = '' #empty the sequence
    else:
       sequence = sequence + line #collect the sequences

if sequence.endswith(f'{stop_codon}'):
    genes.write(f'>{gene_name} {count}\n{sequence}\n') #write down the last required gene name and its sequence 

#close the files
genes.close()
fa_file.close()