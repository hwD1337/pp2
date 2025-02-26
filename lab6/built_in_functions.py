#Python program to multiply all the numbers in a list:
import math

def multiply_list(lst):
    return math.prod(lst)

numbers = [1, 2, 3, 4, 5]
result = multiply_list(numbers)
print("Product of the list:", result)

#Python program to calculate the number of upper case and lower case letters in a string:
def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

input_string = "Hello World!"
upper_case, lower_case = count_case(input_string)
print("Upper case letters:", upper_case)
print("Lower case letters:", lower_case)

#Python program to check if a passed string is a palindrome:
def is_palindrome(s):
    return s == s[::-1]

input_string = "radar"
result = is_palindrome(input_string)
print(f"Is '{input_string}' a palindrome?", result)

#Python program to invoke square root function after specific milliseconds:
import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000.0)
    return math.sqrt(number)

number = 25100
delay = 2123
result = delayed_square_root(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")

#Python program that returns True if all elements of the tuple are true:
def all_true(tpl):
    return all(tpl)

tpl = (True, True, True)
result = all_true(tpl)
print("All elements are true:", result)
