"""
Author: James Nicholson
Last Updated: April 12, 2019
Chapter 6 Exercise 5: Take the following Python code that stores a string:
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function
"""

str = 'X-DSPAM-Confidence:0.8475'
lenStr = len(str)

#find the postion of the colon
colonIndex = str.find(":")

#Extract the porition of the string from after the colon until the end of the string
strNum = str[colonIndex + 1:lenStr]
#Strip blank spaces around the numberic value, and then convert to a floating point number
floatNum = float(strNum.strip())
print(floatNum)
"""
Author: James Nicholson
Last Updated: April 12, 2019
Chapter 6 Exercise 5: Take the following Python code that stores a string:

Use find and string slicing to extract the portion of the string after the
colon character and then use the float function
"""

str = 'X-DSPAM-Confidence:0.8475'
lenStr = len(str)

#find the postion of the colon
colonIndex = str.find(":")

#Extract the porition of the string from after the colon until the end of the string
strNum = str[colonIndex + 1:lenStr]
#Strip blank spaces around the numberic value, and then convert to a floating point number
floatNum = float(strNum.strip())
print(floatNum)
