# Python Lists
# Collection of Ordered, Mutable elements/items
# Can be indexed and sliced
# Allows Duplicate members and is Heterogeneous(i.e. all data types can be stored inside a single list)
# Similar to arrays and can be iterated over in a similar manner

firstFruitList = ["Apple", "Banana", "Mango", "Cherry", "Pineapple", "Watermelon", "Blueberry"]

# Indexing and Slicing
# All slice operations return a new list containing the requested elements
print(firstFruitList[2])
print(type(firstFruitList[3]))  # indexing returns the item and its type is "String"
print(firstFruitList[-4])
print(firstFruitList[:-2])
print(firstFruitList[:])
print(type(firstFruitList[:]))  # slicing returns a new list
print("**********************************************************")

# Looping through the list to display each item
for fruit in firstFruitList:
    print("Fruit: " + fruit)
print("**********************************************************")

# Other functions
print(len(firstFruitList))  # returns the number of elements in the list
firstFruitList.append("Banana")  # adds an item to the end of the list
print(firstFruitList)
print(firstFruitList.pop())  # removes the item at the given position and returns it. If no index is specified,
# firstFruitList.pop() removes and returns the last item in the list
print(firstFruitList)
firstFruitList.insert(1, "Orange")  # inserts an item at a given position
print(firstFruitList)
firstFruitList.remove("Watermelon")  # Removes the first item from the list whose value is equal to "Watermelon".
# A "ValueError" is thrown if there is no such item
print(firstFruitList)
print(firstFruitList.index('Banana'))
print(firstFruitList.count("Grapes"))  # prints the number of times "Grapes" appears in the list
# concatenation
print(firstFruitList + ["Grapes", "Orange"])
# reverse
firstFruitList.reverse()
print(firstFruitList)
# sort
firstFruitList.sort()
print(firstFruitList)
print("**********************************************************")

# Copying (shallow copy) a list to another list. Equivalent to firstFruitList[:]
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
print(secondFruitList)
del secondFruitList[1]  # removes an item from the list using its index
print(secondFruitList)
secondFruitList.clear()  # removes all the items from the list and is equivalent to del secondFruitList[:]
print(secondFruitList)
print(len(secondFruitList))
del secondFruitList
# print(secondFruitList)  # This will throw NameError
print("**********************************************************")

# Assignment to slices (We can assign a list to the slice of another list
# and this can change the size of the list or clear it entirely.
digits = [1, 2, 3, 4, 5, 6, 7]
print(digits)
digits[2:5] = [12, 13, 14]
print(digits)
print("**********************************************************")

# nested lists (creating lists containing other lists)
charList = ['m', 'n', 'o', 'p', 'q', 'r']
digitList = [22, 31, 52]
mixed_list = [charList, digitList]
print(mixed_list)
print(mixed_list[1][2])
print("**********************************************************")

# List Comprehensions
# They provide a concise way to create lists and consist of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the
# context of the for and if clauses which follow it.
newList = []
for n in range(10):
    newList.append(n ** 2)
print(newList)
newList = list(map(lambda i: i ** 2, range(10)))
print(newList)
newList = [i ** 2 for i in range(10)]
print(newList)
print("**********************************************************")

# combines the elements of two lists if t
# hey are not equal
combinedList = []
for first in [4, 2, 5]:
    for second in [5, 1, 4]:
        if first != second:
            combinedList.append((first, second))
print(combinedList)
combinedList = [(i, n) for i in [4, 2, 5] for n in [5, 1, 4] if i != n]
print(combinedList)
print("**********************************************************")

# calling a method on each element.
fresh_fruit = ['  mango', '  orange ', 'banana  ']
clean_fresh_fruit = [fruit.strip() for fruit in fresh_fruit]
print(clean_fresh_fruit)
print("**********************************************************")

# list of two tuples
tuplesSample = [(i, i ** 2) for i in range(4)]
print(tuplesSample)
print("**********************************************************")

# Flatten a list using a list comprehension with two 'for'.
sampleList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattenedSampleList = [i for n in sampleList for i in n]
print(flattenedSampleList)
print("**********************************************************")

# nested List Comprehension
nestedListSample = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# this will transpose rows and columns
nestedListSample_transposed1 = [[row[i] for row in nestedListSample] for i in range(4)]
print(nestedListSample_transposed1)
print("**********************************************************")
nestedListSample_transposed2 = []
for i in range(4):
    nestedListSample_transposed2.append([row[i] for row in nestedListSample])
print(nestedListSample_transposed2)
print("**********************************************************")
nestedListSample_transposed3 = []
for i in range(4):
    transposed_row = []
    for row in nestedListSample:
        transposed_row.append(row[i])
    nestedListSample_transposed3.append(transposed_row)
print(nestedListSample_transposed3)
print("**********************************************************")
print(list(zip(*nestedListSample)))
print("**********************************************************")
