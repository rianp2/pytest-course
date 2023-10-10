import pytest


def test_accumulator_init(accum):
    assert accum.count == 0


def test_accumulator_add_one(accum):
    """Check init count state"""
    accum.add()
    assert accum.count == 1


def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3



def test_accumulator_add_twice23(accum):
    accum.add()
    accum.add()
    assert accum.count == 2


def test_accumilator_cannot_set_count_directly734(accum):
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter"):
        accum.count = 10
