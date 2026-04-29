from computer import Computer

class Desktop(Computer):
    def __init__(self, weight, wattage):

        self.cpu = "Generic CPU"
        self.gpu = "Generic GPU"
        self.ram = "Generic Ram"
        self.mb = "Generic MB"
        self.storage = "Generic SSD"

        self.weight = weight
        self.wattage = wattage

    def cool_better(self):
        print("cooling down")

    def taking_space(self):
        print("taking up space")
