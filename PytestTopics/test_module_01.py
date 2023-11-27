import pytest


@pytest.mark.sanity
def test_a1():
    assert 10 == 10


def test_a2():
    assert 10 != 20


def test_a3():
    assert 5 + 5 == 10
