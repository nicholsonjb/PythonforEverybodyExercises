"""
Data 620 Assignment 11.2 Romeo gets the Mail
Severance Chapter 8 - Exercise 4  - ASSIGNMENT
Written by James Nicholson
Last Update April 21, 2019
Download a copy of the ﬁle from http://www.pythonlearn.com/code3/romeo.txt
Write a program to open the ﬁle romeo.txt and read it line by line. For each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list.
When the program completes, sort and print the resulting words in alphabetical order.
For ease, ensure these files reside in the same folder as the .py file for this assignment.
"""

import sys

#short message to user about program
print("""This program will read through the file romeo.txt and read it line by line. For each line,split the line into a list of words using the split function. For each word, check to see if the word is already in a list.
If the word is not in the list, add it to the list. When the program completes, sort and print the resulting words in alphabetical order.
""")
      
#Prompt user for file name:
fname = input("Enter file name: ")

# Wrap this within a try-except code block to exit gracefully if incorrect file is entered!
try:
    
    fhand = open(fname) #Opens file
    
except:
    print('File not found! File cannot be opened: ', fname)
    sys.exit()
    

words = [] #Initialize empty list to store words


#print("Words in file: ")
#Use for loop to read each line in text. 
for line in fhand:
    llist = line.lower().split(" ") #split the line into a list of words using split function and make all words lower case
    #for loop to check the words in list and add to empty list
    for word in llist:
       # print (word) #prints words from file
        word = word.strip()
        #if word not in words list. Then append to end of the list. 
        if word not in words:
            words.append(word)
            words.sort() #sorts list alphabetical order

#prints out list
print("\n*****Results*****")
print("File name:" ,fname)
print("List of words: \n", words)

#End Script




