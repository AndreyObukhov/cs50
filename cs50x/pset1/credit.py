from cs50 import get_int
from sys import exit
from math import trunc

# Makes variables for input and its copy.
CardNumber = get_int("Number: ")
CardNumberCopy = CardNumber

# If input has more than 16 digits, card is invalid.
if len(str(CardNumber)) > 16:
    print("INVALID")
    exit(1)

# Calculates sum using Luhn’s algorithm.
sum = 0
for i in range(1, 17):
    if i % 2 == 1:
        sum += CardNumberCopy % 10

    else:
        digit = (CardNumberCopy % 10) * 2
        sum += (digit % 10) + trunc(digit / 10)

    CardNumberCopy = trunc(CardNumberCopy / 10)

# Checks conditions and prints result.
if sum % 10 != 0:
    print("INVALID")
    exit(1)
if trunc(CardNumber / (10 ** 15)) == 4:
    print("VISA")
    exit(0)
if trunc(CardNumber / (10 ** 12)) == 4:
    print("VISA")
    exit(0)
if trunc(CardNumber / (10 ** 14)) in range(51, 56):
    print("MASTERCARD")
    exit(0)
if trunc(CardNumber / (10 ** 13)) in [34, 37]:
    print("AMEX")
    exit(0)
print("INVALID")
exit(1)