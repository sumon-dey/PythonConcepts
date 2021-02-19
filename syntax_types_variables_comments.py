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
# A variable name must start with a letter or the underscore character.
# It cannot start with a number and can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
# Python variables are case-sensitive
myAge = 30
myName = "Sam"
myHeight = 1.72
# To get the type of the declared variables
print(type(myAge))
print(type(myName))
print(type(myHeight))
print("**********************************************************")

# Type Casting (to specify a type to a variable using constructor functions)
# Adding different data types will throw error
# constructs Strings from other data types
myAgeInString = str(myAge)
myHeightInString = str(myHeight)
print("My name is: " + myName + ", my age is: " + myAgeInString + " and my height is: " + myHeightInString)
# constructs integers from other data types
print(int("125"))
print(int(3.2))
# constructs float from other data types
print(float("4.22"))
print(float(22242))
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
