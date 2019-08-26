# Python Iterators
# A python iterator is an object that contains a countable number of values and
# can be iterated upon, meaning that, you can traverse through all the values.
# It implements the iterator protocol which consists of the methods _iter_() and next()
# Lists, Sets, Dictionaries, Tuples, Strings are all iterable objects/containers from which we
# can get an iterator. All these objects have an iter() method which is used to get an iterator

# Iterator in List
sampleList=['Apple','Mango','Banana']
print(type(sampleList))
print("**********************************************************")
myListIterator=iter(sampleList)
print(next(myListIterator))
print(next(myListIterator))
print(next(myListIterator))
print("**********************************************************")

# Iterator in Tuple
sampleTuple=('Apple','Mango','Banana')
print(type(sampleTuple))
print("**********************************************************")
myTupleIterator=iter(sampleTuple)
print(next(myTupleIterator))
print(next(myTupleIterator))
print(next(myTupleIterator))
print("**********************************************************")

# Iterator in Set
sampleSet={'Apple','Mango','Banana'}
print(type(sampleSet))
print("**********************************************************")
mySetIterator=iter(sampleSet)
print(next(mySetIterator))
print(next(mySetIterator))
print(next(mySetIterator))
print("**********************************************************")

# Iterator in Dictionary
sampleDictionary={1:'Apple',2:'Mango',3:'Banana'}
print(type(sampleDictionary))
print("**********************************************************")
myDictionaryIterator=iter(sampleDictionary)
print(next(myDictionaryIterator))
print(next(myDictionaryIterator))
print(next(myDictionaryIterator))
print("**********************************************************")

# Iterator in String
sampleString="SampleString"
print(type(sampleString))
print("**********************************************************")
myStringIterator=iter(sampleString)
print(next(myStringIterator))
print(next(myStringIterator))
print(next(myStringIterator))
print(next(myStringIterator))
print("**********************************************************")

# Creating an Iterator
class MyNumbers:
    def _iter_(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a += 1
        return x

myClass=MyNumbers()
print(type(myClass))
print("**********************************************************")
myClassIterator=iter(myClass)
print(next(myClassIterator))
print(next(myClassIterator))
print(next(myClassIterator))
print("**********************************************************")