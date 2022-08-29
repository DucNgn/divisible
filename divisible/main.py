def is_divisible(number: int, division: int) -> bool:
    if division == 0:
        return False
    else:
        return number % division == 0


def is_even(number: int) -> bool:
    return number % 2 == 0


def is_odd(number: int) -> bool:
    return not is_even(number)
