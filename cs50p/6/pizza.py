"""
Program expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format,
and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.
Format the table using the library’s grid format. If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .csv, or if the specified file does not exist,
the program should instead exit via sys.exit.
"""

import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith("csv"):
    sys.exit("not CSV file")
menu = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")
if len(menu) == 0:
    sys.exit("Empty CSV File")
headers = list(menu[0])
table = []
for row in menu:
    table.append([row[headers[0]],row[headers[1]],row[headers[2]]])

print(tabulate(table, headers, tablefmt="grid"))
