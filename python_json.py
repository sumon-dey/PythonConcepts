# Python JSON

# JSON or JavaScript Object Notation is a textual data format for storing and exchanging data

# Conversion of JSON to Python
import json

sampleJSON1 = '{"name": "Sam", "age": 30, "phoneNumbers": [12345, 67892], "city": "Pune"}'
myPythonData = json.loads(sampleJSON1)
print(myPythonData["name"])
print(myPythonData["age"])
print(myPythonData["phoneNumbers"][0])
print(myPythonData["phoneNumbers"][1])
print(myPythonData["city"])
print("**********************************************************")

# Conversion of Python to JSON
print(myPythonData)
sampleJSON2=json.dumps(myPythonData)
print(sampleJSON2)
print("**********************************************************")