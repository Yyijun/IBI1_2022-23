#aim: write a function which determines whether an individual can buy a specific house
#define a function with the name buy_house
def buy_house(value, salary): # value is the total value of the house, salary is the purchaser's annual salary
    if 5*salary < value: #if the house worth more than five times your annual salary
        result = "No"
    else: #if the house worth no more than five times your annual salary
        result = "Yes"
    print("Can you buy the hourse? ", result)

buy_house(90, 20) #an example of how this function should be called 