from Character import Character

class Brave(Character):
    DEFAULT_HP = 200
    DEFAULT_AT = 50
    DEFAULT_DE = 30
    DEFAULT_LV = 10

    def __init__(self, name:str) -> None:
        super().__init__(name)
        self.set_status()

    def set_status(self) -> None:
        lv = self.DEFAULT_LV
        hp = self.DEFAULT_HP
        at = self.DEFAULT_AT
        de = self.DEFAULT_DE
        super().set_status(lv, hp, at, de)

    def self_introduction(self) ->None:
        print("----------------------------------------------")
        print(f"私の名前は勇者{self.get_name()}です。")
