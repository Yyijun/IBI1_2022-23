# What does this piece of code do?
# Answer: This piece of code draws a random integer between 1 and 100 ten times and then prints the maximum value obtained in these ten times.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
#repeat for ten times
while progress<10: 
	progress+=1
	n = randint(1,100)
	if n > stored_random_number:
		stored_random_number = n
#print the maximum value
print(stored_random_number)
