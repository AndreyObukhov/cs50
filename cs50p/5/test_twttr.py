"""
Implement one or more functions that collectively test your implementation of
shorten thoroughly, each of whose names should begin with test_
"""
from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("CAT") == "CT"
    assert shorten("qwerty123") == "qwrty123"
    assert shorten("") == ""
    assert shorten("./?:&") == "./?:&"

if __name__ == "__main__":
    main()
