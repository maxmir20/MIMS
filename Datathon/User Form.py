'''
Form considerations
-income (ordinal)
-Rent control (binary)
-Zipcode
-Roommates
-Dependents
'''

'''
Output Considerations
- Risk level now
- Spending Percentage
- Risk level in X years
'''
import numpy as np
import IPython
import pandas as pd
import matplotlib as plt
import itertools

#from tabpy_tools.client import Client

#client = Client('http://localhost:9004/')


#User input
def user_input():
    print('Sustainable Housing Rental Calculator')
    income = int(input('how much are you making per month: '))
    # bedrooms = int(input('How many bedrooms does your place have: '))
    people = int(input('How many roommates do you live with (not including yourself): ')) + 1 #+1 is for the user entering
    # rent_control = bool(input('Is your place rent controlled: y/n '))
    zipcode = int(input('Please enter your 5 digit zipcode: '))

    ML_return = 100

    
    rental_calculator(income, bedrooms, people, zipcode, ML_return)
    
#Pass zipcode, Bedrooms  to ML


#ML return
    #should return a current average and a predicted average
    
    


#risk model

def rental_calculator(income, bedrooms, people, zipcode, ML_return):


    #ML Return: Average
    average = ML_return
    rent_burden = burden(income, people, average)
    print(rent_burden)
    risk_score = risk_level(rent_burden)



    print ('the average price for a ' + str(bedrooms) + ' bedroom house in this zipcode is $' + str(average)) #average ML return
    print( 'with an income of $' + str(income)+ ' and ' + str(people-1) + ' roommates, the average rent burden in this area would be ' + str(rent_burden) + '%')
    #Category of Over-burdening
    print ('This is a risk level of ' + risk_score)


    #forecasting
    projected = ML_return #next years estimate of average price
    print('next year, the average cost of renting in this zipcode is predicted to be $' + str(projected))

    #years until risk_level becomes high
    years = years_until_burdened(income, people, projected)


    print('at the current rate (with no change in income) it will be ' + str(years) + ' years until you are spending over 50 percent of your income on rent')

    #pass zipcode, average, risk level to Tableau



def burden(income, people, df):
    #value = float(df['Average'])
    #print(value)
    #type(value)
    return round(((df/people)/income) * 100)
        
def risk_level(rent_burden):
    risk_level = ''
    if rent_burden > 50:
        risk_level = 'High'
    elif rent_burden >30:
        risk_level = 'Medium'
    else:
        risk_level = 'Low'
    return risk_level
#output

def years_until_burdened(income, people, projected):
    estimated = projected
    years = 0
    rent_control = 7.7 #pulled from current project SF rates
    while burden(income, people, estimated) < 50:
        estimated = estimated + estimated*rent_control
        years += 1
    return years


def main():
    if __name__== "__main__" :
        user_input()
main()
