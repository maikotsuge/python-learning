from pandas import read_csv
from abc import ABCMeta, abstractmethod
from random import randint

class Charactor():
    def __init__(self, name: str, hp: int, lv:int, at: int, de: int):
        self.name = name
        self.lv = lv
        self.hp = hp
        self.at = at
        self.de = de

class CharactorType(metaclass=ABCMeta):
    @abstractmethod
    def adjust_parameter(self, charactor: Charactor):
        pass

class Player(CharactorType):
    def adjust_parameter(self, charactor: Charactor):
        return charactor

class Enemy(CharactorType):
    def adjust_parameter(self, charactor: Charactor):
        charactor.hp = (charactor.hp + randint(0, 50)) * charactor.lv
        charactor.at = (charactor.at + randint(0, 9)) * charactor.lv
        charactor.de = (charactor.de + randint(0, 9)) * charactor.lv
        return charactor

class CharactorLoader():
    def __init__(self, file_path: str):
        self.charactors = read_csv(filepath_or_buffer = file_path, sep = "\t", index_col=0)

    def get_charactor_by_id(self, id: int, lv: int, charactor_type: CharactorType):
        return charactor_type.adjust_parameter(
            Charactor(
                name = self.charactors.at[id, "name"],
                lv = lv,
                hp = self.charactors.at[id, "hp"],
                at = self.charactors.at[id, "at"],
                de = self.charactors.at[id, "de"]
                )
        )

    def get_charactor_ids(self):
        return list(self.charactors.index.values)
