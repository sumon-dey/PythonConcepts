# Python Classes and Objects

# Python is an Object-oriented Programming Language and almost everything in Python is an object with it properties and methods
# A Python Class is like an object constructor or a blueprint for creating objects

class Employee:
    # This "Employee" class contains one variable "age"
    age = 30


# Class instantiation uses function notation.
# The class object is a parameterless function that returns a new instance of the class.
# The below code creates a new instance of the class named "Employee" and assigns this object to the local variable named "employeeObject"
employeeObject = Employee()
print(employeeObject.age)
print("**********************************************************")


# _init_function of a class
# This gets executed when the class is being initiated. It can be used to assign values
# to object properties or ot other properties that are necessary when the object is
# being created
class Person:
    # This "Person" class contains one public method "printAge" and a constructor
    # The "self" parameter is a reference to the class itself, and is used to access variables
    # that belongs to the class. It does not have to be named "self" , we can call it
    # whatever we like, but it has to be the first parameter of any function in the class.
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    # Object Methods
    # Objects can also contain methods. Methods in objects are functions that belong to the object
    def printAge(self):
        print("Printing the age of the person and his age is: " + str(self.age))


personObject1 = Person("Sam", 30, "Pune")
print("The name of the person is: " + personObject1.name)
print("The age of the person is: " + str(personObject1.age))
print("The city where the person lives is: " + personObject1.city)
print("**********************************************************")

personObject2 = Person("Richard", 35, "Kolkata")
personObject2.printAge()
print("**********************************************************")

# We can also modify, delete the object properties like below
personObject2.age = 40
personObject2.printAge()
del personObject2.age
# personObject2.printAge()  # This will throw AttributeError
print("**********************************************************")

# We can also delete objects
del personObject2
# personObject2.printAge()  # This will throw NameError
print("**********************************************************")
