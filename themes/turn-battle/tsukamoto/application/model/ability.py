
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
        self.before_hp = self.hp
        self.attack = attack
        self.defense = defense

    def damage(self, damage) -> None:
        self.before_hp = self.hp
        self.hp = max(self.hp - damage, 0)

    def print(self) -> None:
        print(f"  Lv: {self.level}")
        print(f"  HP: {self.hp}")
        print(f"  AT: {self.attack}")
        print(f"  DE: {self.defense}")
