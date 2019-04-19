from Character import Character
import random

class Enemy(Character):
    ENEMY_LV_MIN = 1
    ENEMY_LV_MAX = 10
    ENEMY_HP_MIN = 100
    ENEMY_HP_MAX = 150
    ENEMY_AT_MIN = 1
    ENEMY_AT_MAX = 10
    ENEMY_DE_MIN = 1
    ENEMY_DE_MAX = 10
    
    def __init__(self, name:str) -> None:
        super().__init__(name)
        self.set_status()
    
    def set_status(self) -> None:
        lv = random.randint(self.ENEMY_LV_MIN, self.ENEMY_LV_MAX)
        hp = random.randint(self.ENEMY_HP_MIN, self.ENEMY_HP_MAX) * lv
        at = random.randint(self.ENEMY_AT_MIN, self.ENEMY_AT_MAX) * lv
        de = random.randint(self.ENEMY_DE_MIN, self.ENEMY_DE_MAX) * lv
        super().set_status(lv, hp, at, de)

    def self_introduction(self) -> None:
        print("----------------------------------------------")
        print(f"あ！ {self.get_name()} が 飛び出してきた！")
