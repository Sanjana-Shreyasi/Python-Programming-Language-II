#U3Q9P1
#Create a module called shapes.py with functions to calculate the area of a circle (with radius), rectangle (with length and width) and 
#triangle (with length and width). Based on user input, determine and show the area of shapes using the user-defined module.		
import math

# Area of circle
def circle(radius):
    return math.pi * radius * radius

# Area of rectangle
def rectangle(length, width):
    return length * width

# Area of triangle
def triangle(base, height):
    return 0.5 * base * height
		