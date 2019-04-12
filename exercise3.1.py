# Written by James Nicholson
# Last Updated March 24, 2019
# Given (1) number of hours, and (2) rate of pay
# This program computes gross pay according to the formula: number of hours * rate of pay
#For hours worked beyond 40. pay = 1.5 * number of hours * rate of pay

import sys

# Initialize variables to be used in the program
fixedHours = 40
intHours = 0
floatRate = 0
floatOTRate = 1.5

# Prompt user for the number of hours worked. 
hours = input("Enter number of hours: ")

# Convert input to integer, because the input statement accepts user input as a string by default.
intHours = int(hours)

# Prompt user for the rate of pay 
rate = input("Enter rate of pay: ")

# Convert this rate to float, because the input statement accepts user input as a string by default.
floatRate = float(rate)
    
# With valid inputs, we are now ready to compute pay. Round the computation to two decimal places
if intHours > fixedHours:
    hoursOverFixed = intHours - fixedHours
    #pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
    grossPay = round((fixedHours * floatRate) + (floatOTRate * hoursOverFixed * floatRate), 2)
else:
    #pay computation to give pay for less than  40 hours.
    grossPay = round((intHours * floatRate), 2)
    
# Print the result
print("Gross pay is: $" + str(grossPay))

