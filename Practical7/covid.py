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
