# "try" statements
# Used for handling Exceptions
# Blocks - try, except, else, finally
# With the help of the "try" block we can test a Python code block for errors(exceptions)
# With the help of the "except" block we can handle the caught errors(exceptions)
# With the help of the "else" block we can execute the code if no errors(exceptions) are raised
# With the help of the "finally" block we can execute the code, regardless of the result of the try and except blocks

# with the "try" and "except" block
message = ""
try:
    print(x)  # this will throw error since the variable "x" is not defined
except NameError:
    print("Exception caught")
    message = "Exception caught"
print(message)
print("**********************************************************")

# with the "try", "except" and "else" block
x = 2
message = ""
try:
    print(x)
except NameError:
    message = "Exception caught"
else:
    message = "No Exception occured"
print(message)
print("**********************************************************")

# with the "try", "except" and "finally" block
x = 2
message = ""
try:
    print(x)
except NameError:
    message = "Exception caught"
finally:
    print("This will get executed regardless")
print("**********************************************************")
