#Python Operators

firstVariable=35
secondVariable=24
thirdVariable=41
fourthVariable=32
fifthVariable=32
sixthVariable=25

#Arithmetic Operators
print(firstVariable+secondVariable) #Addition Operator
print(firstVariable-secondVariable) #Subtraction Operator
print(firstVariable*secondVariable) #Multiplication Operator
print(firstVariable/secondVariable) #Division Operator
print(firstVariable%secondVariable) #Modulus Operator
print(firstVariable//secondVariable)#Floor Division Operator(results in whole number adjusted to the left in the number line)
print(3**2) #Exponent Operator (3 to the power 2)
print("**********************************************************")

#Assignment Operators
thirdVariable=fourthVariable
thirdVariable+=2
print(thirdVariable)
thirdVariable-=4
print(thirdVariable)
thirdVariable*=3
print(thirdVariable)
thirdVariable/=2
print(thirdVariable)
thirdVariable%=5
print(thirdVariable)
thirdVariable//=3
print(thirdVariable)
thirdVariable**=4
print(thirdVariable)
print("**********************************************************")

#Comparison Operators
print(fourthVariable==fifthVariable)
print(fifthVariable!=sixthVariable)
print(sixthVariable>fifthVariable)
print(sixthVariable<fifthVariable)
print(sixthVariable>=fifthVariable)
print(sixthVariable<=fifthVariable)
print("**********************************************************")

#Logical Operators (and, or, not)
print(firstVariable==35 and secondVariable==24)
print(firstVariable==35 or secondVariable==21)
print(not firstVariable==14)
print("**********************************************************")

#Identity Operators (is, is not)
print(fifthVariable is sixthVariable)
print(fifthVariable is not sixthVariable)
fifthVariable=sixthVariable
print(fifthVariable is sixthVariable)
print("**********************************************************")

#Membership Operators (in, not in)
mySampleString="Hello John Doe"
print("Hello" in mySampleString)
print("ll"in mySampleString)
print("Sam" not in mySampleString)
print("John" not in mySampleString)
print("**********************************************************")

#Bitwise Operators
print(firstVariable & secondVariable)
print(firstVariable | secondVariable)
print(firstVariable ^ secondVariable)
print(firstVariable << secondVariable)
print(firstVariable >> secondVariable)
print("**********************************************************")