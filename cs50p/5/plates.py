"""
Reimplementation of the Vanity Plates from Problem Set 2,
where is_valid still expects a str as input and returns True if that str meets all requirements and
False if it does not, but main is only called if the value of __name__ is "__main__"
"""


def main():
    if is_valid(input("Plate: ")):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():
        return False
    elif not 1 < len(s) < 7:
        return False
    for i in range(1, len(s)):
        if not s[i].isdigit() and not s[i].isalpha():
            return False
        if s[i - 1].isdigit() and not s[i].isdigit():
            return False
        if not s[i - 1].isdigit() and s[i] == "0":
            return False
    return True


if __name__ == "__main__":
    main()
