#Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Create an iterator that returns numbers, starting with 3, and each sequence will increase by one (returning 3,5,7,9,11, etc.):
class MyNumbers:
  def __iter__(self):
    self.a = 3
    return self

  def __next__(self):
    x = self.a
    self.a += 2
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Stop after 15 iterations:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 15:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#Generator for squares of numbers up to N
def squares_up_to_n(N):
    for i in range(N + 1):
        yield i * i
for square in squares_up_to_n(5):
    print(square)

#Generator to print even numbers between 0 and n in comma-separated form
def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
n = int(input("Enter a number: "))
even_nums = list(even_numbers(n))
print(", ".join(map(str, even_nums)))

#Generator for numbers divisible by 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for num in divisible_by_3_and_4(20):
    print(num)

#Generator called squares to yield the square of all numbers from (a) to (b)
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
for square in squares(3, 6):
    print(square)

#Generator that returns all numbers from (n) down to 0
def countdown(n):
    for i in range(n, -1, -1):
        yield i
for num in countdown(5):
    print(num)


