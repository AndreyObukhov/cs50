import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    """
    Expects an IPv4 address as input as a str and then returns True or False,
    respectively, if that input is a valid IPv4 address or not.
    """
    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        numbers = ip.split(".")
        for number in numbers:
            if not 0 <= int(number) <= 255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
