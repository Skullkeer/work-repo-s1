class Computer:
    def __init__(self, cpu, gpu, ram, mb, storage):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.mb = mb
        self.storage = storage

    def work(self):
        print("working")

    def compute(self):
        print("computrer is computing")

    def turn_on(self):
        print("turning on")

    def turn_off(self):
        print("turning off")

    def print_specs(self):
        print(f"""
    GPU: {self.gpu}
    CPU: {self.cpu}
    RAM: {self.ram}
    MB:  {self.mb}
    SSD: {self.storage}
            """)


#     stuff that computer has
#         cpu
#         gpu
#         ram
#         motherboard
#         storage

#     stuff they can do
#         work()
#         compute()
#         turn_on()
#         turn_off

