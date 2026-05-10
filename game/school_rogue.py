#!/usr/bin/env python3
"""
school_rogue.py

A small ASCII top-down dungeon crawler with plugin loading for:
- enemies
- equipment

Run:
    python3 school_rogue.py
"""

from __future__ import annotations

import importlib.util
import inspect
import random
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Type
import os
import termios
import tty

sys.modules["school_rogue"] = sys.modules[__name__]

@dataclass
class Item:
    name: str
    glyph: str
    attack_bonus: int = 0
    defense_bonus: int = 0
    heal_amount: int = 0
    consumable: bool = False
    description: str = ""


class EquipmentPlugin:
    """
    Student equipment files should subclass this.
    """
    name = "Plain Trinket"
    glyph = "!"
    attack_bonus = 0
    defense_bonus = 0
    heal_amount = 0
    description = "No description."
    consumable = False

    @classmethod
    def build(cls) -> Item:
        return Item(
            name=cls.name,
            glyph=cls.glyph,
            attack_bonus=cls.attack_bonus,
            defense_bonus=cls.defense_bonus,
            heal_amount=cls.heal_amount,
            consumable=cls.consumable,
            description=cls.description,
        )


@dataclass
class Enemy:
    name: str
    glyph: str
    max_hp: int
    hp: int
    attack: int
    defense: int
    xp_reward: int = 1
    description: str = ""

    def is_alive(self) -> bool:
        return self.hp > 0


class EnemyPlugin:
    """
    Student enemy files should subclass this.
    """
    name = "Training Dummy"
    glyph = "g"
    max_hp = 6
    attack = 1
    defense = 0
    xp_reward = 1
    description = "A harmless practice target."

    @classmethod
    def build(cls) -> Enemy:
        return Enemy(
            name=cls.name,
            glyph=cls.glyph,
            max_hp=cls.max_hp,
            hp=cls.max_hp,
            attack=cls.attack,
            defense=cls.defense,
            xp_reward=cls.xp_reward,
            description=cls.description,
        )


@dataclass
class Player:
    x: int
    y: int
    hp: int = 20
    max_hp: int = 20
    base_attack: int = 2
    base_defense: int = 0
    xp: int = 0
    alive: bool = True

    def total_attack(self, inventory: List[Item]) -> int:
        return self.base_attack + sum(i.attack_bonus for i in inventory)

    def total_defense(self, inventory: List[Item]) -> int:
        return self.base_defense + sum(i.defense_bonus for i in inventory)


@dataclass
class EnemyInstance:
    x: int
    y: int
    enemy: Enemy


@dataclass
class ItemInstance:
    x: int
    y: int
    item: Item


