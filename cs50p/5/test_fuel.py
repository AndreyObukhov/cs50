"""
Implement two or more functions that collectively test implementations of
convert and gauge thoroughly, each of whose names should begin with test_
"""

from fuel import convert, gauge


def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("3/4") == 75
    assert convert("0/1") == 0
    try:
        assert convert("1/0")
    except ZeroDivisionError:
        assert True
    try:
        assert convert("2/1")
    except ValueError:
        assert True
    try:
        assert convert("0.5/1")
    except ValueError:
        assert True
    try:
        assert convert("1/1.5")
    except ValueError:
        assert True
    try:
        assert convert("cat")
    except ValueError:
        assert True
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(75) == "75%"


if __name__ == "__main__":
    main()
