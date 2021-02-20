# Generators

# Generator functions allow us to declare a function that behaves like an iterator

# They can return an iterable set of items, one at a time, in a special way

# When an iteration over a set of item starts using the for statement, the generator is run. Once the
# generator's function code reaches a "yield" statement, the generator yields its execution back to
# the for loop, returning a new value from the set. The generator function can generate as many
# values (possibly infinite) as it wants, yielding each one in its turn
# A simple generator function
def sample_generator_function():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


for item in sample_generator_function():
    print(item)
