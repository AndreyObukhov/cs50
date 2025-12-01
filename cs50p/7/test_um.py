from um import count


def main():
    test_zero()
    test_inside()
    test_main()


def test_zero():
    assert count("cat") == 0
    assert count("") == 0
    assert count("CS50") == 0


def test_inside():
    assert count("yummi") == 0
    assert count("umumUM") == 0


def test_main():
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    assert count("um...") == 1
    assert count("Um...") == 1


if __name__ == "__main__":
    main()
