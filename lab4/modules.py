#Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name)
#Import the module named mymodule, and call the greeting function:
import mymodule

mymodule.greeting("Jonathan")

#Create an alias for mymodule called mx:
import mymodule as mx

a = mx.person1["age"]
print(a)

#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
import platform

x = dir(platform)
print(x)



def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
#Import only the person1 dictionary from the module:

from mymodule import person1

print (person1["age"])
