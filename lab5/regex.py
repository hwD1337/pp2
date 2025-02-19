#Search the string to see if it starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

#Print a list of all matches:
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Search for the first white-space character in the string:
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#Matching a string that has an 'a' followed by zero or more 'b''s:
import re

def match_ab(string):
    pattern = r'a*b*'
    return re.fullmatch(pattern, string)

print(match_ab("ab"))  # Match
print(match_ab("aabbbb"))  # Match
print(match_ab("ac"))  # No match

#Matching a string that has an 'a' followed by two to three 'b''s:
import re

def match_ab2to3(string):
    pattern = r'ab{2,3}'
    return re.fullmatch(pattern, string)

print(match_ab2to3("abb"))  # Match
print(match_ab2to3("abbb"))  # Match
print(match_ab2to3("abbbb"))  # No match

#Finding sequences of lowercase letters joined with an underscore:
import re

def find_lowercase_underscore(string):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, string)

print(find_lowercase_underscore("hello_world this_is_a_test"))  # ['hello_world', 'this_is_a_test']

#Finding sequences of one uppercase letter followed by lowercase letters:
import re

def find_upper_lower_sequence(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)

print(find_upper_lower_sequence("Hello World Test"))  # ['Hello', 'World', 'Test']

#Matching a string that has an 'a' followed by anything, ending in 'b':
import re

def match_a_anything_b(string):
    pattern = r'a.*b'
    return re.fullmatch(pattern, string)
  
print(match_a_anything_b("a123b"))  # Match
print(match_a_anything_b("a_b"))  # Match
print(match_a_anything_b("ab"))  # Match
print(match_a_anything_b("a12"))  # No match

#Replacing all occurrences of space, comma, or dot with a colon:
import re

def replace_space_comma_dot(string):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', string)

print(replace_space_comma_dot("Hello, world. How are you?"))  # Hello:world:How:are:you:

#Converting snake case string to camel case string:
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

print(snake_to_camel("this_is_a_test"))  # thisIsATest

#Splitting a string at uppercase letters:
import re

def split_at_uppercase(string):
    pattern = r'(?=[A-Z])'
    return re.split(pattern, string)

print(split_at_uppercase("HelloWorldTest"))  # ['Hello', 'World', 'Test']

#Inserting spaces between words starting with capital letters:
import re

def insert_spaces(string):
    pattern = r'(?<=[a-z])(?=[A-Z])'
    return re.sub(pattern, ' ', string)

print(insert_spaces("HelloWorldTest"))  # Hello World Test

#Converting a given camel case string to snake case:
import re

def camel_to_snake(camel_str):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, '_', camel_str).lower()

print(camel_to_snake("thisIsATest"))  # this_is_a_test






