
class Ability:
    def __init__(self, level: int, hp_max: int, hp: int, attack: int, defense: int) -> None:
        assert(level >= 0)
        assert(hp_max >= 0)
        assert(hp >= 0)
        assert(attack >= 0)
        assert(defense >= 0)
        self.level = level
        self.hp_max = hp_max
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def print(self, name: str) -> None:
        print(f"  {name}")
        print(f"  Lv: {self.level}")
        print(f"  HP: {self.hp}")
        print(f"  AT: {self.attack}")
        print(f"  DE: {self.defense}")
