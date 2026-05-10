class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Methods
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

p = Point(2, 3)
print(f"the point is at {p.x}, {p.y}")
p.move(4, -5)
print(f"the point is at {p.x}, {p.y}")


