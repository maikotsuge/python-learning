from character import Character
import random

class Monster(Character):
    def __init__(self):
        super().__init__()
        self._lv_coefficient()

    def init_param(self):
        self.name = random.choice(self.get_name())
        self.lv = random.randint(1, 10)
        self.hp = random.randint(100, 150)
        self.at = random.randint(1, 10)
        self.de = random.randint(1, 10)

    def get_name(self):
        return ["スライム", "ゴブリン", "キメラ"]

    def _lv_coefficient(self):
        "モンスターはレベルで係数をかけるよ"
        self.hp *= self.lv
        self.at *= self.lv
        self.de *= self.lv