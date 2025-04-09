import pytest
from fonctionmath import add,divide
from projectaircraft.models.flight import Flight


@pytest.fixture
def flight():
    return Flight()
def test_one(flight):
    assert add(2, 3) == 5
    assert flight.name == "XX"

def test_two(flight):
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 45

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

# IDEMPOTENT