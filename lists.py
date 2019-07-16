# Python Lists
# Ordered, Mutable, Allows Duplicate members, Heterogeneous(All data types can be stored inside a single list)

firstFruitList = ["Apple", "Banana", "Mango", "Cherry", "Pineapple", "Watermelon", "Blueberry"]

# Looping through the list to display each item
for fruit in firstFruitList:
    print("Fruit: " + fruit)
print("**********************************************************")

# Other functions
print(len(firstFruitList))
firstFruitList.append("Banana")
print(firstFruitList)
print(firstFruitList.pop())
print(firstFruitList)
firstFruitList.insert(1, "Orange")
print(firstFruitList)
firstFruitList.remove("Watermelon")
print(firstFruitList)
print("**********************************************************")

# Copying a list to another list
secondFruitList = firstFruitList.copy()
print(secondFruitList)
print(secondFruitList[2])
print("**********************************************************")

# Conversion of String to List
mySampleString1 = "Favorite Fruits"
mySampleList1 = list(mySampleString1)
print(mySampleList1)
print("**********************************************************")

# Conversion of List to String
mySampleList2 = ["T", "h", "i", "s", " ", "is", " ", "awesome"]
mySampleString2 = " ".join(mySampleList2)
print(mySampleString2)
print("**********************************************************")

# Clearing and Deleting
secondFruitList.clear()
print(secondFruitList)
print(len(secondFruitList))
del secondFruitList
print(secondFruitList)  # This will throw NameError
print("**********************************************************")
