import math

class Shape:
    """A base class representing a generic shape."""
    
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """A class representing a rectangle, derived from Shape."""
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    """A class representing a circle, derived from Shape."""
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

#from polymorphism_demo import Shape, Rectangle, Circle

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
