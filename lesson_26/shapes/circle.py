from shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return round(math.pi * pow(self.radius, 2))



