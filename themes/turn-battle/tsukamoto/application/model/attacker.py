from model.ability import Ability
from util.random_util import is_hit_percentage


class Attacker:
    # クリティカル率[%]
    CRITICAL_RATE: int = 25
    # クリティカル倍数[倍]
    CRITICAL_DAMAGE: int = 2
    # クリティカル演出
    CRITICAL_EFFECT: str = "会心の一撃！"

    def __init__(self, ability: Ability) -> None:
        self.ability = ability
        self.damage = 0
        self._is_critical = False

    def __calc_damage(self, enemy_ability: Ability) -> int:
        # 自分の攻撃力 - 敵の防御力のダメージ！
        _damage = self.ability.attack - enemy_ability.defense

        # 最低でも1はダメージを与えられる
        _damage = max(_damage, 1)

        # クリティカルの時はダメージをN倍にする
        return _damage * self.CRITICAL_DAMAGE if self._is_critical else _damage

    def __is_critical_hit(self) -> bool:
        # N%の確率でクリティカルになる
        return is_hit_percentage(self.CRITICAL_RATE)

    def get_critical_effect(self) -> str:
        return self.CRITICAL_EFFECT if self._is_critical else ""

    def do_attack(self, enemy_ability: Ability) -> None:
        # クリティカル判定
        self._is_critical = self.__is_critical_hit()

        # ダメージ計算
        self.damage = self.__calc_damage(enemy_ability)

        # HP更新
        enemy_ability.hp.damage(self.damage)
