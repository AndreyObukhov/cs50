from seasons import calculate
import pytest


def main():
    test_calculate()

def test_calculate():
    with pytest.raises(SystemExit) as sample:
        calculate("January 1, 1999")
        assert sample.type == SystemExit
        calculate("1999-01-32")
        assert sample.type == SystemExit
        calculate("1999-12-01")
        assert sample.type == SystemExit
        calculate("1999/12/01")
        assert sample.type == SystemExit


if __name__ == "__main__":
    main()
