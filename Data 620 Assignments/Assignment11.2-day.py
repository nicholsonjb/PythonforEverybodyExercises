"""
Data 620 Assignment 10.2 Python Loops
Severance Chapter 9 - Exercise 2 – Dictionary Mailbox Day Analysis
Written by James Nicholson
Last Update April 12, 2019
Write a program that categorizes each mail message by which day of
the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
The input file you will use for this is the ‘mbox.txt’ file,
first introduced in Severance Section 7.3.
It can be found at http://www.pythonlearn.com/code3/mbox.txt.
A shorter file for debugging can be found at
http://www.pythonlearn.com/code3/mbox-short.txt.
For ease, ensure these files reside in the same folder as the .py file for this
"""
import sys

#short message to user about program
print("""
This program will read a file that categorizes each mail message by which day of the week the commit was done.
To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary
(order does not matter).
""")
      
#Prompt user for file name:
fname = input("Enter file name: ")

# Wrap this within a try-except code block to exit gracefully if incorrect file is entered!
try:
    
    fhand = open(fname) #Opens file
    
except:
    print('File not found! File cannot be opened: ', fname)
    sys.exit()
    

dictionary_days = dict()    #Initializes the dictionary

#Use for loop to read each line in text.
for line in fhand:
    words = line.split()#split the line into a list of words using split function

    #if statement to check length of words to match the word 'From' and adds them to the dictonary and keeps a running count. 
    if len(words) == 0 or len(words) < 2 or words[0] != 'From': 
        continue
    else:
        if words[2] not in dictionary_days:
            dictionary_days[words[2]] = 1       #First entry
        else:
            dictionary_days[words[2]] += 1      #Additional counts

#print out dictionary
print("\n*****Results*****")
print("File name:" ,fname)
print(dictionary_days)

#End script
