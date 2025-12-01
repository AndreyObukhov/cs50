import re


def main():
    print(count(input("Text: ").strip()))


def count(s):
    s = re.split(r"\bum\b", s, flags=re.IGNORECASE)
    return len(s) - 1


if __name__ == "__main__":
    main()
