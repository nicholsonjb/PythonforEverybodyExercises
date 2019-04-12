#Data 620 Assignment 8.2 Python Score
#Severance Chapter 4 - Exercise 7 – ASSIGNMENT
#Written by James Nicholson
#Last Updated March 27, 2019
#Use a custome function to do the following: 
# Write a program to prompt for a score between 0.0 and
#1.0. If the score is out of range, print an error message. If the score is
#between 0.0 and 1.0, print a grade using the following table:
#print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#Use try/catch expection handling to gracefullly exit not non-numeric user input.


import sys

def computegrade(fScore):
    #Use conditional loop to to determine grade on user supplied input.
    if fScore > 1.0 or fScore < 0.0:
        print('Bad score')
    elif fScore > 0.9:
        print('The grade is A!')
    elif fScore > 0.8:
        print('The grade is B!')
    elif fScore > 0.7:
        print('The grade is C!')
    elif fScore > 0.6:
        print('The grade is D!')
    else:
        print('The grade is F!')
    return fScore
        
print("This program will calculate a letter grade based on the student's score.")


# Prompt user for the score
# Convert this input to float, because the input statement accepts user input as a string by default.
# Wrap this within a try-except code block to exit gracefully as the conversion to float will fail if the user supplied a non-numeric input!
try:
    inputScore = input('Enter score: ')
    floatScore = float(inputScore)
except:
    score = -1
    print ("Score must be an integer. Please try again. Goodbye.")
    sys.exit()

#Invoke computegrade function with the user-supplied score
scoreRecieved = computegrade(floatScore)



#End Script
