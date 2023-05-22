#aim: write a new Python class that can be used to contain information about individual athletes and their recorded times for each of the three disciplines (swim, cycle, run)
#create a class called 'triathlon'
class triathlon(object):
   def __init__(self, a, b, c, d, e, f):
       #define attributes
       self.firstname=a
       self.lastname=b
       self.location=c
       self.swim=d
       self.cycle=e
       self.run=f
       self.total=d+e+f
   def information(self):
       print("name:",self.firstname,self.lastname," location:",self.location," swim time:",self.swim, "s", " cycle time:",self.cycle, "s", " run time:", self.run, "s", " total time:", self.total, "s")

#an example of how this class can be used 
Enna = triathlon("Enna", "Green", "China", 3, 4, 5) #please input all the time in second and do not include the unit when inputing the data
Enna.information()
