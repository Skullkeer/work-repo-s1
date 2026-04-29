from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, num_verticies, name):
        self.num_verticies = num_verticies
        self.name = name

    @abstractmethod
    def get_area(self):
        pass
