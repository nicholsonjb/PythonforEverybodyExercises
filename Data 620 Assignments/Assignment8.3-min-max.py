#Data 620 Assignment 8.3 Python Loops
#Severance Chapter 5 - Exercise 2 – ASSIGNMENT
#Written by James Nicholson
#Last Update March 27, 2019
#Write a program which repeatedly reads numbers until the user enters 
#“done”. Once “done” is entered, print out the total, count,and prints
#out both the maximum and minimum of the numbers instead of the average. 
#of the numbers. If the user enters anything other than a number, detect 
#their mistake using try and except and print an error message and skip to 
#the next number.

# Initialize variables to be used in the program
totalSum = 0
count = 0
largest = None
smallest = None

print("""This program will read numbers entered into a loop and then print out the total,
count, and the maximum and minimum of the numbers. Type "done" to exit the loop
and find your results.
""")

#Use while loop to to determine read numbers until user enters done.
while True:

 # Wrap this within a try-except code block to exit gracefully as the conversion to float will fail if the user supplied a non-numeric input!
  try:

    #Prompt user for the number
   
    number = input("Enter a number: ")
    
    if (number == "done" or number == "Done"): #Exits loop when user enters "done"
     break
    # Convert this input to float, because the input statement accepts user input as a string by default.
    floatNumber = float(number)
    totalSum =  floatNumber + totalSum #Calculates sum
    count = count + 1 #Calculates count
    
    #Use conditional loop to to determine maximum and minimum  numbers on user supplied input.
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number
  except:
      print("Invalid input.")

#Prints results of sum, count and maximum and minimum  number  of the numbers entered by the user
print("Sum: "+str(totalSum) ,"\nNumber Count: " +str(count), "\nSmallest: "+str(smallest),"\nLargest: "+str(largest))
