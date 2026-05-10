from school_rogue import EnemyPlugin

class WanderingNoble(EnemyPlugin):
    name = "Wandering Noble"
    glyph = "N"
    max_hp = 3
    attack = 1
    defence = 1
    xp_reward = 3
    description = "A mindless noble of a house long lost..."

class FlyingDrake(EnemyPlugin):
    name = "Dragon"
    glyph = "D"
    max_hp = 200
    attack = 200
    defence = 200
    xp_reward = 20000
    description = "A terrifying dragon, still clutching the dead body of a hero"

