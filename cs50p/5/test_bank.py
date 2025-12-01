"""
Three or more functions that collectively test your implementation of
value thoroughly, each of whose names should begin with test_
"""

from bank import value


def main():
    test_0()
    test_20()
    test_100()


def test_0():
    assert value("hello") == 0
    assert value("hello//12.") == 0
    assert value("     hello") == 0
    assert value("HELLO    ") == 0


def test_20():
    assert value("h") == 20
    assert value("h//12.") == 20
    assert value("     h") == 20
    assert value("H    ") == 20


def test_100():
    assert value("cat") == 100
    assert value("//12.") == 100
    assert value("     ") == 100
    assert value("C    ") == 100


if __name__ == "__main__":
    main()
