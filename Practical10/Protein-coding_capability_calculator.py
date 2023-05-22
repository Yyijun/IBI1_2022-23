#aim: write a function that determines whether a given DNA sequence is likely to be protein-coding or not
#define a function with the name "sequence"
def sequence(dna_seq):
   #import module
   import re
   dna_seq=dna_seq.upper() #convert all the letters in the dna_seq into capital letters
   within_codons=re.findall(r'ATG(.*)TGA', dna_seq) #read out the bases between 'ATG' and 'TGA'
   within_codons="".join(within_codons) #convert the list into string
   count=len(within_codons)
   total_count=len(dna_seq)
   proportion=count/total_count*100
   if proportion > 50:
      return "The percentage of this sequence which is coding is", proportion,"%.","The sequence should be labelled as 'protein-coding'."
   if proportion < 10:
      return "The percentage of this sequence which is coding is", proportion,"%.","The sequence should be labelled as 'non-coding'."
   elif proportion <= 50:
      return "The percentage of this sequence which is coding is", proportion,"%.","The sequence should be labelled as 'unclear'."
 
#an example of how the function should be called 
result=sequence("ATGAaATGA")
print(*result)
