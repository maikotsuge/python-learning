class Character:
    name: str = None
    lv: int = 0
    hp: int = 0
    at: int = 0
    de: int = 0

    def __init__(self) -> None:
        self.init_param()
        pass

    def init_param(self):
        pass
    
    def damage(self, hp: int):
        self.hp -= hp

    def get_param(self):
        pass

    def get_name(self):
        pass