# Python Dictionaries

# Unordered, Indexed, Mutable/Changeable collection, written with curly braces and have key:value pairs.

# A pair of braces, with no elements in it, creates an empty dictionary.

# They have No Duplicate Members.

# They are indexed by their keys and the keys can be any immutable type (strings and numbers).

# Python Tuples can also be used as keys if they contain only strings, numbers or tuples.

# If a tuple contains any mutable object (either directly or indirectly) it cannot be used as a key.

# We can’t use Python lists as keys (since lists can be modified using index assignments, slice assignments,
# or methods like append() and extend().

personDict = {"name": "Sam", "age": 30, "phoneNumber": 1234567892, "city": "Pune"}
print(type(personDict))
print(len(personDict))
print(personDict["age"])
print(personDict.get("age"))
personDict["age"] = 22;
print(personDict)
personDict["favorite game"] = "soccer"
print(personDict)
print("**********************************************************")

# Looping through a dictionary and extracting the keys and values
for keys in personDict:
    print("Key: " + str(keys))
print("**********************************************************")
for keys in personDict:
    print("Value: " + str(personDict[keys]))
print("**********************************************************")
for values in personDict.values():
    print("Value: " + str(values))
print("**********************************************************")
for key, value in personDict.items():
    print("Key: " + str(key) + " and its Value: " + str(value))
print("**********************************************************")

# Printing the keys (with their values) in sorted order
for key, value in sorted(personDict.items()):
    print("Key: " + str(key) + ", Value: " + str(value))
print("**********************************************************")

# Other functions
print(personDict)
personDict.popitem()
print(personDict)
personDict.pop("phoneNumber")
print(personDict)
personDict.clear()
print(personDict)
del personDict  # This will delete the dictionary
# print(personDict)  # This will throw error since the dictionary has been deleted
print("**********************************************************")

# using "assert" with a dictionary
carsDict = {"name2": "Tata", "name1": "Hyundai", "name3": "Maruti"}
# assert carsDict["name1"] == "Tata"  # gives "AssertionError"
assert carsDict["name1"] == "Hyundai"
print("**********************************************************")

# check whether a key is present in the dictionary or not
print("name2" in carsDict)
print("name4" not in carsDict)
print("**********************************************************")

# Converting dictionary to a list (of keys)
# -> The "list" function returns a list of all the keys used in the dictionary in insertion order
# if we want it to be sorted, we can use the "sorted" function
print(list(carsDict))
print(sorted(carsDict))
print("**********************************************************")

# Delete a key:value pair in the dictionary
del carsDict['name2']
print(carsDict)
print("**********************************************************")

# The dict() constructor builds dictionaries directly from key-value pairs.
dictionary_via_constructor = dict([("name1", "Hyundai"), ("name2", "Tata"), ("name3", "Maruti")])
print(dictionary_via_constructor)
print("**********************************************************")

# Comprehensions (used to create dictionaries from arbitrary key and value expressions)
dictionary_via_expression = {i: i ** 4 for i in (4, 8, 12)}
print(dictionary_via_expression)
print("**********************************************************")

# If the keys are simple strings, it is easier to specify pairs using keyword arguments.
dictionary_for_string_keys = dict(name1="Hyundai", name2="Tata", name3="Maruti")
print(dictionary_for_string_keys)
print("**********************************************************")
