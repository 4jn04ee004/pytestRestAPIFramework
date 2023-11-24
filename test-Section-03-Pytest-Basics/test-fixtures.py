import pytest


@pytest.fixture()
def set_up():
    print("\nIn Fixture set up.\n")
    city = ['New york', 'London', 'Singapore']
    return city


def test_get_item(set_up):
    for city in set_up:
        print()
        print(city)
    assert set_up[0] == 'New york'
