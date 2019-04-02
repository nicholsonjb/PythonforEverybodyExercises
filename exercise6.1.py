#Written by James Nicholson
#Last Updated April 1, 2019
#Exercise 1: Write a while loop that starts at the last character in the
#string and works its way backwards to the first character in the string,
#printing each letter on a separate line, except backwards.


string ="Monty Python"


def reverse(string):
    strIndex = len(string) - 1 

    while strIndex >= 0:
       print (string[strIndex])
       strIndex -= 1

print(string)
reverse(string)
