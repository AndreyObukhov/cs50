"""
Program:

- Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
- Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is
a non-negative integer with n digits. No need to support operations other than addition (+).
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
If the user has still not answered correctly after three tries, the program should output the correct answer.
- The program should ultimately output the user’s score: the number of correct answers out of 10.
"""

from random import randrange


def main():
    level = get_level()
    score = 0
    for i in range(0, 10):
        X = generate_integer(level)
        Y = generate_integer(level)
        Z = X + Y
        for j in range(0, 3):
            print(f"{X} + {Y} = ", end="")
            if get_answer() == Z:
                score += 1
                break
            else:
                print("EEE")
            if j == 2:
                print(f"{X} + {Y} = {Z}")

    print(f"Score: {score}")


def get_answer():
    try:
        Input = int(input())
        return Input
    except ValueError:
        return None


def get_level():
    while True:
        try:
            number = int(input("Level: "))
            if 1 <= number <= 3:
                return number
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return randrange(0, 10)
    elif level == 2:
        return randrange(10, 100)
    elif level == 3:
        return randrange(100, 1000)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
