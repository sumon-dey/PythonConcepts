# Exceptions
# An error(exception) may occur when running or executing a Python code due to many reasons.
# It is possible to handle the occurrence of such exceptions from within the code itself

# The try statement works as follows:

# First, The "try" clause is executed.
# If there is no exception, the "except" block gets skipped and the execution of the "try" statement is finished.
# If an exception occurs during execution of the "try" block, the rest of the block gets skipped.
# Then if the exception type matches the exception named after the "except" keyword, the "except" block gets executed, and execution continues after the "try" statement
# If an exception occurs which does not match the exception named after the "except" keyword, the control is passed on to outer "try" statements
# If no handler is found, the exception becomes an "unhandled exception" and the execution stops with an error/exception message

try:
    a = 4 / 0
    # We will not get in the below part of the "try" block at all.
    print(a)
except ZeroDivisionError:
    print(
        "ZeroDivisionError is caught")  # The control will come here because division by zero in the "try" block will throw "ZeroDivisionError"
print("**********************************************************")

# Chained Exceptions
try:
    print(b)
    # We will not get in the below part of the "try" block at all.
    a = 4 / 0
    print(a)
except ZeroDivisionError:
    print("ZeroDivisionError is caught")
except NameError:
    print(
        "NameError is caught")  # The control will come here because "NameError" will be thrown first since "b" is not defined
print("**********************************************************")

# It is possible to name multiple exceptions as a parenthesized tuple
try:
    print(b)
    a = 4 / 0
    print(a)
except (NameError, ZeroDivisionError):
    print("Exception is caught")
print("**********************************************************")

# Raising Exceptions
# We can raise a specified exception forcefully too using the "raise" statement
try:
    # The argument used with the "raise" statement will indicate the exception to be raised. This must be either an
    # exception instance or an exception class (a class that derives from Exception).If an exception class is passed,
    # it will be implicitly instantiated by calling its constructor with no arguments
    raise NameError('Hello Python Exception')
except NameError:
    print("NameError exception is thrown from the \"try\" block forcefully and caught in the \"except\" block")
print("**********************************************************")


# User - defined Custom Exceptions
class CustomExceptionClass(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


isCustomExceptionCaught = False
try:
    raise CustomExceptionClass("Custom Message from my Custom Exception")
except CustomExceptionClass:
    isCustomExceptionCaught = True
print("isCustomExceptionCaught: " + str(isCustomExceptionCaught))
print("**********************************************************")
