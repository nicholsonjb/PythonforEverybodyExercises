"""
Data 620 Assignment 8.3 Python Loops
Severance Chapter 7 - Exercise 2 – ASSIGNMENT
Written by James Nicholson
Last Update April 12, 2019
Write a program to prompt for a ﬁle name, and then read through the ﬁle and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Conﬁdence:” pull apart the line to extract the ﬂoating-point number on the line.
Count these lines and then compute the total of the spam conﬁdence values from these lines. When you reach the end of the ﬁle, print out the average spam conﬁdence.
Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your ﬁle on the mbox.txt and mbox-short.txt ﬁles
Download the two text files: mbox.txt and mbox-short.txt from http://www.pythonlearn.com/code3/  to your local machine.
For ease, ensure these files reside in the same folder as the .py file for this assignment.
"""

import sys

#short message to user about program
print("""This program will read through a file and look for lines of the form of X-DSPAM-Confidence.
Then count these lines and then compute the total of the spam conﬁdence values from these lines and print out the average spam conﬁdence.
""")
      

#Prompt user for file name:
fname = input("Enter file name: ")

# Wrap this within a try-except code block to exit gracefully if incorrect file is entered!
try:
    
    fhand = open(fname) #Opens file
    
except:
    print('File not found! File cannot be opened: ', fname)
    sys.exit()

# Initialize variables to be used in the program
count = 0
total = 0
answer = 0
    
#Use for loop to determine count of lines with X-DSPAM-Confidence skip lines that do not have that form
    
for line in fhand:
     if not line.startswith("X-DSPAM-Confidence:") : continue
     count = count + 1
     floatNum = float(line[21:])
     total = floatNum + total
answer = total / count

#Print out Average spam confidence and file name
print("\n*****Results*****")
print("File name:" ,fname)
print("Average spam confidence:", answer)

#End Script


    



