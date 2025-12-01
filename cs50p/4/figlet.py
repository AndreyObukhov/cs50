"""
Program expects zero or two command-line arguments:
- Zero if the user would like to output text in a random font.
- Two if the user would like to output text in a specific font, in which case the first
of the two should be -f or --font, and the second of the two should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.
- If the user provides two command-line arguments and the first is not -f or --font or
the second is not the name of a font, the program should exit via sys.exit with an error message.
"""

from pyfiglet import Figlet
from random import choice
import sys

if len(sys.argv) not in {1, 3}:
    sys.exit("Mistake with arguments")

figlet = Figlet()

if len(sys.argv) == 1:
    f = choice(figlet.getFonts())
    figlet.setFont(font=f)
elif sys.argv[1] not in {"-f", "--font"}:
    sys.exit("Mistake with arguments")
else:
    figlet.setFont(font=sys.argv[2])
text = input("Input: ")
print("Output ")
print(figlet.renderText(text))
