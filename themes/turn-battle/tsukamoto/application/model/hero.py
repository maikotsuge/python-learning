from model.ability import Ability
from model.character import Character


class Hero(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name, Ability(
            level=10,
            hp_max=80,
            hp=80,
            attack=40,
            defense=20,
        ))
