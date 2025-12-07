# main.py

# Base Class - Shape
class Shape:
    def area(self):
        raise NotImplementedError("derived classes need to override this method.")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        from math import pi
        return pi * (self.radius ** 2)