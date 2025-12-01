def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
    Accept a str as input (formatted as $##.##, wherein each # is a decimal digit),
    removes the leading $, and returns the amount as a float.
    """
    d = float(d.removeprefix('$'))
    return(d)


def percent_to_float(p):
    """
    Accepts a str as input (formatted as ##%, wherein each # is a decimal digit),
    removes the trailing %, and returns the percentage as a float.
    """
    p = p.removesuffix('%')
    p = float(p) * 0.01
    return(p)


main()