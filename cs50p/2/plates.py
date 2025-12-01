"""
Program prompts the user for a vanity plate and then output Valid if
meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase.

Among the requirements are:

- All vanity plates must start with at least two letters.
- Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
- Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would
be an acceptable.
- The first number used cannot be a ‘0’.
- No periods, spaces, or punctuation marks are allowed.
"""
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():
        return False
    if not 1 < len(s) < 7:
        return False
    for i in range(1, len(s)):
        if not s[i].isdigit() and not s[i].isalpha():
            return False
        if s[i-1].isdigit() and not s[i].isdigit():
            return False
        if not s[i-1].isdigit() and s[i] == '0':
            return False
    return True

main()
