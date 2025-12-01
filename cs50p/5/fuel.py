"""
Reimplementation of th Fuel Gauge from Problem Set 3, restructuring your code per the below:

 - convert expects a str in X/Y format as input, wherein each of X and Y is an integer,
 and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
 If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
 If Y is 0, then convert should raise a ZeroDivisionError.
- gauge expects an int and returns a str that is:
  - "E" if that int is less than or equal to 1,
  - "F" if that int is greater than or equal to 99,
  -"Z%" otherwise, wherein Z is that same int.
"""


def main():
    while True:
        try:
            print(gauge(convert(input("Fraction: "))))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    (X, _, Y) = fraction.partition("/")
    try:
        f = int(round(int(X) / int(Y) * 100, 0))
        if f > 100:
            raise ValueError
        return f
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(percentage):
    if percentage in [99, 100]:
        return "F"
    elif percentage in [1, 0]:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
