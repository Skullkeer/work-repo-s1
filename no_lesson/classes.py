class Claymore(EquipmentPlugin):
    name = "Claymore"
    glyph = "T"
    attack_bonus = 5
    defence_bonus = 0
    heal_amount = 0
    consumable = False
    description: "A steel sword, weilded with two hands. Capable of thrusting attacks"

class MoonlightGreatsword(EquipmentPlugin):
    name = "Moonlight Greatsword"
    glyph = "/"
    attack_bonus = 20
    defence_bonus = 0
    heal_amount = 0
    consumable = False
    description = "Pale blue, cold greatsword. Feels magical"

class WanderingNoble(EnemyPlugin):
    name = "Wandering Noble"
    glyph = "I"
    max_hp = 3
    attack = 1
    defence = 1
    xp_reward = 3
    description = "A mindless noble of a house long lost..."

class FlyingDrake(EnemyPlugin):
    name = "Dragon"
    glyph = "§"
    max_hp = 200
    attack = 200
    defence = 200
    xp_reward = 20000
    description = "A terrifying dragon, still clutching the dead body of a hero"
