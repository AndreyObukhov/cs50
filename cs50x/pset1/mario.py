from cs50 import get_int

# Prints output piramid.


def Output(Input):
    for i in range(1, Input + 1):
        for j in range(Input - i, 0, -1):
            print(" ", end="")
        for j in range(1, i + 1):
            print("#", end="")
        print("  ", end="")
        for j in range(1, i + 1):
            print("#", end="")
        print("")

# Main function.


def main():
    Input = int(0)
    while (Input < 1 or Input > 8):
        Input = get_int("Height: ")
    Output(Input)


if __name__ == "__main__":
    main()