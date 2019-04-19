import Brave, Enemy
from enum import Enum

class BattleState(Enum):
    BEFORE＿BATTLE = 0
    BATTLE_START = 1
    IN_BATTLE = 2
    BATTLE_RESULT = 3

class TurnBattle():
    def __init__(self):
        self.turn_num = 0
        self.battle_state = BattleState.BEFORE＿BATTLE

    def turn_start(self, brave:Brave, enemy:Enemy)->None:
        self.battle_state = BattleState.BATTLE_START
        enemy.self_introduction()
        enemy.self_status()
        brave.self_status()

    def battle_turn(self, brave:Brave, enemy:Enemy)->None:
        self.battle_state = BattleState.IN_BATTLE
        while(self.battle_state is BattleState.IN_BATTLE):
            self.turn_num += 1
            print("----------------------------------------------")
            print(f"TURN {self.turn_num}")
            self.brave_turn(brave, enemy)
            self.enemy_turn(brave, enemy)
            enemy.self_status()
            brave.self_status()
            self.battle_state = self.battle_result_check(brave, enemy)

    
    def brave_turn(self, brave:Brave, enemy:Enemy)->None:
        brave.attack(enemy)
        return
    
    def enemy_turn(self, brave:Brave, enemy:Enemy)->None:
        enemy.attack(brave)
        return

    def battle_result_check(self, brave:Brave, enemy:Enemy)->BattleState:
        is_brave_arive = brave.is_check_hp()
        is_enemy_arive = enemy.is_check_hp()
        if not is_brave_arive and not is_enemy_arive:
            print("----------------------------------------------")
            print("相打ち…")
            print("----------------------------------------------")
            print("そういうこともあるよ")
            return BattleState.BATTLE_RESULT
        elif not is_brave_arive:
            print("----------------------------------------------")
            print(f"{enemy.get_name()}の勝利")
            print("----------------------------------------------")
            print("おお 勇者！ しんでしまうとは なにごとだ！")
            return BattleState.BATTLE_RESULT
        elif not is_enemy_arive:
            print("----------------------------------------------")
            print(f"勇者:{brave.get_name()}の勝利")
            print("----------------------------------------------")
            print("今日も世界に平和が訪れた")
            return BattleState.BATTLE_RESULT

        return BattleState.IN_BATTLE

turn_battle = TurnBattle()
 # 敵味方の生成・出力
print("勇者の名前を入力してね。")
name = input()
brave = Brave.Brave(name)
brave.self_introduction()
enemy = Enemy.Enemy()

# 開始
turn_battle.turn_start(brave, enemy)
turn_battle.battle_turn(brave, enemy)
print("----------------------------------------------")

