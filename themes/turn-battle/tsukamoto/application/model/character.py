from model.ability import Ability
from model.attacker import Attacker


class Character(Attacker):
    def __init__(self, name: str, ability: Ability) -> None:
        super().__init__(ability)
        self.name = name

    def is_alive(self) -> bool:
        return self.ability.hp > 0

    def is_dead(self) -> bool:
        return not self.is_alive()

    def print_ability(self) -> None:
        print(f"  {self.name}")
        self.ability.print()
