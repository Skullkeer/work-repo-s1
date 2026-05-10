from school_rogue import EquipmentPlugin

class Claymore(EquipmentPlugin):
    name = "Claymore"
    glyph = "C"
    attack_bonus = 5
    defence_bonus = 0
    heal_amount = 0
    consumable = False
    description: "A steel sword, weilded with two hands. Capable of thrusting attacks"

class MoonlightGreatsword(EquipmentPlugin):
    name = "Moonlight Greatsword"
    glyph = "M"
    attack_bonus = 20
    defence_bonus = 0
    heal_amount = 0
    consumable = False
    description = "Pale blue, freezing cold greatsword. Feels magical"

