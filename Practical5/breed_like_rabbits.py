#start with two rabbits
n = 2
#it is the first generation
generation = 1
#stop when having at least 100 rabbits
if n < 100:
#  the number of rabbits that will be born at this gneration
   born_rabbits_number = n
#  the total number of rabbits
   n = n+born_rabbits_number
#  count the number of generations
   generation = generation+1

#convert a number into a string
generation_number = str(generation)
#print the output
print ("At",generation_number,"th generation, over 100 rabbits have been born")