# Inheritance

# Inheritance allows a derived class to reuse the same code from its parent(base class)

# Base Class
class Person:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


# Derived Class
class Employee(Person):
    """The Base Class (in our case Person) must be defined in a scope containing the derived class ("Employee")
    definition. Derived classes may override methods of their base classes. Because methods have no special
    privileges when calling other methods of the same object, a method of a base class that calls
    another method defined in the same base class may end up calling a method of a derived class
    that overrides it.

    An overriding method in a derived class may want to extend rather than simply replace
    the base class method of the same name. There is a simple way to call the base class method
    directly: BaseClassName.methodname(self, arguments) and this only works if the base class is accessible as BaseClassName
    in the global scope"""

    def __init__(self, name, staff_id):
        Person.__init__(self, name)
        # super().__init__(name) -> "super" can also be used here instead of directly using the Base class name
        self.staff_id = staff_id

    def get_full_id(self):
        return self.get_name() + ', ' + self.staff_id


def test_inheritance():
    person = Person("Sam")
    employee = Employee("Tom", "D29")
    print(person.get_name())
    print(employee.get_name())
    print(employee.get_full_id())
    # Python has two built-in functions that work with inheritance
    # isinstance() -> to check an instance’s type
    # issubclass() -> to check class inheritance
    print(isinstance(employee, Employee))
    print(issubclass(Employee, Person))
