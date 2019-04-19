from hero import Hero
from monster import Monster
from character import Character

class TurnBattle:
    def __init__(self):
        hero = Hero()
        monster = Monster()
        self.print_parameter(monster)
        self.print_parameter(hero)

    def print_parameter(self, character: Character):
        print(f'''{character.name}
Lv:{character.lv}
HP:{character.hp}
AT:{character.at}
DE:{character.de}''')

if __name__ == '__main__':
    turn = TurnBattle()