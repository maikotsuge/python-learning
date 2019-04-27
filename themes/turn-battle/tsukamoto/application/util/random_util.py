from random import randint


MAX_PERCENT: int = 100


def is_hit_percentage(value: int) -> bool:
    assert(0 <= value <= MAX_PERCENT)
    if value == 0:
        return False
    elif value == MAX_PERCENT:
        return True
    return randint(1, MAX_PERCENT) <= value
