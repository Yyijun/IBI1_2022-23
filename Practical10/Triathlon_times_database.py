#aim: write a new Python class that can be used to contain information about individual athletes and their recorded times for each of the three disciplines (swim, cycle, run)
#please input all the time in second or minute
#create a class called 'triathlon'
class triathlon(object):
   def __init__(self, a, b, c, d, e):
       #define attributes
       self.name=a
       self.location=b
       self.swim=c
       self.cycle=d
       self.run=e
       self.total=c+d+e
   def information(self):
       print("name:",self.name," location:",self.location," swim time:",self.swim, " cycle time:",self.cycle, " run time:", self.run," total time:", self.total)

#an example of how this class can be used
Enna = triathlon("Enna Green", "China", 3, 4, 5) 
Enna.information()
