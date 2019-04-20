from random import randint


MAX_PERCENT = 100

def hit_percentage(value: int) -> bool:
    assert(0 <= value <= MAX_PERCENT)
    if value == 0:
        return False
    elif value == MAX_PERCENT:
        return True
    return randint(1, MAX_PERCENT) <= value
