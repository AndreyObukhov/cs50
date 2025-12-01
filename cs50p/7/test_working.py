from working import convert


def main():
    test_AMPM()
    test_24()
    test_errors()


def test_AMPM():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    try:
        assert convert("9:00 AM to 5:60 PM") == "09:00 to 18:00"
    except ValueError:
        assert True


def test_24():
    try:
        assert convert("09:00 to 17:00") == "09:00 to 17:00"
    except ValueError:
        assert True


def test_errors():
    try:
        assert convert("cat") == "cat"
    except ValueError:
        assert True


if __name__ == "__main__":
    main()
