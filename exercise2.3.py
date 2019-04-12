# Written by James Nicholson
# Last Updated March 24, 2019
# Given (1) number of hours, and (2) rate of pay
# This program computes gross pay according to the formula: number of hours * rate of pay

import sys

# Initialize variables to be used in the program
intHours = 0
floatRate = 0

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
    
# With valid inputs, we are now ready to compute pay. Round the computation to two decimal places
grossPay = round((intHours * floatRate), 2)

# Print the result
print("Gross pay is: $" + str(grossPay))
