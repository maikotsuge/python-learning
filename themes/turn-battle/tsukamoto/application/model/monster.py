from random import randint

from model.ability import Ability
from model.character import Character


class Monster(Character):
    def __init__(self, name: str) -> None:
        _level = randint(1, 10)
        _hp_max = randint(10, 15) * _level
        super().__init__(name, Ability(
            level=_level,
            hp_max=_hp_max,
            hp=_hp_max,
            attack=randint(1, 5) * _level,
            defense=randint(1, 3) * _level,
        ))


class Slime(Monster):
    def __init__(self):
        super().__init__("スライム")


class Goblin(Monster):
    def __init__(self):
        super().__init__("ゴブリン")


class Chimera(Monster):
    def __init__(self):
        super().__init__("キメラ")
