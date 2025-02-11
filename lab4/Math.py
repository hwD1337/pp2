x = min(5, 15, 40)
y = max(5, 10, 50)

print(x)
print(y)

#make positive 
x = abs(-15.34)

print(x)

#Return the value of 5 to the power of 6:
x = pow(5, 6)

print(x)

#d
import math
x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#Convert Degree to Radian
import math

def degree_to_radian(degree):
    radian = degree * (math.pi / 180)
    return radian
degree = 15
print(f"Input degree: {degree}\nOutput radian: {degree_to_radian(degree):.6f}")

#Calculate the Area of a Trapezoid
def area_of_trapezoid(height, base1, base2):
    area = ((base1 + base2) * height) / 2
    return area
height = 5
base1 = 5
base2 = 6
print(f"Height: {height}\nBase, first value: {base1}\nBase, second value: {base2}\nExpected Output: {area_of_trapezoid(height, base1, base2)}")

#Calculate the Area of a Regular Polygon
def area_of_regular_polygon(sides, length):
    area = (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))
    return area
sides = 4
length = 25
print(f"Input number of sides: {sides}\nInput the length of a side: {length}\nThe area of the polygon is: {area_of_regular_polygon(sides, length):.1f}")

#Calculate the Area of a Parallelogram
def area_of_parallelogram(base, height):
    area = base * height
    return area
base = 5
height = 6
print(f"Length of base: {base}\nHeight of parallelogram: {height}\nExpected Output: {area_of_parallelogram(base, height)}")
