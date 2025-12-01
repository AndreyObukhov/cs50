"""
Program:

- Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and n, inclusive, using the random module.
- Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
- If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
- If the guess is larger than that integer, the program should output Too large! and prompt the user again.
- If the guess is the same as that integer, the program should output Just right! and exit.
"""

from random import randrange


def prompt(text):
    while True:
        try:
            number = int(input(text))
            if 0 < number:
                return number
        except (TypeError, ValueError):
            pass


unknown = randrange(1, prompt("Level: ") + 1)

guess = 0
while guess != unknown:
    guess = prompt("Guess: ")
    if guess > unknown:
        print("Too large!")
    elif guess < unknown:
        print("Too small!")
    else:
        print("Just right!")
