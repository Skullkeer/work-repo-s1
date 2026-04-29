from shape import Shape

class Square(Shape):
    def __init__(self, num_verticies, name, length):
        super().__init__(num_verticies, name) # shape stuff
        self.length = length # square stuff

    def get_area(self):
        return self.length ** 2
