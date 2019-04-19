import random

class Enemy():
    CRITICAL_ATTACK_RATE = 2.0
    CRITICAL_RATE = 0.25
    ENEMY_NAMES = [
        "スライム",
        "ゴブリン",
        "ドラゴン"
    ]
    ENEMY_LV_MIN = 1
    ENEMY_LV_MAX = 10
    ENEMY_HP_MIN = 100
    ENEMY_HP_MAX = 150
    ENEMY_AT_MIN = 1
    ENEMY_AT_MAX = 10
    ENEMY_DE_MIN = 1
    ENEMY_DE_MAX = 10
    
    def __init__(self) -> None:
        self.__name = self.set_name()
        self.__lv = random.randint(self.ENEMY_LV_MIN, self.ENEMY_LV_MAX)
        self.__hp = random.randint(self.ENEMY_HP_MIN, self.ENEMY_HP_MAX) * self.__lv
        self.__at = random.randint(self.ENEMY_AT_MIN, self.ENEMY_AT_MAX) * self.__lv
        self.__de = random.randint(self.ENEMY_DE_MIN, self.ENEMY_DE_MAX) * self.__lv

    def self_introduction(self) -> None:
        print("----------------------------------------------")
        print(f"あ！ {self.__name} が 飛び出してきた！")
    
    def self_status(self) -> None:
        print("----------------------------------------------")
        print(f"名前：{self.__name}")
        print(f"Lv.{self.__lv}")
        print(f"HP:{self.__hp}")
        print(f"AT:{self.__at}")
        print(f"De:{self.__de}")

    def set_name(self) -> str:
        ram = random.randint(0, 2)
        return self.ENEMY_NAMES[ram]

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
        print(f"{self.__name} の HP:{before_hp} が {self.__hp} になった！")
    
    def real_damege(self, damage) -> int:
        real_damage = damage - self.__de
        if real_damage <= 0:
            real_damage = 1
        print(f"{real_damage} = {damage} - {self.__de}")
        return real_damage

    def is_check_hp(self) -> bool:
        return (self.__hp > 0)


