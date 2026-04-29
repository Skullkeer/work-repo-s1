from shape import Shape

class Square(Shape):
    def __init__(self, num_verticies, name, blength, pheight):
        super().__init__(num_verticies, name) # shape stuff
        self.blength = length # square stuff
        self.pheight

    def get_area(self):
        return 0.5 * self.blength * self.pheight
