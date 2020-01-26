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

#read ML model (returns predicted next year price and 2021 price)
datathon = pd.read_csv("predicted_rent_burden.csv", low_memory=False, encoding = "ISO-8859-1")


#User input
def user_input():
    print('Sustainable Housing Rental Calculator')
    print()
    income = int(input('What is your annual household income: '))
    # bedrooms = int(input('How many bedrooms does your place have: '))
    # people = int(input('How many roommates do you live with (not including yourself): ')) + 1 #+1 is for the user entering
    # rent_control = bool(input('Is your place rent controlled: y/n '))
    zipcode = int(input('Please enter your 5 digit zipcode: '))

    
    #Pass zipcode to ML model to return results
    ML_return = datathon[datathon['RegionName'] == zipcode]
    ML_next_year = round(ML_return['2020'].tolist()[0])
    ML_2021 = round(ML_return['2021'].tolist()[0])
    
    
    #plug into rental calculator
    rental_calculator(income, bedrooms, people, zipcode, ML_return)

    
    


#risk model

def rental_calculator(income, bedrooms, people, zipcode, ML_return):


    #ML Return: Average
    ML_next_year = round(ML_return['2020'].tolist()[0])
    ML_2021 = round(ML_return['2021'].tolist()[0])
    average = ML_return
    
    
    rent_burden = burden(income, people, ML_next_year)
    risk_score = risk_level(rent_burden)
    print ()

    print ('###########################################################################################################')
    print ()

    print ('PREDICTED RENT BURDEN:')
    print ('next year, the estimated average price for a 2 bedroom house in this zipcode is $' + str(ML_next_year)) #average ML return
    print( 'with a household income of $' + str(income)+ ' the average rent burden in this area would be ' + str(rent_burden) + '% of your monthly income')
    #Category of Over-burdening
    print ()
    print ('This is a risk level of ' + risk_score)

    print ()
    print ('2021 RENT BURDEN:')
    #forecasting
    projected = ML_2021 #2021 estimate of average price
    print('In 2021, the average cost of renting in this zipcode is predicted to be $' + str(projected))
    print ()
    print()
    print ('YEARS UNTIL >50% RENT BURDEN:')
    #years until risk_level becomes high
    years = years_until_burdened(income, people, projected)
    

    print('At your current rate (with no change in income) it will be ' + str(years) + ' years until you are spending more than 50 percent of your monthly income on rent')
    print ()
    print ('###########################################################################################################')

def burden(income, people, rental_cost):
    monthly_income = income/12 #converts to monthly amount
    return round(((rental_cost/people)/monthly_income) * 100)
        
def risk_level(rent_burden):
    risk_level = ''
    if rent_burden > 50:
        risk_level = 'High'
        #message = 'By spending over 50% of your income on rent, you increase the strain of supporting'
    elif rent_burden >30:
        risk_level = 'Medium'
        #message = 'By spending over '
    else:
        risk_level = 'Low'
    return risk_level
    
def years_until_burdened(income, people, projected):
    estimated = projected
    years = 0
    rent_control = 7.7 #pulled from current projected SF Rent control rates
    while burden(income, people, estimated) < 50:
        estimated = estimated + estimated*rent_control
        years += 1
    return years


def main():
    if __name__== "__main__" :
        user_input()
main()
