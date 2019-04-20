from enum import Enum
from random import randint
from typing import List

from util.random_util import hit_percentage


class AdventureResultType(Enum):
    HERO_WIN = 1 # 勇者の勝ち
    MONSTER_WIN = 2 # モンスターの勝ち
    DRAW = 3 # 引き分け


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


class Attacker:
    def __init__(self, ability: Ability) -> None:
        self.ability = ability
        self.before_hp = ability.hp
        self.damage = 0
        self._is_critical = False

    def __calc_damage(self, enemy_ability: Ability) ->int:
        # 自分の攻撃力 - 敵の防御力のダメージ！
        # 最低でも1はダメージを与えられる
        _damage = max(self.ability.attack - enemy_ability.defense, 1)

        # クリティカルの時はダメージを2倍にする
        return _damage * 2 if self._is_critical else _damage

    def __is_critical_hit(self) ->bool:
        # 25%の確率でクリティカルになる
        return hit_percentage(25)

    def get_critical_effect(self) -> str:
        return "会心の一撃！" if self._is_critical else ""

    def do_attack(self, enemy_ability: Ability) -> None:
        # クリティカル判定
        self._is_critical = self.__is_critical_hit()

        # ダメージ計算
        self.damage = self.__calc_damage(enemy_ability)

        # HP更新
        self.before_hp = enemy_ability.hp
        enemy_ability.hp = max(enemy_ability.hp - self.damage, 0)



class Character(Attacker):
    def __init__(self, name: str, ability: Ability) -> None:
        super().__init__(ability)
        self.name = name

    def do_attack(self, enemy_name: str, enemy_ability: Ability) -> None:
        super().do_attack(enemy_ability)

        print(f"  {self.name}が{enemy_name}に攻撃した！{self.damage} のダメージ！{self.get_critical_effect()}")
        print(f"  {enemy_name} の HP:{self.before_hp}/{enemy_ability.hp_max} が {enemy_ability.hp} になった！")

    def is_alive(self) -> bool:
        return self.ability.hp > 0

    def is_dead(self) -> bool:
        return not self.is_alive()


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


class Hero(Character):
    def __init__(self, name: str) -> None:
        super().__init__(name, Ability(
            level=10,
            hp_max=80,
            hp=80,
            attack=40,
            defense=20,
        ))


class Adventure:
    def __init__(self) -> None:
        self.hero = Hero("勇者")
        self.current_monster = None

    def __get_encount_monster(self) -> Monster:
        # スライム、ゴブリン、キメラのどれかが出現する
        _monster_classes = [Slime, Goblin, Chimera]
        return _monster_classes[randint(0, len(_monster_classes) - 1)]()

    def __encount(self) -> Monster:
        #   A A
        # (｢・ω・)｢ｶﾞｵｰ (・ω・`)ﾔﾒﾃｰ
        print("----------------------------------------------")
        self.current_monster = self.__get_encount_monster()
        print(f"あ！ {self.current_monster.name} が 飛び出してきた！")
        print("----------------------------------------------")
        self.current_monster.ability.print(self.current_monster.name)
        print("----------------------------------------------")
        self.hero.ability.print(self.hero.name)

    def __get_adventure_result_type(self) -> AdventureResultType:
        if self.hero.is_dead() and self.current_monster.is_dead():
            # 勇者とモンスターがともに倒れた場合は、引き分け
            return AdventureResultType.DRAW
        elif self.hero.is_dead():
            # 勇者が倒れた場合は、モンスターの勝ち
            return AdventureResultType.MONSTER_WIN
        # それ以外の場合は、勇者の勝ち
        return AdventureResultType.HERO_WIN

    def __result(self) -> None:
        _adventure_result_type = self.__get_adventure_result_type()

        print("----------------------------------------------")
        if _adventure_result_type is AdventureResultType.HERO_WIN:
            print(f"{self.hero.name}の勝利")
            print("----------------------------------------------")
            print("今日も世界に平和が訪れた。")
            return
        elif _adventure_result_type is AdventureResultType.MONSTER_WIN:
            print(f"{self.current_monster.name}の勝利")
            print("----------------------------------------------")
            print("おお 勇者！ しんでしまうとは なにごとだ！")
            return
        else:
            print("相打ち...")
            print("----------------------------------------------")
            print("そういうこともあるよ")
        print("----------------------------------------------")

    def go(self, monster_count: int) -> None:
        for _ in range(monster_count):
            self.__encount()
            while self.hero.is_alive() and self.current_monster.is_alive():
                print("----------------------------------------------")
                self.current_monster.do_attack(self.hero.name, self.hero.ability)
                print("")
                self.hero.do_attack(self.current_monster.name, self.current_monster.ability)
            if self.hero.is_dead():
                break

        self.__result()


adventure = Adventure()
adventure.go(monster_count=3)
