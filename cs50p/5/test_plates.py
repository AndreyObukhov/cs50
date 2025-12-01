"""
Implement four or more functions that collectively test your implementation of
is_valid thoroughly, each of whose names should begin with test_
"""

from plates import is_valid


def main():
    test_length()
    test_numbers()
    test_punctuation()
    test_zero()


def test_length():
    assert not is_valid("C")
    assert is_valid("CS1111")
    assert not is_valid("CS11112")


def test_numbers():
    assert is_valid("CS50")
    assert is_valid("CS5")
    assert not is_valid("5CS")
    assert not is_valid("CS50P")
    assert not is_valid("C11111")
    assert not is_valid("CS50X5")


def test_punctuation():
    assert not is_valid("CS.")
    assert not is_valid(".CS")
    assert not is_valid("C.S")
    assert not is_valid("/.?")


def test_zero():
    assert not is_valid("CS05")
    assert is_valid("CS505")
    assert is_valid("CS1000")


if __name__ == "__main__":
    main()
