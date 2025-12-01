from datetime import date
import sys
import inflect


def main():
    """
    Program prompts the user for their date of birth in YYYY-MM-DD format and
    then prints how old they are in minutes, rounded to the nearest integer,
    using English words instead of numerals, just like the song from Rent, without any and
    between words. Since a user might not know the time at which they were born, assume,
    for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date.
    And assume that the current time is also midnight. In other words, even if the user
    runs the program at noon, assume that it’s actually midnight, on the same date.
    Use datetime.date.today to get today’s date.
    """
    birth_day = input("Date of Birth: ")
    print(calculate(birth_day).capitalize() + " minutes")


def calculate(str):
    """Converts birthday to lenght up till now"""
    try:
        birthday = date.fromisoformat(str)
    except ValueError:
        sys.exit("Invalid date")

    p = inflect.engine()

    return p.number_to_words((date.today() - birthday).days * 24 * 60, andword = "")


if __name__ == "__main__":
    main()
