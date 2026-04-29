from computer import Computer

class Laptop(Computer):
    def __init__(self, weight, battery, portability, trackpad, touchscreen, hinge_angle):

        self.cpu = "Generic CPU"
        self.gpu = "Generic GPU"
        self.ram = "Generic Ram"
        self.mb = "Generic MB"
        self.storage = "Generic SSD"

        self.weight = weight
        self.battery = battery
        self.portability = portability
        self.trackpad = trackpad
        self.touchscreen = touchscreen
        self.hinge_angle = hinge_angle

    def charge(self):
        print("The laptop is charging")

    def fold(self):
        print("The laptop is folding")

    def compute(self):
        print("laptop is computing")
