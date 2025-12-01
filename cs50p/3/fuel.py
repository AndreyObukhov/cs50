"""
Program prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""
def output():
    while True:
      try:
            frac = input('Fraction: ')
            (X, _, Y) = frac.partition('/')
            f = int(X) / int(Y)
            if f <=1: return(f)
        except (ValueError, ZeroDivisionError):
            pass
fuel = output()
if fuel >= 0.99: print('F')
elif fuel <= 0.01: print('E')
else: print(f'{fuel:.0%}')
