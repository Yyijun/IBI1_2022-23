#aim: write a new Python class that can be used to contain information about individual athletes and their recorded times for each of the three disciplines (swim, cycle, run)
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
       print("name:",self.name," location:",self.location," swim time:",self.swim, "s", " cycle time:",self.cycle, "s", " run time:", self.run, "s", " total time:", self.total, "s")

#an example of how this class can be used 
Enna = triathlon("Enna Green", "China", 3, 4, 5) #please input all the time in second and do not include the unit when inputing the data
Enna.information()