def get_key() -> str:
    """
    Read a single keypress without requiring Enter.
    Supports regular keys and arrow keys.
    Returns:
        'w', 'a', 's', 'd', 'i', 'q'
        or 'UP', 'DOWN', 'LEFT', 'RIGHT'
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch1 = sys.stdin.read(1)

        if ch1 == "\x1b":
            ch2 = sys.stdin.read(1)
            ch3 = sys.stdin.read(1)
            if ch2 == "[":
                if ch3 == "A":
                    return "UP"
                if ch3 == "B":
                    return "DOWN"
                if ch3 == "C":
                    return "RIGHT"
                if ch3 == "D":
                    return "LEFT"
            return ch1

        return ch1.lower()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def load_module_from_file(py_file: Path):
    spec = importlib.util.spec_from_file_location(py_file.stem, py_file)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load spec for {py_file}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def discover_plugins(folder: Path, base_class: Type) -> List[Type]:
    found = []
    if not folder.exists():
        return found

    for py_file in sorted(folder.glob("*.py")):
        if py_file.name.startswith("_"):
            continue
        try:
            module = load_module_from_file(py_file)
        except Exception as exc:
            print(f"[PLUGIN ERROR] {py_file.name}: {exc}")
            continue

        for _, obj in inspect.getmembers(module, inspect.isclass):
            if obj is base_class:
                continue
            if issubclass(obj, base_class):
                found.append(obj)

    return found


class Game:
    WALL = "#"
    FLOOR = "."
    EXIT = ">"
    PLAYER_GLYPH = "@"

    def __init__(self) -> None:
        self.root = Path(__file__).resolve().parent
        self.enemy_plugins = discover_plugins(
            self.root / "plugins" / "enemies",
            EnemyPlugin,
        )
        self.equipment_plugins = discover_plugins(
            self.root / "plugins" / "equipment",
            EquipmentPlugin,
        )

        self.width = 40
        self.height = 18
        self.turn = 0
        self.floor = 1
        self.messages: List[str] = []
        self.inventory: List[Item] = []
        self.player = Player(x=2, y=2)

        self.map: List[List[str]] = []
        self.enemies: List[EnemyInstance] = []
        self.items: List[ItemInstance] = []
        self.exit_pos = (0, 0)

        self.generate_floor()

    def log(self, message: str) -> None:
        self.messages.append(message)
        self.messages = self.messages[-8:]

    def generate_floor(self) -> None:
        self.map = [[self.FLOOR for _ in range(self.width)]
                    for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or y == 0 or x == self.width - 1 or y == self.height - 1:
                    self.map[y][x] = self.WALL

        # Random internal walls
        wall_count = 45
        for _ in range(wall_count):
            x = random.randint(2, self.width - 3)
            y = random.randint(2, self.height - 3)
            if (x, y) != (2, 2):
                self.map[y][x] = self.WALL

        self.player.x, self.player.y = 2, 2
        self.enemies.clear()
        self.items.clear()

        # Place exit
        while True:
            ex = random.randint(2, self.width - 3)
            ey = random.randint(2, self.height - 3)
            if self.is_floor(ex, ey) and (ex, ey) != (2, 2):
                self.map[ey][ex] = self.EXIT
                self.exit_pos = (ex, ey)
                break

        # Place enemies
        enemy_count = min(3 + self.floor, 10)
        if not self.enemy_plugins:
            self.enemy_plugins = [EnemyPlugin]
        for _ in range(enemy_count):
            px, py = self.find_empty_tile()
            enemy_cls = random.choice(self.enemy_plugins)
            enemy = enemy_cls.build()
            enemy.hp += max(0, self.floor - 1)
            enemy.max_hp += max(0, self.floor - 1)
            self.enemies.append(EnemyInstance(px, py, enemy))

        # Place equipment
        item_count = min(2 + self.floor // 2, 6)
        if not self.equipment_plugins:
            self.equipment_plugins = [EquipmentPlugin]
        for _ in range(item_count):
            px, py = self.find_empty_tile()
            item_cls = random.choice(self.equipment_plugins)
            self.items.append(ItemInstance(px, py, item_cls.build()))

        self.log(f"Entered floor {self.floor}.")
        self.log(
            f"Loaded {len(self.enemy_plugins)} enemy type(s), "
            f"{len(self.equipment_plugins)} equipment type(s)."
        )

    def is_floor(self, x: int, y: int) -> bool:
        return self.map[y][x] in {self.FLOOR, self.EXIT}

    def enemy_at(self, x: int, y: int) -> Optional[EnemyInstance]:
        for e in self.enemies:
            if e.x == x and e.y == y and e.enemy.is_alive():
                return e
        return None

    def item_at(self, x: int, y: int) -> Optional[ItemInstance]:
        for i in self.items:
            if i.x == x and i.y == y:
                return i
        return None

    def tile_occupied(self, x: int, y: int) -> bool:
        if (x, y) == (self.player.x, self.player.y):
            return True
        if self.enemy_at(x, y):
            return True
        if self.item_at(x, y):
            return True
        return False

    def find_empty_tile(self) -> tuple[int, int]:
        while True:
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if not self.is_floor(x, y):
                continue
            if self.tile_occupied(x, y):
                continue
            return x, y

    def draw(self) -> None:
        os.system("clear")
        print("\n" * 2)
        print("=" * self.width)
        print(f"ASCII SCHOOL ROGUE  |  Floor {self.floor}  |  Turn {self.turn}")
        print(
            f"HP {self.player.hp}/{self.player.max_hp}  "
            f"ATK {self.player.total_attack(self.inventory)}  "
            f"DEF {self.player.total_defense(self.inventory)}  "
            f"XP {self.player.xp}"
        )
        print("=" * self.width)

        for y in range(self.height):
            row = []
            for x in range(self.width):
                if (x, y) == (self.player.x, self.player.y):
                    row.append(self.PLAYER_GLYPH)
                    continue

                enemy_here = self.enemy_at(x, y)
                if enemy_here:
                    row.append(enemy_here.enemy.glyph)
                    continue

                item_here = self.item_at(x, y)
                if item_here:
                    row.append(item_here.item.glyph)
                    continue

                row.append(self.map[y][x])
            print("".join(row))

        print("-" * self.width)
        print("Controls: W A S D move | Q quit")
        print("Goal: reach > and survive.")
        print("-" * self.width)

        if self.inventory:
            print("Inv:")
            for idx, item in enumerate(self.inventory, start=1):
                print(
                    f"{item.name} [ATK+{item.attack_bonus}/DEF+{item.defense_bonus}]"
                )
                if item.description:
                    print(f"  {item.description}")
        else:
            print("Inventory: empty")

        print("-" * self.width)
        print("Recent messages:")
        if self.messages:
            for msg in self.messages[-8:]:
                print(f"  - {msg}")
        else:
            print("  - None yet.")
        print("=" * self.width)

    def pickup_if_present(self) -> None:
        item_here = self.item_at(self.player.x, self.player.y)
        if not item_here:
            return

        item = item_here.item
        self.items.remove(item_here)
        self.log(f"Picked up {item.name}.")

        if item.description:
            self.log(item.description)

        if item.consumable:
            old_hp = self.player.hp
            self.player.hp = min(
                self.player.max_hp,
                self.player.hp + item.heal_amount,
            )
            healed = self.player.hp - old_hp
            self.log(f"{item.name} is consumed.")
            if healed > 0:
                self.log(f"{item.name} restored {healed} HP.")
            else:
                self.log("It had no effect.")
            return

        self.inventory.append(item)

    def step_to_next_floor_if_needed(self) -> None:
        if self.map[self.player.y][self.player.x] == self.EXIT:
            self.floor += 1
            self.generate_floor()

    def resolve_combat(self, enemy_inst: EnemyInstance) -> None:
        enemy = enemy_inst.enemy
        self.log(f"You engage {enemy.name}.")

        if enemy.description:
            self.log(enemy.description)

        while self.player.alive and enemy.is_alive():
            player_roll = random.randint(1, 6)
            enemy_roll = random.randint(1, 6)

            player_damage = max(
                1,
                player_roll + self.player.total_attack(self.inventory) - enemy.defense
            )
            enemy_damage = max(
                1,
                enemy_roll + enemy.attack - self.player.total_defense(self.inventory)
            )

            enemy.hp -= player_damage
            self.log(
                f"You roll {player_roll} and hit {enemy.name} "
                f"for {player_damage}."
            )

            if enemy.hp <= 0:
                enemy.hp = 0
                self.player.xp += enemy.xp_reward
                self.log(f"{enemy.name} dies. You gain {enemy.xp_reward} XP.")
                break

            self.player.hp -= enemy_damage
            self.log(
                f"{enemy.name} rolls {enemy_roll} and hits you "
                f"for {enemy_damage}."
            )

            if self.player.hp <= 0:
                self.player.hp = 0
                self.player.alive = False
                self.log("You died.")
                return

        if not enemy.is_alive():
            self.enemies = [e for e in self.enemies if e.enemy.is_alive()]

    def try_move(self, dx: int, dy: int) -> None:
        tx = self.player.x + dx
        ty = self.player.y + dy

        if self.map[ty][tx] == self.WALL:
            self.log("You bump into a wall.")
            return

        enemy_here = self.enemy_at(tx, ty)
        if enemy_here:
            self.resolve_combat(enemy_here)
            if not self.player.alive:
                return
            if not enemy_here.enemy.is_alive():
                self.player.x = tx
                self.player.y = ty
                self.pickup_if_present()
                self.step_to_next_floor_if_needed()
            return

        self.player.x = tx
        self.player.y = ty
        self.pickup_if_present()
        self.step_to_next_floor_if_needed()

    def handle_input(self, cmd: str) -> bool:
        cmd = cmd.strip().lower()

        if cmd == "q":
            return False
        if cmd in ("w", "up"):
            self.try_move(0, -1)
        elif cmd in ("s", "down"):
            self.try_move(0, 1)
        elif cmd in ("a", "left"):
            self.try_move(-1, 0)
        elif cmd in ("d", "right"):
            self.try_move(1, 0)
        else:
            self.log("Unknown command.")
            return True

        self.turn += 1
        return True

        self.turn += 1
        return True

    def run(self) -> None:
        self.log("Welcome to the dungeon.")
        while self.player.alive:
            self.draw()
            cmd = get_key()
            if not self.handle_input(cmd):
                print("Goodbye.")
                return

        self.draw()
        print("GAME OVER")


if __name__ == "__main__":
    try:
        Game().run()
    except KeyboardInterrupt:
        print("\nGoodbye.")
        sys.exit(0)
