def convert(Input):
    """
    Function accepts a str as input and returns that same input with any :) converted to 🙂 and any :( to 🙁.
    """
    Input = Input.replace(":)", '🙂')
    Input = Input.replace(":(", '🙁 ')
    return(Input)

def main():
    """
    Function prompts the user for input, calls convert() on that input, and prints the result.
    """
    Input = input()
    Input = convert(Input)
    print(Input)

main()