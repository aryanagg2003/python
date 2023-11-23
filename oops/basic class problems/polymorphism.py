# Question:

# Create a set of classes representing different geometric shapes: Circle, Rectangle, and Triangle. Each class should have a method called area() 
# that calculates and returns the area of the respective shape.

# Implement a generic function called calculate_area(shape) that takes an instance of any of these shape classes and calculates its area using the 
# area() method.

# Demonstrate polymorphism by creating instances of each shape, passing them to the calculate_area function, and printing the results.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

def calculate_area(shape):
    return shape.area()

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

print(f"Circle Area: {calculate_area(circle)}")
print(f"Rectangle Area: {calculate_area(rectangle)}")
print(f"Triangle Area: {calculate_area(triangle)}")