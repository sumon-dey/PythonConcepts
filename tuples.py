# Python Tuples
# Ordered, Immutable collection of items which allows Duplicate Members
# We can put the data, which will not change throughout the program, in a Tuple
# Tuples can be called as "Immutable Python Lists" or "Constant Python Lists"

employeeTuple = ("Sam", "Sam" "Mike", "John", "Harry", "Tom", "Sean", "Justin")
# to check the variable type
print(type(employeeTuple))
# to check whether the type is "Tuple" or not
print(isinstance(employeeTuple, tuple))
# to print all the elements in the Tuple
for employeeName in employeeTuple:
    print("Employee: " + employeeName)
print("**********************************************************")

# Other functions
# to display an element using index
print(employeeTuple[0])
# to display the length of the Tuple
print(len(employeeTuple))
# employeeTuple[2] = "David"  # This will throw a TypeError since Tuple cannot be modified
print(employeeTuple)
print("**********************************************************")

# we can use the tuple() constructor to create a tuple
employeeName2 = tuple(("Richard", "Henry", "Brian"))
print(employeeName2)
# we can also omit the use of brackets to create a tuple
employeeName3 = "David", "Michael", "Shaun"
print(employeeName3)
print(type(employeeName3))
print("**********************************************************")

# Difference between a Tuple and a String
myStr = ("Sam")  # This is a String
print(type(myStr))
# This is a Tuple (for a Tuple, comma is mandatory) with one item
myTuple1 = ("Sam",)
print(type(myTuple1))
print(len(myTuple1))
# This is an empty Tuple
myTuple2 = ()
print(type(myTuple2))
print(len(myTuple2))
print("**********************************************************")

# Value Swapping using Tuple
myNumber1 = 2
myNumber2 = 3
myNumber1, myNumber2 = myNumber2, myNumber1
print(myNumber1)
print(myNumber2)
print("**********************************************************")

# Nested Tuples
employeeName4 = employeeName3, ("Raj", "Vinith")
print(employeeName4)
print("**********************************************************")

# Tuple Sequence Packing
packed_tuple = 1, 2, "Python"
print(packed_tuple)
# Tuple Sequence Unpacking
number1, number2, string1 = packed_tuple
print(number1)
print(number2)
print(string1)
print("**********************************************************")
