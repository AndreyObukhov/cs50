"""
Program prompts the user for a str of text and then outputs that same text
but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""
vowel = {'a', 'e', 'i', 'o', 'u',
         'A', 'E', 'I', 'O', 'U'
         }

input = input('Input: ')
for character in input:
    if character not in vowel:
        print(character, end="")
print()
