import pytest

from run import subtraction

def test_subtraction_positive():
    assert subtraction(5, 2) == 3
