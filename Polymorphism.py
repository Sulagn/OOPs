# ---------- Shape Area Calculator: Polymorphism Demonstration ----------

import math

# Base class
class Shape:
    def area(self):
        # Abstract method (no implementation here)
        raise NotImplementedError("Subclasses must implement this method")


# Derived class 1: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        return math.pi * self.radius ** 2


# Derived class 2: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length 
        self.width = width 

    def area(self):
        return self.length * self.width


# Derived class 3: Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# ---------- Try It Out Section ----------

# Create objects of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Polymorphism in action: same method name, different outputs
shapes = [circle, rectangle, triangle]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is {shape.area():.2f}") 
    #Runtime Polymorphism(shape.area()) — the correct method is determined while the program is running, not during compilation.
