"""
Reimplementation of the Home Federal Savings Bank from Problem Set 1,
value expects a str as input and returns an int, namely 0 if that str
starts with “hello”, 20 if that str starts with an “h” (but not “hello”),
or 100 otherwise, treating the str case-insensitively.
Assume that the string passed to the value function will not contain any leading spaces.
Only main should call print.
"""


def main():
    print(value(input("Greeting: ")))


def value(greeting):
    greeting = greeting.lower().lstrip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
