# Python Loops
# Loops are a programming element that repeat a portion of code a set number of times until the desired process is complete.
# In Python, there can be two kinds of loops - "while" and "for"

# while loop
# It executes as long as the condition remains true. The condition may be an integer, string, list or any sequence
mySampleIntValue = 68
while (mySampleIntValue <= 80):
    print("Desired number is: " + str(mySampleIntValue))
    mySampleIntValue += 1
print("**********************************************************")

# for loop
# It iterates over the items of any sequence (a list or a string) in the order that they appear in the sequence
mySampleString = "Every day is a beautiful day."
for letter in mySampleString:
    print(letter, end="")
print("")
print("**********************************************************")

# for loop with range (generates Arithmetic progression)
# In the below, the loop start from "1" (1st argument), ends at "19" (2nd argument - 1) and increments by 2(3rd argument) in each iteration
for number in range(1, 20, 2):
    print("Number is: " + str(number))
print("**********************************************************")

# for loop with else
for number in range(6):
    print(number)
else:
    print("The for loop with else is finally finished.")
print("**********************************************************")

# Nested for loops
color_list = ['red', 'green', 'yellow']
fruit_list = ['apple', 'banana', 'mango']
for x in fruit_list:
    for y in color_list:
        print(x + " is having color: " + y)
print("**********************************************************")

# When looping through dictionaries, the key and its corresponding value can be retrieved at the same time using the items() method.
name = []
age = []
person = {"Sam": 32, "Tom": 40}
for key, value in person.items():
    name.append(key)
    age.append(value)
print(name)
print(age)
print("**********************************************************")

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
combinations = []
for question, answer in zip(questions, answers):
    combinations.append('What is your {0}?  It is {1}.'.format(question, answer))
print(combinations)
print("**********************************************************")
