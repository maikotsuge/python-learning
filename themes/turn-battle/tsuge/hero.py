from character import Character
import random

class Hero(Character):
    def __init__(self):
        super().__init__()
        pass

    def init_param(self):
        # TODO
        self.name = random.choice(self.get_name())
        self.lv = random.randint(10, 10)
        self.hp = random.randint(200, 200)
        self.at = random.randint(30, 30)
        self.de = random.randint(10, 10)

    def get_name(self):
        return ["勇者"]
