# Python Sets
# Immutable, Unordered, Unindexed, Iterable, No Duplicate members

citySet = {"Pune", "Mumbai", "Bangalore", "Chennai", "Hyderabad", "Kolkata"}
print(type(citySet))
print(len(citySet))
# print(citySet[2]) -> This will throw a TypeError since sets are unindexed
for cityName in citySet:
    print("City: " + cityName)
print("**********************************************************")

# Other functions
print("Chennai" in citySet)
# To add a single member
citySet.add("Delhi")
print(citySet)
# To add multiple members
citySet.update(("Jammu", "Guwahati", "Ahmedabad"))
print(citySet)
# Element removal
citySet.remove("Delhi")
print(citySet)
citySet.discard("Nagpur")  # Will not throw error if element is not present
# citySet.remove("Nagpur")  # Will throw error if element is not present
print("**********************************************************")
print(citySet.pop())  # Will remove the last item (last item is not fixed)
print(citySet)
# To clear the set
citySet.clear()
print(citySet)
# To delete the complete set
del citySet
# print(citySet) # will throws a NameError
print("**********************************************************")

# String to Set
mySampleString = "Hello"
print(set(mySampleString))  # Will take only the unique members
print("**********************************************************")
