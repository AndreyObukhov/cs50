"""
Reimplementation of Setting up my twttr from Problem Set 2,
wherein shorten expects a str as input and returns
that same str but with all vowels omitted,
whether inputted in uppercase or lowercase.
"""


def main():
    word = shorten(input("Input: "))
    print(word)


def shorten(word):
    vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    output = ""
    for character in word:
        if character not in vowel:
            output += character
    return output


if __name__ == "__main__":
    main()
