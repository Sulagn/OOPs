# ---------- Vector Operator Overloading Demonstration ----------
# Concept: Special Methods (__add__, __sub__, __mul__, __eq__, __str__)
# Purpose: To show how a user-defined class can behave like built-in types (e.g., numbers)

import math  # Importing for any future mathematical operations (not essential here)


# Base class representing a mathematical vector
class Vector:
    # Constructor: initializes x and y coordinates for the vector
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Defines how the vector object should look when printed
    def __str__(self):
        return f"({self.x}, {self.y})"

    # Overloads the + operator (v1 + v2)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overloads the - operator (v1 - v2)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Overloads the * operator for scalar multiplication (v1 * 3)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Overloads the == operator for vector comparison (v1 == v2)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# ---------- Testing Section ----------
# Creating vector objects
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Displaying operations and results
print("v1 + v2 =", v1 + v2)   # Calls __add__
print("v1 - v2 =", v1 - v2)   # Calls __sub__
print("v1 * 3 =", v1 * 3)     # Calls __mul__
print("v1 == v2?", v1 == v2)  # Calls __eq__
print("v1:", v1)              # Calls __str__
