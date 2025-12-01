import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
try:
    (input_name, input_format) = os.path.splitext(sys.argv[1])
    (output_name, output_format) = os.path.splitext(sys.argv[2])
except (TypeError, ValueError):
    sys.exit("Invalid input")
formats = (".jpg", ".png", ".jpeg")
if not input_format.lower().endswith(formats) and not output_format.lower().endswith(formats):
    sys.exit("Invalid input")
if input_format.lower() != output_format.lower():
    sys.exit("Input and output have different extensions")
try:
    input = Image.open(sys.argv[1])
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("Input does not exist")
# output = Image.open("after.jpg", mode="w")
output = ImageOps.fit(input, shirt.size)
output.paste(shirt, shirt)
output.save(sys.argv[2])
