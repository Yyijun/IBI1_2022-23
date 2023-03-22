#store costs in a list
costs = [1,8,15,7,5,14,43,40]
#sort the values in costs
sorted_costs = sorted(costs)
print(sorted_costs)

#creat a list to store Olympic games
Olympic_Games = ['Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012']

#I had help from instructor Hugo Samano in IBI1 practical 6 to sort the Olympic_Games according to the sorted costs
#import module
import numpy
Olympic_Games = numpy.array(Olympic_Games)
costs = numpy.array(costs)
inds = costs.argsort() #inds is used to store changes in the costs
sorted_Olympic_Games = Olympic_Games[inds] #change the the Olympic_Games according to the sorted costs

#import modules
import numpy as np
import matplotlib.pyplot as plt
#set options 
N = 8 #the number of columns
ind = np.arange(N) #the x locations
width = 0.35 #the bar width 
plt.bar(ind, sorted_costs, width, color='pink')
#add label, title, x-axis tick labels and y-axis tick labels
plt.ylabel('costs')
plt.title('The costs of hosting the Summer Olympic Games')
plt.xticks(ind, (sorted_Olympic_Games), rotation=15) #to prevent overlapping, change the angle of x-axis tick tabels
plt.yticks(np.arange(0,41,5))

plt.show()
