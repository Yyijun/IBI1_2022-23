#store costs in a list
costs=[1,8,15,7,5,14,43,40]
print(costs)

#import modules
import numpy as np
import matplotlib.pyplot as plt
#set options 
N = 8 #the number of columns
costs = (1, 8, 15, 7, 5, 14, 43, 40)
ind = np.arange(N) #the x locations
width = 0.35 #the bar width 
plt.bar(ind, costs, width, color='pink')
#add label, title, x-axis tick labels and y-axis tick labels
plt.ylabel('costs')
plt.title('The cost of hosting the Summer Olympic Games')
plt.xticks(ind, ('Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012'), rotation=15) #to prevent overlapping, change the angle of x-axis tick tabels
plt.yticks(np.arange(0,41,5))

plt.show()