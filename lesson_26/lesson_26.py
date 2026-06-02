from computer import Computer
from laptop import Laptop
from desktop import Desktop

comp = Computer(
    "AMD Ryzen 9 9950X3D Duo",
    "nVIDIA 5090 RTX",
    "Corsair 32GB RAM DDR5",
    "ASUS ROG Crosshair V EXTREME",
    "Samsung m.2 NVME 16TB"
    )

# comp.turn_on()
# comp.compute()
# comp.print_specs()
# comp.turn_off()


lapt = Laptop(
        2.2,
        100,
        7,
        "Capacative",
        False,
        180
    )

#
# lapt.charge()
# lapt.compute()
# lapt.print_specs()
# lapt.turn_off()
#
# desk = Desktop(100, 1000)
#
# desk.turn_on()
# desk.cool_better()
# desk.taking_space()
# desk.turn_off()
#

print(comp.cpu)
