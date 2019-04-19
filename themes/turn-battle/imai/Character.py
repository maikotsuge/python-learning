import random
class Character():
    name: str = None
    lv: int = 0
    hp: int = 0
    at: int = 0
    de: int = 0
    CRITICAL_ATTACK_RATE = 2.0
    CRITICAL_RATE = 0.25

    def __init__(self, name:str) -> None:
        self.__name = name

    def set_status(self, lv:int, hp:int, at:int, de:int) -> None:
        self.__lv = lv
        self.__hp = hp
        self.__at = at
        self.__de = de

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
        print(f"{self.__name}が{opponent.get_name()}に攻撃した！{real_damage} のダメージ！")
        opponent.damage(real_damage)

    def is_critical(self) -> bool:
        ram = random.random()
        return (ram <= self.CRITICAL_RATE)

    def damage(self, damage:float) -> None:
        before_hp = self.__hp
        self.__hp = self.__hp - damage
        print(f"{self.__name} の HP:{before_hp} が HP:{self.__hp} になった！")

    def real_damege(self, damage:float) -> int:
        real_damage = damage - self.__de
        if real_damage <= 0:
            real_damage = 1
        print(f"{real_damage} = {damage} - {self.__de}")
        return real_damage

    def is_check_hp(self) -> bool:
        return (self.__hp > 0)