#Data 620 Assignment 7.2
#Written by James Nicholson
#Last Updated March 20, 2019

#Write a program which prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit, and print out the converted temperature

import sys

print("This program will convert the temperature in degrees Celsius(°C)\nto degrees Fahrenheit(°F). \n")

#Prompt user for Celsius temperature
celsius = input("Enter degrees Celsius(°C) temperature: ")

#Covert input from default string value to float. Uses try-execpt code block to exit
#exit program if users enters a non numeric input. 
try:
    floatCelsius = float(celsius)
except ValueError:
    print("Celsius(°C) temperature must be a float. Please Try again. Goodbye!\n")
    sys.exit()

#After vaild inputs are entered by user comupte Fahrenheit temperature.
#Round the computiaton two two decimal places. 
faharenheit = round(((floatCelsius * 9/5) + 32),2)

#Print the result
print("\nTemperature in degrees Fahrenheit(°F) is: " + str(faharenheit)+"\n")

#keeps command window from closing when program is done running.
input("Press enter to exit. ")

#End script
