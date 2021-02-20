# Python Conditional Statements

personName = "Sam"
personAge = 42
personHeight = 1.82

# if-elif-else
if (personName == "Richard"):
    print("The person is Richard")
# There can be zero or more than zero elif (short form for "else-if") parts in conjunction with the "if" clause
elif (personName == "Sam"):
    print("The person is Sam")
# The "else" part is optional
else:
    print("The person is someone else!")
print("**********************************************************")

# ShortHand if-elif-else
personName = "Richard"
if (personAge != 43 and personName != "Sam"): print("The age of the person is not 43 and he is not Sam")
print("The person is Sam") if (personName == "Sam") else print("The person is Richard") if (
        personName == "Richard") else print("The person is someone else.")
print("**********************************************************")
