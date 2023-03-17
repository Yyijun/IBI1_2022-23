#start with two rabbits
n = 2
#define a variable to count the number of generations
generation = 1
#repeat
while 1 == 1:
#  the number of rabbits that will be born at this gneration
   born_rabbits_number = n
#  the total number of rabbits
   n = n+born_rabbits_number
#  count the number of generations
   generation = generation+1
#  if less than 100: keep breeding
#  if more than 100: DONE
   if n > 100:
      break
#convert a number into a string
generation_number = str(generation)
print("At",generation_number,"th generation, over 100 rabbits have been born")
