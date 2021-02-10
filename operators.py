# Python Operators

firstVariable = 35
secondVariable = 24
thirdVariable = 41
fourthVariable = 32
fifthVariable = 32
sixthVariable = 25

# Arithmetic Operators (used with numeric values to perform common mathematical operations)
print(firstVariable + secondVariable)  # Addition Operator
print(firstVariable - secondVariable)  # Subtraction Operator
print(firstVariable * secondVariable)  # Multiplication Operator
print(firstVariable / secondVariable)  # Division Operator
print(firstVariable % secondVariable)  # Modulus Operator
print(
    firstVariable // secondVariable)  # Floor Division Operator(results in whole number adjusted to the left in the number line)
print(3 ** 2)  # Exponent Operator (3 to the power 2)
print("**********************************************************")

# Assignment Operators (used to assign values to variables)
thirdVariable = fourthVariable
thirdVariable += 2
print(thirdVariable)
thirdVariable -= 4
print(thirdVariable)
thirdVariable *= 3
print(thirdVariable)
thirdVariable /= 2
print(thirdVariable)
thirdVariable %= 5
print(thirdVariable)
thirdVariable //= 3
print(thirdVariable)
thirdVariable **= 4
print(thirdVariable)
# Multiple assignment (The variables firstVariable and secondVariable simultaneously get the new values 2 and 3)
firstVariable, secondVariable = 2, 3
print(firstVariable)
print(secondVariable)
# We can switch variable values using multiple assignment
firstVariable, secondVariable = secondVariable, firstVariable
print(firstVariable)
print(secondVariable)
print("**********************************************************")

# Comparison Operators (used to compare two values)
print(fourthVariable == fifthVariable)
print(fifthVariable != sixthVariable)
print(sixthVariable > fifthVariable)
print(sixthVariable < fifthVariable)
print(sixthVariable >= fifthVariable)
print(sixthVariable <= fifthVariable)
print("**********************************************************")

# Logical Operators (and, or, not) (used to combine conditional statements)
print(firstVariable == 35 and secondVariable == 24)
print(firstVariable == 35 or secondVariable == 21)
print(not firstVariable == 14)
print("**********************************************************")

# Identity Operators (is, is not) (used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location)
print(fifthVariable is sixthVariable)
print(fifthVariable is not sixthVariable)
fifthVariable = sixthVariable
print(fifthVariable is sixthVariable)
print("**********************************************************")

# Membership Operators (in, not in) (used to test if a sequence is presented in an object)
mySampleString = "Hello John Doe"
print("Hello" in mySampleString)
print("ll" in mySampleString)
print("Sam" not in mySampleString)
print("John" not in mySampleString)
print("**********************************************************")

# Bitwise Operators (performs operations on numbers at the bit level)
print(firstVariable & secondVariable)  # Sets each bit to 1 if both bits are 1
print(firstVariable | secondVariable)  # Sets each bit to 1 if one of two bits is 1
print(firstVariable ^ secondVariable)  # Sets each bit to 1 if only one of two bits is 1
print(~secondVariable)  # Inverts all the bits
print(
    firstVariable << secondVariable)  # Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(
    firstVariable >> secondVariable)  # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print("**********************************************************")
