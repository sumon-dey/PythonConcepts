# Python Tuples
# Ordered, Immutable, Allows Duplicate Members
# We can put the data, which will not change throughout the program, in a Tuple
# Tuples can be called as "Immutable Python Lists" or "Constant Python Lists"

employeeTuple = ("Sam", "Sam" "Mike", "John", "Harry", "Tom", "Sean", "Justin")
print(type(employeeTuple))
for employeeName in employeeTuple:
    print("Employee: " + employeeName)
print("**********************************************************")

# Difference between a Tuple and a String
myStr = ("Sam")  # This is a String
print(type(myStr))
myTuple = ("Sam",)  # This is a Tuple (for a Tuple, comma is mandatory)
print(type(myTuple))
print("**********************************************************")

# Other functions
print(employeeTuple[0])
print(len(employeeTuple))
employeeTuple[2] = "David"  # This will throw a TypeError since Tuple cannot be modified
print(employeeTuple)
print("**********************************************************")
