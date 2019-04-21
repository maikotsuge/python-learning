from enum import Enum
from random import randint

from model.character import Character
from model.hero import Hero
from model.monster import Chimera, Goblin, Monster, Slime


class AdventureResultType(Enum):
    HERO_WIN = 1 # 勇者の勝ち
    MONSTER_WIN = 2 # モンスターの勝ち
    DRAW = 3 # 引き分け


class Adventure:
    def __init__(self) -> None:
        self.hero = Hero("勇者")
        self.current_monster = None

    def __get_encount_monster(self) -> Monster:
        # スライム、ゴブリン、キメラのどれかが出現する
        _monster_classes = [Slime, Goblin, Chimera]
        return _monster_classes[randint(0, len(_monster_classes) - 1)]()

    def __encount(self) -> None:
        #   A A
        # (｢・ω・)｢ｶﾞｵｰ (・ω・`)ﾔﾒﾃｰ
        print("----------------------------------------------")
        self.current_monster = self.__get_encount_monster()
        print(f"あ！ {self.current_monster.name} が 飛び出してきた！")
        print("----------------------------------------------")
        self.current_monster.print_ability()
        print("----------------------------------------------")
        self.hero.print_ability()

    def __do_attack(self, attacker: Character, defender: Character) -> None:
        attacker.do_attack(defender.ability)
        print(f"  {attacker.name}が{defender.name}に攻撃した！{attacker.damage} のダメージ！{attacker.get_critical_effect()}")
        print(f"  {defender.name} の HP:{defender.ability.hp.before}/{defender.ability.hp.max} が {defender.ability.hp.current} になった！")

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
        elif _adventure_result_type is AdventureResultType.MONSTER_WIN:
            print(f"{self.current_monster.name}の勝利")
            print("----------------------------------------------")
            print("おお 勇者！ しんでしまうとは なにごとだ！")
        else:
            print("相打ち...")
            print("----------------------------------------------")
            print("そういうこともあるよ")
        print("----------------------------------------------")

    def go(self, monster_count: int) -> None:
        # 冒険に出発する

        for _ in range(monster_count):
            # モンスターが現れた！
            self.__encount()

            _turn_count = 0
            while self.hero.is_alive() and self.current_monster.is_alive():
                _turn_count += 1
                print("----------------------------------------------")
                print(f"TURN {_turn_count}")
                print("----------------------------------------------")

                # 勇者がモンスターを攻撃する
                self.__do_attack(self.hero, self.current_monster)

                # モンスターが倒れたらターンを終了する
                if self.current_monster.is_dead():
                    break
                print("")

                # 勇者がモンスターから反撃される
                self.__do_attack(self.current_monster, self.hero)

            # 勇者が倒れたら冒険を終了する
            if self.hero.is_dead():
                break

        # 冒険から帰ってきた
        self.__result()


adventure = Adventure()
adventure.go(monster_count=3)
