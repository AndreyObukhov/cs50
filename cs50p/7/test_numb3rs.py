from numb3rs import validate


def main():
    test_numbers()
    test_letters()


def test_numbers():
    assert validate("1.1.1.1")
    assert not validate("1.1.1.1.1")
    assert validate("1.11.111.2")
    assert validate("255.155.15.75")
    assert not validate("255.255.255.256")
    assert not validate("-1.1.1.1")


def test_letters():
    assert not validate("cat")
    assert not validate(".c.a.t")
    assert not validate("1.1.1.x")
    assert not validate("...")


if __name__ == "__main__":
    main()
