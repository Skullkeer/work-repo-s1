class Player:
    def __init__(self, hp, attack, weapon):
        self.hp = hp
        self.attack = attack
        self.weapon = weapon

    def take_damage(damage):
        self.hp -= damage
        print(self.hp)

    def attack(target):
        print(f"attacks {target}")

    def ls_weapon():
        print(f"Weapon: {self.weapon}")

# -------------------------------------------------------

p1 = Player(12, 6, "axe")

p2 = Player(12, 9, "Sword")
