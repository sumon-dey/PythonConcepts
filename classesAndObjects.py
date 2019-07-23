# Python Classes and Objects

# Almost everthing in Python is an object with it properties ans methods
# A Python Class is like an object constructor or a blueprint for creating objects
class Employee:
    age = 30


employeeObject = Employee()
print(employeeObject.age)
print("**********************************************************")


# _init_function of a class
# This gets executed when the class is being initiated. It can be used to assign values
# to object propertiesor ot other properties that are necessary to do when the object is
# being created
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    # Object Methods
    # Objects can also contain methods. Methods in objects are functions that belong to the object
    def printAge(self):
        print("Printing the age of the person and his age is: " + str(self.age))


# The self parameter is a reference to the class itself, and is used to access variables
# that belongs to the class. It does not have to be named "self", we can call it anything
# but it is has to be the first parameter of any function in the class

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
personObject2.printAge()  # This will throw AttributeError
print("**********************************************************")

# We can also delete objects
del personObject2
personObject2.printAge()  # This will throw NameError
print("**********************************************************")
