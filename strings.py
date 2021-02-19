# Python Strings
# Sequence of characters enclosed within double quotes

mySampleString = "This is a sample string which will be used to demonstrate the string functionality."
# to check the type of the variable
print(type(mySampleString))
# to check whether the instance is String or not
print(isinstance(mySampleString, str))
print("**********************************************************")

# Indexing,Substring,Slicing,Splitting and other functionalities

# Indexing (to extract individual characters)
# Strings can be indexed, with the first character having index 0 (there is no separate character type)
# A character is simply a string of size one. Since -0 is the same as 0, negative indices start from -1
# first character.
print(mySampleString[0])
# Last character.
print(mySampleString[-1])
# 3rd character.
print(mySampleString[2])
# second Last character.
print(mySampleString[-2])
# if you try to use an index that is too large, it will throw an error.
# print(mySampleString[85])  # this will throw "IndexError: string index out of range"
# if you try to assign to an indexed position in the string, it will result in an error
# mySampleString[-2] = "H" # this will throw "TypeError: 'str' object does not support item assignment"
print("**********************************************************")

# Slicing (to extract substring)
# to extract characters from position 5 (included) to 16 (excluded).
print(mySampleString[5:16])
# to extract all characters from beginning to end
print(mySampleString[:])
# to extract characters from position 2 (included) to end
print(mySampleString[2:])
# to extract characters from beginning to last character (excluded)
print(mySampleString[:-1])
# to extract characters from the second-last (included) to the end
print(mySampleString[-2:])
# to reverse a String
print(mySampleString[::-1])
# out of range slice indexes are handled gracefully unlike index
print(mySampleString[2:85])  # this will not throw error
print("**********************************************************")

sampleStr = " Hello "
# to return the length of the String
print(len(sampleStr))
# to trim the String by removing any whitespace from the beginning or the end
print(sampleStr.strip())
# to return the String in uppercase
print(mySampleString.upper())
# to return the String in lowercase
print(mySampleString.lower())
# to replace a String with another String
print(mySampleString.replace("s", "h"))
# to split a String into substrings if it finds instances of the separator(e.g. whitespace)
print(mySampleString.split(" "))
# to return the number of times a specified value occurs in a string
print("sam smith".count("s"))
# to convert the first character to upper case
print("sam smith".capitalize())
# to convert the first character of each word to upper case
print("hello python progammers".title())
# Multiple line String literal
multi_line_string = '''\
       First line
       Second line
   '''
print(multi_line_string)
# to search the String for a specified value and return the position of where it was found
print("Sam Smith".find("Sm"))
# to return a String where a specified value is replaced with a specified value.
print("I love Python".replace("Python", "Java"))
# to check whether all the characters in the String are upper case
print("SAM".isupper())
# to check whether all the characters in the String are letters
print("SAM".isalpha())
# to check whether all the characters in the String are decimals
print("222".isdecimal())
print("**********************************************************")

# Concatenation
var1 = "Hello "
print("Sam " + "Smith")
print("Sam " "Smith")
print(var1 + "Sam " "Smith")
print("**********************************************************")

# Handling User Input
myInputString = input("How are you feeling?")
print("You are feeling " + myInputString)
print("**********************************************************")

# Escape Sequence
# to escape double quotes
print("Hello \"World\"")
# new line
print("Hello \n World")
print("**********************************************************")

# String Formatting (used to format the output)
name = "Sam"
age = 32
print(f"Name and Age of the player is: {name} {age}")
# to generate representations which can be read by the interpreter (or will force a SyntaxError if there is no equivalent syntax)
print(repr("Hello, Python."))
pi_value = 3.14159
print(f"Value of pi is: {pi_value:.3f}")
mySampleString2 = {'Sam': 32, "Tom": 23}
mySampleString3 = ""
for name, age in mySampleString2.items():
    mySampleString3 += f"{name:2}==>{age:2d}"
print(mySampleString3)
print("{0} and {1}".format("Hello", "World"))
mySampleString4 = "{language} is {adjective}".format(
    language="Python",
    adjective="good"
)
print(mySampleString4)
mySampleString5 = {'Sam': 32, 'Tom': 40}
print("Sam: {0[Sam]:d}; Tom: {0[Tom]:d}".format(mySampleString5))
mySampleString6 = "Sam: {Sam:d}; Tom: {Tom:d}".format(**mySampleString5)
print(mySampleString6)
print("**********************************************************")
