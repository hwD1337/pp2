#Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#Loop through the letters in the word "Kazakhstan":

for x in "Kazakhstan":
  print(x)
#Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#Using the range() function:

for x in range(6):
  print(x)
#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)
#Print all numbers from 0 to 11, and print a message when the loop has ended:

for x in range(12):
  print(x)
else:
  print("Finally finished!")
#Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#
