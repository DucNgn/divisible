from divisible import __version__
from divisible.main import is_divisible, is_even, is_odd

import pytest


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.parametrize(
    "numerator,denominator,expected",
    [(10, 2, True), (10, 3, False), (9, 7, False), (9, 10, False), (10, 0, False)],
)
def test_is_divisible(numerator, denominator, expected):
    assert is_divisible(numerator, denominator) == expected


@pytest.mark.parametrize(
    "number,expected",
    [(10, True), (3, False), (-2, True), (0, True)]
)
def test_is_even(number: int, expected: bool):
    assert is_even(number) == expected

@pytest.mark.parametrize(
    "number,expected",
    [(10, False), (3, True), (-5, True), (0, False)]
)
def test_is_odd(number: int, expected: bool):
    assert is_odd(number) == expected