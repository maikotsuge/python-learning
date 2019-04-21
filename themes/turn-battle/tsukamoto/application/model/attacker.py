from model.ability import Ability
from util.random_util import hit_percentage


class Attacker:
    def __init__(self, ability: Ability) -> None:
        self.ability = ability
        self.before_hp = ability.hp
        self.damage = 0
        self._is_critical = False

    def __calc_damage(self, enemy_ability: Ability) ->int:
        # 自分の攻撃力 - 敵の防御力のダメージ！
        # 最低でも1はダメージを与えられる
        _damage = max(self.ability.attack - enemy_ability.defense, 1)

        # クリティカルの時はダメージを2倍にする
        return _damage * 2 if self._is_critical else _damage

    def __is_critical_hit(self) ->bool:
        # 25%の確率でクリティカルになる
        return hit_percentage(25)

    def get_critical_effect(self) -> str:
        return "会心の一撃！" if self._is_critical else ""

    def do_attack(self, enemy_ability: Ability) -> None:
        # クリティカル判定
        self._is_critical = self.__is_critical_hit()

        # ダメージ計算
        self.damage = self.__calc_damage(enemy_ability)

        # HP更新
        self.before_hp = enemy_ability.hp
        enemy_ability.hp = max(enemy_ability.hp - self.damage, 0)
