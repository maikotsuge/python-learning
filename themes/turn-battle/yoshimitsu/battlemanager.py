from charactor import Charactor
from numpy.random import choice
from abc import ABCMeta, abstractmethod


class Behave(metaclass=ABCMeta):
    @abstractmethod
    def calcurate_damage(self, attacker: Charactor, defencer: Charactor):
        pass

class Attack(Behave):
    def calcurate_damage(self, attacker: Charactor, defencer: Charactor):
        critical_rate = 0.25
        weight = [1-critical_rate, critical_rate]
        return max([0, attacker.at * choice([1, 2], p=weight) - defencer.de])


class BattleManager():
    def __init__(self, enemy: Charactor, player: Charactor):
        self.turn = 0
        self.enemy = enemy
        self.player = player
        self.enemy_damage = 0
        self.player_damage = 0

    def get_turn(self):
        return self.turn

    def get_player(self):
        return self.player

    def get_enemy(self):
        return self.enemy

    def get_player_damage(self):
        return self.player_damage

    def get_enemy_damage(self):
        return self.enemy_damage

    def update(self):
        behave = Attack()
        self.player_damage = behave.calcurate_damage(self.enemy, self.player)
        self.player.hp = max([0, self.player.hp - self.player_damage])
        self.enemy_damage = behave.calcurate_damage(self.player, self.enemy)
        self.enemy.hp = max([0, self.enemy.hp - self.enemy_damage])
        self.turn = self.turn + 1
