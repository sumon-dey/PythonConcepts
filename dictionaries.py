# Python Dictionaries
# Unordered,Indexed,No Duplicate Members,Mutable

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
