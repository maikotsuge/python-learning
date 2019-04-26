from abc import ABCMeta, abstractmethod
from subwindow import (
    SubWindow,
    WindowStyle,
    EncountMessage,
    EnemyStatus,
    PlayerStatus,
    Top,
    NoTop,
    Turn,
    DamageMessage,
    Win,
    Lose,
    Draw,
    NormalEnd,
    BadEnd,
    TrueEnd,
)
from battlemanager import BattleManager


class Phase(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, subwindow: SubWindow, battlemanager: BattleManager):
        pass


class Encount(Phase):
    def draw(self, subwindow: SubWindow, battlemanager: BattleManager):
        subwindow.draw(body=EncountMessage(), pos=Top())
        subwindow.draw(body=EnemyStatus(), pos=NoTop())
        subwindow.draw(body=PlayerStatus(), pos=NoTop())


class Battle(Phase):
    def draw(self, subwindow: SubWindow, battlemanager: BattleManager):
        subwindow.draw(body=Turn(), pos=NoTop())
        subwindow.draw(body=DamageMessage(), pos=NoTop())


class Result(Phase):
    def draw(self, subwindow: SubWindow, battlemanager: BattleManager):
        player = battlemanager.get_player()
        enemy = battlemanager.get_enemy()
        if player.hp <= 0 and enemy.hp <= 0:
            subwindow.draw(body=Draw(), pos=NoTop())
            subwindow.draw(body=NormalEnd(), pos=NoTop())
        elif player.hp <= 0:
            subwindow.draw(body=Lose(), pos=NoTop())
            subwindow.draw(body=BadEnd(), pos=NoTop())
        else:
            subwindow.draw(body=Win(), pos=NoTop())
            subwindow.draw(body=TrueEnd(), pos=NoTop())


class Window:
    def __init__(self, style: WindowStyle, battlemanager: BattleManager):
        self.subwindow = SubWindow(style=style, battlemanager=battlemanager)
        self.battlemanager = battlemanager

    def draw(self, phase: Phase):
        phase.draw(subwindow=self.subwindow, battlemanager=self.battlemanager)
