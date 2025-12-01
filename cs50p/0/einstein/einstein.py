"""
Program prompts the user for mass as an int (in kg) and outputs the equivalent number of Joules as an int.
Assume that the user will input an int.
Uses the formula E = m * c^2.
"""
m = int(input("m: "))
E = m * 9 * pow(10, 16)
print(f"E: {E}")