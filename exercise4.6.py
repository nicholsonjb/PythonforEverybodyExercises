# Written by James Nicholson
# Last Updated March 27, 2019
#Use a costum function to do the following: 
# Given (1) number of hours, and (2) rate of pay
# This program computes gross pay according to the formula: number of hours * rate of pay
#For hours worked beyond 40. pay = 1.5 * number of hours * rate of pay
#Use try/catch expection handling to gracefullly exit not non-numeric user input. 

import sys

# Initialize variables to be used in the program
fixedHours = 40
floatOTRate = 1.5

def computePay(iHours, fRate):
    #Use conditional loop to carry out the two different calculations on user-supplied hours
    #Round the compuation to two decimal places
    if iHours > fixedHours:
        hoursOverFixed = iHours - fixedHours
    #pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
        grossPay = round((fixedHours * fRate) + (floatOTRate * hoursOverFixed * floatRate), 2)
    else:
    #pay computation to give pay for less than  40 hours.
        grossPay = round((iHours * fRate), 2)
    return grossPay

    
# Prompt user for the number of hours worked. 
hours = input("Enter number of hours: ")

# Convert input to integer, because the input statement accepts user input as a string by default.
# Wrap this within a try-except code block to exit gracefully as the conversion to integer will fail if the user supplied a non-numeric input!
try:
    intHours = int(hours)
except ValueError:
    print ("Hours worked must be an integer. Please try again. Goodbye.")
    sys.exit()

# Prompt user for the rate of pay 
rate = input("Enter rate of pay: ")

# Convert this rate to float, because the input statement accepts user input as a string by default.
# Wrap this within a try-except code block to exit gracefully as the conversion to float will fail if the user supplied a non-numeric input!
try:
    floatRate = float(rate)
except ValueError:
    print ("Rate of pay must be numeric. Please try again. Goodbye.")
    sys.exit()
    


    
# Print the result
grossPayRecieved = computePay(intHours, floatRate)
print("Gross pay is: $" + str(grossPayRecieved))
