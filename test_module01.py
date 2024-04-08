import time
import pytest

@pytest.mark.sanity
def test_add():
    assert 5 + 5 == 10

@pytest.mark.vanity
def test_subs():
    assert 21 - 10 == 11

@pytest.mark.panity
def test_mul():

    assert 5 * 5 == 25


def test_div():
    assert 5 / 5 == 1



def test_add11():
    assert 5 + 5 == 10


def test_subs22():
    assert 21 - 10 == 11


def test_mul33():
    assert 5 * 5 == 25


def test_div44():
    x = [a for a in range(100000000)]
    assert 5 / 5 == 1
