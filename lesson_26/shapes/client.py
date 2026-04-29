from shape import Shape
from circle import Circle
from square import Square

radius = 2

c = Circle(radius)

print(f"the circle with radius {radius} has area {c.get_area()}")

length = 3

s = Square(4, "Sqaure", length)

print(f"{s.name} with length {length} has area {s.get_area()} and {s.num_verticies} verticies")
