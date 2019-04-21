
class Hp:
    def __init__(self, max: int, current: int) -> None:
        assert(max >= 0)
        assert(current >= 0)
        self.max = max
        self.current = current
        self.before = current

    def damage(self, damage) -> None:
        self.before = self.current
        self.current = max(self.current - damage, 0)


class Ability:
    def __init__(self, level: int, hp_max: int, hp: int, attack: int, defense: int) -> None:
        assert(level >= 0)
        assert(attack >= 0)
        assert(defense >= 0)
        self.level = level
        self.hp = Hp(hp_max, hp)
        self.attack = attack
        self.defense = defense

    def print(self) -> None:
        print(f"  Lv: {self.level}")
        print(f"  HP: {self.hp.current}/{self.hp.max}")
        print(f"  AT: {self.attack}")
        print(f"  DE: {self.defense}")
