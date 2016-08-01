#ZZimport intro_to_sprinting.x
import pytest
from ..x import func


def test_fail():
    assert func(3) == 5

def test_pass():
    assert func(41) == 42

