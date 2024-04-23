from cs50 import get_string

Input = get_string("Text: ")
letters = 0
words = 0
sentences = 0

# We read each character one by one and determine
# if it is a letter, end of a word, end of a sentence or non.
for char in Input:
    if char.isalpha():
        letters += 1
    elif char == ' ':
        words += 1
    elif char == '.' or char == '!' or char == '?':
        sentences += 1

# We must add one more word to a counter.
# It was not considered by a program.
words += 1

# Now we are counting values L, S and final value of index.
L = letters * 100 / words
S = sentences * 100 / words
index = round(0.0588 * L - 0.296 * S - 15.8)

# Printing results.
if index < 1:
    print("Before Grade 1")
elif index > 15:
    print("Grade 16+")
else:
    print(f"Grade {index}")
    print(words)