#import modules
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# input .csv file
covid_data = pd.read_csv("full_data.csv")


# showing the second column from every 100th row from the first 1000 rows (inclusive)
covid_data.iloc[0:1001:100,1]


# Aim: used a Boolean to show “total cases” for all rows corresponding to Afghanistan
# read the "location" column with all the rows
location_column = [False, True, False, False, False, False]
location_data = covid_data.iloc[:,location_column]
# create a Boolean that is True when the “location” is “Afghanistan”, but false otherwise
Afghanistan_row = [] #create a list to store Boolean values
for i in location_data.location: #use loop to read locations
    Boolean = i=="Afghanistan"
    Afghanistan_row.append(Boolean) #add elements

# use the Boolean to find exactly the rows I need in the dataframe
covid_data.loc[Afghanistan_row,"total_cases"]


# Aim: computed the mean number of new cases and new deaths on 31 March 2020
# read out specific rows and columns
date_column = [True, False, False, False, False, False]
date_data = covid_data.iloc[:,date_column]
need_row = [] #create a list to store Boolean values
for i in date_data.date: #use loop to read dates
    BV = i=="2020-03-31"
    need_row.append(BV) #add elements

new_data = covid_data.loc[need_row,["location","new_cases","new_deaths"]]
#compute the mean new cases and new deaths on this date
mean_new_cases = np.mean(new_data.new_cases)
mean_new_deaths = np.mean(new_data.new_deaths)
print("mean_new_cases=",mean_new_cases)
print("mean_new_deaths=",mean_new_deaths)


# Aim: create boxplot of new cases and new deaths on 31 March 2020
# create the boxplot of new cases
plt.boxplot(new_data.new_cases, vert = True, whis = 1.5, patch_artist = True, meanline = False, showbox = True, showcaps = True, showfliers = True, notch = False) 
plt.show()
# create the boxplot of new deaths
plt.boxplot(new_data.new_deaths, vert = True, whis = 1.5, patch_artist = True, meanline = False, showbox = True, showcaps = True, showfliers = True, notch = False) 
plt.show()


# Aim: plot both new cases and new deaths worldwide over time
# plot the new cases worldwide over time with blue circles
# find all the dates
world_date = []
for i in covid_data.date:
    if not i in world_date:
       world_date.append(i)

world_date = sorted(world_date)
# compute the numbers of new cases and new deaths worldwide of different days
new_cases_worldwide = []
for i in world_date:
    new_cases_worldwide.append(np.sum(covid_data.loc[covid_data.loc[:,"date"] == i, "new_cases"]))

new_deaths_worldwide = []
for i in world_date:
    new_deaths_worldwide.append(np.sum(covid_data.loc[covid_data.loc[:,"date"] == i, "new_deaths"]))

#plot the new cases worldwide over time with blue circles
plt.plot(world_date, new_cases_worldwide, 'bo') #"bo" means: plot the points with small circles in blue
#plot the new deaths worldwide over time with red circles
plt.plot(world_date, new_deaths_worldwide, 'ro') #"ro" means: plot the points with small circles in red
#modify the plot 
plt.ylabel('number')
plt.xlabel('date')
plt.title('New cases and new deaths worldwide')
plt.xticks(world_date[0:len(world_date):4],rotation=-90) # Change the date interval to every four days and change the angle of x-axis to -90
plt.show()