def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])
  
my_function("Emil", "Tobias", "Linus")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Kazakhstan")
my_function("India")
my_function()
my_function("Hungary")

#List as an arguement
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)

my_function(x = 7)

#To specify that a function can have only positional arguments, add , / after the arguments:
def my_function(x, /):
  print(x)

my_function(5)

#Combining both
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#Recursion Example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

#Convert Grams to Ounces
def grams_to_ounces(grams):
    ounces = grams * 0.03527396195
    return ounces
grams = 100
print(grams_to_ounces(grams))  # Output: 3.527396195

#Convert Fahrenheit to Centigrade
def fahrenheit_to_centigrade(F):
    C = (5 / 9) * (F - 32)
    return C
F = 98.6
print(fahrenheit_to_centigrade(F))  # Output: 37.0

#Solve the Classic Puzzle
def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) / 2
    chickens = numheads - rabbits
    return int(chickens), int(rabbits)
numheads = 35
numlegs = 94
print(solve(numheads, numlegs))  # Output: (23, 12)

#Filter Prime Numbers from a List
def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return list(filter(is_prime, numbers))
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(numbers))  # Output: [2, 3, 5, 7]

#Print All Permutations of a String
from itertools import permutations

def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))
string = "abc"
print_permutations(string)

#Reverse Words in a Sentence
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
sentence = "We are ready"
print(reverse_sentence(sentence))  # Output: "ready are We"

#Check for 3 Next to 3
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))  # Output: True
print(has_33([1, 3, 1, 3]))  # Output: False
print(has_33([3, 1, 3]))  # Output: False

#Check for 007 in Order
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Output: True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # Output: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Output: False

#Compute the Volume of a Sphere
import math

def volume_of_sphere(radius):
    volume = (4/3) * math.pi * (radius**3)
    return volume
radius = 5
print(volume_of_sphere(radius))  # Output: 523.5987755982989

#Get Unique Elements from a List
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
lst = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(lst))  # Output: [1, 2, 3, 4, 5]

#Check if a Word or Phrase is a Palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
word = "Madam"
print(is_palindrome(word))  # Output: True

phrase = "A man a plan a canal Panama"
print(is_palindrome(phrase))  # Output: True

#Print a Histogram
def histogram(lst):
    for value in lst:
        print('*' * value)
histogram([4, 9, 7])

#Guess the Number Game
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
guess_the_number()



