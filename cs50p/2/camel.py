"""
Program prompts the user for the name of a variable in camelCase and
outputs the corresponding name in snake_case. Assume that the user’s
input will indeed be in camelCase.
"""
name = input('camelCase: ')
print('snake_case: ', end="")
for character in name:
    if character.isupper():
        print(f'_{character.lower()}', end="")
    else:
        print(character, end="")
print()
