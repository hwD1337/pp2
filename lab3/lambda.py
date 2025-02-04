#Add 15 to argument a, and return the result:
x = lambda a : a + 15
print(x(10))

#lambda in function
def myfunc(n):
  return lambda a : a * n

#Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(15))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
