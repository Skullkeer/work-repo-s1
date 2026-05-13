class PlayerSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance



    def __init__(self, hp, attk, weapon):
        self.hp = hp
        self.attk = attk
        self.weapon = weapon

    def set_hp(self, hp):
        self.hp = hp

    def set_attk(self, attk):
        self.attk = attk

    def set_weapon(self, weapon):
        self.weapon = weapon

    def ls_weapon(self):
        print(self.weapon)

p1 = PlayerSingleton()

p1.set_hp(12)
p1.set_attk(4)
p1.set_weapon("Axe")

print(f"p1 == p2: {p1 == p2}")

p2 = PlayerSingleton

p2.ls_weapon()
