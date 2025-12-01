from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError) as sample:
        jar.deposit(1)
        assert sample.type == ValueError


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.withdraw(3)
    assert str(jar) == "🍪🍪"
    with pytest.raises(ValueError) as sample:
        jar.withdraw(3)
        assert sample.type == ValueError
