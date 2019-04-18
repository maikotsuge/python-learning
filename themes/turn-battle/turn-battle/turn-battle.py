from random import choice, randint

class Ability:
    def __init__(self, level, hp_max, hp, attack, defense) -> None:
        self.level = level
        self.hp_max = hp_max
        self.hp = hp
        self.attack = attack
        self.defense =defense

class Character:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ability = None

    def is_critical(self) ->bool:
        return randint(1, 100) <= 25

    def calc_damage(self, enemy_ability) ->int:
        return max(self.ability.attack - enemy_ability.defense, 0)

    def do_attack(self, enemy_name: str, enemy_ability: Ability) -> None:
        # ダメージ計算
        _damage = self.calc_damage(enemy_ability)

        # クリティカル計算
        _is_critical = self.is_critical()
        _efect_string = "会心の一撃！" if _is_critical else ""
        _damage = _damage * 2 if _is_critical else _damage

        # HP更新
        _before_hp = enemy_ability.hp
        enemy_ability.hp = max(enemy_ability.hp - _damage, 0)

        print(f"  {self.name}が{enemy_name}に攻撃した！{_damage} のダメージ！{_efect_string}")
        print(f"  {enemy_name} の HP:{_before_hp} が {enemy_ability.hp} になった！")

    def is_alive(self) -> bool:
        return self.ability.hp > 0

    def is_dead(self) -> bool:
        return not self.is_alive()

    def print_ability(self) -> None:
        print(f"  {self.name}")
        print(f"  Lv: {self.ability.level}")
        print(f"  HP: {self.ability.hp}")
        print(f"  AT: {self.ability.attack}")
        print(f"  DE: {self.ability.defense}")

class Monster(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        _level = randint(1, 10)
        _hp_max = randint(10, 15) * _level
        self.ability = Ability(
            level=_level,
            hp_max=_hp_max,
            hp=_hp_max,
            attack=randint(1, 5) * _level,
            defense=randint(1, 3) * _level,
        )

    def encount(self) -> None:
        print(f"あ！ {self.name} が 飛び出してきた！")

class Slime(Monster):
    def __init__(self):
        super().__init__("スライム")

class Goblin(Monster):
    def __init__(self):
        super().__init__("ゴブリン")

class Chimera(Monster):
    def __init__(self):
        super().__init__("キメラ")

class Hero(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.ability = Ability(
            level=10,
            hp_max=80,
            hp=80,
            attack=40,
            defense=20,
        )

    def end_adventure(self, enemy: Character) -> None:
        if self.is_dead() and enemy.is_dead():
            print("相打ち...")
            print("----------------------------------------------")
            print("そういうこともあるよ")
            return
        elif self.is_dead():
            print(f"{enemy.name}の勝利")
            print("----------------------------------------------")
            print("おお 勇者！ しんでしまうとは なにごとだ！")
            return

        print(f"{self.name}の勝利")
        print("----------------------------------------------")
        print("今日も世界に平和が訪れた。")

def game_main() -> None:
    hero = Hero("勇者")
    monster = None

    count = 3
    for _ in range(count):
        #   A A
        # (｢・ω・)｢ｶﾞｵｰ (・ω・`)ﾔﾒﾃｰ
        print("----------------------------------------------")
        monster = choice([Slime(), Goblin(), Chimera()])
        monster.encount()
        print("----------------------------------------------")
        monster.print_ability()
        print("----------------------------------------------")
        hero.print_ability()
        while hero.is_alive() and monster.is_alive():
            print("----------------------------------------------")
            monster.do_attack(hero.name, hero.ability)
            print("")
            hero.do_attack(monster.name, monster.ability)
        if hero.is_dead():
            break

    print("----------------------------------------------")
    hero.end_adventure(monster)
    print("----------------------------------------------")

game_main()
