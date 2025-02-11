#Create a class named MyClass, with a property named x:
class MyClass:
  x = 15

#Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Michael", 24)

print(p1.name)
print(p1.age)

#The string representation of an object WITHOUT the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
#The result will be <__main__.Person object at 0x15039e602100>

#The string representation of an object WITH the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#Insert a function that prints a greeting, and execute it on the p1 object: Creating method in the class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#Class with getString and printString methods
class MyString:
    def getString(self):
        self.string = input("Enter a string: ")
        
    def printString(self):
        print(self.string.upper())

my_str = MyString()
my_str.getString()
my_str.printString()

#Shape and Square Classes
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
        
    def area(self):
        return self.length * self.length
square = Square(4)
print(square.area())

#Rectangle Class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
rectangle = Rectangle(4, 5)
print(rectangle.area())

#Point Class
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print(f"Point({self.x}, {self.y})")
        
    def move(self, x, y):
        self.x = x
        self.y = y
        
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
point1 = Point(0, 0)
point2 = Point(3, 4)
point1.show()
point2.show()
print(point1.dist(point2))

#Bank Account Class
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Added {amount} to the balance. New balance is {self.balance}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance is {self.balance}")
acc = Account("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(150)

#Filter Prime Numbers using Lambda
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)



