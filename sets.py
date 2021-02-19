# Python Sets
# Immutable, Unordered, Unindexed, Iterable collection having no Duplicate members
# Supports mathematical operations like union, intersection, difference and symmetric difference

citySet = {"Pune", "Mumbai", "Bangalore", "Chennai", "Hyderabad", "Kolkata"}
# to check the type of the variable
print(type(citySet))
# to check the length of the set
print(len(citySet))
# print(citySet[2]) -> This will throw a TypeError since sets are unindexed
for cityName in citySet:
    print("City: " + cityName)
# to check whether "citySet" is an instance of "set"
print(isinstance(citySet, set))
print("**********************************************************")

# Other functions
# to check whether the item is in the set
print("Chennai" in citySet)
# to check whether the item is not in the set
print("Chennai2" not in citySet)
# To add a single member to the set
citySet.add("Delhi")
print(citySet)
# To add multiple members to the set
citySet.update(("Jammu", "Guwahati", "Ahmedabad"))
print(citySet)
# to remove a single member from the set
citySet.remove("Delhi")
print(citySet)
citySet.discard("Nagpur")  # Will not throw error if element is not present
# citySet.remove("Nagpur")  # Will throw error if element is not present
print("**********************************************************")
# to remove the last item (last item is not fixed) from the set
print(citySet.pop())
print(citySet)
# To clear the set
citySet.clear()
print(citySet)
# To delete the complete set
del citySet
# print(citySet) # will throws a NameError
print("**********************************************************")

# Mathematical operations (like union, intersection, difference and symmetric difference)
# to extract unique characters from a word
set1 = set('abracadabra')
set2 = set('alacazam')
# to extract letters in first word but not in second.
print(set1 - set2)
# to extract letters in first word or second word or both.
print(set1 | set2)
# to extract common letters in both words.
print(set1 & set2)
# to extract letters in first or second word but not both.
print(set1 ^ set2)
print("**********************************************************")

# using a set constructor to create a set
citySet2 = set(("Nagpur", "Delhi", "Chennai"))
print(citySet2)
print("**********************************************************")

# String to Set
mySampleString = "Hello"
print(set(mySampleString))  # Will take only the unique members
print("**********************************************************")

# Set Comprehensions
set3 = {char for char in 'Samuel' if char not in 'am'}
print(set3)
print("**********************************************************")
