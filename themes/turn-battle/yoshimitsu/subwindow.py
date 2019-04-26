from abc import ABCMeta, abstractmethod
from battlemanager import BattleManager

window_style_simple_line = "----------------------------------------------"

window_message = {
    "encount": "あ! {} が 飛び出してきた！",
    "turn": "TRUN {}",
    "damage": "{} が {} に攻撃した！ {} のダメージ！",
    "reduce_hp": "{} の HP:{} が {} になった！",
    "new_line": "\n",
    "win": "{}の勝利",
    "draw": "相打ち…",
    "true_end": "今日も世界に平和が訪れた。",
    "bad_end": "おお 勇者！ しんでしまうとは なにごとだ！",
    "normal_end": "そういうこともあるよ",
    "status": "{}\nLv:{}\nHP:{}\nAT:{}\nDE:{}",
}


class SubWindowPos(metaclass=ABCMeta):
    @abstractmethod
    def draw_frame(self, frame: str):
        pass


class Top(SubWindowPos):
    def draw_frame(self, frame: str):
        print(frame)


class NoTop(SubWindowPos):
    def draw_frame(self, frame: str):
        pass


class WindowStyle(metaclass=ABCMeta):
    @abstractmethod
    def draw_frame_top(self, pos: SubWindowPos):
        pass

    @abstractmethod
    def draw_frame_bottom(self):
        pass


class SimpleLine(WindowStyle):
    def draw_frame_top(self, pos: SubWindowPos):
        pos.draw_frame(window_style_simple_line)

    def draw_frame_bottom(self):
        print(window_style_simple_line)


class SubWindowBody(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, battlemanager: BattleManager):
        pass


class EncountMessage(SubWindowBody):
    def draw(self, battlemanager: BattleManager):
        enemy = battlemanager.get_enemy()
        print(window_message["encount"].format(enemy.name))


class Turn(SubWindowBody):
    def draw(self, battlemanager: BattleManager):
        turn = battlemanager.get_turn()
        print(window_message["turn"].format(turn))


class DamageMessage(SubWindowBody):
    def draw(self, battlemanager: BattleManager):
        player = battlemanager.get_player()
        player_damage = battlemanager.get_player_damage()
        enemy = battlemanager.get_enemy()
        enemy_damage = battlemanager.get_enemy_damage()

        print(window_message["damage"].format(player.name, enemy.name, enemy_damage))
        print(
            window_message["reduce_hp"].format(
                enemy.name, enemy.hp + enemy_damage, enemy.hp
            )
        )

        print(window_message["new_line"])

        print(window_message["damage"].format(enemy.name, player.name, player_damage))
        print(
            window_message["reduce_hp"].format(
                player.name, player.hp + player_damage, player.hp
            )
        )


# TODO: どこにも使ってない。うまくしばれてない。
class ResultMessage(SubWindowBody):
    @abstractmethod
    def draw(self, battlemanager: BattleManager):
        pass


class Win(ResultMessage):
    def draw(self, battlemanager: BattleManager):
        player = battlemanager.get_player()
        print(window_message["win"].format(player.name))


class Lose(ResultMessage):
    def draw(self, battlemanager: BattleManager):
        enemy = battlemanager.get_enemy()
        print(window_message["win"].format(enemy.name))


class Draw(ResultMessage):
    def draw(self, battlemanager: BattleManager):
        print(window_message["draw"])


class EnemyStatus(SubWindowBody):
    def draw(self, battlemanager: BattleManager):
        enemy = battlemanager.get_enemy()
        print(
            window_message["status"].format(
                enemy.name, enemy.lv, enemy.hp, enemy.at, enemy.de
            )
        )


class PlayerStatus(SubWindowBody):
    def draw(self, battlemanager: BattleManager):
        player = battlemanager.get_player()
        print(
            window_message["status"].format(
                player.name, player.lv, player.hp, player.at, player.de
            )
        )


class EndMessage(SubWindowBody):
    @abstractmethod
    def draw(self, battlemanager: BattleManager):
        pass


class TrueEnd(SubWindowBody):
    def draw(self, battlemanager: BattleManager):
        print(window_message["true_end"])


class BadEnd(SubWindowBody):
    def draw(self, battlemanager: BattleManager):
        print(window_message["bad_end"])


class NormalEnd(SubWindowBody):
    def draw(self, battlemanager: BattleManager):
        print(window_message["normal_end"])


class SubWindow:
    def __init__(self, style: WindowStyle, battlemanager: BattleManager):
        self.style = style
        self.battlemanager = battlemanager

    def draw(self, body: SubWindowBody, pos: SubWindowPos):
        self.style.draw_frame_top(pos=pos)
        body.draw(battlemanager=self.battlemanager)
        self.style.draw_frame_bottom()
