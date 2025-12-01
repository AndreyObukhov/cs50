"""
Program:
- expects the user to provide two command-line arguments:
  . the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
  . the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
- converts that input to that output, splitting each name into a first name and last name.
Assume that each student will have both a first name and last name.
- If the user does not provide exactly two command-line arguments, or if the first cannot be read,
the program should exit via sys.exit with an error message.
"""

import sys
import csv

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
students = []
try:
    with open(sys.argv[1], newline='') as input:
        reader = csv.DictReader(input, delimiter=',')
        for row in reader:
            student_name = row["name"].split(", ")
            students.append(
                {
                    "last": student_name[0],
                    "first": student_name[1],
                    "house": row["house"],
                }
            )
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w", newline='') as output:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=',')
    writer.writeheader()
    for student in students:
        writer.writerow(student)
