# "try" statements
# Used for handling Exceptions
# Blocks - try, except, else, finally
# With the help of the "try" block we can test a Python code block for errors(exceptions)
# With the help of the "except" block we can handle the caught errors(exceptions)
# With the help of the "else" block we can execute the code if no errors(exceptions) are raised
# With the help of the "finally" block we can execute the code, regardless of the result of the try and except blocks

# The try statement works as follows:

# First, The "try" clause is executed.
# If there is no exception, the "except" block gets skipped and the execution of the "try" statement is finished.
# If an exception occurs during execution of the "try" block, the rest of the block gets skipped.
# Then if the exception type matches the exception named after the "except" keyword, the "except" block gets executed, and execution continues after the "try" statement
# If an exception occurs which does not match the exception named after the "except" keyword, the control is passed on to outer "try" statements
# If no handler is found, the exception becomes an "unhandled exception" and the execution stops with an error/exception message

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
