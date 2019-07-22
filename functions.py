# Python Functions
# Funtions are used to describe the behavior and is defined by "def"

# Declaring the function
def formatInputData(inputData):
    print("The input data is: " + str(inputData))


# Calling the function
inputData = input("Enter the data")
formatInputData(inputData)
print("**********************************************************")


# Default Paramters of a function
# If we call a parameterized function(having default value parameter) without passing any parameter,
# then it takes the default value
def printCityName(city="Pune"):
    print("City I have lived in: " + city)


printCityName("Kolkata")
printCityName("Bangalore")
printCityName("Hyderabad")
printCityName()
print("**********************************************************")

# Lambda Functions
# A lambda function is a small anonymous function which can take any number
# of arguments but can have only one expression
lambdaFunction1 = lambda a: a + 10
print(lambdaFunction1(5))
lambdaFunction2 = lambda a, b: (a * b) + 10
print(lambdaFunction2(4, 5))
lambdaFunction3 = lambda a, b, c: a + b + c
print(lambdaFunction3(5,6,5))
print("**********************************************************")
