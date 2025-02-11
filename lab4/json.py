#Convert from JSON to Python:
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#Convert from Python to JSON:
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None

#Convert a Python object containing all the legal data types:
import json

x = {
  "name": "Kanat",
  "age": 21,
  "married": False,
  "divorced": False,
  "children": None,
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

#The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

#The json.dumps() method has parameters to make it easier to read the result:
#Use the indent parameter to define the numbers of indents:

json.dumps(x, indent=4)

#Use the separators parameter to change the default separator:

json.dumps(x, indent=4, separators=(". ", " = "))

#Use the sort_keys parameter to specify if the result should be sorted or not:

json.dumps(x, indent=4, sort_keys=True)
