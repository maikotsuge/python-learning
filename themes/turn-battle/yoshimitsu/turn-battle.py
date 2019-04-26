from random import randint, choice
from window import Window, Encount, Battle, Result
from subwindow import SimpleLine
from charactor import CharactorLoader, Player, Enemy
from battlemanager import BattleManager

enemies = CharactorLoader("m_enemy_charactor.tsv")
enemy = enemies.get_charactor_by_id(
    id=choice(enemies.get_charactor_ids()), lv=randint(1, 10), charactor_type=Enemy()
)

players = CharactorLoader("m_player_charactor.tsv")
player = players.get_charactor_by_id(id=0, lv=10, charactor_type=Player())

battlemanager = BattleManager(enemy=enemy, player=player)

window = Window(style=SimpleLine(), battlemanager=battlemanager)
window.draw(phase=Encount())

while player.hp > 0 and enemy.hp > 0:
    battlemanager.update()
    window.draw(phase=Battle())

window.draw(phase=Result())
