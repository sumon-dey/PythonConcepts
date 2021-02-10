# Following are the basic concepts to get started with Python 3.7

"""This is a sample Python
multiline docstring"""

# Display
print("Let's get started with Python")
print("Let's understand", end=" ")
print("The Basic Concepts first")
print("**********************************************************")

# Variables
# In Python, there is no need for variable type declaration
# Every Python variable is an object and a variable is created the moment we first assign a value to it.
myAge = 30
myName = "Sam"
myHeight = 1.72
# To get the type of the declared variables
print(type(myAge))
print(type(myName))
print(type(myHeight))
print("**********************************************************")

# Type Casting
# Adding different data types will throw error
myAgeInString = str(myAge)
myHeightInString = str(myHeight)
print("My name is: " + myName + ", my age is: " + myAgeInString + " and my height is: " + myHeightInString)
print("**********************************************************")

# Numeric Types
myIntValue = 24
myFloatValue = 4.5433
myScientificFloatValue = 35e3
myComplexValue = 4 + 3j
print(myIntValue)
print(myFloatValue)
print(myScientificFloatValue)
print(myComplexValue)
print("**********************************************************")
