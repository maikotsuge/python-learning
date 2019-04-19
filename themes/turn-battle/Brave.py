import random

class Brave():
    DEFAULT_HP = 200
    DEFAULT_AT = 50
    DEFAULT_DE = 30
    DEFAULT_LV = 10
    CRITICAL_ATTACK_RATE = 2.0
    CRITICAL_RATE = 0.25

    def __init__(self, name) -> None:
        self.__name = name
        self.__lv = self.DEFAULT_LV
        self.__hp = self.DEFAULT_HP
        self.__at = self.DEFAULT_AT
        self.__de = self.DEFAULT_DE

    def self_introduction(self) ->None:
        print("----------------------------------------------")
        print(f"私の名前は勇者{self.__name}です。")

    def self_status(self) -> None:
        print("----------------------------------------------")
        print(f"名前：{self.__name}")
        print(f"Lv.{self.__lv}")
        print(f"HP:{self.__hp}")
        print(f"AT:{self.__at}")
        print(f"De:{self.__de}")

    def get_name(self) -> str:
        return self.__name

    def attack(self, opponent) -> None:
        _damage = self.__at * self.CRITICAL_ATTACK_RATE if self.is_critical() else self.__at
        real_damage = opponent.real_damege(_damage)
        print("----------------------------------------------")
        print(f"damage:{_damage}, real_damage:{real_damage}")
        print(f"{self.__name}が{opponent.get_name()}に攻撃した！{real_damage} のダメージ！")
        opponent.damage(real_damage)
    
    def is_critical(self) -> bool:
        ram = random.random()
        return (ram <= self.CRITICAL_RATE)
    
    def damage(self, damage) -> None:
        before_hp = self.__hp
        self.__hp = self.__hp - damage
        print(f"{self.__name} の HP:{before_hp} が HP:{self.__hp} になった！")

    def real_damege(self, damage) -> int:
        real_damage = damage - self.__de
        if real_damage <= 0:
            real_damage = 1
        print(f"{real_damage} = {damage} - {self.__de}")
        return real_damage

    def is_check_hp(self) -> bool:
        return (self.__hp > 0)


