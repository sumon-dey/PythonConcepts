# Data Type in Python is an attribute of data which tells the interpreter how the programmer intends to use the data

# There are three numeric data types in Python:
# Integers
# Integers (e.g. 2, 4, 20)
#     - Boolean (e.g. False and True, acting like 0 and 1)
# Floating Point Numbers (e.g. 3.0, 5.2)
# Complex Numbers (e.g. 1+j, 2+9j)

# Integers (represents a whole number, positive or negative, without decimals and have no value limit)
positive_integer = 34
negative_integer = -3237937
big_integer = 62733287329879274032843048
print(positive_integer)
print(negative_integer)
print(big_integer)
print("**********************************************************")

# Boolean (represents the truth values False and True and is a subtype of the Integer type)
myBooleanValue1 = True
myBooleanValue2 = False
print(myBooleanValue1)
print(myBooleanValue2)
print("**********************************************************")
# Conversion of Boolean to String
print(type(str(myBooleanValue1)))
print(type(str(myBooleanValue2)))
print("**********************************************************")

# Floats (represents a number, positive or negative, containing one or more decimals)
myFloatValue1 = 3.2
myFloatValue2 = -91.9
myFloatValue3 = float(3.4)  # using the "float" function
myScientificFloatValue1 = 35e3  # small "e"
myScientificFloatValue2 = 2E8  # big "E"
print(myFloatValue1)
print(myFloatValue2)
print(myFloatValue3)
print(myScientificFloatValue1)
print(myScientificFloatValue2)
print("**********************************************************")

# Complex Numbers
myComplexValue1 = 3 + 9j
myComplexValue2 = 2 - 3j
print(myComplexValue1)
print(myComplexValue2)
print("**********************************************************")
